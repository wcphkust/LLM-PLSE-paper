# The Emergence of Large Language Models in Static Analysis: A First Look through Micro-Benchmarks

**Authors**: Venkatesh, Ashwin Prasad Shivarpatna and Sabu, Samkutty and Mir, Amir M and Reis, Sofia and Bodden, Eric

**Abstract**:

Binary code similarity detection(BCSD), as a fundamental technique in software security, has various applications, including malware family detection, known vulnerability detection and code plagiarism detection. Recent deep learning-based BCSD approaches have demonstrated promising performance. However, they face two significant challenges that limit detection performance. First, most approaches that use sequence networks (like RNN and Transformer) utilize coarse-grained tokenization methods, which results in large vocabulary size and severe out-of-vocabulary (OOV) problem. Second, CFG-based methods typically use variants of graph convolutional networks, which only consider local structural information and discard long-distance dependencies between basic blocks.To address these challenges, this paper proposes Syntax Tree-based instruction embedding and introduces the acyclic graph neural network. The former decomposes assembly instructions into fine-grained tokens and employs a tree-structured neural network to generate vector representations for instructions. The latter transforms CFGs into directed acyclic graphs based on their reducibility, and further captures the dependency between basic blocks with a directed acyclic graph neural network. We implemented these two techniques in a prototype named RCFG2Vec and conducted comprehensive evaluation on two public datasets. The experiment results demonstrate that RCFG2Vec outperforms almost all baselines and achieves detection performance comparable with jTrans, a large model-based approach. Meanwhile, when integrated with our proposed techniques, several baseline approaches exhibit significant improvements in detection performance.

**Link**: [Read Paper](https://doi.org/10.1145/3650105.3652288)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)
