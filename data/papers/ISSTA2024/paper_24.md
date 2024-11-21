# HECS: A Hypergraph Learning-Based System for Detecting Extract Class Refactoring Opportunities

**Authors**: Wang, Luqiao and Wang, Qiangqiang and Wang, Jiaqi and Zhao, Yutong and Wei, Minjie and Quan, Zhou and Cui, Di and Li, Qingshan

**Abstract**:

HECS is an advanced tool designed for Extract Class refactoring by leveraging hypergraph learning to model complex dependencies within large classes. Unlike traditional tools that rely on direct one-to-one dependency graphs, HECS uses intra-class dependency hypergraphs to capture one-to-many relationships. This allows HECS to provide more accurate and relevant refactoring suggestions. The tool constructs hypergraphs for each target class, attributes nodes using a pre-trained code model, and trains an enhanced hypergraph neural network. Coupled with a large language model, HECS delivers practical refactoring suggestions. In evaluations on large-scale and real-world datasets, HECS achieved a 38.5\% increase in precision, 9.7\% in recall, and 44.4\% in f1-measure compared to JDeodorant, SSECS, and LLMRefactor. These improvements make HECS a valuable tool for developers, offering practical insights and enhancing existing refactoring techniques.

**Link**: [Read Paper](https://doi.org/10.1145/3650212.3685307)

**Labels**: code generation, program transformation
