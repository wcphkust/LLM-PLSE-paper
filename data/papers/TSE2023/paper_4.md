# CoSS: Leveraging Statement Semantics for Code Summarization

**Authors**: Shi, Chaochen and Cai, Borui and Zhao, Yao and Gao, Longxiang and Sood, Keshav and Xiang, Yong

**Abstract**:

Automated code summarization tools allow generating descriptions for code snippets in natural language, which benefits software development and maintenance. Recent studies demonstrate that the quality of generated summaries can be improved by using additional code representations beyond token sequences. The majority of contemporary approaches mainly focus on extracting code syntactic and structural information from abstract syntax trees (ASTs). However, from the view of macro-structures, it is challenging to identify and capture semantically meaningful features due to fine-grained syntactic nodes involved in ASTs. To fill this gap, we investigate how to learn more code semantics and control flow features from the perspective of code statements. Accordingly, we propose a novel model entitled CoSS for code summarization. CoSS adopts a Transformer-based encoder and a graph attention network-based encoder to capture token-level and statement-level semantics from code token sequence and control flow graph, respectively. Then, after receiving two-level embeddings from encoders, a joint decoder with a multi-head attention mechanism predicts output sequences verbatim. Performance evaluations on Java, Python, and Solidity datasets validate that CoSS outperforms nine state-of-the-art (SOTA) neural code summarization models in effectiveness and is competitive in execution efficiency. Further, the ablation study reveals the contribution of each model component.

**Link**: [Read Paper](https://doi.org/10.1109/TSE.2023.3256362)

**Labels**: static analysis, code summarization, code model, training, source code model
