# Self-Edit: Fault-Aware Code Editor for Code Generation

**Authors**: Zhang, Kechi and Li, Zhuo and Li, Jia and Li, Ge and Jin, Zhi

**Abstract**:

Large language models (LLMs) have demonstrated an impressive ability to generate codes on competitive programming tasks. However, with limited sample numbers, LLMs still suffer from poor accuracy. Inspired by the process of human programming, we propose a generate-and-edit approach named Self-Edit that utilizes execution results of the generated code from LLMs to improve the code quality on the competitive programming task. We execute the generated code on the example test case provided in the question and wrap execution results into a supplementary comment. Utilizing this comment as guidance, our fault-aware code editor is employed to correct errors in the generated code. We perform extensive evaluations across two competitive programming datasets with nine different LLMs. Compared to directly generating from LLMs, our approach can improve the average of pass@1 by 89% on APPS-dev, 31% on APPS-test, and 48% on HumanEval over nine popular code generation LLMs with parameter sizes ranging from 110M to 175B. Compared to other post-processing methods, our method demonstrates superior accuracy and efficiency.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2023.acl-long.45)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [benchmark](../../labels/benchmark.md)
