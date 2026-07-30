**Language:** [English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md)

# 数学建模竞赛知识库

面向**全类型数学建模竞赛**的通用知识库。以数学模型 + 代码实现为核心，论文写作为辅助，覆盖 Python 和 MATLAB 两种语言。

## 目录结构

```
MCM-Resource/
├── README.md                    ← 你在这里
├── requirements.txt             # Python 依赖（分层：核心/算法/可选）
├── pyproject.toml               # pytest + ruff + coverage 配置
├── pyrightconfig.json           # 类型检查配置
├── models/                      # 模型知识体系（按问题类型组织）
│   ├── optimization/            # 优化与控制
│   ├── evaluation/              # 评价与决策
│   ├── prediction/              # 预测与预报
│   ├── classification/          # 分类与判别
│   ├── differential/            # 机理分析（微分方程/物理建模）
│   ├── statistics/              # 统计与计量
│   ├── simulation/              # 仿真与模拟
│   └── auxiliary/               # 通用辅助方法
├── algorithms/                  # 可运行代码
│   ├── python/
│   │   └── tests/               # pytest 测试套件（67 个测试）
│   └── matlab/
├── competitions/                # 各赛事专项指南
├── templates/                   # 论文/数据处理模板
│   ├── python/
│   ├── matlab/
│   └── latex/
├── ai-tools/                    # ★ AI 辅助工具集（2026新增）
│   ├── prompts/                 # 分阶段提示词模板
│   ├── skills/                  # Claude Code Skill 配置
│   └── workflow/                # AI 辅助全流程
├── data/                        # 示例数据集（CSV）
├── .github/                     # CI/CD + Issue/PR 模板
│   └── workflows/               # GitHub Actions（pytest + 链接检查 + lint）
├── tools/                       # 工具脚本
├── papers/                      # 优秀论文分析笔记
├── notes/                       # 学习笔记
└── scripts/                     # 辅助脚本
```

## 赛事-方法速查矩阵

| 赛题特征 | 对应模型目录 | 优先查阅 |
|---------|-------------|---------|
| 需要找最优方案 | `models/optimization/` | linear_programming → multi_objective → intelligent_algorithm |
| 需要排名/打分 | `models/evaluation/` | ahp → topsis → entropy_weight |
| 预测未来趋势 | `models/prediction/` | grey_prediction → time_series → deep_learning_prediction |
| 分类/聚类 | `models/classification/` | clustering → svm → xgboost_lightgbm |
| 物理/工程建模 | `models/differential/` | ode_basics → pde_numerical → dimensional_analysis |
| 政策评估/因果推断 | `models/statistics/` | did → panel_data → synthetic_control |
| 不确定性/随机问题 | `models/simulation/` | monte_carlo → bootstrap |
| 文本数据处理 | `models/classification/` | nlp_basics → clustering |
| 金融数据 | `models/optimization/` + `models/statistics/` | portfolio_optimization → time_series |
| 需要 AI 辅助 | `ai-tools/` | prompts/stage-prompts → skills/claude-skill |

## AI 辅助工具（2026 新增）

美赛 2026 起明确允许使用 AI 工具。本仓库提供：
- **[分阶段提示词模板](ai-tools/prompts/stage-prompts.md)** — 从选题到论文写作的完整提示词
- **[去 AI 化写作技巧](ai-tools/prompts/anti-ai-writing.md)** — 40+ 技巧让 AI 写得不带 AI 味
- **[Claude Code Skill](ai-tools/skills/claude-skill.md)** — 安装后可自动激活数学建模专业知识
- **[AI 辅助全流程](ai-tools/workflow/ai-workflow.md)** — 96 小时时间线 + AI 检查清单

## 覆盖赛事

| 梯队 | 赛事 | 时间 | 核心题型 |
|------|------|------|---------|
| 1 | **MCM/ICM 美赛** | 1月底 | A连续 B离散 C大数据 D运筹 E环境 F政策 |
| 1 | **CUMCM 国赛** | 9月中 | A工程机理 B优化决策 C数据分析 |
| 1 | **华为杯 研赛** | 9月底 | 研究生级别，六大方向 |
| 2 | **MathorCup 妈妈杯** | 4月中 | 企业实际问题（阿里、滴滴等出题） |
| 2 | **统计建模大赛** | 5月 | 主题制，偏计量 DID/RDD/面板数据 |
| 2 | **电工杯** | 5月底 | 电力/能源方向，免费 |
| 2 | **深圳杯** | 7-8月 | 开放题，高难度 |
| 2 | **APMCM 亚太赛** | 11月 | 全英文，美赛模拟 |
| 专 | **泰迪杯** | 4月 | 大数据/数据挖掘 |
| 专 | **大湾区杯** | 11月 | 金融数学建模 |

