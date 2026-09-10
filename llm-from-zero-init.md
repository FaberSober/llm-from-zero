# LLM From Zero

> 从零开始理解、实现并训练一个小型大语言模型（LLM），通过可独立运行的小实验逐步掌握大模型的底层原理。

---

## 1. 项目目标

本项目不是为了快速调用现成大模型，而是为了从底层逐步理解：

- 神经网络如何进行前向计算；
- Loss 是什么，以及为什么模型需要 Loss；
- Gradient、Backpropagation、Gradient Descent 的工作原理；
- 文本如何转换为 Token；
- Language Model 为什么本质上是在预测下一个 Token；
- Embedding 如何表示 Token；
- Self-Attention 如何让 Token 之间建立联系；
- Transformer Block 如何工作；
- GPT 如何从多个 Transformer Block 组成；
- 一个模型如何从随机参数开始训练；
- Pretraining、SFT、DPO 等训练阶段分别解决什么问题；
- 大模型训练中的优化器、学习率、混合精度、Checkpoint 等工程机制；
- RoPE、RMSNorm、GQA、KV Cache、Flash Attention、MoE 等现代 LLM 技术。

最终目标：

1. 自己实现一个 TinyGPT；
2. 使用真实文本数据完成预训练；
3. 支持文本生成；
4. 完成一次简单的 SFT；
5. 将 Base Model 转换为可进行简单对话的 Chat Model；
6. 建立一套可以长期复习的大模型知识与实验仓库。

---

## 2. 项目定位

本仓库同时承担三个角色：

### 2.1 学习项目

通过逐步编码理解大模型原理，而不是只阅读文章或调用框架。

### 2.2 可执行速查手册

每个 Feature 都是一个独立的小实验。

例如想复习 Loss：

```text
sprint01-foundations/
└── feature02-loss/
```

进入目录即可查看说明并直接运行代码。

### 2.3 综合实验仓库

在掌握单个知识点之后，通过 `experiments/` 将不同能力组合起来，最终训练完整 GPT。

---

## 3. 推荐目录结构

```text
llm-from-zero/
├── README.md
├── AGENTS.md
├── ROADMAP.md
│
├── docs/
│   ├── glossary.md
│   ├── formulas.md
│   └── learning-notes.md
│
├── sprint01-foundations/
│   ├── README.md
│   ├── feature01-forward/
│   ├── feature02-loss/
│   ├── feature03-gradient/
│   ├── feature04-backprop/
│   └── feature05-gradient-descent/
│
├── sprint02-neural-network/
│   ├── README.md
│   ├── feature01-neuron/
│   ├── feature02-activation/
│   ├── feature03-mlp/
│   └── feature04-training-loop/
│
├── sprint03-language-model/
│   ├── README.md
│   ├── feature01-character-tokenizer/
│   ├── feature02-bigram/
│   ├── feature03-embedding/
│   └── feature04-language-model-loss/
│
├── sprint04-attention/
│   ├── README.md
│   ├── feature01-dot-product/
│   ├── feature02-query-key-value/
│   ├── feature03-self-attention/
│   ├── feature04-causal-attention/
│   └── feature05-multi-head-attention/
│
├── sprint05-transformer/
├── sprint06-tiny-gpt/
├── sprint07-pretraining/
├── sprint08-tokenizer/
├── sprint09-sft/
├── sprint10-mini-chat-model/
│
└── experiments/
    ├── tiny-gpt-1m/
    ├── tiny-gpt-10m/
    ├── shakespeare-gpt/
    └── tinystories-gpt/
```

---

## 4. Sprint 与 Feature 的定义

### Sprint

一个 Sprint 表示一个完整的学习阶段。

例如：

```text
sprint04-attention
```

表示整个 Sprint 都围绕 Attention 学习。

### Feature

一个 Feature 只解决一个明确的问题。

例如：

```text
feature02-loss
```

目标只需要回答：

> Loss 是什么？如何计算？为什么训练模型需要它？

不要在一个 Feature 中塞入过多知识点。

---

## 5. Feature 标准结构

简单 Feature：

```text
feature02-loss/
├── README.md
└── main.py
```

稍复杂 Feature：

```text
feature03-self-attention/
├── README.md
├── main.py
├── experiment.py
└── notes.md
```

各文件职责：

| 文件 | 用途 |
|---|---|
| `README.md` | 解释知识点、公式、输入输出和运行方式 |
| `main.py` | 最小可运行代码 |
| `experiment.py` | 对比实验或参数实验，可选 |
| `notes.md` | 自己的理解、疑问和总结，可选 |

---

## 6. Feature README 模板

每个 Feature 的 `README.md` 尽量采用统一结构。

```markdown
# Feature 名称

## 1. 这是什么

用简洁语言解释概念。

## 2. 为什么需要它

解释它解决了什么问题。

## 3. 核心原理

描述最关键的逻辑。

## 4. 核心公式

必要时给出公式。

## 5. 最小示例

说明代码如何运行。

## 6. 输入与输出

描述输入和预期输出。

## 7. 在 LLM 中的作用

说明该知识点最终会出现在大模型哪个位置。

## 8. 我需要记住什么

只保留 3~5 个最关键结论。

## 9. 相关知识

链接前置或后续 Feature。
```

