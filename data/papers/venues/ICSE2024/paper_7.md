# When Neural Code Completion Models Size up the Situation: Attaining Cheaper and Faster Completion through Dynamic Model Inference

**Authors**: Sun, Zhensu and Du, Xiaoning and Song, Fu and Wang, Shangwen and Li, Li

**Abstract**:

Leveraging recent advancements in large language models, modern neural code completion models have demonstrated the capability to generate highly accurate code suggestions. However, their massive size poses challenges in terms of computational costs and environmental impact, hindering their widespread adoption in practical scenarios. Dynamic inference emerges as a promising solution, as it allocates minimal computation during inference while maintaining the model's performance. In this research, we explore dynamic inference within the context of code completion. Initially, we conducted an empirical investigation on GPT-2, focusing on the inference capabilities of intermediate layers for code completion. We found that 54.4\% of tokens can be accurately generated using just the first layer, signifying significant computational savings potential. Moreover, despite using all layers, the model still fails to predict 14.5\% of tokens correctly, and the subsequent completions continued from them are rarely considered helpful, with only a 4.2\% Acceptance Rate. These findings motivate our exploration of dynamic inference in code completion and inspire us to enhance it with a decision-making mechanism that stops the generation of incorrect code. We thus propose a novel dynamic inference method specifically tailored for code completion models. This method aims not only to produce correct predictions with largely reduced computation but also to prevent incorrect predictions proactively. Our extensive evaluation shows that it can averagely skip 1.7 layers out of 16 layers in the models, leading to an 11.2\% speedup with only a marginal 1.1\% reduction in ROUGE-L.

**Link**: [Read Paper](https://doi.org/10.1145/3597503.3639120)

**Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md), [empirical study](../../labels/empirical_study.md)
