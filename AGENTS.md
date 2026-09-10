# 项目通用说明

## Feature 模块生成顺序

每个 Feature 都是一个独立、可运行、可复习的小实验。开发一个 Feature 时，必须按照以下顺序执行：

### 第一步：读取知识点并规划说明文档

1. 先阅读初始化文档、Roadmap、上一个 Feature 的 README，以及当前 Feature 相关的已有资料。
2. 明确本 Feature 只解决的一个核心问题，避免提前引入后续 Feature 的内容。
3. 规划一份说明文档，至少包含：学习目标、核心概念、计算流程、公式、输入输出、与 LLM 的关系和完成标准。
4. 先确认知识点边界，再进入代码实现。

### 第二步：编排 Demo 代码

1. 根据说明文档编排最小 Demo，优先保证代码短小、独立、可读和可运行。
2. 核心数学过程应尽量手写，不用高级 API 隐藏本 Feature 要学习的逻辑。
3. 允许 Feature 之间存在少量重复代码，不为了复用而提前设计复杂架构。
4. Demo 应提供清晰的输入、计算过程和输出，必要时通过对比实验展示知识点的作用。

### 第三步：生成 Demo 使用 README

Demo 代码完成后，再生成或补充本 Feature 的 `README.md`，说明如何使用该 Demo。README 至少包含：

- 本 Feature 解决的问题；
- Demo 文件和函数的作用；
- 输入与输出；
- 运行命令和预期结果；
- 练习或可观察的实验现象。

README 中必须使用 UV 管理 Python 版本、环境和代码运行，不直接使用裸 `python` 命令。默认运行形式为：

```bash
uv run python main.py
```

如果项目存在 `pyproject.toml` 或依赖发生变化，应根据项目配置使用 `uv sync`、`uv add` 等 UV 命令维护环境。

### 第四步：追加本 Feature 的知识点说明

在 README 中追加“知识点说明”部分，只总结本 Feature 相关的内容，作为后续生成图片卡片提示词的素材。内容应优先包括：

- 核心概念和关键术语；
- 主要流程或元素之间的关系；
- 必要的公式或伪代码；
- 本 Feature 在神经网络或 LLM 中的作用；
- 常见、容易混淆、需要记住的知识点。

这部分说明使用简洁、准确的中文，不扩展无关知识，不提前替代后续 Feature 的学习内容。需要生成图片卡片时，可直接根据这部分内容提炼视觉布局、标注文案和图片提示词。

## UV 使用约定

- 所有 Python Demo 的运行和验证优先使用 `uv run`。
- 新增依赖使用 UV 管理，不手动维护隐藏的虚拟环境路径。
- 每个 Feature 的具体 UV 执行命令必须写在该 Feature 对应的 README 中。
- 根目录 README 只保留通用导航和进入 Feature 目录的提示，不堆积各 Feature 的具体命令。

## Feature 完成检查

完成一个 Feature 后，需要确认：

1. 知识点边界和说明文档已明确。
2. Demo 可以通过 UV 独立运行。
3. README 已说明使用方式、预期输出和知识点。
4. README 中的知识点总结可以作为图片卡片提示词素材。
5. 最终汇报本次 Feature 的修改内容、验证命令、验证结果和 Git 提交 Comment。

## Git 提交 Comment

每个 Feature 完成后，提供一个简洁、符合 Conventional Commits 风格的 Git 提交 Comment，内容应准确反映本次 Feature 的实际改动。例如：

```text
feat(sprint01): add manual mean squared error demo
```
