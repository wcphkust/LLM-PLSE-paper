# ReSym: Harnessing LLMs to Recover Variable and Data Structure Symbols from Stripped Binaries

**Authors**: Xie, Danning and Zhang, Zhuo and Jiang, Nan and Xu, Xiangzhe and Tan, Lin and Zhang, Xiangyu

**Abstract**:

Decompilation aims to recover a binary executable to the source code form and hence has a wide range of applications in cyber security, such as malware analysis and legacy code hardening. A prominent challenge is to recover variable symbols, including both primitive and complex types such as user-defined data structures, along with their symbol information such as names and types. Existing efforts focus on solving parts of the problem, eg, recovering only types (without names) or only local variables (without user-defined structures). In this paper, we propose ReSym, a novel hybrid technique that combines Large Language Models (LLMs) and program analysis to recover both names and types for local variables and user-defined data structures. Our method encompasses fine-tuning two LLMs to handle local variables and structures, respectively. To overcome the inherent token limitations in current LLMs, we devise a novel Prolog-based algorithm to aggregate and cross-check results from multiple LLM queries, suppressing uncertainty and hallucinations. Our experiments show that ReSym is effective in recovering variable information and user-defined data structures, substantially outperforming the state-of-the-art methods.

**Link**: [Read Paper](https://www.cs.purdue.edu/homes/lintan/publications/resym-ccs24.pdf)

**Labels**: [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md), [code generation](../../labels/code_generation.md), [program decompilation](../../labels/program_decompilation.md)
