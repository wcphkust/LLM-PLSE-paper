# SelfPiCo: Self-Guided Partial Code Execution with LLMs

**Authors**: Xue, Zhipeng and Gao, Zhipeng and Wang, Shaohua and Hu, Xing and Xia, Xin and Li, Shanping

**Abstract**:

Code executability plays a vital role in software debugging and testing (e.g., detecting runtime exceptions or assertion violations). However, code execution, especially partial or arbitrary code execution, is a non-trivial task due to missing definitions and complex third-party dependencies. To make partial code (such as code snippets posted on the web or code fragments deep inside complex software projects) executable, the existing study has proposed a machine learning model to predict the undefined element types and inject the pre-defined dummy values into execution. However, the performance of their tool is limited due to its simply designed dummy values and the inability to continue learning. In this paper, we design and implement a novel framework, named SelfPiCo (Self-Guided Partial Code Executor), to dynamically guide partial code execution by incorporating the open-source LLM (i.e., Code Llama) within an interactive loop. Particularly, SelfPiCo leverages few-shot in-context learning and chain-of-thought reasoning to elicit human knowledge and logical reasoning based on fine-tuning the Code Llama model. SelfPiCo continuously learns from code execution results and refines its predictions step after step. Our evaluations demonstrate that SelfPiCo can execute 72.7\% and 83.3\% of all lines in the open-source code and Stack Overflow snippets, outperforming the most recent state-of-the-art Lexecutor by 37.9\% and 33.5\%, respectively. Moreover, SelfPiCo successfully detected 18 and 33 runtime type error issues by executing the partial code from eight GitHub software projects and 43 Stack Overflow posts, demonstrating the practical usage and potential application of our framework in practice.

**Link**: [Read Paper](https://doi.org/10.1145/3650212.3680368)

**Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md)
