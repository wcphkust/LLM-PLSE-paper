# LLMorpheus: Mutation Testing using Large Language Models

**Authors**: Tip, Frank and Bell, Jonathan and Sch{\"a}fer, Max

**Abstract**:

In mutation testing, the quality of a test suite is evaluated by introducing faults into a program and determining whether the program's tests detect them. Most existing approaches for mutation testing involve the application of a fixed set of mutation operators, e.g., replacing a "+" with a "-" or removing a function's body. However, certain types of real-world bugs cannot easily be simulated by such approaches, limiting their effectiveness. This paper presents a technique where a Large Language Model (LLM) is prompted to suggest mutations by asking it what placeholders that have been inserted in source code could be replaced with. The technique is implemented in LLMorpheus, a mutation testing tool for JavaScript, and evaluated on 13 subject packages, considering several variations on the prompting strategy, and using several LLMs. We find LLMorpheus to be capable of producing mutants that resemble existing bugs that cannot be produced by StrykerJS, a state-of-the-art mutation testing tool. Moreover, we report on the running time, cost, and number of mutants produced by LLMorpheus, demonstrating its practicality.

**Link**: [Read Paper](https://arxiv.org/pdf/2404.09952)

**Labels**: [program testing](../../labels/program_testing.md), [mutation testing](../../labels/mutation_testing.md)
