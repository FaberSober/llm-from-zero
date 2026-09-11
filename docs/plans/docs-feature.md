# Docs Feature 专项 PLAN

> 本文是“LLM From Zero 教学网站”功能的唯一实施计划和进度记录。每完成一个功能，应同步更新下方功能清单和对应阶段说明。

## 1. 功能目标

为项目增加一个适合长期阅读、复习和查阅的在线教学网站，并建立稳定的内容维护流程：

1. Feature README 继续作为教学内容唯一来源；
2. GitHub Actions 在代码 push 后自动构建文档；
3. `main` 分支构建成功后自动发布到 GitHub Pages；
4. Codex / 大模型按照统一规范维护每个 Feature 章节；
5. 内容修改通过 Pull Request 审核后再上线。

本功能不是独立博客系统，也不引入后端、数据库、CMS 或在线运行 Python。

## 2. 当前项目基础

当前仓库已经具备：

- 根目录 `README.md`；
- `sprint01-foundations/README.md`；
- 两个可独立运行的 Feature 及其 `README.md`、`main.py` 和图片资源；
- `uv run python main.py` 的 Feature 运行约定；
- `AGENTS.md` 中的 Feature 文档编写规则；
- `docs/prompts/` 下的知识卡片提示词。

当前尚未具备：

- `ROADMAP.md` 和 `CURRENT.md`；
- `pyproject.toml`、`uv.lock`；
- Zensical 配置；
- 文档装配脚本；
- GitHub Actions 工作流；
- GitHub Pages 发布配置。

## 3. 技术方案

| 能力 | 方案 |
| --- | --- |
| 文档框架 | Zensical |
| 内容源 | 各 Sprint / Feature 目录中的 `README.md` |
| 包管理 | UV、`pyproject.toml`、`uv.lock` |
| 文档装配 | `scripts/prepare_docs.py` |
| 代码托管 | GitHub |
| 网站托管 | GitHub Pages |
| CI/CD | GitHub Actions |
| 内容维护 | Codex / 大模型 |
| 内容审核 | Pull Request |
| 数学公式 | Markdown + KaTeX |
| 图示 | Mermaid |
| 搜索 | Zensical 内置搜索 |

核心原则：

> README 是唯一内容源，网站只是 README 的展示层。

