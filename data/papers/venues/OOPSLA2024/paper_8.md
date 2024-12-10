# Evaluating the effectiveness of deep learning models for foundational program analysis tasks

**Authors**: Chen, Qian and Yu, Chenyang and Liu, Ruyan and Zhang, Chi and Wang, Yu and Wang, Ke and Su, Ting and Wang, Linzhang

**Abstract**:

While deep neural networks provide state-of-the-art solutions to a wide range of programming language tasks, their effectiveness in dealing with foundational program analysis tasks remains under explored. In this paper, we present an empirical study that evaluates four prominent models of code (i.e., CuBERT, CodeBERT, GGNN, and Graph Sandwiches) in two such foundational tasks: (1) alias prediction, in which models predict whether two pointers must alias, may alias or must not alias; and (2) equivalence prediction, in which models predict whether or not two programs are semantically equivalent. At the core of this study is CodeSem, a dataset built upon the source code of real-world flagship software (e.g., Linux Kernel, GCC, MySQL) and manually validated for the two prediction tasks. Results show that all models are accurate in both prediction tasks, especially CuBERT with an accuracy of 89% and 84% in alias prediction and equivalence prediction, respectively. We also conduct a comprehensive, in-depth analysis of the results of all models in both tasks, concluding that deep learning models are generally capable of performing foundational tasks in program analysis even though in specific cases their weaknesses are also evident.

**Link**: [Read Paper](https://dl.acm.org/doi/pdf/10.1145/3649829)

**Labels**: [static analysis](../../labels/static_analysis.md), [pointer analysis](../../labels/pointer_analysis.md), [equivalence checking](../../labels/equivalence_checking.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)
