# EvoCodeBench: An Evolving Code Generation Benchmark Aligned with Real-World Code Repositories

**Authors**: Li, Jia and Li, Ge and Zhang, Xuanming and Dong, Yihong and Jin, Zhi

**Abstract**:

How to evaluate Large Language Models (LLMs) in code generation is an open question. Existing benchmarks demonstrate poor alignment with real-world code repositories and are insufficient to evaluate the coding abilities of LLMs. This paper proposes a new benchmark - EvoCodeBench to address the preceding problems, which has three primary advances. (1) EvoCodeBench aligns with real-world repositories in multiple dimensions, e.g., code distributions and dependency distributions. (2) EvoCodeBench offers comprehensive annotations (e.g., requirements, reference code, and reference dependencies), and robust evaluation metrics (e.g., Pass@k and Recall@k). (3) EvoCodeBench is an evolving benchmark to avoid data leakage. We build an automatic pipeline to update EvoCodeBench from the latest repositories. We release the first version - EvoCodeBench-2403, containing 275 samples from 25 real-world repositories. Based on EvoCodeBench, we propose repository-level code generation and evaluate 10 popular LLMs (e.g., gpt-4, gpt-3.5, DeepSeek Coder, StarCoder 2, CodeLLaMa, Gemma, and Qwen 1.5). Our experiments reveal the coding abilities of these LLMs in real-world repositories. For example, the highest Pass@1 of gpt-4 only is 20.73% in our experiments. We also analyze failed cases and summarize the shortcomings of existing LLMs in EvoCodeBench. We release EvoCodeBench, all prompts, and LLMs' completions for further community analysis.

**Link**: [Read Paper](https://arxiv.org/pdf/2404.00599)

**Labels**: [benchmark](../../labels/benchmark.md), [code generation](../../labels/code_generation.md)
