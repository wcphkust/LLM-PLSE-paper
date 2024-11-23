# Program Decompilation

- [DeGPT: Optimizing Decompiler Output with LLM](../venues/NDSS2024/paper_1.md), ([NDSS2024](../venues/NDSS2024/README.md))

  - **Abstract**: Reverse engineering is essential in malware analysis, vulnerability discovery, etc. Decompilers assist the reverse engineers by lifting the assembly to the high-level programming language, which highly boosts binary comprehension. However, decompilers suffer from problems such as meaningless variable names, redundant variables, and lacking comments describing the purpose of the code. Previous studies have shown promising performance in refining the decompiler output by training the models with h...
  - **Labels**: [code generation](code_generation.md), [program decompilation](program_decompilation.md)


- [LLM4Decompile: Decompiling Binary Code with Large Language Models](../venues/EMNLP2024/paper_19.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Decompilation aims to convert binary code to high-level source code, but traditional tools like Ghidra often produce results that are difficult to read and execute. Motivated by the advancements in Large Language Models (LLMs), we propose LLM4Decompile, the first and largest open-source LLM series (1.3B to 33B) trained to decompile binary code. We optimize the LLM training process and introduce the LLM4Decompile-End models to decompile binary directly. The resulting models significantly outperfo...
  - **Labels**: [code generation](code_generation.md), [program decompilation](program_decompilation.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [ReSym: Harnessing LLMs to Recover Variable and Data Structure Symbols from Stripped Binaries](../venues/CCS2024/paper_1.md), ([CCS2024](../venues/CCS2024/README.md))

  - **Abstract**: Decompilation aims to recover a binary executable to the source code form and hence has a wide range of applications in cyber security, such as malware analysis and legacy code hardening. A prominent challenge is to recover variable symbols, including both primitive and complex types such as user-defined data structures, along with their symbol information such as names and types. Existing efforts focus on solving parts of the problem, eg, recovering only types (without names) or only local vari...
  - **Labels**: [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md), [code generation](code_generation.md), [program decompilation](program_decompilation.md)


- [Self-Constructed Context Decompilation with Fined-grained Alignment Enhancement](../venues/EMNLP2024/paper_8.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Decompilation transforms compiled code back into a high-level programming language for analysis when source code is unavailable. Previous work has primarily focused on enhancing decompilation performance by increasing the scale of model parameters or training data for pre-training. Based on the characteristics of the decompilation task, we propose two methods: (1) Without fine-tuning, the Self-Constructed Context Decompilation (sc²dec) method recompiles the LLM’s decompilation results to constru...
  - **Labels**: [code generation](code_generation.md), [program decompilation](program_decompilation.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md), [benchmark](benchmark.md)


- [WaDec: Decompiling WebAssembly Using Large Language Model](../venues/ASE2024/paper_9.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: WebAssembly (abbreviated Wasm) has emerged as a cornerstone of web development, offering a compact binary format that allows high-performance applications to run at near-native speeds in web browsers. Despite its advantages, Wasm's binary nature presents significant challenges for developers and researchers, particularly regarding readability when debugging or analyzing web applications. Therefore, effective decompilation becomes crucial. Unfortunately, traditional decompilers often struggle wit...
  - **Labels**: [code generation](code_generation.md), [program decompilation](program_decompilation.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)