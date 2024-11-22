# Out of Context: How important is Local Context in Neural Program Repair?

**Authors**: Prenner, Julian Aron and Robbes, Romain

**Abstract**:

Deep learning source code models have been applied very successfully to the problem of automated program repair. One of the standing issues is the small input window of current models which often cannot fully fit the context code required for a bug fix (e.g., method or class declarations of a project). Instead, input is often restricted to the local context, that is, the lines below and above the bug location. In this work we study the importance of this local context on repair success: how much local context is needed?; is context before or after the bug location more important? how is local context tied to the bug type? To answer these questions we train and evaluate Transformer models in many different local context configurations on three datasets and two programming languages. Our results indicate that overall repair success increases with the size of the local context (albeit not for all bug types) and confirm the common practice that roughly 50--60\% of the input window should be used for context leading the bug. Our results are not only relevant for researchers working on Transformer-based APR tools but also for benchmark and dataset creators who must decide what and how much context to include in their datasets.

**Link**: [Read Paper](https://doi.org/10.1145/3597503.3639086)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [empirical study](../../labels/empirical_study.md)
