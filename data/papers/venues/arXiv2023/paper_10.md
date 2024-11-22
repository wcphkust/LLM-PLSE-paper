# Finding inductive loop invariants using large language models

**Authors**: Kamath, Adharsh and Senthilnathan, Aditya and Chakraborty, Saikat and Deligiannis, Pantazis and Lahiri, Shuvendu K and Lal, Akash and Rastogi, Aseem and Roy, Subhajit and Sharma, Rahul

**Abstract**:

    Loop invariants are fundamental to reasoning about programs with loops. They establish properties about a given loop's behavior. When they additionally are inductive, they become useful for the task of formal verification that seeks to establish strong mathematical guarantees about program's runtime behavior. The inductiveness ensures that the invariants can be checked locally without consulting the entire program, thus are indispensable artifacts in a formal proof of correctness. Finding inductive loop invariants is an undecidable problem, and despite a long history of research towards practical solutions, it remains far from a solved problem. This paper investigates the capabilities of the Large Language Models (LLMs) in offering a new solution towards this old, yet important problem. To that end, we first curate a dataset of verification problems on programs with loops. Next, we design a prompt for exploiting LLMs, obtaining inductive loop invariants, that are checked for correctness using sound symbolic tools. Finally, we explore the effectiveness of using an efficient combination of a symbolic tool and an LLM on our dataset and compare it against a purely symbolic baseline. Our results demonstrate that LLMs can help improve the state-of-the-art in automated program verification.

**Link**: [Read Paper](https://arxiv.org/abs/2311.07948)

**Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md), [invariant generation](../../labels/invariant_generation.md)
