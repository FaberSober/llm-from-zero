# Feature 04 - Chain Rule

## 1. 本章目标

理解当 Loss 通过多个计算步骤依赖一个参数时，如何用 Chain Rule 把各步骤的局部导数相乘，得到 Loss 对该参数的梯度。

本章只研究一条最小计算链：

~~~text
weight → prediction → loss
~~~

本章暂不实现多节点梯度汇总、完整反向传播或参数更新。

## 2. 这是什么

Chain Rule（链式法则）用于计算复合函数的导数。如果一个变量通过多个函数影响 Loss，就把每一步的局部导数相乘。

Feature 03 计算了 Loss 对预测值的梯度。本章继续沿着计算链向前追溯，计算 Loss 对 `weight` 的梯度。

## 3. 为什么需要它

模型训练最终要调整参数，而不是直接修改预测值。只知道 `Loss` 对预测值的变化方向还不够，还要知道参数变化如何影响预测值。

Chain Rule 正好连接了这两件事：

- Loss 对预测值的影响；
- 参数对预测值的影响；
- Loss 对参数的最终影响。

## 4. 核心原理

对于一条没有分支的计算链：

~~~text
x → y → L
~~~

有：

$$
\frac{\partial L}{\partial x}
=\frac{\partial L}{\partial y}
\times
\frac{\partial y}{\partial x}
$$

每个导数只描述相邻两个变量之间的局部关系，连乘后才得到起点变量对最终 Loss 的影响。

## 5. 数学表示

本 Demo 使用一个权重和一个输入值：

$$
\hat{y}=w x
$$

Loss 使用单样本平方误差：

$$
L=(\hat{y}-y)^2
$$

分别计算两段局部导数：

$$
\frac{\partial L}{\partial \hat{y}}
=2(\hat{y}-y)
$$

$$
\frac{\partial \hat{y}}{\partial w}=x
$$

应用 Chain Rule：

$$
\frac{\partial L}{\partial w}
=\frac{\partial L}{\partial \hat{y}}
\times
\frac{\partial \hat{y}}{\partial w}
=2(\hat{y}-y)x
$$

本章使用标量和一条路径，重点是理解“局部导数连乘”，不是构建通用自动求导系统。

## 6. 手工计算

取：

- 权重 `w = 1.5`
- 输入 `x = 2.0`
- 目标值 `y = 5.0`

前向计算：

1. 预测值：`ŷ = w × x = 1.5 × 2.0 = 3.0`
2. 误差：`ŷ - y = 3.0 - 5.0 = -2.0`
3. Loss：`(-2.0)² = 4.0`

反向计算局部导数：

1. `∂L/∂ŷ = 2 × (-2.0) = -4.0`
2. `∂ŷ/∂w = x = 2.0`
3. `∂L/∂w = (-4.0) × 2.0 = -8.0`

最终梯度为 `-8.0`。它表示在当前位置附近，增加 `weight` 会让 Loss 下降。

## 7. 输入与输出

输入：

- 一个权重 `weight`；
- 一个输入值 `input`；
- 一个目标值 `target`。

输出：

- 前向计算得到的 `prediction` 和 `loss`；
- 两段局部导数；
- 通过 Chain Rule 得到的 `gradient_wrt_weight`；
- 有限差分得到的完整梯度近似值；
- 权重向两个方向小幅变化后的 Loss。

## 8. 运行 Demo

在本目录执行：

~~~bash
uv run python main.py
~~~

预期输出：

~~~text
weight = 1.5
input = 2.0
prediction = 3.0
target = 5.0
loss = 4.00
d_loss_d_prediction = -4.00
d_prediction_d_weight = 2.00
gradient_wrt_weight = -8.00
finite_difference_gradient = -8.000000
loss_if_weight_plus_0.1 = 3.24
loss_if_weight_minus_0.1 = 4.84
~~~

有限差分只用于检查连乘结果；本 Demo 的核心实现是显式计算两段导数并相乘。

## 9. 在 LLM 中的作用

神经网络可以看成许多计算函数串联而成。LLM 通过前向计算得到输出和 Loss 后，Chain Rule 让梯度能够沿着计算链从输出逐步传回参数。

真实 LLM 会有大量参数、分支和重复使用的中间变量。如何系统地保存中间结果、沿计算图反向计算并汇总梯度，将在 Backpropagation 中学习。

## 10. 常见误区

- `∂L/∂ŷ` 是输出梯度，不等于 `∂L/∂w`；
- 一条连续路径上的局部导数需要相乘，不是相加；
- 导数的方向必须保持一致，不能把不同变量的导数混用；
- Chain Rule 只负责计算梯度，不会自动更新参数；
- 本例没有 bias 和分支，不能代表完整神经网络的全部反向计算。

## 11. 我需要记住什么

1. 复合函数的导数可以拆成相邻步骤的局部导数。
2. 一条路径上的局部导数连乘，得到起点变量对最终 Loss 的梯度。
3. `∂L/∂ŷ` 经过 `∂ŷ/∂w` 才能得到 `∂L/∂w`。
4. Chain Rule 是把输出梯度传到参数的数学基础。
5. 梯度计算完成后，还需要 Gradient Descent 才会真正更新参数。

## 12. 配套代码

- `main.py`：手写线性预测、平方 Loss、局部导数和 Chain Rule 验证。

## 13. 前置知识

- [Feature 01 - Forward Computation](../feature01-forward/)
- [Feature 02 - Loss](../feature02-loss/)
- [Feature 03 - Gradient](../feature03-gradient/)

## 14. 下一章

[Feature 05 - Backpropagation](../feature05-backprop/)

下一章将学习：如何在包含多个节点的计算图中，系统地进行反向计算并处理梯度汇总。

## 15. 知识点说明

- 核心概念：Chain Rule 将复合计算拆成相邻步骤的局部导数，并沿路径连乘。
- 关键公式：`∂L/∂w = (∂L/∂ŷ) × (∂ŷ/∂w)`。
- Demo 链路：`weight → prediction → loss`，其中 `ŷ=wx`、`L=(ŷ-y)²`。
- 实验关系：`w=1.5`、`x=2.0`、`y=5.0` 时，`∂L/∂ŷ=-4.0`、`∂ŷ/∂w=2.0`、`∂L/∂w=-8.0`。
- 边界：本 Feature 只演示单路径连乘，不处理分支、梯度累加、自动求导或参数更新。