Zensical 负责将临时文档目录构建为静态网站，支持 `serve`、`build` 和 `--strict` 检查；静态产物可以直接部署到 GitHub Pages。[Zensical Build](https://zensical.org/docs/usage/build/)、[Zensical 创建网站](https://zensical.org/docs/create-your-site/)

## 4. 目录与内容装配

### 4.1 计划中的目录

```text
llm-from-zero/
├── README.md
├── ROADMAP.md
├── CURRENT.md
├── AGENTS.md
│
├── sprint01-foundations/
│   ├── README.md
│   ├── feature01-forward/
│   └── feature02-loss/
│
├── docs/
│   ├── plans/
│   │   └── docs-feature.md
│   ├── standards/
│   │   └── feature-readme.md
│   └── prompts/
│       ├── gen_knowledge_card.md
│       └── maintain-feature.md
│
├── scripts/
│   └── prepare_docs.py
│
├── docs-build/
├── zensical.toml
├── pyproject.toml
├── uv.lock
└── .github/
    └── workflows/
        └── docs.yml
```

### 4.2 网站内容映射

| 网站内容 | Git 内容源 |
| --- | --- |
| 首页 | `README.md` |
| 学习路线 | `ROADMAP.md` |
| 当前进度 | `CURRENT.md` |
| Sprint 首页 | `sprintXX-xxx/README.md` |
| Feature 章节 | `sprintXX-xxx/featureXX-xxx/README.md` |
| 图片资源 | 对应 Feature 的 `assets/` |
| 完整代码 | GitHub 源文件链接 |

`prepare_docs.py` 只负责装配，不负责创作内容，也不成为第二套文档源。它将 README 复制到 `docs-build/`，并将临时目录中的 README 规范为 `index.md`，使目录链接和网站 URL 更自然：

```text
README.md
  → docs-build/index.md

ROADMAP.md
  → docs-build/ROADMAP.md

CURRENT.md
  → docs-build/CURRENT.md

sprint01-foundations/README.md
  → docs-build/sprint01-foundations/index.md

sprint01-foundations/feature01-forward/README.md
  → docs-build/sprint01/feature01-forward/index.md
```

Feature 的 `assets/` 复制到对应临时目录，保证现有相对图片链接继续有效。Python 源码不复制到网站目录，页面只保留必要代码片段和 GitHub 源文件链接。

### 4.3 导航策略

临时目录按以下规则生成：

```text
sprint01 → sprint02 → sprint03
feature01 → feature02 → feature03
```

通过目录名称中的序号保证默认导航顺序，避免每增加一个 Feature 都手动维护长导航配置。Zensical 默认可根据目录结构和 Markdown 页面生成导航，也支持后续为重要页面增加显式导航。[Zensical Navigation](https://zensical.org/docs/setup/navigation/)

## 5. Feature 教学内容规范

每个 Feature 只解决一个明确的核心知识问题。Feature README 推荐使用以下结构，不要求所有章节机械填满：

```markdown
# Feature 名称

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
## 15. 知识点说明
```

内容规则：

1. 先理解 `main.py`，再维护 README；
2. 示例、公式和输出必须与代码一致；
3. 运行代码后才能填写预期结果；
4. 变量、输入、输出和公式必须有解释；
5. 不虚构历史、实验结果或不存在的功能；
6. 不提前替代后续 Feature 的教学内容；
7. 不修改无关章节；
8. 保留正确的图片、代码和相对路径；
9. 在 README 末尾追加本 Feature 的知识点总结，作为复习和生成知识卡片的素材。

具体模板放在 `docs/standards/feature-readme.md`，大模型维护提示词放在 `docs/prompts/maintain-feature.md`。

## 6. 自动构建与发布流程

### 6.1 本地流程

```bash
uv sync
uv run python scripts/prepare_docs.py
uv run zensical serve
```

正式构建检查：

```bash
uv run python scripts/prepare_docs.py
uv run zensical build --strict --clean
```

构建产物目录为 `site/`，临时文档目录为 `docs-build/`，两者都不提交到 Git。

### 6.2 Pull Request

```text
Pull Request
  ↓
uv sync --locked
  ↓
prepare_docs.py
  ↓
zensical build --strict --clean
  ↓
通过 / 阻止合并
```

PR 只做构建检查，不发布正式网站。检查内容包括 Markdown、内部链接、图片路径、数学公式配置、Mermaid 代码块和导航结果。

### 6.3 Main 分支

```text
push main
  ↓
prepare_docs.py
  ↓
zensical build --strict --clean
  ↓
上传 Pages Artifact
  ↓
部署 GitHub Pages
```

GitHub Pages 的发布源设置为 `GitHub Actions`。工作流使用官方 Pages Artifact 和 Deploy Actions，并配置 `github-pages` 环境；只有构建 Job 成功后才执行部署。[GitHub Pages 自定义工作流](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)

预计网址：

```text
https://fabersober.github.io/llm-from-zero/
```

### 6.4 手动发布

保留 `workflow_dispatch`，用于以下情况：

- 重新发布当前 `main`；
- 修复 Pages 环境后重新部署；
- 验证发布流程而不新增内容提交。

## 7. 大模型内容维护流程

大模型不参与网站 Build。Build 必须保持确定、可重复，并且不依赖外部 AI API。

### 7.1 默认模式

每完成一个 Feature，按照以下顺序维护：

```text
修改 main.py
  ↓
运行 Feature 代码
  ↓
Codex 读取相关上下文
  ↓
维护 Feature README
  ↓
更新 Sprint / CURRENT（必要时）
  ↓
运行文档构建
  ↓
人工 Review
  ↓
Commit / Push
```

维护当前 Feature 时只读取必要上下文：

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

### 7.2 大模型输出边界

大模型可以：

- 完善当前 Feature 的教学解释；
- 校正公式、变量说明和示例；
- 根据真实运行结果补充输出；
- 更新当前 Sprint 的学习进度；
- 更新 `CURRENT.md`；
- 提供文档和代码 Review 摘要。

大模型不可以：

- 直接 push `main`；
- 自动合并自己的修改；
- 在 Build 阶段改写 Markdown；
- 修改无关 Feature；
- 为填充模板而增加未学习的知识点；
- 虚构代码运行结果。

### 7.3 后续自动化模式

未来可增加手动触发或 Issue 标签触发的 AI 工作流：

```text
Issue / workflow_dispatch
  ↓
大模型读取当前 Feature
  ↓
修改 README
  ↓
运行代码和文档检查
  ↓
创建 Draft PR
  ↓
人工审核并合并
  ↓
Pages 自动发布
```

AI 只创建 Draft PR，不直接修改 `main`。该阶段需要额外的 API Key、成本控制、权限隔离和提示词注入防护，因此不纳入 MVP。

## 8. 实施阶段

### 阶段 0：方案固化

产物为当前专项 PLAN，明确技术栈、内容源、装配方式、发布边界和 AI 维护边界。

### 阶段 1：文档基础设施

完成 UV 依赖、Zensical 配置、临时文档装配、资源复制、忽略规则和本地预览。先使用当前已有的根 README、Sprint README 和两个 Feature README 验证链路。

### 阶段 2：自动构建与 GitHub Pages

完成 PR 构建检查、`main` 自动发布、手动发布和 GitHub Pages 环境配置，验证预计网址可以访问。

### 阶段 3：内容规范与进度维护

增加 `ROADMAP.md`、`CURRENT.md`、Feature README 标准和大模型维护提示词，并逐步让后续章节遵循统一规范。

### 阶段 4：可选增强

在基础工作流稳定后，再评估 AI Draft PR、知识点索引、术语表、公式索引、前后章节导航和学习进度展示。

当前实施状态：

- 阶段 1 的文档基础设施已完成并通过本地构建；
- 阶段 2 的工作流文件已完成，等待 GitHub Pages 设置和远端 Actions 验证；
- 阶段 3 的 README 规范和大模型维护提示词已完成；
- 阶段 4 暂不启动。

## 9. MVP 完成标准

| 项目 | 完成标准 |
| --- | --- |
| 内容唯一来源 | Feature README |
| 临时文档目录 | 构建时自动生成，未提交到 Git |
| 本地预览 | `uv run zensical serve` 可用 |
| Strict Build | `uv run zensical build --strict --clean` 通过 |
| PR 检查 | 自动构建，不发布 |
| Main 部署 | 构建成功后自动发布 |
| 图片 | Feature assets 正常显示 |
| 数学公式 | KaTeX 正常渲染 |
| 图示 | Mermaid 正常渲染 |
| 搜索 | 网站内置搜索可用 |
| 内容维护 | Codex 按规范维护 Feature README |
| Build 独立性 | 网站 Build 不调用 AI API |
| 发布地址 | GitHub Pages 可访问 |

## 10. 明确不纳入 MVP

- 后端、数据库、CMS、登录和评论；
- 独立博客系统；
- 在线运行 Python；
- 网站维护第二套 Markdown；
- Build 阶段调用 AI API；
- AI 自动 Merge；
- 复杂主题和大规模前端定制；
- 增强中文全文检索；
- AI Draft PR 自动化；
- 知识点、公式和术语的高级索引。

## 11. 功能清单与进度

进度标记约定：❌未完成、🟡进行中、🔍验证中、⏸️已暂停、🚫已阻塞、🔄待返工、👀待确认、🕒待处理、⚪已取消、✅已完成。

| 模块 | 功能 | 功能详情 | 当前规划 | 进度 |
| --- | --- | --- | --- | --- |
| 规划 | 专项 PLAN | 固化目标、边界、技术方案和验收标准 | 执行开发 | ✅已完成 |
| 内容体系 | README 唯一内容源 | 网站不复制维护第二套教学文章 | 执行开发 | ✅已完成 |
| 内容体系 | ROADMAP | 维护 Sprint 和 Feature 学习路线 | 执行开发 | ✅已完成 |
| 内容体系 | CURRENT | 展示当前学习进度和最近完成内容 | 执行开发 | ✅已完成 |
| 内容规范 | Feature README 模板 | 统一目标、原理、公式、实验和复习总结 | 执行开发 | ✅已完成 |
| 内容规范 | 大模型维护提示词 | 固定上下文范围、输出边界和验证要求 | 执行开发 | ✅已完成 |
| 构建基础 | UV 文档环境 | 增加 `pyproject.toml` 和 `uv.lock` | 执行开发 | ✅已完成 |
| 构建基础 | 临时文档目录 | 使用 `docs-build/` 隔离网站输入 | 执行开发 | ✅已完成 |
| 构建基础 | 文档装配脚本 | 复制 README、重排目录并复制 assets | 执行开发 | ✅已完成 |
| 构建基础 | 构建产物隔离 | 忽略 `docs-build/` 和 `site/` | 执行开发 | ✅已完成 |
| 网站配置 | Zensical 配置 | 配置站点信息、源目录、主题和站点 URL | 执行开发 | ✅已完成 |
| 网站配置 | 自动目录导航 | 按 Sprint / Feature 编号生成稳定顺序 | 执行开发 | ✅已完成 |
| 网站能力 | KaTeX | 支持教学公式的行内和块级渲染 | 执行开发 | 🔍验证中 |
| 网站能力 | Mermaid | 支持流程图和结构图代码块 | 执行开发 | 🔍验证中 |
| 网站能力 | 内置搜索 | 支持按章节查找教学内容 | 执行开发 | ✅已完成 |
| 网站能力 | 本地预览 | 使用 `uv run zensical serve` 实时查看 | 执行开发 | ✅已完成 |
| 质量检查 | Strict Build | 检查 Markdown、链接、资源和构建配置 | 执行开发 | ✅已完成 |
| CI/CD | PR 构建检查 | PR 构建成功后才允许进入审核流程 | 执行开发 | 🔍验证中 |
| CI/CD | Main 自动部署 | `main` push 后构建并发布 Pages | 执行开发 | 🔍验证中 |
| CI/CD | 手动部署 | 通过 `workflow_dispatch` 重新发布 | 执行开发 | 🔍验证中 |
| 托管 | GitHub Pages 配置 | 设置 Actions 为发布源和 `github-pages` 环境 | 执行开发 | 🕒待处理 |
| 托管 | 在线地址 | 验证 `fabersober.github.io/llm-from-zero` 可访问 | 执行开发 | 🕒待处理 |
| 内容协作 | Codex 手动维护 | 每个 Feature 完成后更新对应 README | 执行开发 | ✅已完成 |
| 内容协作 | Draft PR | 大模型修改内容后只创建待审核 PR | 未来版本规划 | 🕒待处理 |
| 内容索引 | Glossary | 自动维护术语表和概念关系 | 未来版本规划 | 🕒待处理 |
| 内容索引 | Formula Index | 汇总公式并链接回对应章节 | 未来版本规划 | 🕒待处理 |
| 内容索引 | 前后章节导航 | 自动生成上一章、下一章入口 | 未来版本规划 | 🕒待处理 |
| 学习体验 | 学习进度展示 | 在网站中展示 Sprint / Feature 完成状态 | 未来版本规划 | 🕒待处理 |
| 内容扩展 | 知识卡片索引 | 汇总各 Feature 的图片知识卡片 | 未来版本规划 | 🕒待处理 |

## 12. 建议提交 Comment

基础设施完成后的建议提交信息：

```text
feat(docs): add learning site and GitHub Pages deployment
```

内容维护规范完成后的建议提交信息：

```text
docs: add feature content maintenance workflow
```
