**Language:** [English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md)

# Mathematical Modeling Contest Knowledge Base

A comprehensive knowledge base designed for **all types of mathematical modeling competitions**. Centered on mathematical models + code implementation, with thesis writing as a supplement, covering both Python and MATLAB.

## Directory Structure

```
math-modeling-kb/
├── README.md                    ← You are here
├── requirements.txt             # Python dependencies (tiered: core / algorithm / optional)
├── pyproject.toml               # pytest + ruff + coverage configuration
├── pyrightconfig.json           # Type checking configuration
├── models/                      # Model knowledge system (organized by problem type)
│   ├── optimization/            # Optimization and Control
│   ├── evaluation/              # Evaluation and Decision Making
│   ├── prediction/              # Prediction and Forecasting
│   ├── classification/          # Classification and Discrimination
│   ├── differential/            # Mechanistic Analysis (Differential Equations / Physical Modeling)
│   ├── statistics/              # Statistics and Econometrics
│   ├── simulation/              # Simulation and Modeling
│   └── auxiliary/               # General Auxiliary Methods
├── algorithms/                  # Runnable code
│   ├── python/
│   │   └── tests/               # pytest test suite (67 tests)
│   └── matlab/
├── competitions/                # Competition-specific guides
├── templates/                   # Thesis/Data processing templates
│   ├── python/
│   ├── matlab/
│   └── latex/
├── ai-tools/                    # ★ AI-Assisted Toolset (New in 2026)
│   ├── prompts/                 # Stage-specific prompt templates
│   ├── skills/                  # Claude Code Skill configurations
│   └── workflow/                # AI-assisted full workflow
├── data/                        # Sample datasets (CSV)
├── .github/                     # CI/CD + Issue/PR templates
│   └── workflows/               # GitHub Actions (pytest + link check + lint)
├── tools/                       # Utility scripts
├── papers/                      # Excellent paper analysis notes
├── notes/                       # Learning notes
└── scripts/                     # Helper scripts
```

## Competition-Method Quick Reference Matrix

| Problem Feature | Corresponding Model Directory | Priority Reading Order |
|---------------|-----------------------------|----------------------|
| Need optimal solution | `models/optimization/` | linear_programming → multi_objective → intelligent_algorithm |
| Need ranking/scoring | `models/evaluation/` | ahp → topsis → entropy_weight |
| Predict future trends | `models/prediction/` | grey_prediction → time_series → deep_learning_prediction |
| Classification/Clustering | `models/classification/` | clustering → svm → xgboost_lightgbm |
| Physics/Engineering modeling | `models/differential/` | ode_basics → pde_numerical → dimensional_analysis |
| Policy evaluation/Causal inference | `models/statistics/` | did → panel_data → synthetic_control |
| Uncertainty/Stochastic problems | `models/simulation/` | monte_carlo → bootstrap |
| Text data processing | `models/classification/` | nlp_basics → clustering |
| Financial data | `models/optimization/` + `models/statistics/` | portfolio_optimization → time_series |
| Need AI assistance | `ai-tools/` | prompts/stage-prompts → skills/claude-skill |

## AI-Assisted Tools (New in 2026)

Starting from MCM/ICM 2026, the use of AI tools is explicitly permitted. This repository provides:
- **[Stage-Specific Prompt Templates](ai-tools/prompts/stage-prompts.md)** — Complete prompts from topic selection to thesis writing
- **[De-AI-ification Writing Techniques](ai-tools/prompts/anti-ai-writing.md)** — 40+ techniques to make AI-generated text sound human-written
- **[Claude Code Skill](ai-tools/skills/claude-skill.md)** — Automatically activates mathematical modeling expertise after installation
- **[AI-Assisted Full Workflow](ai-tools/workflow/ai-workflow.md)** — 96-hour timeline + AI checklist

## Covered Competitions

| Tier | Competition | Time | Core Problem Types |
|------|------------|------|-------------------|
| 1 | **MCM/ICM** | Late January | A Continuous B Discrete C Data Insights D Operations Research E Environmental F Policy |
| 1 | **CUMCM (China National)** | Mid-September | A Engineering Mechanism B Optimization Decision C Data Analysis |
| 1 | **Huawei Cup (Graduate)** | Late September | Graduate level, six major directions |
| 2 | **MathorCup** | Mid-April | Real-world corporate problems (set by Alibaba, Didi, etc.) |
| 2 | **Statistics Modeling Contest** | May | Thematic, focuses on econometrics DID/RDD/Panel Data |
| 2 | **Electrical Engineering Cup** | Late May | Power/Energy direction, free |
| 2 | **Shenzhen Cup** | July-August | Open-ended problems, high difficulty |
| 2 | **APMCM (Asia-Pacific)** | November | Full English, MCM simulation |
| S | **Teddy Cup** | April | Big Data/Data Mining |
| S | **Greater Bay Area Cup** | November | Financial Mathematical Modeling |

