# Large Language Models for Equivalent Mutant Detection: How Far Are We?

**Authors**: Tian, Zhao and Shu, Honglin and Wang, Dong and Cao, Xuejie and Kamei, Yasutaka and Chen, Junjie

**Abstract**:

Mutation testing is vital for ensuring software quality. However, the presence of equivalent mutants is known to introduce redundant cost and bias issues, hindering the effectiveness of mutation testing in practical use. Although numerous equivalent mutant detection (EMD) techniques have been proposed, they exhibit limitations due to the scarcity of training data and challenges in generalizing to unseen mutants. Recently, large language models (LLMs) have been extensively adopted in various code-related tasks and have shown superior performance by more accurately capturing program semantics. Yet the performance of LLMs in equivalent mutant detection remains largely unclear. In this paper, we conduct an empirical study on 3,302 method-level Java mutant pairs to comprehensively investigate the effectiveness and efficiency of LLMs for equivalent mutant detection. Specifically, we assess the performance of LLMs compared to existing EMD techniques, examine the various strategies of LLMs, evaluate the orthogonality between EMD techniques, and measure the time overhead of training and inference. Our findings demonstrate that LLM-based techniques significantly outperform existing techniques (i.e., the average improvement of 35.69\% in terms of F1-score), with the fine-tuned code embedding strategy being the most effective. Moreover, LLM-based techniques offer an excellent balance between cost (relatively low training and inference time) and effectiveness. Based on our findings, we further discuss the impact of model size and embedding quality, and provide several promising directions for future research. This work is the first to examine LLMs in equivalent mutant detection, affirming their effectiveness and efficiency.

**Link**: [Read Paper](https://doi.org/10.1145/3650212.3680395)

**Labels**: [program testing](../../labels/program_testing.md), [mutation testing](../../labels/mutation_testing.md), [empirical study](../../labels/empirical_study.md)
