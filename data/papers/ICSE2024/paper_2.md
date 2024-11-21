# Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection

**Authors**: Steenhoek, Benjamin and Gao, Hongyang and Le, Wei

**Abstract**:

Deep learning-based vulnerability detection has shown great performance and, in some studies, outperformed static analysis tools. However, the highest-performing approaches use token-based transformer models, which are not the most efficient to capture code semantics required for vulnerability detection. Classical program analysis techniques such as dataflow analysis can detect many types of bugs based on their root causes. In this paper, we propose to combine such causal-based vulnerability detection algorithms with deep learning, aiming to achieve more efficient and effective vulnerability detection. Specifically, we designed DeepDFA, a dataflow analysis-inspired graph learning framework and an embedding technique that enables graph learning to simulate dataflow computation. We show that DeepDFA is both performant and efficient. DeepDFA outperformed all non-transformer baselines. It was trained in 9 minutes, 75x faster than the highest-performing baseline model. When using only 50+ vulnerable and several hundreds of total examples as training data, the model retained the same performance as 100\% of the dataset. DeepDFA also generalized to real-world vulnerabilities in DbgBench; it detected 8.7 out of 17 vulnerabilities on average across folds and was able to distinguish between patched and buggy versions, while the highest-performing baseline models did not detect any vulnerabilities. By combining DeepDFA with a large language model, we surpassed the state-of-the-art vulnerability detection performance on the Big-Vul dataset with 96.46 F1 score, 97.82 precision, and 95.14 recall. Our replication package is located at https://doi.org/10.6084/m9.figshare.21225413.

**Link**: [Read Paper](https://doi.org/10.1145/3597503.3623345)

**Labels**: static analysis, bug detection, code model, training, source code model
