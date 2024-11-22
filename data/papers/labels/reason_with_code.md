# Reason With Code

- [Can LLMs Reason in the Wild with Programs?](../venues/EMNLP2024/paper_12.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have shown superior capability to solve reasoning problems with programs. While being a promising direction, most of such frameworks are trained and evaluated in settings with a prior knowledge of task requirements. However, as LLMs become more capable, it is necessary to assess their reasoning abilities in more realistic scenarios where many real-world problems are open-ended with ambiguous scope, and often require multiple formalisms to solve. To investigate this, ...
  - **Labels**: [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [Chain of code: Reasoning with a language model-augmented code emulator](../venues/Google2023/paper_1.md), ([Google2023](../venues/Google2023/README.md))

  - **Abstract**: Code provides a general syntactic structure to build complex programs and perform precise computations when paired with a code interpreter -- we hypothesize that language models (LMs) can leverage code-writing to improve Chain of Thought reasoning not only for logic and arithmetic tasks, but also for linguistic ones (and in particular, those that are a mix of both). For example, consider prompting an LM to write code that counts the number of times it detects sarcasm in an essay: the LM may stru...
  - **Labels**: [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [Code Prompting Elicits Conditional Reasoning Abilities in Text+Code LLMs](../venues/EMNLP2024/paper_26.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Reasoning is a fundamental component of language understanding. Recent prompting techniques, such as chain of thought, have consistently improved LLMs’ performance on various reasoning tasks. Nevertheless, there is still little understanding of what triggers reasoning abilities in LLMs in the inference stage. In this paper, we investigate the effect of the input representation on the reasoning abilities of LLMs. We hypothesize that representing natural language tasks as code can enhance specific...
  - **Labels**: [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [Complementary explanations for effective in-context learning](../venues/ACL2023/paper_7.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Large language models (LLMs) have exhibited remarkable capabilities in learning from explanations in prompts, but there has been limited understanding of exactly how these explanations function or why they are effective. This work aims to better understand the mechanisms by which explanations are used for in-context learning. We first study the impact of two different factors on the performance of prompts with explanations: the computation trace (the way the solution is decomposed) and the natur...
  - **Labels**: [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md), [empirical study](empirical_study.md)


- [Don't Transform the Code, Code the Transforms: Towards Precise Code Rewriting using LLMs](../venues/Meta2024/paper_2.md), ([Meta2024](../venues/Meta2024/README.md))

  - **Abstract**: Tools for rewriting, refactoring and optimizing code should be fast and correct. Large language models (LLMs), by their nature, possess neither of these qualities. Yet, there remains tremendous opportunity in using LLMs to improve code. We explore the use of LLMs not to transform code, but to code transforms. We propose a chain-of-thought approach to synthesizing code transformations from a small number of input/output code examples that incorporates execution and feedback. Unlike the direct rew...
  - **Labels**: [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [EHRAgent: Code Empowers Large Language Models for Few-shot Complex Tabular Reasoning on Electronic Health Records](../venues/EMNLP2024/paper_37.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Clinicians often rely on data engineers to retrieve complex patient information from electronic health record (EHR) systems, a process that is both inefficient and time-consuming. We propose EHRAgent, a large language model (LLM) agent empowered with accumulative domain knowledge and robust coding capability. EHRAgent enables autonomous code generation and execution to facilitate clinicians in directly interacting with EHRs using natural language. Specifically, we formulate a multi-tabular reaso...
  - **Labels**: [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [Empowering Multi-step Reasoning across Languages via Program-Aided Language Models](../venues/EMNLP2024/paper_28.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: In-context learning methods are popular inference strategies where Large Language Models (LLMs) are elicited to solve a task using provided demonstrations without parameter updates. Among these approaches are the reasoning methods, best exemplified by Chain-of-Thought (CoT) and Program-Aided Language Models (PAL), which elicit LLMs to generate reasoning paths, thus promoting accuracy and attracting increasing attention. However, despite the success of these methods, the ability to deliver multi-...
  - **Labels**: [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [Explanation selection using unlabeled data for chain-of-thought prompting](../venues/EMNLP2023/paper_14.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Recent work has shown how to prompt large language models with explanations to obtain strong performance on textual reasoning tasks, i.e., the chain-of-thought paradigm. However, subtly different explanations can yield widely varying downstream task accuracy. Explanations that have not been "tuned" for a task, such as off-the-shelf explanations written by nonexperts, may lead to mediocre performance. This paper tackles the problem of how to optimize explanation-infused prompts in a blackbox fash...
  - **Labels**: [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md), [empirical study](empirical_study.md)


- [Fact-Checking Complex Claims with Program-Guided Reasoning](../venues/ACL2023/paper_3.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Fact-checking real-world claims often requires collecting multiple pieces of evidence and applying complex multi-step reasoning. In this paper, we present Program-Guided Fact-Checking (ProgramFC), a novel fact-checking model that decomposes complex claims into simpler sub-tasks that can be solved using a shared library of specialized functions. We first leverage the in-context learning ability of large language models to generate reasoning programs to guide the verification process. Afterward, w...
  - **Labels**: [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [If llm is the wizard, then code is the wand: A survey on how code empowers large language models to serve as intelligent agents](../venues/arXiv2024/paper_27.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: The prominent large language models (LLMs) of today differ from past language models not only in size, but also in the fact that they are trained on a combination of natural language and formal language (code). As a medium between humans and computers, code translates high-level goals into executable steps, featuring standard syntax, logical consistency, abstraction, and modularity. In this survey, we present an overview of the various benefits of integrating code into LLMs' training data. Speci...
  - **Labels**: [survey](survey.md), [agent design](agent_design.md), [reason with code](reason_with_code.md)


- [Language Models as Compilers: Simulating Pseudocode Execution Improves Algorithmic Reasoning in Language Models](../venues/EMNLP2024/paper_38.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Algorithmic reasoning tasks that involve complex logical patterns, such as completing Dyck language, pose challenges for large language models (LLMs), despite their recent success. Prior work has used LLMs to generate programming language and applied external compilers for such tasks. Yet, when on the fly, it is hard to generate an executable code with the correct logic for the solution. Even so, code for one instance cannot be reused for others, although they might require the same logic to sol...
  - **Labels**: [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [PaD: Program-aided Distillation Can Teach Small Models Reasoning Better than Chain-of-thought Fine-tuning](../venues/NAACL2024/paper_3.md), ([NAACL2024](../venues/NAACL2024/README.md))

  - **Abstract**: While large language models (LLMs) excel in various natural language processing tasks, their huge size and the inaccessibility of parameters present challenges for practical deployment. Previous studies try to distill task-specific ability from LLMs to smaller models, using data synthesis and chain-of-thought (CoT) fine-tuning. However, synthetic CoT data often contains faulty reasoning, which deteriorates the quality of distillation, especially in reasoning capabilities. In this work, we propos...
  - **Labels**: [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [Program-Aided Reasoners (Better) Know What They Know](../venues/NAACL2024/paper_2.md), ([NAACL2024](../venues/NAACL2024/README.md))

  - **Abstract**: Prior work shows that program-aided reasoning, in which large language models (LLMs) are combined with programs written in programming languages such as Python, can significantly improve accuracy on various reasoning tasks. However, while accuracy is essential, it is also important for such reasoners to “know what they know”, which can be quantified through the calibration of the model. In this paper, we compare the calibration of Program Aided Language Models (PAL) and text-based Chain-of-thoug...
  - **Labels**: [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [Prompting with Pseudo-Code Instructions](../venues/EMNLP2023/paper_10.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Prompting with natural language instructions has recently emerged as a popular method of harnessing the capabilities of large language models (LLM). Given the inherent ambiguity present in natural language, it is intuitive to consider the possible advantages of prompting with less ambiguous prompt styles, like pseudo-code. In this paper, we explore if prompting via pseudo-code instructions helps improve the performance of pre-trained language models. We manually create a dataset of pseudo-code p...
  - **Labels**: [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [Question Answering as Programming for Solving Time-Sensitive Questions](../venues/EMNLP2023/paper_7.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Question answering plays a pivotal role in human daily life because it involves our acquisition of knowledge about the world. However, due to the dynamic and ever-changing nature of real-world facts, the answer can be completely different when the time constraint in the question changes. Recently, Large Language Models (LLMs) have shown remarkable intelligence in question answering, while our experiments reveal that the aforementioned problems still pose a significant challenge to existing LLMs....
  - **Labels**: [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [Steering Large Language Models between Code Execution and Textual Reasoning](../venues/Microsoft2024/paper_1.md), ([Microsoft2024](../venues/Microsoft2024/README.md))

  - **Abstract**: While a lot of recent research focuses on enhancing the textual reasoning capabilities of Large Language Models (LLMs) by optimizing the multi-agent framework or reasoning chains, several benchmark tasks can be solved with 100% success through direct coding, which is more scalable and avoids the computational overhead associated with textual iterating and searching. Textual reasoning has inherent limitations in solving tasks with challenges in math, logics, optimization, and searching, which is ...
  - **Labels**: [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md)


- [When Do Program-of-Thought Works for Reasoning?](../venues/AAAI2024/paper_1.md), ([AAAI2024](../venues/AAAI2024/README.md))

  - **Abstract**: In the realm of embodied artificial intelligence, the reasoning capabilities of Large Language Models (LLMs) play a pivotal role. Although there are effective methods like program-of-thought prompting for LLMs which uses programming language to tackle complex reasoning tasks, the specific impact of code data on the improvement of reasoning capabilities remains under-explored. To address this gap, we propose complexity-impacted reasoning score CIRS, which combines structural and logical attribute...
  - **Labels**: [prompt strategy](prompt_strategy.md), [reason with code](reason_with_code.md), [empirical study](empirical_study.md)
