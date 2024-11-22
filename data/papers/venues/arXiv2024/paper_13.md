# Source Code Vulnerability Detection: Combining Code Language Models and Code Property Graphs

**Authors**: Ruitong Liu and Yanbin Wang and Haitao Xu and Bin Liu and Jianguo Sun and Zhenhao Guo and Wenrui Ma

**Abstract**:

Currently, deep learning successfully applies to code vulnerability detection by learning from code sequences or property graphs. However, sequence-based methods often overlook essential code attributes such as syntax, control flow, and data dependencies, whereas graph-based approaches might underestimate the semantics of code and face challenges in capturing long-distance contextual information.To address this gap, we propose Vul-LMGNN, a unified model that combines pre-trained code language models with code property graphs for code vulnerability detection. Vul-LMGNN constructs a code property graph that integrates various code attributes (including syntax, flow control, and data dependencies) into a unified graph structure, thereafter leveraging pre-trained code model to extract local semantic features as node embeddings in the code property graph. Furthermore, to effectively retain dependency information among various attributes, we introduce a gated code Graph Neural Network (GNN). By jointly training the code language model and the gated code GNN modules in Vul-LMGNN, our proposed method efficiently leverages the strengths of both mechanisms. Finally, we utilize a pre-trained CodeBERT as an auxiliary classifier, with the final detection results derived by learning the linear interpolation of Vul-LMGNN and CodeBERT. The proposed method, evaluated across four real-world vulnerability datasets, demonstrated superior performance compared to six state-of-the-art approaches.

**Link**: [Read Paper](https://doi.org/10.48550/arXiv.2404.14719)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)
