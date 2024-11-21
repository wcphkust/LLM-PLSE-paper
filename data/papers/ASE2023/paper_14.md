# On the Evaluation of Neural Code Translation: Taxonomy and Benchmark

**Authors**: Jiao, Mingsheng and Yu, Tingrui and Li, Xuan and Qiu, Guanjie and Gu, Xiaodong and Shen, Beijun

**Abstract**:

In recent years, neural code translation has gained increasing attention. While most of the research focuses on improving model architectures and training processes, we notice that the evaluation process and benchmark for code translation models are severely limited: they primarily treat source code as natural languages and provide a holistic accuracy score while disregarding the full spectrum of model capabilities across different translation types and complexity. In this paper, we present a comprehensive investigation of four state-of-the-art models and analyze in-depth the advantages and limitations of three existing benchmarks. Based on the empirical results, we develop a taxonomy that categorizes code translation tasks into four primary types according to their complexity and knowledge dependence: token level (type 1), syntactic level (type 2), library level (type 3), and algorithm level (type 4). We then conduct a thorough analysis of how existing approaches perform across these four categories. Our findings indicate that while state-of-the-art code translation models excel in type-1 and type-2 translations, they struggle with knowledge-dependent ones such as type-3 and type-4. Existing benchmarks are biased towards trivial translations, such as keyword mapping. To overcome these limitations, we construct G-TransEval, a new benchmark by manually curating type-3 and type-4 translation pairs and unit test cases. Results on our new benchmark suggest that G-TransEval can exhibit more comprehensive and finer-grained capability of code translation models and thus provide a more rigorous evaluation. Our studies also provide more insightful findings and suggestions for future research, such as building type-3 and type-4 training data and ensembling multiple pretraining approaches.

**Link**: [Read Paper](No Link Available)

**Labels**: code generation, code completion, empirical study
