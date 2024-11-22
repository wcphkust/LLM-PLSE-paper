# BinCola: Diversity-Sensitive Contrastive Learning for Binary Code Similarity Detection

**Authors**: Jiang, Shuai and Fu, Cai and He, Shuai and Lv, Jianqiang and Han, Lansheng and Hu, Hong

**Abstract**:

Binary Code Similarity Detection (BCSD) is a fundamental binary analysis technique in the area of software security. Recently, advanced deep learning algorithms are integrated into BCSD platforms to achieve superior performance on well-known benchmarks. However, real-world large programs embed more complex diversities due to different compilers, various optimization levels, multiple architectures and even obfuscations. Existing BCSD solutions suffer from low accuracy issues in such complicated real-world application scenarios. In this paper, we propose BinCola, a novel Transformer-based dual diversity-sensitive contrastive learning framework that comprehensively considers the diversity of compiler options and candidate functions in the real-world application scenarios and employs the attention mechanism to fuse multi-granularity function features for enhancing generality and scalability. BinCola simultaneously compares multiple candidate functions across various compilation option scenarios to learn the differences caused by distinct compiler options and different candidate functions. We evaluate BinCola's performance in a variety of ways, including binary similarity detection and real-world vulnerability search in multiple application scenarios. The results demonstrate that BinCola achieves superior performance compared to state-of-the-art (SOTA) methods, with improvements of 2.80\%, 33.62\%, 22.41\%, and 34.25\% in cross-architecture, cross-optimization level, cross-compiler, and cross-obfuscation scenarios, respectively.

**Link**: [Read Paper](https://doi.org/10.1109/TSE.2024.3411072)

**Labels**: [static analysis](../../labels/static_analysis.md), [code similarity analysis](../../labels/code_similarity_analysis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md)
