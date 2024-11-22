# Improving Binary Code Similarity Transformer Models by Semantics-Driven Instruction Deemphasis

**Authors**: Xu, Xiangzhe and Feng, Shiwei and Ye, Yapeng and Shen, Guangyu and Su, Zian and Cheng, Siyuan and Tao, Guanhong and Shi, Qingkai and Zhang, Zhuo and Zhang, Xiangyu

**Abstract**:

Given a function in the binary executable form, binary code similarity analysis determines a set of similar functions from a large pool of candidate functions. These similar functions are usually compiled from the same source code with different compilation setups. Such analysis has a large number of applications, such as malware detection, code clone detection, and automatic software patching. The state-of-the art methods utilize complex Deep Learning models such as Transformer models. We observe that these models suffer from undesirable instruction distribution biases caused by specific compiler conventions. We develop a novel technique to detect such biases and repair them by removing the corresponding instructions from the dataset and finetuning the models. This entails synergy between Deep Learning model analysis and program analysis. Our results show that we can substantially improve the state-of-the-art models’ performance by up to 14.4\% in the most challenging cases where test data may be out of the distributions of training data.

**Link**: [Read Paper](https://doi.org/10.1145/3597926.3598121)

**Labels**: [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md), [static analysis](../../labels/static_analysis.md), [code similarity analysis](../../labels/code_similarity_analysis.md)
