# -*- coding: utf-8 -*-
"""
整数规划 — Python 实现
支持：分支定界 / 0-1 规划 / 指派问题（匈牙利算法）

用法：
    pip install pulp
    python integer_programming.py
"""

import numpy as np


def solve_ip(c, A_ub, b_ub, bounds=None, sense='minimize'):
    """
    整数线性规划（基于 PuLP）

    Parameters
    ----------
    c : ndarray (n,)
        目标函数系数
    A_ub : ndarray (m, n)
        不等式约束矩阵 (A_ub @ x <= b_ub)
    b_ub : ndarray (m,)
        不等式约束右侧
    bounds : list of (low, high), optional
        变量边界，默认 (0, None)
    sense : str
        'minimize' or 'maximize'

    Returns
    -------
    dict: {'x': 最优解, 'objective': 目标值, 'status': 状态}
    """
    try:
        import pulp
    except ImportError:
        raise ImportError("PuLP 未安装，请运行: pip install pulp")

    n = len(c)
    if bounds is None:
        bounds = [(0, None)] * n

    # 创建问题
    prob = pulp.LpProblem("IP", pulp.LpMinimize if sense == 'minimize' else pulp.LpMaximize)

    # 决策变量
    x = [pulp.LpVariable(f"x{i}", lowBound=bounds[i][0],
                         upBound=bounds[i][1] if bounds[i][1] is not None else None,
                         cat='Integer') for i in range(n)]

    # 目标函数
    prob += pulp.lpSum([c[i] * x[i] for i in range(n)])

    # 约束
    for i in range(len(b_ub)):
        prob += pulp.lpSum([A_ub[i, j] * x[j] for j in range(n)]) <= b_ub[i]

    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    return {
        'x': np.array([pulp.value(x[i]) for i in range(n)]),
        'objective': pulp.value(prob.objective),
        'status': pulp.LpStatus[prob.status],
    }


def solve_knapsack(values, weights, capacity):
    """
    0-1 背包问题

    Parameters
    ----------
    values : array-like
        物品价值
    weights : array-like
        物品重量
    capacity : float
        背包容量

    Returns
    -------
    dict: {'selected': 选中的物品索引, 'total_value': 总价值, 'total_weight': 总重量}
    """
    n = len(values)
    c = -np.asarray(values, dtype=float)  # 最大化 → 最小化负数
    A = np.asarray(weights, dtype=float).reshape(1, -1)
    b = np.array([capacity])
    bounds = [(0, 1)] * n

    result = solve_ip(c, A, b, bounds, sense='minimize')
    selected = np.where(np.abs(result['x'] - 1) < 1e-6)[0]

    return {
        'selected': selected.tolist(),
        'total_value': sum(values[i] for i in selected),
        'total_weight': sum(weights[i] for i in selected),
    }


def solve_assignment(cost_matrix):
    """
    指派问题（匈牙利算法）

    Parameters
    ----------
    cost_matrix : ndarray (n, n)
        成本矩阵

    Returns
    -------
    dict: {'assignment': 指派方案, 'total_cost': 总成本}
    """
    from scipy.optimize import linear_sum_assignment

    C = np.asarray(cost_matrix, dtype=float)
    row_ind, col_ind = linear_sum_assignment(C)

    return {
        'assignment': list(zip(row_ind.tolist(), col_ind.tolist())),
        'total_cost': C[row_ind, col_ind].sum(),
    }


# ==========================================
# 示例运行
# ==========================================

if __name__ == '__main__':
    np.set_printoptions(precision=4, suppress=True)

    # --- 示例1: 整数线性规划 ---
    print("=" * 60)
    print("整数线性规划示例")
    print("=" * 60)

    # max z = 3x1 + 2x2
    # s.t.  2x1 + x2 <= 100
    #        x1 + x2 <= 80
    #        x1       <= 40
    #        x1, x2 >= 0, integer
    c = np.array([-3, -2])  # 最大化用负数
    A = np.array([
        [2, 1],
        [1, 1],
        [1, 0],
    ])
    b = np.array([100, 80, 40])
    bounds = [(0, None), (0, None)]

    try:
        result = solve_ip(c, A, b, bounds, sense='minimize')
        print(f"最优解: x1={result['x'][0]:.0f}, x2={result['x'][1]:.0f}")
        print(f"目标值: {-result['objective']:.0f} (max)")
        print(f"状态: {result['status']}")
    except ImportError as e:
        print(f"[跳过] {e}")

    # --- 示例2: 背包问题 ---
    print("\n" + "=" * 60)
    print("0-1 背包问题示例")
    print("=" * 60)

    values = [60, 100, 120, 80, 50]
    weights = [10, 20, 30, 15, 5]
    capacity = 50

    try:
        result = solve_knapsack(values, weights, capacity)
        print(f"选中物品: {result['selected']}")
        print(f"总价值: {result['total_value']}")
        print(f"总重量: {result['total_weight']} / {capacity}")
    except ImportError as e:
        print(f"[跳过] {e}")

    # --- 示例3: 指派问题 ---
    print("\n" + "=" * 60)
    print("指派问题示例")
    print("=" * 60)

    cost = np.array([
        [4, 8, 7, 9],
        [7, 6, 9, 8],
        [6, 5, 8, 7],
        [9, 7, 6, 5],
    ])

    result = solve_assignment(cost)
    print(f"指派方案: {result['assignment']}")
    print(f"总成本: {result['total_cost']}")
