# When to Stop? Towards Efficient Code Generation in LLMs with Excess Token Prevention

**Authors**: Guo, Lianghong and Wang, Yanlin and Shi, Ensheng and Zhong, Wanjun and Zhang, Hongyu and Chen, Jiachi and Zhang, Ruikai and Ma, Yuchi and Zheng, Zibin

**Abstract**:

Code generation aims to automatically generate code snippets that meet given natural language requirements and plays an important role in software development. Although Code LLMs have shown excellent performance in this domain, their long generation time poses a signification limitation in practice use. In this paper, we first conduct an in-depth preliminary study with different Code LLMs on code generation task and identify a significant efficiency issue, i.e., continual generation of excess tokens. It harms the developer productivity and leads to huge computational wastes. To address it, we introduce CodeFast, an inference acceleration approach for Code LLMs on code generation. The key idea of CodeFast is to terminate the inference process in time when unnecessary excess tokens are detected. First, we propose an automatic data construction framework to obtain training data. Then, we train a unified lightweight model GenGuard applicable to multiple programming languages to predict whether to terminate inference at the current step. Finally, we enhance Code LLM with GenGuard to accelerate its inference in code generation task. We conduct extensive experiments with CodeFast on five representative Code LLMs across four widely used code generation datasets. Experimental results show that (1) CodeFast can significantly improve the inference speed of various Code LLMs in code generation, ranging form 34\% to 452\%, without compromising the quality of generated code. (2) CodeFast is stable across different parameter settings and can generalize to untrained datasets. Our code and data are available at https://github.com/DeepSoftwareAnalytics/CodeFast.

**Link**: [Read Paper](https://doi.org/10.1145/3650212.3680343)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)
