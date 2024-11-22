# Lmpa: Improving decompilation by synergy of large language model and program analysis

**Authors**: Xu, Xiangzhe and Zhang, Zhuo and Feng, Shiwei and Ye, Yapeng and Su, Zian and Jiang, Nan and Cheng, Siyuan and Tan, Lin and Zhang, Xiangyu

**Abstract**:

Decompilation aims to recover the source code form of a binary executable. It has many applications in security and software engineering such as malware analysis, vulnerability detection and code reuse. A prominent challenge in decompilation is to recover variable names. We propose a novel method that leverages the synergy of large language model (LLM) and program analysis. Language models encode rich multi-modal knowledge, but its limited input size prevents providing sufficient global context for name recovery. We propose to divide the task to many LLM queries and use program analysis to correlate and propagate the query results, which in turn improves the performance of LLM by providing additional contextual information. Our results show that 75% of the recovered names are considered good by users and our technique outperforms the state-of-the-art technique by 16.5% and 20.23% in precision and recall, respectively.

**Link**: [Read Paper](https://arxiv.org/pdf/2306.02546v1)

**Labels**: [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md)
