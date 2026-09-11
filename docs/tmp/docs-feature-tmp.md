# LLM From Zero 教学网站建设方案

## 1. 方案结论

采用：

| 能力    | 方案                       |
| ----- | ------------------------ |
| 文档框架  | **Zensical**             |
| 教学内容  | Feature 目录中的 `README.md` |
| 包管理   | `uv`                     |
| 代码托管  | GitHub                   |
| 网站托管  | GitHub Pages             |
| CI/CD | GitHub Actions           |
| 内容维护  | Codex / 大模型              |
| 内容审核  | Pull Request             |
| 搜索    | Zensical 内置搜索            |
| 数学公式  | Markdown + KaTeX         |
| 图示    | Mermaid                  |

核心原则：

> **README 是唯一内容源，网站只是 README 的展示层。**

不额外维护一套教学文章。

---

# 2. 整体工作流

```text
学习 / 编写 Feature
        ↓
修改 main.py
        ↓
修改 Feature README
        ↓
Codex Review / 完善教学内容
        ↓
运行代码验证
        ↓
创建 Git Commit
        ↓
Push GitHub
        ↓
GitHub Actions
        ↓
prepare_docs.py
        ↓
生成临时文档目录
        ↓
Zensical Build --strict
        ↓
GitHub Pages
        ↓
在线教材更新
```

预计网站：

```text
https://fabersober.github.io/llm-from-zero/
```

注意：

```text
git commit
```

仅产生本地提交，不会触发 GitHub Actions。

必须：

```text
git push
```

到 GitHub 后才会触发 CI/CD。

---

# 3. 核心目录结构

```text
llm-from-zero/
│
├── README.md
├── ROADMAP.md
├── CURRENT.md
├── AGENTS.md
│
├── sprint01-foundations/
│   ├── README.md
│   │
│   ├── feature01-forward/
│   │   ├── README.md
│   │   ├── main.py
│   │   └── assets/
│   │
│   ├── feature02-loss/
│   │   ├── README.md
│   │   ├── main.py
│   │   └── assets/
│   │
│   └── ...
│
├── sprint02-neural-network/
├── sprint03-language-model/
├── ...
│
├── experiments/
│
├── docs/
│   ├── standards/
│   │   └── feature-readme.md
│   │
│   └── prompts/
│       └── maintain-feature.md
│
├── scripts/
│   └── prepare_docs.py
│
├── .docs-build/
│
├── zensical.toml
├── pyproject.toml
├── uv.lock
│
└── .github/
    └── workflows/
        └── docs.yml
```

其中：

```text
.docs-build/
```

为构建时生成的临时目录：

```gitignore
.docs-build/
site/
```

不提交到 Git。

---

# 4. 教学内容来源

不创建第二套 Markdown 教材。

网站内容直接来源于现有仓库。

| 网站内容       | 内容源                       |
| ---------- | ------------------------- |
| 首页         | `README.md`               |
| 学习路线       | `ROADMAP.md`              |
| 当前学习进度     | `CURRENT.md`              |
| Sprint 首页  | `sprintXX-xxx/README.md`  |
| Feature 章节 | `featureXX-xxx/README.md` |
| 图片         | Feature 中的 `assets/`      |
| 示例代码       | Feature 中的 `main.py`      |

Feature README 同时承担两个角色：

```text
GitHub README
+
在线教材章节
```

因此任何知识点只维护一次。

---

# 5. 文档装配层

不直接让 Zensical 扫描整个代码仓库。

增加：

```text
scripts/prepare_docs.py
```

职责仅为：

```text
README.md
        ↓
.docs-build/index.md

ROADMAP.md
        ↓
.docs-build/roadmap.md

CURRENT.md
        ↓
.docs-build/current.md

sprint01-foundations/README.md
        ↓
.docs-build/sprint01/README.md

feature01-forward/README.md
        ↓
.docs-build/sprint01/feature01-forward/README.md
```

同时复制：

```text
assets/
```

必要时复制用于下载的示例文件。

**不复制 Python 源码到网站目录。**

网页需要展示源码时：

* Markdown 中保留关键代码片段；
* 完整代码链接到 GitHub；
* 给出本地运行命令。

`prepare_docs.py` 只是构建工具，不是新的内容源。

---

# 6. Feature README 规范

