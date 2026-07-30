# 贡献指南

欢迎为本资源库贡献内容！无论是新增模型、修复代码、补充文档还是分享参赛经验，都非常欢迎。

## 贡献方式

### 1. 报告问题

发现 bug、文档错误或有改进建议？请提交 [Issue](https://github.com/sixtdreanight/MCM-Resource/issues)。

### 2. 提交代码

**Fork & Pull Request 流程：**

1. Fork 本仓库
2. 创建功能分支：`git checkout -b feat/your-feature`
3. 提交更改：`git commit -m "feat: 添加XXX模型"`
4. 推送分支：`git push origin feat/your-feature`
5. 提交 Pull Request

### 3. 提交规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 格式：

| 类型 | 用途 |
|------|------|
| `feat:` | 新增模型、算法、模板 |
| `fix:` | 修复 bug 或错误 |
| `docs:` | 更新文档 |
| `refactor:` | 代码重构 |
| `style:` | 代码格式调整 |

## 内容规范

### 模型文档 (.md)

模板结构：

```markdown
# 模型名称
## 1. 模型原理（数学公式 + 直观解释）
## 2. 适用场景（赛事题型 + 典型赛题举例）
## 3. 建模步骤（分步说明）
## 4. 代码实现（Python + MATLAB 关键片段）
## 5. 注意事项（优缺点、常见坑）
## 6. 论文呈现建议
## 7. 参考资料
```

### 代码文件 (.py / .m)

- 每个文件必须包含 `if __name__ == '__main__':` 示例
- 函数需要 docstring（中文或英文）
- 使用 `numpy` `scipy` `pandas` `sklearn` 等常用库
- 处理除零、空值等边界情况

### AI 提示词 / Skill

- 提示词需注明来源（原创/改编/引用）
- Skill 配置需注明兼容的工具版本

## 目录约定

```
models/<类别>/model_name.md      # 模型文档
algorithms/python/model_name.py  # Python 实现
algorithms/matlab/model_name.m   # MATLAB 实现
competitions/competition_name.md # 赛事指南
ai-tools/prompts/topic.md        # 提示词
ai-tools/skills/topic.md         # Skill 配置
```

## 行为准则

- 尊重所有贡献者的劳动
- 建设性讨论，反对人身攻击
- 引用他人成果时注明来源
