# LLM4Decompile: Decompiling Binary Code with Large Language Models

**Authors**: Tan, Hanzhuo and Luo, Qi and Li, Jing and Zhang, Yuqun

**Abstract**:

Decompilation aims to convert binary code to high-level source code, but traditional tools like Ghidra often produce results that are difficult to read and execute. Motivated by the advancements in Large Language Models (LLMs), we propose LLM4Decompile, the first and largest open-source LLM series (1.3B to 33B) trained to decompile binary code. We optimize the LLM training process and introduce the LLM4Decompile-End models to decompile binary directly. The resulting models significantly outperform GPT-4o and Ghidra on the HumanEval and ExeBench benchmarks by over 100% in terms of re-executability rate. Additionally, we improve the standard refinement approach to fine-tune the LLM4Decompile-Ref models, enabling them to effectively refine the decompiled code from Ghidra and achieve a further 16.2% improvement over the LLM4Decompile-End. LLM4Decompile demonstrates the potential of LLMs to revolutionize binary code decompilation, delivering remarkable improvements in readability and executability while complementing conventional tools for optimal results.

**Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.203)

**Labels**: [code generation](../../labels/code_generation.md), [program decompilation](../../labels/program_decompilation.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md)