每个 Feature 都是一个独立知识章节。

统一结构：

```markdown
# Loss：模型如何知道自己错了

## 1. 本章目标

## 2. 这是什么

## 3. 为什么需要它

## 4. 核心原理

## 5. 数学表示

## 6. 手工计算

## 7. 最小代码实现

## 8. 实验

## 9. 在 LLM 中的位置

## 10. 常见误区

## 11. 本章需要记住什么

## 12. 配套代码

## 13. 前置知识

## 14. 下一章
```

不要求所有章节机械填满。

核心原则：

> 一个 Feature 只解决一个核心知识问题。

---

# 7. 网站导航

导航结构与仓库学习结构保持一致：

```text
首页

开始学习
├── 项目介绍
├── 学习路线
└── 当前进度

Sprint 01 · Foundations
├── Forward Computation
├── Loss
├── Gradient
├── Chain Rule
├── Backpropagation
├── Gradient Descent
└── Learning Rate

Sprint 02 · Neural Network
├── Neuron
├── Activation
├── MLP
└── Training Loop

Sprint 03 · Language Model
...

Experiments
├── TinyGPT 1M
├── TinyGPT 10M
└── TinyStories GPT

附录
├── Glossary
├── Formula
└── References
```

导航顺序应根据：

```text
sprintXX
featureXX
```

自动确定。

避免每增加一个 Feature 都手动维护大量导航配置。

---

# 8. GitHub Actions

采用三种触发方式。

### Pull Request

```text
PR
↓
准备文档
↓
构建
↓
检查
↓
不发布
```

用于检查：

* Markdown；
* 页面导航；
* 内部链接；
* 图片路径；
* Zensical 构建。

---

### Push Main

```text
push main
↓
prepare_docs
↓
build --strict
↓
上传 Pages Artifact
↓
GitHub Pages
```

只有：

```text
main
```

允许正式发布。

---

### workflow_dispatch

允许手动重新部署。

---

# 9. CI 构建命令

依赖统一通过：

```text
pyproject.toml
+
uv.lock
```

锁定。

本地：

```bash
uv sync
uv run python scripts/prepare_docs.py
uv run zensical serve
```

正式验证：

```bash
uv run python scripts/prepare_docs.py
uv run zensical build --strict --clean
```

CI 必须使用锁定依赖，避免本地和 GitHub Actions 使用不同版本。

---

# 10. GitHub Pages 发布

GitHub：

```text
Settings
↓
Pages
↓
Build and deployment
↓
Source
↓
GitHub Actions
```

部署流程：

```text
Checkout
↓
Setup Python
↓
Setup uv
↓
uv sync
↓
prepare_docs.py
↓
zensical build --strict
↓
configure-pages
↓
upload-pages-artifact
↓
deploy-pages
```

部署 Job 仅在：

```text
main
```

执行。

---

# 11. 大模型角色

大模型不参与网站 Build。

大模型只负责：

```text
教学内容维护
+
代码 Review
+
文档 Review
```

CI/CD 必须保持：

```text
确定性
可重复
无外部 AI API 依赖
```

禁止：

```text
GitHub Actions Build
↓
调用 LLM API
↓
修改 Markdown
↓
直接发布
```

---

# 12. 大模型维护 Feature 的上下文

维护某一个 Feature 时，只读取必要内容：

```text
AGENTS.md

ROADMAP.md

CURRENT.md

docs/standards/feature-readme.md

当前 Sprint README

当前 Feature README

当前 Feature main.py

上一个 Feature README
```

原则：

> 控制上下文范围，不让模型读取整个仓库。

---

# 13. 大模型教学内容维护规则

维护 Feature 时：

1. 先理解 `main.py`；
2. 确认本 Feature 的唯一核心知识点；
3. 运行代码验证；
4. 再修改 README；
5. 数学公式必须正确；
6. 公式中的变量必须解释；
7. 示例必须对应实际代码；
8. 不虚构运行结果；
9. 不提前扩展后续知识点；
10. 不修改无关 Feature；
11. 必要时更新 Sprint 进度；
12. 必要时更新 `CURRENT.md`；
13. 完成后运行文档构建检查。

---

# 14. AI 内容修改方式

第一阶段：

```text
人工要求 Codex 修改
↓
Codex 修改 README
↓
人工 Review
↓
Commit
```

