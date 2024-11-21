# ArchCode: Incorporating Software Requirements in Code Generation with Large Language Models

**Authors**: Han, Hojae and Kim, Jaejin and Yoo, Jaeseok and Lee, Youngwon and Hwang, Seung-won

**Abstract**:

This paper aims to extend the code generation capability of large language models (LLMs) to automatically manage comprehensive software requirements from given textual descriptions. Such requirements include both functional (i.e. achieving expected behavior for inputs) and non-functional (e.g., time/space performance, robustness, maintainability) requirements. However, textual descriptions can either express requirements verbosely or may even omit some of them. We introduce ARCHCODE, a novel framework that leverages in-context learning to organize requirements observed in descriptions and to extrapolate unexpressed requirements from them. ARCHCODE generates requirements from given descriptions, conditioning them to produce code snippets and test cases. Each test case is tailored to one of the requirements, allowing for the ranking of code snippets based on the compliance of their execution results with the requirements. Public benchmarks show that ARCHCODE enhances to satisfy functional requirements, significantly improving Pass@k scores.Furthermore, we introduce HumanEval-NFR, the first evaluation of LLMs’ non-functional requirements in code generation, demonstrating ARCHCODE’s superiority over baseline methods. The implementation of ARCHCODE and the HumanEval-NFR benchmark are both publicly accessible.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.730)

**Labels**: code generation, program synthesis
