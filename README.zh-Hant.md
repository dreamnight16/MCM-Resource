**Language:** [English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md)

# 數學建模競賽知識庫

面向**全類型數學建模競賽**的通用知識庫。以數學模型 + 程式碼實現為核心，論文寫作為輔助，覆蓋 Python 和 MATLAB 兩種語言。

## 目錄結構

```
MCM-Resource/
├── README.md                    ← 你在這裡
├── models/                      # 模型知識體系（按問題類型組織）
│   ├── optimization/            # 優化與控制
│   ├── evaluation/              # 評價與決策
│   ├── prediction/              # 預測與預報
│   ├── classification/          # 分類與判別
│   ├── differential/            # 機理分析（微分方程/物理建模）
│   ├── statistics/              # 統計與計量
│   ├── simulation/              # 模擬與仿真
│   └── auxiliary/               # 通用輔助方法
├── algorithms/                  # 可執行程式碼
│   ├── python/
│   └── matlab/
├── competitions/                # 各賽事專項指南
├── templates/                   # 論文/資料處理模板
│   ├── python/
│   ├── matlab/
│   └── latex/
├── ai-tools/                    # ★ AI 輔助工具集（2026新增）
│   ├── prompts/                 # 分階段提示詞模板
│   ├── skills/                  # Claude Code Skill 配置
│   └── workflow/                # AI 輔助全流程
├── tools/                       # 工具腳本
├── data/                        # 範例資料集
├── papers/                      # 優秀論文分析筆記
├── notes/                       # 學習筆記
└── scripts/                     # 輔助腳本
```

## 賽事-方法速查矩陣

| 賽題特徵 | 對應模型目錄 | 優先查閱 |
|---------|-------------|---------|
| 需要找最優方案 | `models/optimization/` | linear_programming → multi_objective → intelligent_algorithm |
| 需要排名/評分 | `models/evaluation/` | ahp → topsis → entropy_weight |
| 預測未來趨勢 | `models/prediction/` | grey_prediction → time_series → deep_learning_prediction |
| 分類/聚類 | `models/classification/` | clustering → svm → xgboost_lightgbm |
| 物理/工程建模 | `models/differential/` | ode_basics → pde_numerical → dimensional_analysis |
| 政策評估/因果推斷 | `models/statistics/` | did → panel_data → synthetic_control |
| 不確定性/隨機問題 | `models/simulation/` | monte_carlo → bootstrap |
| 文字資料處理 | `models/classification/` | nlp_basics → clustering |
| 金融資料 | `models/optimization/` + `models/statistics/` | portfolio_optimization → time_series |
| 需要 AI 輔助 | `ai-tools/` | prompts/stage-prompts → skills/claude-skill |

## AI 輔助工具（2026 新增）

美賽 2026 起明確允許使用 AI 工具。本倉庫提供：
- **[分階段提示詞模板](ai-tools/prompts/stage-prompts.md)** — 從選題到論文寫作的完整提示詞
- **[去 AI 化寫作技巧](ai-tools/prompts/anti-ai-writing.md)** — 40+ 技巧讓 AI 寫得不帶 AI 味
- **[Claude Code Skill](ai-tools/skills/claude-skill.md)** — 安裝後可自動啟動數學建模專業知識
- **[AI 輔助全流程](ai-tools/workflow/ai-workflow.md)** — 96 小時時間線 + AI 檢查清單

## 覆蓋賽事

