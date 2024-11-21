# Fair: Flow type-aware pre-training of compiler intermediate representations

**Authors**: Niu, Changan and Li, Chuanyi and Ng, Vincent and Lo, David and Luo, Bin

**Abstract**:

While the majority of existing pre-trained models from code learn source code features such as code tokens and abstract syntax trees, there are some other works that focus on learning from compiler intermediate representations (IRs). Existing IR-based models typically utilize IR features such as instructions, control and data flow graphs (CDFGs), call graphs, etc. However, these methods confuse variable nodes and instruction nodes in a CDFG and fail to distinguish different types of flows, and the neural networks they use fail to capture long-distance dependencies and have over-smoothing and over-squashing problems. To address these weaknesses, we propose FAIR, a Flow type-Aware pre-trained model for IR that involves employing (1) a novel input representation of IR programs; (2) Graph Transformer to address over-smoothing, over-squashing and long-dependencies problems; and (3) five pre-training tasks that we specifically propose to enable FAIR to learn the semantics of IR tokens, flow type information, and the overall representation of IR. Experimental results show that FAIR can achieve state-of-the-art results on four code-related downstream tasks.

**Link**: [Read Paper](No Link Available)

**Labels**: general coding task, code model, training, IR code model
