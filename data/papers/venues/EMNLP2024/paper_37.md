# Language Models as Compilers: Simulating Pseudocode Execution Improves Algorithmic Reasoning in Language Models

**Authors**: Chae, Hyungjoo and Kim, Yeonghyeon and Kim, Seungone and Ong, Kai Tzu-iunn and Kwak, Beong-woo and Kim, Moohyeon and Kim, Sunghwan and Kwon, Taeyoon and Chung, Jiwan and Yu, Youngjae and Yeo, Jinyoung

**Abstract**:

Algorithmic reasoning tasks that involve complex logical patterns, such as completing Dyck language, pose challenges for large language models (LLMs), despite their recent success. Prior work has used LLMs to generate programming language and applied external compilers for such tasks. Yet, when on the fly, it is hard to generate an executable code with the correct logic for the solution. Even so, code for one instance cannot be reused for others, although they might require the same logic to solve. We present Think-and-Execute, a novel framework that improves LLMs’ algorithmic reasoning: (1) In Think, we discover task-level logic shared across all instances, and express such logic with pseudocode; (2) In Execute, we tailor the task-level pseudocode to each instance and simulate the execution of it. Think-and-Execute outperforms several strong baselines (including CoT and PoT) in diverse algorithmic reasoning tasks. We manifest the advantage of using task-level pseudocode over generating instance-specific solutions one by one. Also, we show that pseudocode can better improve LMs’ reasoning than natural language (NL) guidance, even though they are trained with NL instructions.

**Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.1253)

**Labels**: [prompt strategy](../../labels/prompt_strategy.md), [reason with code](../../labels/reason_with_code.md)
