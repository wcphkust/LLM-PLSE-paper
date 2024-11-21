# Jtrans: Jump-aware transformer for binary code similarity detection

**Authors**: Wang, Hao and Qu, Wenjie and Katz, Gilad and Zhu, Wenyu and Gao, Zeyu and Qiu, Han and Zhuge, Jianwei and Zhang, Chao

**Abstract**:

Binary code similarity detection (BCSD) has important applications in various fields such as vulnerabilities detection, software component analysis, and reverse engineering. Recent studies have shown that deep neural networks (DNNs) can comprehend instructions or control-flow graphs (CFG) of binary code and support BCSD. In this study, we propose a novel Transformer-based approach, namely jTrans, to learn representations of binary code. It is the first solution that embeds control flow information of binary code into Transformer-based language models, by using a novel jump-aware representation of the analyzed binaries and a newly-designed pre-training task. Additionally, we release to the community a newly-created large dataset of binaries, BinaryCorp, which is the most diverse to date. Evaluation results show that jTrans outperforms state-of-the-art (SOTA) approaches on this more challenging dataset by 30.5% (i.e., from 32.0% to 62.5%). In a real-world task of known vulnerability searching, jTrans achieves a recall that is 2X higher than existing SOTA baselines.

**Link**: [Read Paper](No Link Available)

**Labels**: static analysis, bug detection, code model, training, binary code model
