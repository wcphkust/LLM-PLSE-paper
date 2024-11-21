# Preference-Guided Refactored Tuning for Retrieval Augmented Code Generation

**Authors**: Gao, Xinyu and Xiong, Yun and Wang, Deze and Guan, Zhenhan and Shi, Zejian and Wang, Haofen and Li, Shanshan

**Abstract**:

Retrieval-augmented code generation utilizes Large Language Models as the generator and significantly expands their code generation capabilities by providing relevant code, documentation, and more via the retriever. The current approach suffers from two primary limitations: 1) information redundancy. The indiscriminate inclusion of redundant information can result in resource wastage and may misguide generators, affecting their effectiveness and efficiency. 2) preference gap. Due to different optimization objectives, the retriever strives to procure code with higher ground truth similarity, yet this effort does not substantially benefit the generator. The retriever and the generator may prefer different golden code, and this gap in preference results in a suboptimal design. Additionally, differences in parameterization knowledge acquired during pre-training result in varying preferences among different generators.To address these limitations, in this paper, we propose RRG (Retrieve, Refactor, Generate), a novel framework for effective and efficient code generation. This framework introduces a code refactorer module between the retriever and the generator to bridge them. The refactoring process transforms the raw retrieved code into a more concise, efficient, and model-friendly version. It eliminates redundant information and noise, reducing the input length. Consequently, the generator receives higher-quality context, enabling it to produce more accurate results with lower inference costs. We conducted comprehensive experiments on multiple datasets. In the experiments, we confirmed the existence of a preference gap between the retriever and the generator, and RRG effectively bridges this gap. Specifically, RRG achieved significant performance improvements, with increases of up to 28\% on EM, 13\% on BLEU, and 6.8\% on CodeBLEU.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3694987)

**Labels**: code generation, program synthesis
