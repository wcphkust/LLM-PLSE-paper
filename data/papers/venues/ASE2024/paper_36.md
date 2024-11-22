# CoqPilot, a plugin for LLM-based generation of proofs

**Authors**: Kozyrev, Andrei and Solovev, Gleb and Khramov, Nikita and Podkopaev, Anton

**Abstract**:

We present CoqPilot, a VS Code extension designed to help automate writing of Coq proofs. The plugin collects the parts of proofs marked with the admit tactic in a Coq file, i.e., proof holes, and combines LLMs along with non-machine-learning methods to generate proof candidates for the holes. Then, CoqPilot checks if each proof candidate solves the given subgoal and, if successful, replaces the hole with it. The focus of CoqPilot is twofold. Firstly, we want to allow users to seamlessly combine multiple Coq generation approaches and provide a zero-setup experience for our tool. Secondly, we want to deliver a platform for LLM-based experiments on Coq proof generation. We developed a benchmarking system for Coq generation methods, available in the plugin, and conducted an experiment using it, showcasing the framework's possibilities. Demo of CoqPilot is available at: https://youtu.be/oB1Lx-So9Lo. Code at: https://github.com/JetBrains-Research/coqpilot

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695357)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)