| 梯隊 | 賽事 | 時間 | 核心題型 |
|------|------|------|---------|
| 1 | **MCM/ICM 美賽** | 1月底 | A連續 B離散 C大數據 D運籌 E環境 F政策 |
| 1 | **CUMCM 國賽** | 9月中 | A工程機理 B優化決策 C資料分析 |
| 1 | **華為盃 研賽** | 9月底 | 研究生級別，六大方向 |
| 2 | **MathorCup 媽媽盃** | 4月中 | 企業實際問題（阿里、滴滴等出題） |
| 2 | **統計建模大賽** | 5月 | 主題制，偏計量 DID/RDD/面板資料 |
| 2 | **電工盃** | 5月底 | 電力/能源方向，免費 |
| 2 | **深圳盃** | 7-8月 | 開放題，高難度 |
| 2 | **APMCM 亞太賽** | 11月 | 全英文，美賽模擬 |
| 專 | **泰迪盃** | 4月 | 大數據/資料探勘 |
| 專 | **大灣區盃** | 11月 | 金融數學建模 |

詳見 [`competitions/`](competitions/) 目錄下各賽事專項指南。

## 使用指引

### 快速開始

1. **確定賽題類型** → 查閱上方速查矩陣定位模型目錄
2. **閱讀模型文件** → `models/<類別>/<模型名>.md`，了解原理和適用場景
3. **執行程式碼範例** → `algorithms/{python,matlab}/` 下有獨立可執行的實現
4. **套用論文模板** → `templates/latex/` 有美賽/國賽論文模板

### 模型文件結構

每個 .md 文件包含：
1. 模型原理（數學公式 + 直觀解釋）
2. 適用場景（賽事題型 + 典型賽題舉例）
3. 建模步驟（分步說明）
4. 程式碼實現（Python + MATLAB 關鍵片段）
5. 注意事項（優缺點、常見坑、調參建議）
6. 論文呈現建議（公式編號、圖表類型、結論寫法）
7. 參考資料

### 程式碼使用

```bash
# Python 範例
python algorithms/python/grey_model.py

# MATLAB 範例（在 MATLAB 中執行）
run('algorithms/matlab/grey_model.m')
```

每個文件包含 `if __name__ == '__main__':`（Python）或內置範例資料（MATLAB），可直接執行驗證。

## 模型分類總覽

### 優化與控制 — `models/optimization/`
線性規劃 · 整數規劃 · 非線性規劃 · 動態規劃 · 多目標優化 · 圖論優化 · 排隊論 · 博弈論 · 投資組合 · 排程優化

### 評價與決策 — `models/evaluation/`
AHP · TOPSIS · 模糊綜合評價 · 灰色關聯 · 熵權法 · PCA · 資料包絡分析(DEA) · 秩和比法 · 因子分析 · 組合評價

### 預測與預報 — `models/prediction/`
灰色預測 · 時間序列(ARIMA/SARIMA) · 迴歸分析 · 馬可夫預測 · 神經網路預測 · 深度學習預測(LSTM/GRU) · 插值與擬合 · 組合預測

### 分類與判別 — `models/classification/`
SVM · 決策樹/隨機森林 · XGBoost/LightGBM · 聚類(K-means/層次/DBSCAN) · Fisher判別 · 邏輯迴歸 · 集成學習(Stacking) · NLP基礎 · 貝氏方法

### 機理分析 — `models/differential/`
ODE建模 · PDE數值解 · 穩定性分析 · 人口/生態模型 · 傳染病模型(SIR/SEIR) · 擴散模型 · 量綱分析 · 運動學/動力學

### 統計與計量 — `models/statistics/`
面板資料分析 · 雙重差分(DID) · 斷點迴歸(RDD) · 工具變數(IV) · 中介/調節效應 · 結構方程(SEM) · 空間計量 · 存活分析 · 合成控制法

### 模擬與仿真 — `models/simulation/`
蒙地卡羅模擬 · 系統動力學 · 元胞自動機 · Agent-Based建模 · Bootstrap

### 通用輔助 — `models/auxiliary/`
靈敏性分析 · 資料預處理 · 特徵工程 · 相關性分析 · 穩健性分析 · 不確定性分析

---

<div align="center">
  <a href="README.md">English</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-Hant.md">繁體中文</a> |
  <a href="README.ja.md">日本語</a>
</div>
