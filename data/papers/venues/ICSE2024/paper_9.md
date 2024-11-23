# Evaluating Large Language Models in Class-Level Code Generation

**Authors**: Du, Xueying and Liu, Mingwei and Wang, Kaixin and Wang, Hanlin and Liu, Junwei and Chen, Yixuan and Feng, Jiayi and Sha, Chaofeng and Peng, Xin and Lou, Yiling

**Abstract**:

Recently, many large language models (LLMs) have been proposed, showing advanced proficiency in code generation. Meanwhile, many efforts have been dedicated to evaluating LLMs on code generation benchmarks such as HumanEval. Although being very helpful for comparing different LLMs, existing evaluation focuses on a simple code generation scenario (i.e., function-level or statement-level code generation), which mainly asks LLMs to generate one single code unit (e.g., a function or a statement) for the given natural language description. Such evaluation focuses on generating independent and often small-scale code units, thus leaving it unclear how LLMs perform in real-world software development scenarios.To fill this knowledge gap, we make the first attempt to evaluate LLMs in a more challenging code generation scenario, i.e., class-level code generation. Compared with existing code generation benchmarks, it better reflects real-world software development scenarios due to it comprising broader contextual dependencies and multiple, interdependent units of code. We first manually construct the first class-level code generation benchmark ClassEval of 100 class-level Python code generation tasks with approximately 500 person-hours. Based on the new benchmark ClassEval, we then perform the first study of 11 state-of-the-art LLMs on class-level code generation. Based on our results, we find that all LLMs perform much worse on class-level code generation compared to the method-level. While GPT models still dominate other LLMs on class-level code generation, the performance rankings of other models on method-level code generation no longer holds for class-level code generation. Besides, most models (except GPT models) perform better when generating the class method by method; and they have the limited ability of generating dependent code. Based on our findings, we call for software engineering (SE) researchers' expertise to build more LLM benchmarks based on practical and complicated software development scenarios.

**Link**: [Read Paper](https://doi.org/10.1145/3597503.3639219)

**Labels**: [code generation](../../labels/code_generation.md), [benchmark](../../labels/benchmark.md)