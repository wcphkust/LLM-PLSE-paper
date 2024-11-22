# LLM-Generated Invariants for Bounded Model Checking Without Loop Unrolling

**Authors**: Pirzada, Muhammad A. A. and Reger, Giles and Bhayat, Ahmed and Cordeiro, Lucas C.

**Abstract**:

We investigate a modification of the classical Bounded Model Checking (BMC) procedure that does not handle loops through unrolling but via modifications to the control flow graph (CFG). A portion of the CFG representing a loop is replaced by a node asserting invariants of the loop. We generate these invariants using Large Language Models (LLMs) and use a first-order theorem prover to ensure the correctness of the generated statements. We thus transform programs to loop-free variants in a sound manner. Our experimental results show that the resulting tool, ESBMC ibmc, is competitive with state-of-the-art formal verifiers for programs with unbounded loops, significantly improving the number of programs verified by the industrial-strength software verifier ESBMC and verifying programs that state-of-the-art software verifiers such as SeaHorn and VeriAbs could not.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695512)

**Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md), [invariant generation](../../labels/invariant_generation.md)
