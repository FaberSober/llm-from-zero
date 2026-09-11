# Feature 教学内容维护提示词

你负责维护当前 Feature 的教学内容。

## 需要读取的上下文

只读取以下必要文件：

1. AGENTS.md
2. ROADMAP.md
3. CURRENT.md
4. docs/standards/feature-readme.md
5. 当前 Sprint 的 README.md
6. 当前 Feature 的 README.md
7. 当前 Feature 的 Python 代码
8. 上一个 Feature 的 README.md（如果存在）

## 工作要求

1. 先理解当前 Feature 的代码和唯一核心知识点。
2. 使用 uv run python main.py 验证代码和输出。
3. 按 Feature README 规范维护当前章节。
4. 从直觉、原理、数学、代码、实验逐步解释。
5. 所有公式必须正确，并解释变量。
6. 所有示例和预期输出必须来自真实代码。
7. 不提前扩展后续 Feature 的内容。
8. 不修改无关目录。
9. 必要时更新当前 Sprint README 和 CURRENT.md。
10. 最后执行文档装配和 Strict Build。

## 输出内容

完成后输出：

- 修改了哪些文件；
- 章节补充了哪些内容；
- 执行了哪些验证命令；
- 验证结果；
- 仍需人工确认的问题。
