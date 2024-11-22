# Introducing Compiler Semantics into Large Language Models as Programming Language Translators: A Case Study of C to x86 Assembly

**Authors**: Zhang, Shuoming and Zhao, Jiacheng and Xia, Chunwei and Wang, Zheng and Chen, Yunji and Cui, Huimin

**Abstract**:

Compilers are complex software containing millions of lines of code, taking years to develop. This paper investigates to what extent Large Language Models (LLMs) can replace hand-crafted compilers in translating high-level programming languages to machine instructions, using C to x86 assembly as a case study. We identify two challenges of using LLMs for code translation and introduce two novel data pre-processing techniques to address the challenges: numerical value conversion and training data resampling. While only using a 13B model, our approach achieves a behavioral accuracy of over 91%, outperforming the much larger GPT-4 Turbo model by over 50%. Our results are encouraging, showing that LLMs have the potential to transform how compilation tools are constructed.

**Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.55)

**Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)
