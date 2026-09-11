# llm-from-zero

从零开始理解、实现并训练一个小型大语言模型（LLM）。

## 使用提示

每个 Sprint 和 Feature 都是相对独立的学习项目。请先进入目标 Feature 目录：

```bash
cd <sprint-directory>/<feature-directory>
```

进入后阅读该目录下的 `README.md`，按照其中的 UV 命令执行。

## 在线阅读

完整的学习路线和 Feature 章节已规划为在线教材：

- [在线教材](https://fabersober.github.io/llm-from-zero/)
- [学习路线](ROADMAP.md)
- [当前学习进度](CURRENT.md)

## 本地预览网站

在仓库根目录执行：

~~~bash
uv sync
uv run python scripts/prepare_docs.py
uv run zensical serve
~~~

正式构建检查：

~~~bash
uv run zensical build --strict --clean
~~~
