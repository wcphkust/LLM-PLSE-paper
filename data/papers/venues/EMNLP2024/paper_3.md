# EvoR: Evolving Retrieval for Code Generation

**Authors**: Su, Hongjin and Jiang, Shuyang and Lai, Yuhang and Wu, Haoyuan and Shi, Boao and Liu, Che and Liu, Qian and Yu, Tao

**Abstract**:

Recently the retrieval-augmented generation (RAG) has been successfully applied in code generation. However, existing pipelines for retrieval-augmented code generation (RACG) employ static knowledge bases with a single source, limiting the adaptation capabilities of Large Language Models (LLMs) to domains they have insufficient knowledge of. In this work, we develop a novel pipeline, EVOR, that employs the synchronous evolution of both queries and diverse knowledge bases. On two realistic settings where the external knowledge is required to solve code generation tasks, we compile four new datasets associated with frequently updated libraries and long-tail programming languages, named EVOR-BENCH. Extensive experiments demonstrate that EVOR achieves two to four times of execution accuracy compared to other methods such as Reflexion (Shinn et al., 2024), DocPrompting (Zhou et al., 2023), etc. We demonstrate that EVOR is flexible and can be easily combined with them to achieve further improvement. Further analysis reveals that EVOR benefits from the synchronous evolution of queries and documents and the diverse information sources in the knowledge base. We hope that our studies will inspire more insights into the design of advanced RACG pipelines in future research.

**Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.143)

**Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md), [source code model](../../labels/source_code_model.md), [prompt strategy](../../labels/prompt_strategy.md), [retrieval-augmented generation](../../labels/retrieval-augmented_generation.md)
