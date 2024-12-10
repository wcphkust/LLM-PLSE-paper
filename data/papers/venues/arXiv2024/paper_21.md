# Program Slicing in the Era of Large Language Models

**Authors**: Shahandashti, Kimya Khakzad and Mohajer, Mohammad Mahdi and Belle, Alvine Boaye and Wang, Song and Hemmati, Hadi

**Abstract**:

Program slicing is a critical technique in software engineering, enabling developers to isolate relevant portions of code for tasks such as bug detection, code comprehension, and debugging. In this study, we investigate the application of large language models (LLMs) to both static and dynamic program slicing, with a focus on Java programs. We evaluate the performance of four state-of-the-art LLMs- GPT-4o, GPT-3.5 Turbo, Llama-2, and Gemma-7B leveraging advanced prompting techniques, including few-shot learning and chain-of-thought reasoning. Using a dataset of 100 Java programs derived from LeetCode problems, our experiments reveal that GPT-4o performs the best in both static and dynamic slicing across other LLMs, achieving an accuracy of 60.84% and 59.69%, respectively. Our results also show that the LLMs we experimented with are yet to achieve reasonable performance for either static slicing or dynamic slicing. Through a rigorous manual analysis, we developed a taxonomy of root causes and failure locations to explore the unsuccessful cases in more depth. We identified Complex Control Flow as the most frequent root cause of failures, with the majority of issues occurring in Variable Declarations and Assignments locations. To improve the performance of LLMs, we further examined two independent strategies for prompting guided by our taxonomy, including prompt crafting, which involved refining the prompts to better guide the LLM through the slicing process, and iterative prompting, where the model receives feedback on the root cause and location of the failure and re-generates its responses. Our evaluation shows these two prompting enhancement approaches can improve accuracy by 4% and 3.9%, respectively.

**Link**: [Read Paper](https://arxiv.org/pdf/2409.12369)

**Labels**: [static analysis](../../labels/static_analysis.md), [data-flow analysis](../../labels/data-flow_analysis.md)
