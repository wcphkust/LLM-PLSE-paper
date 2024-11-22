# Multitask Pretraining with Structured Knowledge for Text-to-SQL Generation

**Authors**: Giaquinto, Robert and Zhang, Dejiao and Kleiner, Benjamin and Li, Yang and Tan, Ming and Bhatia, Parminder and Nallapati, Ramesh and Ma, Xiaofei

**Abstract**:

Many machine learning-based low-code or no-code applications involve generating code that interacts with structured knowledge. For example, one of the most studied tasks in this area is generating SQL code from a natural language statement. Prior work shows that incorporating context information from the database schema, such as table and column names, is beneficial to model performance on this task. In this work we present a large pretraining dataset and strategy for learning representations of text, tables, and SQL code that leverages the entire context of the problem. Specifically, we build on existing encoder-decoder architecture by introducing a multitask pretraining framework that complements the unique attributes of our diverse pretraining data. Our work represents the first study on large-scale pretraining of encoder-decoder models for interacting with structured knowledge, and offers a new state-of-the-art foundation model in text-to-SQL generation. We validate our approach with experiments on two SQL tasks, showing improvement over existing methods, including a 1.7 and 2.2 percentage point improvement over prior state-of-the-arts on Spider and CoSQL.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2023.acl-long.620)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [benchmark](../../labels/benchmark.md)