See detailed competition-specific guides under the [`competitions/`](competitions/) directory.

## Usage Guide

### Quick Start

1. **Install dependencies** → `pip install -r requirements.txt` (core deps: numpy, scipy, pandas, scikit-learn)
2. **Determine the problem type** → Refer to the quick reference matrix above to locate the model directory
3. **Read the model documentation** → `models/<category>/<model-name>.md` to understand principles and applicable scenarios
4. **Run code examples** → `algorithms/{python,matlab}/` contains independently runnable implementations
5. **Apply thesis templates** → `templates/latex/` contains MCM/CUMCM thesis templates

### Model Document Structure

Each `.md` file contains:
1. Model principles (mathematical formulas + intuitive explanations)
2. Applicable scenarios (competition problem types + typical problem examples)
3. Modeling steps (step-by-step instructions)
4. Code implementation (Python + MATLAB key snippets)
5. Important notes (pros and cons, common pitfalls, parameter tuning suggestions)
6. Thesis presentation suggestions (equation numbering, chart types, conclusion writing)
7. References

### Code Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Run a single algorithm example
python algorithms/python/grey_model.py

# MATLAB example (run in MATLAB)
run('algorithms/matlab/grey_model.m')
```

Each file includes `if __name__ == '__main__':` (Python) or built-in example data (MATLAB), and can be run directly for verification.

### Development

```bash
# Run all tests (67 tests covering core algorithms)
pytest algorithms/python/tests/ -v

# Run tests with coverage report
pip install pytest-cov
pytest algorithms/python/tests/ --cov=algorithms/python --cov-report=term-missing

# Lint check
pip install ruff
ruff check algorithms/python/
```

CI (GitHub Actions) runs `pytest` + `ruff` on every push and PR.

## Model Classification Overview

### Optimization and Control — `models/optimization/`
Linear Programming · Integer Programming · Nonlinear Programming · Dynamic Programming · Multi-Objective Optimization · Graph Theory Optimization · Queuing Theory · Game Theory · Portfolio Optimization · Scheduling Optimization

### Evaluation and Decision Making — `models/evaluation/`
AHP · TOPSIS · Fuzzy Comprehensive Evaluation · Grey Relational Analysis · Entropy Weight Method · PCA · Data Envelopment Analysis (DEA) · Rank Sum Ratio · Factor Analysis · Combined Evaluation

### Prediction and Forecasting — `models/prediction/`
Grey Prediction · Time Series (ARIMA/SARIMA) · Regression Analysis · Markov Prediction · Neural Network Prediction · Deep Learning Prediction (LSTM/GRU) · Interpolation and Fitting · Combined Forecasting

### Classification and Discrimination — `models/classification/`
SVM · Decision Tree/Random Forest · XGBoost/LightGBM · Clustering (K-means/Hierarchical/DBSCAN) · Fisher Discriminant · Logistic Regression · Ensemble Learning (Stacking) · NLP Fundamentals · Bayesian Methods

### Mechanistic Analysis — `models/differential/`
ODE Modeling · PDE Numerical Solution · Stability Analysis · Population/Ecology Models · Epidemic Models (SIR/SEIR) · Diffusion Models · Dimensional Analysis · Kinematics/Dynamics

### Statistics and Econometrics — `models/statistics/`
Panel Data Analysis · Difference-in-Differences (DID) · Regression Discontinuity (RDD) · Instrumental Variables (IV) · Mediation/Moderation Effects · Structural Equation Modeling (SEM) · Spatial Econometrics · Survival Analysis · Synthetic Control Method

### Simulation and Modeling — `models/simulation/`
Monte Carlo Simulation · System Dynamics · Cellular Automata · Agent-Based Modeling · Bootstrap

### General Auxiliary — `models/auxiliary/`
Sensitivity Analysis · Data Preprocessing · Feature Engineering · Correlation Analysis · Robustness Analysis · Uncertainty Analysis

---

<div align="center">
  <a href="README.md">English</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-Hant.md">繁體中文</a> |
  <a href="README.ja.md">日本語</a>
</div>
