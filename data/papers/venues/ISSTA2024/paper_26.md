# Collaboration to Repository-Level Vulnerability Detection

**Authors**: Wen, Xin-Cheng

**Abstract**:

Large Language Model (LLM)-based methods have proven to be effective for many software engineering domains, with a potential for substantial productivity effective for software vulnerability detection.    However, due to the limitation of the length of input contexts of LLM, the existing LLM-based methods mainly focus on detecting function-level and leveraging the in-file context information for vulnerability detection (i.e., intra-procedural vulnerabilities), ignoring the more complex inter-procedural vulnerability detection scenarios in practice.    For instance, in real-world scenarios, developers routinely engage with program analysis to detect vulnerabilities that span multiple cross-file information within repositories.       Since complex processes tend to have redundancy dependencies from spanning multiple files in the repository level and invoking multiple static analysis tools, the ideal goal of vulnerability detection is to extract the vulnerability-related information from the repository and provide potential possible explanations for vulnerability triggers.   However, such a goal is hard to achieve, and thus in this work, we design three works through multi-agent collaboration to approach the goal of repository-level vulnerability detection.

**Link**: [Read Paper](https://doi.org/10.1145/3650212.3685562)

**Labels**: [code generation](../../labels/code_generation.md), [bug detection](../../labels/bug_detection.md)
