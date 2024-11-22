# CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Challenges

**Authors**: Zhang, Kechi and Li, Jia and Li, Ge and Shi, Xianjie and Jin, Zhi

**Abstract**:

Large Language Models (LLMs) have shown promise in automated code generation but typically excel only in simpler tasks such as generating standalone code units. However, real-world software development often involves complex code repositories with complex dependencies and extensive documentation. To enable LLMs to handle these realworld repo-level code generation, we present CodeAgent, a novel LLM-based agent framework that employs external tools for effective repo-level code generation. CodeAgent integrates five programming tools, enabling interaction with software artifacts for information retrieval, code implementation, and code testing. We implement four agent strategies to optimize these tools’ usage. To the best of our knowledge, CodeAgent is the first agent tool framework specifically for repo-level code generation. In order to measure the effectiveness of our method at the repository level, we have introduced a benchmark dataset CodAgentBench. The performance on this dataset shows a significant improvement brought by our method, with improvements of pass rate ranging from 2.0 to 15.8. Further tests on the HumanEval benchmark confirm CodeAgent’s adaptability and efficacy across various code generation tasks. Notably, CodeAgent outperforms commercial products like Github Copilot, showcasing superior accuracy and efficiency. These results demonstrate CodeAgent’s robust capabilities in code generation, highlighting its potential for real-world repo-level coding challenges.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.737)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [benchmark](../../labels/benchmark.md)
