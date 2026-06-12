# 示例数据集

| 文件 | 行数 | 列数 | 适用模型 |
|------|------|------|----------|
| `evaluation_data.csv` | 5 | 6 | AHP, TOPSIS, 熵权法, 模糊综合评价 |
| `prediction_data.csv` | 24 | 2 | 灰色预测 GM(1,1), ARIMA, LSTM |
| `optimization_data.csv` | 3 产品 | 7 | 线性规划, 整数规划, 投资组合优化 |

## 使用方式

```python
import pandas as pd

# 评价数据
eval_df = pd.read_csv('data/evaluation_data.csv')
data = eval_df.iloc[:, 1:].values  # 数值部分

# 预测数据
pred_df = pd.read_csv('data/prediction_data.csv')
series = pred_df['Sales'].values

# 优化数据
opt_df = pd.read_csv('data/optimization_data.csv')
c = opt_df['Profit'].values
A = opt_df[['Resource_A', 'Resource_B', 'Resource_C']].values
```
