# AMR-Evol: Adaptive Modular Response Evolution Elicits Better Knowledge Distillation for Large Language Models in Code Generation

**Authors**: Luo, Ziyang and Li, Xin and Lin, Hongzhan and Ma, Jing and Bing, Lidong

**Abstract**:

The impressive performance of proprietary LLMs like GPT4 in code generation has led to a trend to replicate these capabilities in open-source models through knowledge distillation (e.g. Code Evol-Instruct). However, these efforts often neglect the crucial aspect of response quality, relying heavily on teacher models for direct response distillation. This paradigm, especially for complex instructions, can degrade the quality of synthesized data, compromising the knowledge distillation process. To this end, our study introduces the Adaptive Modular Response Evolution (AMR-Evol) framework, which employs a two-stage process to refine response distillation. The first stage, modular decomposition, breaks down the direct response into more manageable sub-modules. The second stage, adaptive response evolution, automatically evolves the response with the related function modules. Our experiments with three popular code benchmarks—HumanEval, MBPP, and EvalPlus—attests to the superiority of the AMR-Evol framework over baseline response distillation methods. By comparing with the open-source Code LLMs trained on a similar scale of data, we observed performance enhancements: more than +3.0 points on HumanEval-Plus and +1.0 points on MBPP-Plus, which underscores the effectiveness of our framework. Our codes are available at https://github.com/ChiYeungLaw/AMR-Evol.

**Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.66)

**Labels**: code generation, program synthesis, code model, training, source code model
