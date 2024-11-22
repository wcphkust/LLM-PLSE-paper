# Rust-lancet: Automated Ownership-Rule-Violation Fixing with Behavior Preservation

**Authors**: Yang, Wenzhang and Song, Linhai and Xue, Yinxing

**Abstract**:

As a relatively new programming language, Rust is designed to provide both memory safety and runtime performance. To achieve this goal, Rust conducts rigorous static checks against its safety rules during compilation, effectively eliminating memory safety issues that plague C/C++ programs. Although useful, the safety rules pose programming challenges to Rust programmers, since programmers can easily violate safety rules when coding in Rust, leading their code to be rejected by the Rust compiler, a fact underscored by a recent user study. There exists a desire to automate the process of fixing safety-rule violations to enhance Rust's programmability.In this paper, we concentrate on Rust's ownership rules and develop rust-lancet to automatically fix their violations. We devise three strategies for altering code, each intended to modify a Rust program and make it pass Rust's compiler checks. Additionally, we introduce mental semantics to model the behaviors of Rust programs that cannot be compiled due to ownership-rule violations. We design an approach to verify whether modified programs preserve their original behaviors before patches are applied. We apply rust-lancet to 160 safety-rule violations from two sources, successfully fixing 102 violations under the optimal configuration --- more than rustc and six LLM-based techniques. Notably, rust-lancet avoids generating any incorrect patches, a distinction from all other baseline techniques. We also verify the effectiveness of each fixing strategy and behavior preservation validation and affirm the rationale behind these components.

**Link**: [Read Paper](https://doi.org/10.1145/3597503.3639103)

**Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)
