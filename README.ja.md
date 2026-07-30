**Language:** [English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md)

# 数学モデリングコンテスト知識ベース

**あらゆるタイプの数学モデリングコンテスト**に対応した汎用知識ベース。数学モデル + コード実装を核とし、論文作成を補助として、Python と MATLAB の両言語をカバーしています。

## ディレクトリ構成

```
MCM-Resource/
├── README.md                    ← ここ
├── models/                      # モデル知識体系（問題タイプ別）
│   ├── optimization/            # 最適化と制御
│   ├── evaluation/              # 評価と意思決定
│   ├── prediction/              # 予測と予報
│   ├── classification/          # 分類と判別
│   ├── differential/            # メカニズム分析（微分方程式/物理モデリング）
│   ├── statistics/              # 統計と計量経済
│   ├── simulation/              # シミュレーション
│   └── auxiliary/               # 汎用補助手法
├── algorithms/                  # 実行可能コード
│   ├── python/
│   └── matlab/
├── competitions/                # 各コンテスト別ガイド
├── templates/                   # 論文/データ処理テンプレート
│   ├── python/
│   ├── matlab/
│   └── latex/
├── ai-tools/                    # ★ AI 活用ツールセット（2026年新規）
│   ├── prompts/                 # 段階別プロンプトテンプレート
│   ├── skills/                  # Claude Code Skill 設定
│   └── workflow/                # AI 活用フルワークフロー
├── tools/                       # ユーティリティスクリプト
├── data/                        # サンプルデータセット
├── papers/                      # 優秀論文分析ノート
├── notes/                       # 学習ノート
└── scripts/                     # 補助スクリプト
```

## コンテスト-手法クイックリファレンス表

| 問題の特徴 | 対応モデルディレクトリ | 優先参照順 |
|-----------|---------------------|-----------|
| 最適解を求める | `models/optimization/` | linear_programming → multi_objective → intelligent_algorithm |
| ランキング/スコアリング | `models/evaluation/` | ahp → topsis → entropy_weight |
| 将来予測 | `models/prediction/` | grey_prediction → time_series → deep_learning_prediction |
| 分類/クラスタリング | `models/classification/` | clustering → svm → xgboost_lightgbm |
| 物理/工学的モデリング | `models/differential/` | ode_basics → pde_numerical → dimensional_analysis |
| 政策評価/因果推論 | `models/statistics/` | did → panel_data → synthetic_control |
| 不確実性/確率的問題 | `models/simulation/` | monte_carlo → bootstrap |
| テキストデータ処理 | `models/classification/` | nlp_basics → clustering |
| 金融データ | `models/optimization/` + `models/statistics/` | portfolio_optimization → time_series |
| AI 活用が必要 | `ai-tools/` | prompts/stage-prompts → skills/claude-skill |

## AI 活用ツール（2026年新規）

MCM/ICM 2026 より、AI ツールの使用が明示的に許可されました。このリポジトリでは以下を提供します：
- **[段階別プロンプトテンプレート](ai-tools/prompts/stage-prompts.md)** — テーマ選定から論文作成までの完全プロンプト
- **[AI臭を消すライティングテクニック](ai-tools/prompts/anti-ai-writing.md)** — AI生成文を人間らしくする40以上のテクニック
- **[Claude Code Skill](ai-tools/skills/claude-skill.md)** — インストール後、数学モデリングの専門知識を自動活性化
- **[AI活用フルワークフロー](ai-tools/workflow/ai-workflow.md)** — 96時間タイムライン + AI チェックリスト

## 対象コンテスト

| ティア | コンテスト | 時期 | 主要問題タイプ |
|-------|-----------|------|--------------|
| 1 | **MCM/ICM（米国数学モデリングコンテスト）** | 1月下旬 | A連続 B離散 Cビッグデータ Dオペレーションズ E環境 F政策 |
| 1 | **CUMCM（中国全国数学モデリングコンテスト）** | 9月中旬 | A工学的メカニズム B最適化意思決定 Cデータ分析 |
| 1 | **華為杯（大学院生コンテスト）** | 9月下旬 | 大学院レベル、6分野 |
| 2 | **MathorCup** | 4月中旬 | 企業の実問題（Alibaba、DiDi等が出題） |
| 2 | **統計モデリングコンテスト** | 5月 | テーマ制、計量経済学中心 DID/RDD/パネルデータ |
| 2 | **電工杯** | 5月下旬 | 電力/エネルギー分野、無料 |
| 2 | **深圳杯** | 7-8月 | 自由課題、高難易度 |
| 2 | **APMCM（アジア太平洋）** | 11月 | 完全英語、MCM模擬 |
| 専 | **泰迪杯** | 4月 | ビッグデータ/データマイニング |
| 専 | **大湾区杯** | 11月 | 金融数学モデリング |

