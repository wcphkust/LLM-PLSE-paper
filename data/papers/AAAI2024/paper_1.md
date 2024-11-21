# When Do Program-of-Thought Works for Reasoning?

**Authors**: Bi, Zhen and Zhang, Ningyu and Jiang, Yinuo and Deng, Shumin and Zheng, Guozhou and Chen, Huajun

**Abstract**:

In the realm of embodied artificial intelligence, the reasoning capabilities of Large Language Models (LLMs) play a pivotal role. Although there are effective methods like program-of-thought prompting for LLMs which uses programming language to tackle complex reasoning tasks, the specific impact of code data on the improvement of reasoning capabilities remains under-explored. To address this gap, we propose complexity-impacted reasoning score CIRS, which combines structural and logical attributes, to measure the correlation between code and reasoning abilities. Specifically, we use the abstract syntax tree to encode the structural information and calculate logical complexity by considering the difficulty and the cyclomatic complexity. Through an empirical analysis, we find not all code data of complexity can be learned or understood by LLMs. Optimal level of complexity is critical to the improvement of reasoning abilities by program-aided prompting. Then we design an auto-synthesizing and stratifying algorithm, and apply it to instruction generation for mathematical reasoning and code data filtering for code generation tasks. Extensive results demonstrates the effectiveness of our proposed approach.

**Link**: [Read Paper](No Link Available)

**Labels**: prompt strategy, reason with code, empirical study
