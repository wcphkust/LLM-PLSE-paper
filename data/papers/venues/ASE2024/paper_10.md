# GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph

**Authors**: Liu, Wei and Yu, Ailun and Zan, Daoguang and Shen, Bo and Zhang, Wei and Zhao, Haiyan and Jin, Zhi and Wang, Qianxiang

**Abstract**:

The performance of repository-level code completion depends upon the effective leverage of both general and repository-specific knowledge. Despite the impressive capability of code LLMs in general code completion tasks, they often exhibit less satisfactory performance on repository-level completion due to the lack of repository-specific knowledge in these LLMs. To address this problem, we propose GraphCoder, a retrieval-augmented code completion framework that leverages LLMs' general code knowledge and the repository-specific knowledge via a graph-based retrieval-generation process. In particular, GraphCoder captures the context of completion target more accurately through code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements, a more structured way to capture the completion target context than the sequence-based context used in existing retrieval-augmented approaches; based on CCG, GraphCoder further employs a coarse-to-fine retrieval process to locate context-similar code snippets with the completion target from the current repository. Experimental results demonstrate both the effectiveness and efficiency of GraphCoder: Compared to baseline retrieval-augmented methods, GraphCoder achieves higher exact match (EM) on average, with increases of +6.06 in code match and +6.23 in identifier match, while using less time and space.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695054)

**Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md)