詳細は [`competitions/`](competitions/) ディレクトリ内の各コンテスト別ガイドを参照してください。

## 利用ガイド

### クイックスタート

1. **問題タイプを特定** → 上記クイックリファレンス表でモデルディレクトリを特定
2. **モデルドキュメントを読む** → `models/<カテゴリ>/<モデル名>.md` で原理と適用シナリオを理解
3. **コード例を実行** → `algorithms/{python,matlab}/` に独立実行可能な実装
4. **論文テンプレートを適用** → `templates/latex/` に MCM/CUMCM 論文テンプレート

### モデルドキュメント構成

各 .md ファイルの内容：
1. モデル原理（数式 + 直感的説明）
2. 適用シナリオ（コンテスト問題タイプ + 典型的な問題例）
3. モデリング手順（段階的説明）
4. コード実装（Python + MATLAB の主要スニペット）
5. 注意事項（長所・短所、よくある落とし穴、パラメータ調整のアドバイス）
6. 論文作成の提案（式番号、図表タイプ、結論の書き方）
7. 参考資料

### コードの使用

```bash
# Python 例
python algorithms/python/grey_model.py

# MATLAB 例（MATLAB 上で実行）
run('algorithms/matlab/grey_model.m')
```

各ファイルには `if __name__ == '__main__':`（Python）または組み込みサンプルデータ（MATLAB）が含まれており、直接実行して検証できます。

## モデル分類概要

### 最適化と制御 — `models/optimization/`
線形計画法 · 整数計画法 · 非線形計画法 · 動的計画法 · 多目的最適化 · グラフ理論最適化 · 待ち行列理論 · ゲーム理論 · ポートフォリオ最適化 · スケジューリング最適化

### 評価と意思決定 — `models/evaluation/`
AHP · TOPSIS · ファジィ総合評価 · グレイ関連分析 · エントロピー重み法 · PCA · データ包絡分析(DEA) · 順位和比法 · 因子分析 · 組合せ評価

### 予測と予報 — `models/prediction/`
グレイ予測 · 時系列分析(ARIMA/SARIMA) · 回帰分析 · マルコフ予測 · ニューラルネットワーク予測 · 深層学習予測(LSTM/GRU) · 補間と近似 · 組合せ予測

### 分類と判別 — `models/classification/`
SVM · 決定木/ランダムフォレスト · XGBoost/LightGBM · クラスタリング(K-means/階層的/DBSCAN) · Fisher判別 · ロジスティック回帰 · アンサンブル学習(Stacking) · NLP基礎 · ベイズ法

### メカニズム分析 — `models/differential/`
ODEモデリング · PDE数値解法 · 安定性分析 · 人口/生態モデル · 感染症モデル(SIR/SEIR) · 拡散モデル · 次元解析 · 運動学/力学

### 統計と計量経済 — `models/statistics/`
パネルデータ分析 · 差分の差分法(DID) · 回帰不連続デザイン(RDD) · 操作変数法(IV) · 媒介/調整効果 · 構造方程式モデリング(SEM) · 空間計量経済学 · 生存時間分析 · 合成コントロール法

### シミュレーション — `models/simulation/`
モンテカルロシミュレーション · システムダイナミクス · セルオートマトン · エージェントベースモデリング · Bootstrap

### 汎用補助 — `models/auxiliary/`
感度分析 · データ前処理 · 特徴量エンジニアリング · 相関分析 · ロバスト性分析 · 不確実性分析

---

<div align="center">
  <a href="README.md">English</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-Hant.md">繁體中文</a> |
  <a href="README.ja.md">日本語</a>
</div>
