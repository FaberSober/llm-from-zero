# 提示词说明

## 生成知识卡片
比如下一张做 Loss，只需要给：
```
知识点：损失函数 Loss

核心内容：
预测值和真实值之间会存在误差，
Loss 用一个数衡量预测到底错了多少。

示例：
预测值 = 0.8
真实值 = 1.0
误差需要通过 Loss 量化。

重点解释：
- 什么是 Loss
- 为什么训练需要 Loss
- Loss 和 Gradient 的关系
- 常见 Loss
- 在 LLM 训练中的作用
```

剩下的版式、尺寸、标题、流程图、历史来源、LLM 作用、需要记住全部由母提示词约束。[.\prompts\gen_knowledge_card.md](.\prompts\gen_knowledge_card.md)