# Self-Constructed Context Decompilation with Fined-grained Alignment Enhancement

**Authors**: Feng, Yunlong and Teng, Dechuan and Xu, Yang and Mu, Honglin and Xu, Xiao and Qin, Libo and Zhu, Qingfu and Che, Wanxiang

**Abstract**:

Decompilation transforms compiled code back into a high-level programming language for analysis when source code is unavailable. Previous work has primarily focused on enhancing decompilation performance by increasing the scale of model parameters or training data for pre-training. Based on the characteristics of the decompilation task, we propose two methods: (1) Without fine-tuning, the Self-Constructed Context Decompilation (sc²dec) method recompiles the LLM’s decompilation results to construct pairs for in-context learning, helping the model improve decompilation performance. (2) Fine-grained Alignment Enhancement (FAE), which meticulously aligns assembly code with source code at the statement level by leveraging debugging information, is employed during the fine-tuning phase to achieve further improvements in decompilation. By integrating these two methods, we achieved a Re-Executability performance improvement of approximately 3.90% on the Decompile-Eval benchmark, establishing a new state-of-the-art performance of 52.41%. The code, data, and models are available at https://github.com/AlongWY/sccdec.

**Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.385)

**Labels**: code generation, program decompilation, code model, training, binary code model, benchmark
