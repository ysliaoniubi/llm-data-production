# llm-data-production

大模型训练数据生产与评测作品集。

5 年一线 AI 数据生产经验（2021 至今），覆盖从标注员、质检专员、标注项目组长到远程专家数据生产者的完整链路。本仓库沉淀可复用的规范、样例与质检方法，重点展示：**把模糊需求转成可执行、可质检的任务规范**。

求职方向：大模型评测 / AI 训练与训练数据生产（Xpert 专家社区及同类）。

## 能做什么

| 方向 | 内容 | 对应目录 |
|---|---|---|
| 回复质量评测 | 分维度打分、依据充分的评测结论、一次通过率高于均值 | [samples/eval](samples/eval/) · [docs/01](docs/01-回复质量评测手册.md) |
| SFT 指令 / 多轮对话 | 指令数据编写、多轮改写、边界拒答、格式可控 | [samples/sft](samples/sft/) · [docs/02](docs/02-SFT对话数据规范.md) |
| RLHF 偏好排序 | 成对/列表排序、维度拆解、稳定偏好判断 | [samples/rlhf](samples/rlhf/) · [docs/03](docs/03-RLHF偏好标注SOP.md) |
| 出题与评分细则 | 常识推理、文本写作，参考答案 + 可执行 rubric | [samples/questions](samples/questions/) · [docs/04](docs/04-出题与评分细则设计.md) |
| 数据采集规范 | 采集目标、来源、去重、合规、验收标准 | [docs/05](docs/05-数据采集规范.md) |
| 标注 SOP 与质检 | SOP 编写、badcase 库、抽检与返修闭环 | [templates](templates/) · [qa](qa/) |

## 经历摘要

- **大模型评测与专家数据生产**（2024.06 – 至今，远程项目制，多家头部 AI 数据平台）：按学科与场景出题、撰写参考答案与评分细则；独立完成模型回复评测与推理质量评估；一次通过率长期高于项目均值。
- **AI 训练师 / 标注项目组长**（2022.10 – 2024.05，深圳智数科技，远程）：带 10 余人团队，制定规范、分配任务、培训与质检；沉淀 20 余份 SOP 与 badcase 案例库；按时交付率 95%+。
- **AI 数据标注员 → 质检专员**（2021.07 – 2022.09，长沙君泓）：文本 / 对话 / 图像标注 10 万+ 条；晋升质检后抽检合格率稳定 98%+。

熟悉 GPT、Claude、GLM、DeepSeek、Qwen 的能力边界与表达风格；工具：Label Studio 及主流标注平台。

## 快速导航

1. 想看**评测怎么打分、依据怎么写** → [samples/eval/case-01](samples/eval/case-01-指令遵循-多条件写作.md)
2. 想看**SFT 多轮对话长什么样** → [samples/sft/writing_multi_turn.jsonl](samples/sft/writing_multi_turn.jsonl)
3. 想看**RLHF 排序和理由** → [samples/rlhf/preference_sample.jsonl](samples/rlhf/preference_sample.jsonl)
4. 想看**出题 + 评分细则** → [samples/questions/文本写作题.md](samples/questions/文本写作题.md)
5. 想看**怎么带团队、控质量** → [qa/质检checklist.md](qa/质检checklist.md)

## 使用说明

- 样例中的模型回复为**构造的典型 badcase / goodcase**，用于展示评测与标注方法，不代表任何厂商的真实输出。
- 规范可直接改造成项目 SOP；换模型、换学科时只需替换维度权重与正反例。
- 所有内容为原创方法论与示范数据，不含前雇主未公开项目细节。

## 联系

廖壹顺 · 浙江湖州 · 可远程 · 随时到岗  
邮箱：ysliao666@gmail.com  
电话：18874976145
