# Code Prompting Elicits Conditional Reasoning Abilities in Text+Code LLMs

**Authors**: Puerto, Haritz and Tutek, Martin and Aditya, Somak and Zhu, Xiaodan and Gurevych, Iryna

**Abstract**:

Reasoning is a fundamental component of language understanding. Recent prompting techniques, such as chain of thought, have consistently improved LLMs’ performance on various reasoning tasks. Nevertheless, there is still little understanding of what triggers reasoning abilities in LLMs in the inference stage. In this paper, we investigate the effect of the input representation on the reasoning abilities of LLMs. We hypothesize that representing natural language tasks as code can enhance specific reasoning abilities such as entity tracking or logical reasoning. To study this, we propose code prompting, a methodology we operationalize as a chain of prompts that transforms a natural language problem into code and directly prompts the LLM using the generated code without resorting to external code execution. We find that code prompting exhibits a high-performance boost for multiple LLMs (up to 22.52 percentage points on GPT 3.5, 7.75 on Mixtral, and 16.78 on Mistral) across multiple conditional reasoning datasets. We then conduct comprehensive experiments to understand how the code representation triggers reasoning abilities and which capabilities are elicited in the underlying models. Our analysis on GPT 3.5 reveals that the code formatting of the input problem is essential for performance improvement. Furthermore, the code representation improves sample efficiency of in-context learning and facilitates state tracking of entities.

**Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.629)

**Labels**: prompt strategy, reason with code
