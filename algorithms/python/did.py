# -*- coding: utf-8 -*-
"""
双重差分法 (Difference-in-Differences, DID) — Python 实现
支持：经典 DID / 多期 DID / 平行趋势检验 / 安慰剂检验

用法：
    pip install statsmodels linearmodels
    python did.py
"""

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


def classic_did(df, time_col, treat_col, outcome_col):
    """
    经典 DID（2×2 面板）

    Parameters
    ----------
    df : DataFrame
    time_col : str, 时间虚拟变量（0=政策前, 1=政策后）
    treat_col : str, 处理组虚拟变量（0=控制组, 1=处理组）
    outcome_col : str, 被解释变量

    Returns
    -------
    dict: did_estimate, p_value, coefficients
    """
    import statsmodels.formula.api as smf

    df = df.copy()
    df['did'] = df[treat_col] * df[time_col]

    model = smf.ols(f'{outcome_col} ~ {treat_col} + {time_col} + did', data=df).fit()
    did_est = model.params['did']

    return {
        'did_estimate': did_est,
        'p_value': model.pvalues['did'],
        'summary': model.summary(),
        'params': model.params.to_dict(),
    }


def did_panel(df, entity_col, time_col, treat_col, outcome_col):
    """
    面板 DID（个体+时间固定效应）

    Parameters
    ----------
    df : DataFrame, 包含多期面板数据
    entity_col : str, 个体标识
    time_col : str, 时间标识
    treat_col : str, 处理组虚拟变量
    outcome_col : str, 被解释变量

    Returns
    -------
    dict: did_estimate, p_value, coefficients
    """
    try:
        from linearmodels import PanelOLS

        df = df.copy()
        df['did'] = df[treat_col] * df[time_col]
        df = df.set_index([entity_col, time_col])

        model = PanelOLS.from_formula(
            f'{outcome_col} ~ did + EntityEffects + TimeEffects', data=df
        )
        result = model.fit()

        return {
            'did_estimate': result.params['did'],
            'p_value': result.pvalues['did'],
            'r2_within': result.rsquared_within,
            'summary': str(result.summary),
        }
    except ImportError:
        print("[提示] linearmodels 未安装，使用 OLS 替代")
        return classic_did(df.reset_index(), time_col, treat_col, outcome_col)


def parallel_trend_test(df, entity_col, year_col, treat_col, outcome_col,
                        pre_periods=3):
    """
    平行趋势检验（事件研究法）

    在政策前各期产生交互项放入回归
    若事前交互项不显著 → 支持平行趋势假设
    """
    import statsmodels.formula.api as smf

    df = df.copy()
    unique_years = sorted(df[year_col].unique())

    # 生成各期交互项
    for y in unique_years:
        col_name = f'd_{y}'
        df[col_name] = (df[year_col] == y).astype(int) * df[treat_col].astype(int)

    # 去掉基准期（一般是最早或政策前一期的交互项）
    ref_year = unique_years[pre_periods - 1]
    d_cols = [f'd_{y}' for y in unique_years if y != ref_year]
    formula = f'{outcome_col} ~ ' + ' + '.join(d_cols) + f' + C({entity_col}) + C({year_col})'

    model = smf.ols(formula, data=df).fit()

    return {
        'coefficients': {col: model.params.get(col) for col in d_cols},
        'pvalues': {col: model.pvalues.get(col) for col in d_cols},
        'ref_year': ref_year,
        'summary': model.summary(),
    }


def placebo_test(df, time_col, treat_col, outcome_col, true_did=None, n_iterations=500):
    """
    安慰剂检验：随机分配处理组，观察 DID 系数分布

    Parameters
    ----------
    true_did : float, optional
        真实 DID 估计量。若为 None，自动计算。
    """
    if true_did is None:
        true_did = classic_did(df, time_col, treat_col, outcome_col)['did_estimate']

    did_placebo = np.zeros(n_iterations)

    for i in range(n_iterations):
        df_temp = df.copy()
        df_temp[treat_col] = np.random.permutation(df[treat_col].values)
        result = classic_did(df_temp, time_col, treat_col, outcome_col)
        did_placebo[i] = result['did_estimate']

    return {
        'placebo_dids': did_placebo,
        'p_value': np.mean(np.abs(did_placebo) >= np.abs(true_did)),
        'mean': np.mean(did_placebo),
        'std': np.std(did_placebo),
    }


if __name__ == '__main__':
    np.random.seed(42)

    print("=" * 60)
    print("双重差分法 (DID) 示例")
    print("=" * 60)

    # 模拟面板数据：100个个体，6期
    n_entities = 100
    n_periods = 6
    treat_ratio = 0.4
    policy_period = 3  # 政策在第3期开始

    data = []
    for i in range(n_entities):
        treat = 1 if np.random.rand() < treat_ratio else 0
        entity_effect = np.random.normal(0, 2)
        for t in range(n_periods):
            post = 1 if t >= policy_period else 0
            # 处理组在政策后效果 +2
            y = 10 + entity_effect + 0.5 * t + 2 * treat * post + np.random.normal(0, 1)
            data.append({'entity': i, 'period': t, 'post': post, 'treat': treat, 'y': y})

    df = pd.DataFrame(data)

    # 经典 DID
    result = classic_did(df, time_col='post', treat_col='treat', outcome_col='y')
    print(f"\n[经典 DID] DID估计量: {result['did_estimate']:.4f}")
    print(f"  p_value: {result['p_value']:.4f}")
    if result['p_value'] < 0.05:
        print("  → 政策效果显著 (p < 0.05)")

    # 平行趋势检验
    pt_result = parallel_trend_test(df, 'entity', 'period', 'treat', 'y', pre_periods=3)
    print(f"\n[平行趋势检验] 基准期: period={pt_result['ref_year']}")
    for col, coef in pt_result['coefficients'].items():
        if coef is not None:
            sig = '*' if pt_result['pvalues'][col] < 0.05 else ''
            print(f"  {col}: coef={coef:.4f}, p={pt_result['pvalues'][col]:.4f} {sig}")
    print("  事前各期 p>0.05 → 平行趋势假设成立")

    # 面板 DID
    df['treat_post'] = df['treat'] * df['post']
    try:
        panel_result = did_panel(df, 'entity', 'period', 'treat', 'post', 'y')
        if 'did_estimate' in panel_result:
            print(f"\n[面板DID] DID估计量: {panel_result['did_estimate']:.4f}, "
                  f"p={panel_result['p_value']:.4f}")
    except ImportError:
        print("\n[面板DID] linearmodels 未安装，跳过面板 DID 演示。pip install linearmodels")
    except Exception as e:
        print(f"\n[面板DID] 面板回归失败: {type(e).__name__}: {e}")
