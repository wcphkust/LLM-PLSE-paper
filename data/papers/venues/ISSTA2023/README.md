# ISSTA2023

Number of papers: 5

## [Beware of the unexpected: Bimodal taint analysis](paper_4.md)
- **Authors**: Chow, Yiu Wai and Sch{\"a}fer, Max and Pradel, Michael
- **Abstract**: Static analysis is a powerful tool for detecting security vulnerabilities and other programming problems. Global taint tracking, in particular, can spot vulnerabilities arising from complicated data flow across multiple functions. However, precisely identifying which flows are problematic is challenging, and sometimes depends on factors beyond the reach of pure program analysis, such as conventions and informal knowledge. For example, learning that a parameter name of an API function locale ends...
- **Link**: [Read Paper](https://arxiv.org/pdf/2301.10545.pdf)
[static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)

## [How Effective Are Neural Networks for Fixing Security Vulnerabilities](paper_3.md)
- **Authors**: Wu, Yi and Jiang, Nan and Pham, Hung Viet and Lutellier, Thibaud and Davis, Jordan and Tan, Lin and Babkin, Petr and Shah, Sameena
- **Abstract**: Security vulnerability repair is a difficult task that is in dire need of automation. Two groups of techniques have shown promise: (1) large code language models (LLMs) that have been pre-trained on source code for tasks such as code completion, and (2) automated program repair (APR) techniques that use deep learning (DL) models to automatically fix software bugs. This paper is the first to study and compare Java vulnerability repair capabilities of LLMs and DL-based APR models. The contribution...
- **Link**: [Read Paper](https://doi.org/10.1145/3597926.3598135)
[code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [benchmark](../../labels/benchmark.md)

## [Improving Binary Code Similarity Transformer Models by Semantics-Driven Instruction Deemphasis](paper_5.md)
- **Authors**: Xu, Xiangzhe and Feng, Shiwei and Ye, Yapeng and Shen, Guangyu and Su, Zian and Cheng, Siyuan and Tao, Guanhong and Shi, Qingkai and Zhang, Zhuo and Zhang, Xiangyu
- **Abstract**: Given a function in the binary executable form, binary code similarity analysis determines a set of similar functions from a large pool of candidate functions. These similar functions are usually compiled from the same source code with different compilation setups. Such analysis has a large number of applications, such as malware detection, code clone detection, and automatic software patching. The state-of-the art methods utilize complex Deep Learning models such as Transformer models. We obser...
- **Link**: [Read Paper](https://doi.org/10.1145/3597926.3598121)
[code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md), [static analysis](../../labels/static_analysis.md), [code similarity analysis](../../labels/code_similarity_analysis.md)

## [Large Language Models Are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models](paper_2.md)
- **Authors**: Deng, Yinlin and Xia, Chunqiu Steven and Peng, Haoran and Yang, Chenyuan and Zhang, Lingming
- **Abstract**: Deep Learning (DL) systems have received exponential growth in popularity and have become ubiquitous in our everyday life. Such systems are built on top of popular DL libraries, e.g., TensorFlow and PyTorch which provide APIs as building blocks for DL systems. Detecting bugs in these DL libraries is critical for almost all downstream DL systems in ensuring effectiveness/safety for end users. Meanwhile, traditional fuzzing techniques can be hardly effective for such a challenging domain since the...
- **Link**: [Read Paper](https://doi.org/10.1145/3597926.3598067)
[program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [library testing](../../labels/library_testing.md)

## [Who Judges the Judge: An Empirical Study on Online Judge Tests](paper_1.md)
- **Authors**: Liu, Kaibo and Han, Yudong and Zhang, Jie M. and Chen, Zhenpeng and Sarro, Federica and Harman, Mark and Huang, Gang and Ma, Yun
- **Abstract**: Online Judge platforms play a pivotal role in education, competitive programming, recruitment, career training, and large language model training. They rely on predefined test suites to judge the correctness of submitted solutions. It is therefore important that the solution judgement is reliable and free from potentially misleading false positives (i.e., incorrect solutions that are judged as correct). In this paper, we conduct an empirical study of 939 coding problems with 541,552 solutions, a...
- **Link**: [Read Paper](https://doi.org/10.1145/3597926.3598060)
[static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)