详见 [`competitions/`](competitions/) 目录下各赛事专项指南。

## 使用指引

### 快速开始

1. **安装依赖** → `pip install -r requirements.txt`（核心依赖：numpy, scipy, pandas, scikit-learn）
2. **确定赛题类型** → 查阅上方速查矩阵定位模型目录
3. **阅读模型文档** → `models/<类别>/<模型名>.md`，了解原理和适用场景
4. **运行代码示例** → `algorithms/{python,matlab}/` 下有独立可运行的实现
5. **套用论文模板** → `templates/latex/` 有美赛/国赛论文模板

### 模型文档结构

每个 .md 文件包含：
1. 模型原理（数学公式 + 直观解释）
2. 适用场景（赛事题型 + 典型赛题举例）
3. 建模步骤（分步说明）
4. 代码实现（Python + MATLAB 关键片段）
5. 注意事项（优缺点、常见坑、调参建议）
6. 论文呈现建议（公式编号、图表类型、结论写法）
7. 参考资料

### 代码使用

```bash
# 安装依赖
pip install -r requirements.txt

# 运行单个算法示例
python algorithms/python/grey_model.py

# MATLAB 示例（在 MATLAB 中运行）
run('algorithms/matlab/grey_model.m')
```

每个文件包含 `if __name__ == '__main__':`（Python）或内置示例数据（MATLAB），可直接运行验证。

### 开发指南

```bash
# 运行全部测试（67 个测试，覆盖核心算法）
pytest algorithms/python/tests/ -v

# 运行测试并生成覆盖率报告
pip install pytest-cov
pytest algorithms/python/tests/ --cov=algorithms/python --cov-report=term-missing

# 代码风格检查
pip install ruff
ruff check algorithms/python/
```

CI（GitHub Actions）在每次 push 和 PR 时自动运行 `pytest` + `ruff`。

## 模型分类总览

### 优化与控制 — `models/optimization/`
线性规划 · 整数规划 · 非线性规划 · 动态规划 · 多目标优化 · 图论优化 · 排队论 · 博弈论 · 投资组合 · 调度优化

### 评价与决策 — `models/evaluation/`
AHP · TOPSIS · 模糊综合评价 · 灰色关联 · 熵权法 · PCA · 数据包络分析(DEA) · 秩和比法 · 因子分析 · 组合评价

### 预测与预报 — `models/prediction/`
灰色预测 · 时间序列(ARIMA/SARIMA) · 回归分析 · 马尔可夫预测 · 神经网络预测 · 深度学习预测(LSTM/GRU) · 插值与拟合 · 组合预测

### 分类与判别 — `models/classification/`
SVM · 决策树/随机森林 · XGBoost/LightGBM · 聚类(K-means/层次/DBSCAN) · Fisher判别 · 逻辑回归 · 集成学习(Stacking) · NLP基础 · 贝叶斯方法

### 机理分析 — `models/differential/`
ODE建模 · PDE数值解 · 稳定性分析 · 人口/生态模型 · 传染病模型(SIR/SEIR) · 扩散模型 · 量纲分析 · 运动学/动力学

### 统计与计量 — `models/statistics/`
面板数据分析 · 双重差分(DID) · 断点回归(RDD) · 工具变量(IV) · 中介/调节效应 · 结构方程(SEM) · 空间计量 · 生存分析 · 合成控制法

### 仿真与模拟 — `models/simulation/`
蒙特卡洛模拟 · 系统动力学 · 元胞自动机 · Agent-Based建模 · Bootstrap

### 通用辅助 — `models/auxiliary/`
灵敏性分析 · 数据预处理 · 特征工程 · 相关性分析 · 稳健性分析 · 不确定性分析

---

<div align="center">
  <a href="README.md">English</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-Hant.md">繁體中文</a> |
  <a href="README.ja.md">日本語</a>
</div>