---

## 7. 学习原则

### 7.1 一个目录只学习一个问题

避免：

```text
feature-attention/
├── tokenizer.py
├── dataset.py
├── model.py
├── training.py
├── inference.py
└── utils.py
```

推荐：

```text
feature03-self-attention/
├── README.md
└── main.py
```

---

### 7.2 优先最小实现

优先：

```python
q = x @ wq
k = x @ wk
v = x @ wv
```

而不是一开始封装复杂类库。

先理解，再工程化。

---

### 7.3 允许重复代码

这是学习仓库，不是生产项目。

这里不强制追求 DRY。

优先级：

```text
可理解
>
独立
>
可运行
>
代码复用
```

每个 Feature 应尽量可以独立阅读。

---

### 7.4 先手写，再使用高级 API

例如学习 Cross Entropy 时：

第一步：

```text
手动计算概率
→ 手动计算 log
→ 手动计算 loss
```

第二步才使用：

```python
torch.nn.functional.cross_entropy
```

学习 Attention 时同样如此。

---

### 7.5 不让 AI 直接代写核心算法

Codex 可以：

- 解释报错；
- Review 代码；
- 补充测试；
- 优化注释；
- 检查数学实现；
- 帮助整理 README；
- 检查代码风格。

但以下内容应尽量自己实现：

- Gradient；
- Backpropagation；
- Attention；
- Transformer；
- GPT；
- Training Loop。

---

## 8. Git 使用约定

项目采用 Git 管理。

前期保持单主线：

```text
main
```

不需要每个 Feature 都创建分支。

推荐 Commit：

```text
feat(sprint01): add forward computation example
feat(sprint01): add mse loss example
feat(sprint01): implement numerical gradient
feat(sprint01): implement backpropagation
feat(sprint01): add gradient descent experiment
```

大型实验可以单独使用分支，例如：

```text
experiment/gpt-20m
experiment/rope
experiment/moe
```

---

## 9. 技术栈

前期只使用必要工具。

### Phase 1

```text
Python
NumPy
```

### Phase 2

```text
Python
PyTorch
```

### Phase 3

逐步引入：

```text
tokenizers
datasets
tensorboard / wandb
accelerate
torch distributed
```

原则：

> 能自己写出来的核心逻辑，先不要通过高级框架隐藏。

---

# 10. 总体 Roadmap

## Sprint 01：Foundations

目标：理解训练神经网络最基础的数学和计算过程。

- [ ] Forward Computation
- [ ] Loss
- [ ] Numerical Gradient
- [ ] Chain Rule
- [ ] Backpropagation
- [ ] Gradient Descent
- [ ] Learning Rate

完成标准：

> 能解释并手写一个最小的参数优化过程。

---

## Sprint 02：Neural Network

目标：理解一个基础神经网络是如何组成和训练的。

- [ ] Neuron
- [ ] Linear Layer
- [ ] Activation Function
- [ ] MLP
- [ ] Parameters
- [ ] Training Loop
- [ ] Overfitting / Underfitting

完成标准：

> 不依赖高级训练框架，完成一个简单 MLP 的训练。

---

## Sprint 03：Language Model

目标：第一次真正实现语言模型。

- [ ] Character Tokenizer
- [ ] Vocabulary
- [ ] Token ID
- [ ] Bigram Language Model
- [ ] Logits
- [ ] Softmax
- [ ] Cross Entropy
- [ ] Sampling

完成标准：

> 训练一个能够生成简单字符序列的 Bigram 模型。

---

## Sprint 04：Attention

目标：彻底理解 Self-Attention。

- [ ] Dot Product
- [ ] Query
- [ ] Key
- [ ] Value
- [ ] Attention Score
- [ ] Softmax
- [ ] Self-Attention
- [ ] Causal Mask
- [ ] Scaled Dot-Product Attention
- [ ] Multi-Head Attention

完成标准：

> 不调用 PyTorch MultiheadAttention，自己实现 Causal Self-Attention。

---

## Sprint 05：Transformer

目标：理解 Transformer Block。

- [ ] LayerNorm
- [ ] Residual Connection
- [ ] Feed Forward Network
- [ ] Transformer Block
- [ ] Stacking Blocks
- [ ] Position Information

完成标准：

> 自己实现一个完整 Transformer Block。

---

## Sprint 06：TinyGPT

目标：将所有组件组合成 GPT。

- [ ] Token Embedding
- [ ] Position Embedding
- [ ] Transformer Block
- [ ] LM Head
- [ ] GPT Forward
- [ ] Loss
- [ ] Generate
- [ ] Temperature
- [ ] Top-K

完成标准：

> 完成一个约 1M~10M 参数的 TinyGPT。

---

## Sprint 07：Pretraining

目标：真正训练 GPT。

- [ ] Dataset
- [ ] DataLoader
- [ ] Batch
- [ ] Context Length
- [ ] AdamW
- [ ] Weight Decay
- [ ] Learning Rate Scheduler
- [ ] Warmup
- [ ] Gradient Clipping
- [ ] Validation
- [ ] Checkpoint
- [ ] Resume Training

