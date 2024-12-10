# Nova: Generative Language Models for Assembly Code with Hierarchical Attention and Contrastive Learning

**Authors**: Nan Jiang, Chengxiao Wang, Kevin Liu, Xiangzhe Xu, Lin Tan, Xiangyu Zhang, and Petr Babkin

**Abstract**:

Binary code analysis is the foundation of crucial tasks in the security domain; thus building effective binary analysis techniques is more important than ever. Large language models (LLMs) although have brought impressive improvement to source code tasks, do not directly generalize to assembly code due to the unique challenges of assembly: (1) the low information density of assembly and (2) the diverse optimizations in assembly code. To overcome these challenges, this work proposes a hierarchical attention mechanism that builds attention summaries to capture the semantics more effectively and designs contrastive learning objectives to train LLMs to learn assembly optimization. Equipped with these techniques, this work develops Nova, a generative LLM for assembly code. Nova outperforms existing techniques on binary code decompilation by up to 14.84 -- 21.58% (absolute percentage point improvement) higher Pass@1 and Pass@10, and outperforms the latest binary code similarity detection techniques by up to 6.17% Recall@1, showing promising abilities on both assembly generation and understanding tasks.

**Link**: [Read Paper](https://arxiv.org/pdf/2311.13721)

**Labels**: [static analysis](../../labels/static_analysis.md), [program decompilation](../../labels/program_decompilation.md), [static analysis](../../labels/static_analysis.md), [code similarity analysis](../../labels/code_similarity_analysis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md)
