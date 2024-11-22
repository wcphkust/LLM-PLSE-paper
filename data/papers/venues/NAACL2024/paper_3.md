# PaD: Program-aided Distillation Can Teach Small Models Reasoning Better than Chain-of-thought Fine-tuning

**Authors**: Zhu, Xuekai and Qi, Biqing and Zhang, Kaiyan and Long, Xinwei and Lin, Zhouhan and Zhou, Bowen

**Abstract**:

While large language models (LLMs) excel in various natural language processing tasks, their huge size and the inaccessibility of parameters present challenges for practical deployment. Previous studies try to distill task-specific ability from LLMs to smaller models, using data synthesis and chain-of-thought (CoT) fine-tuning. However, synthetic CoT data often contains faulty reasoning, which deteriorates the quality of distillation, especially in reasoning capabilities. In this work, we propose Program-aided Distillation (PaD), which introduces reasoning programs to suppress the errors in distilled data, and thus achieves better distillation quality for reasoning tasks. In PaD, we utilize the reasoning program to substitute the CoT, allowing automated error checking of synthetic data. Further, through error injecting and further training, the small distilling model could iteratively self-refine the reasoning. Moreover, we conduct a step-wise beam search by step-by-step verifying to acquire more exact reasoning chains. We evaluate PaD on arithmetic reasoning, symbolic reasoning, and general ability.Experimental results demonstrate that smaller models using PaD can not only outperform certain LLMs (e.g., LLaMA-1 13B) but also achieve strong improvement over baselines with a significantly smaller scale of parameters and data. The source code is publicly available athttps://github.com/Xuekai-Zhu/pad.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2024.naacl-long.142)

**Labels**: [prompt strategy](../../labels/prompt_strategy.md), [reason with code](../../labels/reason_with_code.md)