完成标准：

> 在真实文本数据集上训练 TinyGPT，并观察 Loss 持续下降。

---

## Sprint 08：Tokenizer

目标：理解现代 LLM Tokenizer。

- [ ] Character Tokenizer
- [ ] Word Tokenizer
- [ ] Byte
- [ ] BPE
- [ ] Byte-level BPE
- [ ] Vocabulary Training
- [ ] Encode
- [ ] Decode

完成标准：

> 自己实现或训练一个简单 BPE Tokenizer。

---

## Sprint 09：SFT

目标：理解 Base Model 如何变成 Instruction Model。

- [ ] Instruction Dataset
- [ ] Prompt Format
- [ ] Chat Template
- [ ] Supervised Fine-Tuning
- [ ] Loss Mask
- [ ] Evaluation

完成标准：

> 对自己训练的小模型完成一次简单 SFT。

---

## Sprint 10：Mini Chat Model

目标：完成一条最小 LLM 全流程。

```text
Raw Text
↓
Tokenizer
↓
Pretraining
↓
Base Model
↓
Instruction Dataset
↓
SFT
↓
Chat Model
↓
Inference
```

完成标准：

> 得到一个能够完成简单问答的个人 Mini Chat Model。

---

# 11. 后续高级 Roadmap

完成基础路线后，再继续学习现代 LLM。

- [ ] RoPE
- [ ] RMSNorm
- [ ] SwiGLU
- [ ] GQA
- [ ] MQA
- [ ] KV Cache
- [ ] Flash Attention
- [ ] Mixed Precision
- [ ] Gradient Accumulation
- [ ] Gradient Checkpointing
- [ ] Distributed Training
- [ ] DDP
- [ ] FSDP
- [ ] LoRA
- [ ] QLoRA
- [ ] DPO
- [ ] RLHF / RL
- [ ] Quantization
- [ ] MoE
- [ ] Llama Architecture
- [ ] Qwen Architecture
- [ ] DeepSeek Architecture

---

# 12. 综合实验

Feature 用于学习单点知识。

`experiments/` 用于组合多个知识。

推荐实验：

```text
experiments/
├── tiny-gpt-1m/
├── tiny-gpt-10m/
├── shakespeare-gpt/
├── tinystories-gpt/
├── bpe-tokenizer/
└── mini-chat-model/
```

---

# 13. 推荐参考项目

建议按以下顺序学习：

```text
micrograd
↓
makemore
↓
build-nanogpt
↓
nanoGPT
↓
nanochat
↓
现代 LLM 架构
```

主要参考：

- `karpathy/micrograd`
- `karpathy/makemore`
- `karpathy/build-nanogpt`
- `karpathy/nanoGPT`
- `karpathy/nanochat`
- `rasbt/LLMs-from-scratch`

原则：

> 参考代码用于理解，不直接复制整个实现。

---

# 14. Sprint 01 初始规划

建议第一个 Sprint 目录：

```text
sprint01-foundations/
├── README.md
├── feature01-forward/
├── feature02-loss/
├── feature03-gradient/
├── feature04-chain-rule/
├── feature05-backprop/
├── feature06-gradient-descent/
└── feature07-learning-rate/
```

推荐执行顺序：

```text
Forward
↓
Loss
↓
Gradient
↓
Chain Rule
↓
Backpropagation
↓
Gradient Descent
↓
Learning Rate
```

Sprint 01 不追求“大模型”。

唯一目标：

> 理解一个参数究竟是如何通过 Loss 和 Gradient 被训练改变的。

---

# 15. Codex 协作规则

Codex 在本仓库中的角色是“辅助教师和代码 Reviewer”，而不是主要实现者。

开始每个 Feature 时：

1. 先解释当前 Feature 的目标；
2. 给出最小实验要求；
3. 不直接生成完整答案；
4. 优先让我自己实现；
5. 我完成后再 Review；
6. Review 时重点检查：
   - 原理是否正确；
   - 数学计算是否正确；
   - 是否存在隐藏 API 替代核心逻辑；
   - 代码是否足够简单；
7. 完成后协助补充 README；
8. 更新 Sprint 进度。

不要：

- 为了工程化过度抽象；
- 引入不必要依赖；
- 创建复杂架构；
- 对无关目录进行重构；
- 一次实现多个后续 Feature。

---

# 16. 项目成功标准

这个项目不是以代码量衡量成功。

最终应能够不看资料解释下面这条链路：

```text
文本
↓
Token
↓
Embedding
↓
Transformer
↓
Logits
↓
Softmax
↓
Next Token Probability
↓
Cross Entropy Loss
↓
Backpropagation
↓
Gradient
↓
Optimizer
↓
Parameter Update
↓
模型能力提升
```

并且能够亲自训练出一个可以生成文本的小型 GPT。

---

## Current

当前阶段：

```text
Sprint 01 - Foundations
```

下一步：

```text
feature01-forward
```

从最简单的前向计算开始。
