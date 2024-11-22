# Effective Large Language Model Debugging with Best-first Tree Search

**Authors**: Song, Jialin and Raiman, Jonathan and Catanzaro, Bryan

**Abstract**:

Large Language Models (LLMs) show promise in code generation tasks. However, their code-writing abilities are often limited in scope: while they can successfully implement simple functions, they struggle with more complex tasks. A fundamental difference with how an LLM writes code, compared to a human programmer, is that it cannot consistently spot and fix bugs. Debugging is a crucial skill for programmers and it enables iterative code refinement towards a correct implementation. In this work, we propose a novel algorithm to enable LLMs to debug their code via self-reflection and search where a model attempts to identify its previous mistakes. Our key contributions are 1) a best-first tree search algorithm with self-reflections (BESTER) that achieves state-of-the-art Pass@1 in three code generation benchmarks. BESTER maintains its superiority when we measure pass rates taking into account additional inference costs incurred by tree search. 2) A novel interpretability study on what self-reflections attend to in buggy programs and how they impact bug fixes, which provides a deeper understanding of the debugging process. 3) An extensive study on when self-reflections are effective in finding bugs.

**Link**: [Read Paper](https://arxiv.org/pdf/2407.19055)

**Labels**: [code generation](../../labels/code_generation.md), [debugging](../../labels/debugging.md)