这是当前默认模式。

后续可以扩展：

```text
Issue / workflow_dispatch
↓
AI Agent
↓
读取当前 Feature
↓
修改 README
↓
运行代码
↓
运行文档检查
↓
创建 Draft PR
↓
人工 Review
↓
Merge
↓
Pages 自动发布
```

AI **只允许创建 Draft PR**。

不允许：

```text
AI
↓
直接 push main
```

---

# 15. 文档维护提示词

新增：

```text
docs/prompts/maintain-feature.md
```

基础规则：

```text
你负责维护当前 Feature 的教学内容。

要求：

1. 先阅读当前 Feature 的 README.md 和 main.py。
2. 明确本 Feature 只解决一个核心知识点。
3. 运行 main.py，确认代码和输出正确。
4. 再维护 README.md。
5. README 遵循 docs/standards/feature-readme.md。
6. 从直觉 → 原理 → 数学 → 代码 → 实验 → LLM 应用逐步讲解。
7. 所有公式必须正确并解释变量。
8. 示例必须与实际代码一致。
9. 不虚构程序输出。
10. 不提前讲解后续 Feature。
11. 不修改无关目录。
12. 必要时更新 CURRENT.md 和 Sprint 进度。
13. 最后执行文档构建检查。
14. 输出修改摘要和验证结果。
```

---

# 16. README 与教学网站的职责

根 README：

```text
项目是什么
↓
为什么做
↓
如何开始
↓
学习路线
↓
在线教材地址
```

Feature README：

```text
教学章节
+
实验说明
```

网站：

```text
负责展示、导航、搜索
```

因此不存在：

```text
README 文档
+
website 文档
```

两套内容。

---

# 17. 第一阶段 MVP

第一阶段只完成基础设施。

新增：

```text
zensical.toml
pyproject.toml
uv.lock

scripts/prepare_docs.py

docs/standards/feature-readme.md
docs/prompts/maintain-feature.md

.github/workflows/docs.yml
```

修改：

```text
.gitignore
README.md
```

完成：

```text
README → 网站

Feature README → 网站章节

本地预览

Strict Build

Pull Request Build Check

Main 自动 Deploy

GitHub Pages 在线访问
```

---

# 18. 第二阶段

开始 Sprint 01 后逐渐增加：

```text
ROADMAP.md
CURRENT.md

sprint01-foundations/
├── README.md
├── feature01-forward/
├── feature02-loss/
└── ...
```

每完成一个 Feature：

```text
代码
↓
学习
↓
实验
↓
README
↓
Codex Review
↓
Commit
↓
Push
↓
网站更新
```

---

# 19. 第三阶段

等整个工作流稳定后再考虑：

```text
AI Draft PR
自动目录生成
自动前后章节导航
知识点索引
Glossary
公式索引
知识卡片
全文搜索增强
学习进度展示
```

这些都不是 MVP 必需功能。

---

# 20. 第一版明确不做

暂不增加：

* 后端；
* 数据库；
* CMS；
* 登录；
* 评论；
* AI Build API；
* AI 自动 Merge；
* 独立博客系统；
* 第二套教学 Markdown；
* 复杂主题开发；
* 在线运行 Python。

保持：

```text
Git
+
Markdown
+
Python
+
Zensical
+
GitHub Actions
+
GitHub Pages
```

---

# 21. 完成标准

MVP 完成后必须满足：

| 项目              | 标准             |
| --------------- | -------------- |
| 内容唯一来源          | Feature README |
| 本地预览            | ✅              |
| Strict Build    | ✅              |
| PR 自动检查         | ✅              |
| Main 自动部署       | ✅              |
| GitHub Pages    | ✅              |
| 图片正常显示          | ✅              |
| 数学公式            | ✅              |
| Mermaid         | ✅              |
| 站内搜索            | ✅              |
| Codex 内容规范      | ✅              |
| 网站 Build 不依赖 AI | ✅              |

最终目标：

```text
学习知识
      ↓
编写实验
      ↓
沉淀 README
      ↓
Git 管理
      ↓
AI 辅助维护
      ↓
自动发布
      ↓
形成自己的 LLM 在线教材
```

## 推荐 Commit

```text
feat(docs): add learning site and GitHub Pages deployment
```
