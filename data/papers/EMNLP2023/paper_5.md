# Generating Data for Symbolic Language with Large Language Models

**Authors**: Ye, Jiacheng and Li, Chengzu and Kong, Lingpeng and Yu, Tao

**Abstract**:

While large language models (LLMs) bring not only performance but also complexity, recent work has started to turn LLMs into data generators rather than task inferencers, where another affordable task model is trained for efficient deployment and inference. However, such an approach has primarily been applied to natural language tasks, and has not yet been explored for symbolic language tasks with complex structured outputs (e.g., semantic parsing and code generation). In this paper, we propose SymGen which utilizes LLMs for generating various annotation-expensive symbolic language data. SymGen consists of an informative prompt to steer generation and an agreement-based verifier to improve data correctness. We conduct extensive experiments on six symbolic language tasks across various settings. Compared with the LLMs, we demonstrate the 1%-sized task model can achieve comparable or better performance, largely cutting inference and deployment costs. We also show that generated data with only a few human demonstrations can be as effective as over 10 times the amount of human-annotated data when training the task model, saving a considerable amount of annotation effort. SymGen takes a step toward data generation for annotation-expensive complex tasks, and we release the code at URL.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.523)

**Labels**: code model, training, source code model
