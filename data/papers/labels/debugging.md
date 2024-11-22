# Debugging

- [A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization](../venues/FSE2024/paper_5.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Fault Localization (FL), in which a developer seeks to identify which part of the code is malfunctioning and needs to be fixed, is a recurring challenge in debugging. To reduce developer burden, many automated FL techniques have been proposed. However, prior work has noted that existing techniques fail to provide rationales for the suggested locations, hindering developer adoption of these techniques. With this in mind, we propose AutoFL, a Large Language Model (LLM)-based FL technique that gene...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md)


- [Effective Large Language Model Debugging with Best-first Tree Search](../venues/NVDIA2024/paper_1.md), ([NVDIA2024](../venues/NVDIA2024/README.md))

  - **Abstract**: Large Language Models (LLMs) show promise in code generation tasks. However, their code-writing abilities are often limited in scope: while they can successfully implement simple functions, they struggle with more complex tasks. A fundamental difference with how an LLM writes code, compared to a human programmer, is that it cannot consistently spot and fix bugs. Debugging is a crucial skill for programmers and it enables iterative code refinement towards a correct implementation. In this work, w...
  - **Labels**: [code generation](code_generation.md), [debugging](debugging.md)


- [Instruct, Not Assist: LLM-based Multi-Turn Planning and Hierarchical Questioning for Socratic Code Debugging](../venues/EMNLP2024/paper_11.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Socratic questioning is an effective teaching strategy, encouraging critical thinking and problem-solving. The conversational capabilities of large language models (LLMs) show great potential for providing scalable, real-time student guidance. However, current LLMs often give away solutions directly, making them ineffective instructors. We tackle this issue in the code debugging domain with TreeInstruct, an Instructor agent guided by a novel state space-based planning algorithm. TreeInstruct ask...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [agent design](agent_design.md), [planning](planning.md)


- [Isolating Compiler Bugs by Generating Effective Witness Programs With Large Language Models](../venues/TSE2024/paper_4.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Compiler bugs pose a significant threat to safety-critical applications, and promptly as well as effectively isolating these bugs is crucial for assuring the quality of compilers. However, the limited availability of debugging information on reported bugs complicates the compiler bug isolation task. Existing compiler bug isolation approaches convert the problem into a test program mutation problem, but they are still limited by ineffective mutation strategies or high human effort requirements. D...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [LPR: Large Language Models-Aided Program Reduction](../venues/ISSTA2024/paper_5.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Program reduction is a widely used technique to facilitate debugging                compilers by automatically minimizing programs that trigger                compiler bugs. Existing program reduction techniques are either                generic to a wide range of languages (such as Perses and Vulcan)                or specifically optimized for one certain language by exploiting                language-specific knowledge (e.g., C-Reduce). However, synergistically                combining both g...
  - **Labels**: [code generation](code_generation.md), [program transformation](program_transformation.md), [program testing](program_testing.md), [debugging](debugging.md)


- [Large Language Models for Test-Free Fault Localization](../venues/ICSE2024/paper_3.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Fault Localization (FL) aims to automatically localize buggy lines of code, a key first step in many manual and automatic debugging tasks. Previous FL techniques assume the provision of input tests, and often require extensive program analysis, program instrumentation, or data preprocessing. Prior work on deep learning for APR struggles to learn from small datasets and produces limited results on real-world programs. Inspired by the ability of large language models (LLMs) of code to adapt to new...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning](../venues/FSE2024/paper_29.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Program slicing, the process of extracting program statements that influence values at a designated location (known as the slicing criterion), is helpful in both manual and automated debugging. However, such slicing techniques prove ineffective in scenarios where executing specific inputs is prohibitively expensive, or even impossible, as with partial code. In this paper, we introduce ND-Slicer, a predictive slicing methodology that caters to specific executions based on a particular input, over...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [SelfPiCo: Self-Guided Partial Code Execution with LLMs](../venues/ISSTA2024/paper_16.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Code executability plays a vital role in software debugging and testing (e.g., detecting runtime exceptions or assertion violations). However, code execution, especially partial or arbitrary code execution, is a non-trivial task due to missing definitions and complex third-party dependencies. To make partial code (such as code snippets posted on the web or code fragments deep inside complex software projects) executable, the existing study has proposed a machine learning model to predict the und...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md)


- [Teaching large language models to self-debug](../venues/ICLR2024/paper_7.md), ([ICLR2024](../venues/ICLR2024/README.md))

  - **Abstract**: Large language models (LLMs) have achieved impressive performance on code generation. However, for complex programming tasks, generating the correct solution in one go becomes challenging, thus some prior works have designed program repair approaches to improve code generation performance. In this work, we propose Self-Debugging, which teaches a large language model to debug its predicted program via few-shot demonstrations. In particular, we demonstrate that Self-Debugging can teach the large l...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md)
