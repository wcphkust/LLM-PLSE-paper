# CodeIP: A Grammar-Guided Multi-Bit Watermark for Large Language Models of Code

**Authors**: Guan, Batu and Wan, Yao and Bi, Zhangqian and Wang, Zheng and Zhang, Hongyu and Zhou, Pan and Sun, Lichao

**Abstract**:

Large Language Models (LLMs) have achieved remarkable progress in code generation. It now becomes crucial to identify whether the code is AI-generated and to determine the specific model used, particularly for purposes such as protecting Intellectual Property (IP) in industry and preventing cheating in programming exercises. To this end, several attempts have been made to insert watermarks into machine-generated code. However, existing approaches are limited to inserting only a single bit of information. In this paper, we introduce CodeIP, a novel multi-bit watermarking technique that embeds additional information to preserve crucial provenance details, such as the vendor ID of an LLM, thereby safeguarding the IPs of LLMs in code generation. Furthermore, to ensure the syntactical correctness of the generated code, we propose constraining the sampling process for predicting the next token by training a type predictor. Experiments conducted on a real-world dataset across five programming languages demonstrate the effectiveness of CodeIP in watermarking LLMs for code generation while maintaining the syntactical correctness of code.

**Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.541)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md)
