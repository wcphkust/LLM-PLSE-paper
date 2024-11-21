# Evaluating In-Context Learning of Libraries for Code Generation

**Authors**: Patel, Arkil and Reddy, Siva and Bahdanau, Dzmitry and Dasigi, Pradeep

**Abstract**:

Contemporary Large Language Models (LLMs) exhibit a high degree of code generation and comprehension capability. A particularly promising area is their ability to interpret code modules from unfamiliar libraries for solving user-instructed tasks. Recent work has shown that large proprietary LLMs can learn novel library usage in-context from demonstrations. These results raise several open questions: whether demonstrations of library usage is required, whether smaller (and more open) models also possess such capabilities, etc. In this work, we take a broader approach by systematically evaluating a diverse array of LLMs across three scenarios reflecting varying levels of domain specialization to understand their abilities and limitations in generating code based on libraries defined in-context. Our results show that even smaller open-source LLMs like Llama-2 and StarCoder demonstrate an adept understanding of novel code libraries based on specification presented in-context. Our findings further reveal that LLMs exhibit a surprisingly high proficiency in learning novel library modules even when provided with just natural language descriptions or raw code implementations of the functions, which are often cheaper to obtain than demonstrations. Overall, our results pave the way for harnessing LLMs in more adaptable and dynamic coding environments.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2024.naacl-long.161)

**Labels**: code generation, program synthesis, empirical study
