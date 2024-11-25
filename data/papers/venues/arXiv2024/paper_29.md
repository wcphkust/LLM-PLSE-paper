# Context-aware Code Segmentation for C-to-Rust Translation using Large Language Models

**Authors**: Momoko Shiraishi and Takahiro Shinagawa

**Abstract**:

There is strong motivation to translate C code into Rust code due to the continuing threat of memory safety vulnerabilities in existing C programs and the significant attention paid to Rust as an alternative to the C language. While large language models (LLMs) show promise for automating this translation by generating more natural and safer code than rule-based methods, previous studies have shown that LLM-generated Rust code often fails to compile, even for relatively small C programs, due to significant differences between the two languages and context window limitations. We propose an LLM-based translation scheme that improves the success rate of translating large-scale C code into compilable Rust code. Our approach involves three key techniques: (1) pre-processing the C code to better align its structure and expressions with Rust, (2) segmenting the code into optimally sized translation units to avoid exceeding the LLM's context window limits, and (3) iteratively compiling and repairing errors while maintaining consistency between translation units using context-supplementing prompts. Compilation success is an essential first step in achieving functional equivalence, as only compilable code can be further tested. In experiments with 20 benchmark C programs, including those exceeding 4 kilo lines of code, we successfully translated all programs into compilable Rust code without losing corresponding parts of the original code.

**Link**: [Read Paper](https://arxiv.org/abs/2409.10506v1)

**Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)
