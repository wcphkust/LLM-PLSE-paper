# VULGEN: Realistic Vulnerability Generation Via Pattern Mining and Deep Learning

**Authors**: Nong, Yu and Ou, Yuzhe and Pradel, Michael and Chen, Feng and Cai, Haipeng

**Abstract**:

Building new, powerful data-driven defenses against prevalent software vulnerabilities needs sizable, quality vulnerability datasets, so does large-scale benchmarking of existing defense solutions. Automatic data generation would promisingly meet the need, yet there is little work aimed to generate much-needed quality vulnerable samples. Meanwhile, existing similar and adaptable techniques suffer critical limitations for that purpose. In this paper, we present VULGEN, the first injection-based vulnerability-generation technique that is not limited to a particular class of vulnerabilities. VULGEN combines the strengths of deterministic (pattern-based) and probabilistic (deep-learning/DL-based) program transformation approaches while mutually overcoming respective weaknesses. This is achieved through close collaborations between pattern mining/application and DL-based injection localization, which separates the concerns with how and where to inject. By leveraging large, pretrained programming language modeling and only learning locations, VULGEN mitigates its own needs for quality vulnerability data (for training the localization model). Extensive evaluations show that VULGEN significantly outperforms a state-of-the-art (SOTA) pattern-based peer technique as well as both Transformer- and GNN-based approaches in terms of the percentages of generated samples that are vulnerable and those also exactly matching the ground truth (by 38.0--430.1\% and 16.3--158.2\%, respectively). The VULGEN-generated samples led to substantial performance improvements for two SOTA DL-based vulnerability detectors (by up to 31.8\% higher in F1), close to those brought by the ground-truth real-world samples and much higher than those by the same numbers of existing synthetic samples.

**Link**: [Read Paper](https://doi.org/10.1109/ICSE48619.2023.00211)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [benchmark](../../labels/benchmark.md)
