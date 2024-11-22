# Leveraging Large Language Model to Assist Detecting Rust Code Comment Inconsistency

**Authors**: Zhang, Yichi and Liu, Zixi and Feng, Yang and Xu, Baowen

**Abstract**:

Rust is renowned for its robust memory safety capabilities, yet its distinctive memory management model poses substantial challenges in both writing and understanding programs. Within Rust source code, comments are employed to clearly delineate conditions that might cause panic behavior, thereby warning developers about potential hazards associated with specific operations. Therefore, comments are particularly crucial for documenting Rust's program logic and design. Nevertheless, as modern software frequently undergoes updates and modifications, maintaining the accuracy and relevance of these comments becomes a labor-intensive endeavor.In this paper, inspired by the remarkable capabilities of Large Language Models (LLMs) in understanding software programs, we propose a code-comment inconsistency detection tool, namely RustC4, that combines program analysis and LLM-driven techniques to identify inconsistencies in code comments. RustC4 leverages LLMs' ability to interpret natural language descriptions within code comments, facilitating the extraction of design constraints. Program analysis techniques are then employed to accurately verify the implementation of these constraints. To evaluate the effectiveness of RustC4, we construct a dataset from 12 large-scale real-world Rust projects. The experiment results demonstrate that RustC4 is effective in detecting 176 real inconsistent cases and 23 of them have been confirmed and fixed by developers by the time this paper was submitted.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695010)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
