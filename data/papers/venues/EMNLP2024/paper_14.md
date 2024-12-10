# Enhancing Discourse Dependency Parsing with Sentence Dependency Parsing: A Unified Generative Method Based on Code Representation

**Authors**: Shen, Zizhuo and Shao, Yanqiu and Li, Wei

**Abstract**:

Due to the high complexity of Discourse Dependency Parsing (DDP) tasks, their existing annotation resources are relatively scarce compared to other NLP tasks, and different DDP tasks also have significant differences in annotation schema. These issues have led to the dilemma of low resources for DDP tasks. Thanks to the powerful capabilities of Large Language Models (LLMs) in cross-task learning, we can use LLMs to model dependency parsing under different annotation schema in an unified manner, in order to alleviate the dilemma of low resources for DDP tasks. However, enabling LLMs to deeply comprehend dependency parsing tasks is a challenge that remains underexplored. Inspired by the application of code-based methods in complex tasks, we propose a code-based unified dependency parsing method. We treat the process of dependency parsing as a search process of dependency paths and use code to represent this search process. Furthermore, we use a curriculum-learning based instruction tuning strategy for joint training of multiple dependency parsing tasks. The experimental results show that our proposed code-based DDP system has achieved good performance on two Chinese DDP tasks (especially significant improvement on the DDP task with relatively less training data).

**Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.729)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)
