# Program Testing

## Fuzzing

- [CodaMosa: Escaping Coverage Plateaus in Test Generation with Pre-Trained Large Language Models](../venues/ICSE2023/paper_1.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Search-based software testing (SBST) generates high-coverage test cases for programs under test with a combination of test case generation and mutation. SBST's performance relies on there being a reasonable probability of generating test cases that exercise the core logic of the program under test. ...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


- [Code-Aware Prompting: A Study of Coverage-Guided Test Generation in Regression Setting using LLM](../venues/FSE2024/paper_25.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Testing plays a pivotal role in ensuring software quality, yet conventional Search Based Software Testing (SBST) methods often struggle with complex software units, achieving suboptimal test coverage. Recent work using large language models (LLMs) for test generation have focused on improving genera...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


- [Drowzee: Metamorphic Testing for Fact-Conflicting Hallucination Detection in Large Language Models](../venues/OOPSLA2024/paper_4.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Large language models (LLMs) have revolutionized language processing, but face critical challenges with security, privacy, and generating hallucinations — coherent but factually inaccurate outputs. A major issue is fact-conflicting hallucination (FCH), where LLMs produce content contradicting ground...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


- [Fuzz4All: Universal Fuzzing with Large Language Models](../venues/ICSE2024/paper_15.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Fuzzing has achieved tremendous success in discovering bugs and vulnerabilities in various software systems. Systems under test (SUTs) that take in programming or formal language as inputs, e.g., compilers, runtime engines, constraint solvers, and software libraries with accessible APIs, are especia...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


- [Fuzzing JavaScript Interpreters with Coverage-Guided Reinforcement Learning for LLM-Based Mutation](../venues/ISSTA2024/paper_22.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: JavaScript interpreters, crucial for modern web browsers, require an effective fuzzing method to identify security-related bugs. However, the strict grammatical requirements for input present significant challenges. Recent efforts to integrate language models for context- aware mutation in fuzzing a...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [compiler testing](../../labels/compiler_testing.md)


- [How Effective Are They? Exploring Large Language Model Based Fuzz Driver Generation](../venues/ISSTA2024/paper_14.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Fuzz drivers are essential for library API fuzzing. However, automatically generating fuzz drivers is a complex task, as it demands the creation of high-quality, correct, and robust API usage code. An LLM-based (Large Language Model) approach for generating fuzz drivers is a promising area of resear...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


- [LLM-Based Code Generation Method for Golang Compiler Testing](../venues/FSE2023/paper_7.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Modern optimizing compilers are among the most complex software systems humans build. One way to identify subtle compiler bugs is fuzzing. Both the quantity and the quality of testcases are crucial to the performance of fuzzing. Traditional testcase-generation methods, such as Csmith and YARPGen, ha...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [compiler testing](../../labels/compiler_testing.md)


- [LLMIF: Augmented Large Language Model for Fuzzing IoT Devices](../venues/S&P2024/paper_2.md), ([S&P2024](../venues/S&P2024/README.md))

  - **Abstract**: Despite the efficacy of fuzzing in verifying the implementation correctness of network protocols, existing IoT protocol fuzzing approaches grapple with several limitations, including obfuscated message formats, unresolved message dependencies, and a lack of evaluations on the testing cases. These li...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


- [Large Language Model guided Protocol Fuzzing](../venues/NDSS2024/paper_2.md), ([NDSS2024](../venues/NDSS2024/README.md))

  - **Abstract**: How to find security flaws in a protocol implementation without a machine-readable specification of the protocol? Facing the internet, protocol implementations are particularly security-critical software systems where inputs must adhere to a specific structure and order that is often informally spec...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [protocol fuzzing](../../labels/protocol_fuzzing.md)


- [Large Language Models Are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models](../venues/ISSTA2023/paper_2.md), ([ISSTA2023](../venues/ISSTA2023/README.md))

  - **Abstract**: Deep Learning (DL) systems have received exponential growth in popularity and have become ubiquitous in our everyday life. Such systems are built on top of popular DL libraries, e.g., TensorFlow and PyTorch which provide APIs as building blocks for DL systems. Detecting bugs in these DL libraries is...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [library testing](../../labels/library_testing.md)


- [Large Language Models are Edge-Case Generators: Crafting Unusual Programs for Fuzzing Deep Learning Libraries](../venues/ICSE2024/paper_5.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Bugs in Deep Learning (DL) libraries may affect almost all downstream DL applications, and it is crucial to ensure the quality of such systems. It is challenging to generate valid input programs for fuzzing DL libraries, since the input programs need to satisfy both the syntax/semantics of the suppo...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


- [Llm4fuzz: Guided fuzzing of smart contracts with large language models](../venues/arXiv2024/paper_22.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: As blockchain platforms grow exponentially, millions of lines of smart contract code are being deployed to manage extensive digital assets. However, vulnerabilities in this mission-critical code have led to significant exploitations and asset losses. Thorough automated security analysis of smart con...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


- [Prompt Fuzzing for Fuzz Driver Generation](../venues/CCS2023/paper_2.md), ([CCS2023](../venues/CCS2023/README.md))

  - **Abstract**: Writing high-quality fuzz drivers is time-consuming and requires a deep understanding of the library. However, the performance of the state-of-the-art automatic fuzz driver generation techniques leaves a lot to be desired. Fuzz drivers, which are learned from consumer code, can reach deep states but...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


- [SMT Solver Validation Empowered by Large Pre-Trained Language Models](../venues/ASE2023/paper_3.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: SMT solvers are utilized to check the satisfiability of logic formulas and have been applied in various crucial domains, including software verification, test case generation, and program synthesis. However, bugs hidden in SMT solvers can lead to severe consequences, causing erroneous results in the...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


- [Sedar: Obtaining High-Quality Seeds for DBMS Fuzzing via Cross-DBMS SQL Transfer](../venues/ICSE2024/paper_16.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Effective DBMS fuzzing relies on high-quality initial seeds, which serve as the starting point for mutation. These initial seeds should incorporate various DBMS features to explore the state space thoroughly. While built-in test cases are typically used as initial seeds, many DBMSs lack comprehensiv...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [DBMS testing](../../labels/DBMS_testing.md)


- [The Mutators Reloaded: Fuzzing Compilers with Large Language Model Generated Mutation Operators](../venues/ASPLOS2024/paper_1.md), ([ASPLOS2024](../venues/ASPLOS2024/README.md))

  - **Abstract**: Crafting high-quality mutators–the core of mutation-based fuzzing that shapes the search space–is challenging. It requires human expertise and creativity, and their implementation demands knowledge of compiler internals. This paper presents MetaMut framework for developing new, useful mutators for c...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [compiler testing](../../labels/compiler_testing.md)


- [When fuzzing meets llms: Challenges and opportunities](../venues/FSE2024/paper_27.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Fuzzing, a widely-used technique for bug detection, has seen advancements through Large Language Models (LLMs). Despite their potential, LLMs face specific challenges in fuzzing. In this paper, we identified five major challenges of LLM-assisted fuzzing. To support our findings, we revisited the mos...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [survey](../../labels/survey.md)


- [WhiteFox: White-Box Compiler Fuzzing Empowered by Large Language Models](../venues/OOPSLA2024/paper_3.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Compiler correctness is crucial, as miscompilation can falsify program behaviors, leading to serious consequences over the software supply chain. In the literature, fuzzing has been extensively studied to uncover compiler defects. However, compiler fuzzing remains challenging: Existing arts focus on...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [compiler testing](../../labels/compiler_testing.md)


## Library Testing

- [Large Language Models Are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models](../venues/ISSTA2023/paper_2.md), ([ISSTA2023](../venues/ISSTA2023/README.md))

  - **Abstract**: Deep Learning (DL) systems have received exponential growth in popularity and have become ubiquitous in our everyday life. Such systems are built on top of popular DL libraries, e.g., TensorFlow and PyTorch which provide APIs as building blocks for DL systems. Detecting bugs in these DL libraries is...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [library testing](../../labels/library_testing.md)


## Dbms Testing

- [Sedar: Obtaining High-Quality Seeds for DBMS Fuzzing via Cross-DBMS SQL Transfer](../venues/ICSE2024/paper_16.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Effective DBMS fuzzing relies on high-quality initial seeds, which serve as the starting point for mutation. These initial seeds should incorporate various DBMS features to explore the state space thoroughly. While built-in test cases are typically used as initial seeds, many DBMSs lack comprehensiv...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [DBMS testing](../../labels/DBMS_testing.md)


## Compiler Testing

- [Fuzzing JavaScript Interpreters with Coverage-Guided Reinforcement Learning for LLM-Based Mutation](../venues/ISSTA2024/paper_22.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: JavaScript interpreters, crucial for modern web browsers, require an effective fuzzing method to identify security-related bugs. However, the strict grammatical requirements for input present significant challenges. Recent efforts to integrate language models for context- aware mutation in fuzzing a...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [compiler testing](../../labels/compiler_testing.md)


- [LLM-Based Code Generation Method for Golang Compiler Testing](../venues/FSE2023/paper_7.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Modern optimizing compilers are among the most complex software systems humans build. One way to identify subtle compiler bugs is fuzzing. Both the quantity and the quality of testcases are crucial to the performance of fuzzing. Traditional testcase-generation methods, such as Csmith and YARPGen, ha...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [compiler testing](../../labels/compiler_testing.md)


- [The Mutators Reloaded: Fuzzing Compilers with Large Language Model Generated Mutation Operators](../venues/ASPLOS2024/paper_1.md), ([ASPLOS2024](../venues/ASPLOS2024/README.md))

  - **Abstract**: Crafting high-quality mutators–the core of mutation-based fuzzing that shapes the search space–is challenging. It requires human expertise and creativity, and their implementation demands knowledge of compiler internals. This paper presents MetaMut framework for developing new, useful mutators for c...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [compiler testing](../../labels/compiler_testing.md)


- [WhiteFox: White-Box Compiler Fuzzing Empowered by Large Language Models](../venues/OOPSLA2024/paper_3.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Compiler correctness is crucial, as miscompilation can falsify program behaviors, leading to serious consequences over the software supply chain. In the literature, fuzzing has been extensively studied to uncover compiler defects. However, compiler fuzzing remains challenging: Existing arts focus on...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [compiler testing](../../labels/compiler_testing.md)


## Protocol Fuzzing

- [Large Language Model guided Protocol Fuzzing](../venues/NDSS2024/paper_2.md), ([NDSS2024](../venues/NDSS2024/README.md))

  - **Abstract**: How to find security flaws in a protocol implementation without a machine-readable specification of the protocol? Facing the internet, protocol implementations are particularly security-critical software systems where inputs must adhere to a specific structure and order that is often informally spec...
  - **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [protocol fuzzing](../../labels/protocol_fuzzing.md)


## Mutation Testing

- [LLMorpheus: Mutation Testing using Large Language Models](../venues/arXiv2024/paper_23.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: In mutation testing, the quality of a test suite is evaluated by introducing faults into a program and determining whether the program's tests detect them. Most existing approaches for mutation testing involve the application of a fixed set of mutation operators, e.g., replacing a "+" with a "-" or ...
  - **Labels**: [program testing](../../labels/program_testing.md), [mutation testing](../../labels/mutation_testing.md)


- [Large Language Models for Equivalent Mutant Detection: How Far Are We?](../venues/ISSTA2024/paper_23.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Mutation testing is vital for ensuring software quality. However, the presence of equivalent mutants is known to introduce redundant cost and bias issues, hindering the effectiveness of mutation testing in practical use. Although numerous equivalent mutant detection (EMD) techniques have been propos...
  - **Labels**: [program testing](../../labels/program_testing.md), [mutation testing](../../labels/mutation_testing.md), [empirical study](../../labels/empirical_study.md)


## Unit Testing

- [An Empirical Evaluation of Using Large Language Models for Automated Unit Test Generation](../venues/TSE2024/paper_10.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Unit tests play a key role in ensuring the correctness of software. However, manually creating unit tests is a laborious task, motivating the need for automation. Large Language Models (LLMs) have recently been applied to various aspects of software development, including their suggested use for aut...
  - **Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md), [empirical study](../../labels/empirical_study.md)


- [ChatGPT vs SBST: A Comparative Assessment of Unit Test Suite Generation](../venues/TSE2024/paper_5.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Recent advancements in large language models (LLMs) have demonstrated exceptional success in a wide range of general domain tasks, such as question answering and following instructions. Moreover, LLMs have shown potential in various software engineering applications. In this study, we present a syst...
  - **Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md), [empirical study](../../labels/empirical_study.md)


- [Domain Adaptation for Code Model-Based Unit Test Case Generation](../venues/ISSTA2024/paper_28.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Recently, deep learning-based test case generation approaches have been proposed to automate the generation of unit test cases. In this study, we leverage Transformer-based code models to generate               unit tests with the help of Domain Adaptation (DA) at a project level. Specifically, we u...
  - **Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md)


- [Evaluating and Improving ChatGPT for Unit Test Generation](../venues/FSE2024/paper_7.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Unit testing plays an essential role in detecting bugs in functionally-discrete program units (e.g., methods). Manually writing high-quality unit tests is time-consuming and laborious. Although the traditional techniques are able to generate tests with reasonable coverage, they are shown to exhibit ...
  - **Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md), [empirical study](../../labels/empirical_study.md), [code generation](../../labels/code_generation.md)


- [On the Evaluation of Large Language Models in Unit Test Generation](../venues/ASE2024/paper_26.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Unit testing is an essential activity in software development for verifying the correctness of software components. However, manually writing unit tests is challenging and time-consuming. The emergence of Large Language Models (LLMs) offers a new direction for automating unit test generation. Existi...
  - **Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md), [empirical study](../../labels/empirical_study.md)


- [Towards Understanding the Effectiveness of Large Language Models on Directed Test Input Generation](../venues/ASE2024/paper_42.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Automatic testing has garnered significant attention and success over the past few decades. Techniques such as unit testing and coverage-guided fuzzing have revealed numerous critical software bugs and vulnerabilities. However, a long-standing, formidable challenge for existing techniques is how to ...
  - **Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md), [empirical study](../../labels/empirical_study.md)


- [UniTSyn: A Large-Scale Dataset Capable of Enhancing the Prowess of Large Language Models for Program Testing](../venues/ISSTA2024/paper_27.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: The remarkable capability of large language models (LLMs) in generating high-quality code has drawn increasing attention in the software testing community. However, existing code LLMs often demonstrate unsatisfactory capabilities in generating accurate, complete tests since they were trained on code...
  - **Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md), [benchmark](../../labels/benchmark.md)


## Differential Testing

- [Nuances are the Key: Unlocking ChatGPT to Find Failure-Inducing Tests with Differential Prompting](../venues/ASE2023/paper_7.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Automated detection of software failures is an important but challenging software engineering task. It involves finding in a vast search space the failure-inducing test cases that contain an input triggering the software fault and an oracle asserting the incorrect execution. We are motivated to stud...
  - **Labels**: [program testing](../../labels/program_testing.md), [differential testing](../../labels/differential_testing.md)


## Debugging

- [A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization](../venues/FSE2024/paper_5.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Fault Localization (FL), in which a developer seeks to identify which part of the code is malfunctioning and needs to be fixed, is a recurring challenge in debugging. To reduce developer burden, many automated FL techniques have been proposed. However, prior work has noted that existing techniques f...
  - **Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md)


- [Effective Large Language Model Debugging with Best-first Tree Search](../venues/NVDIA2024/paper_1.md), ([NVDIA2024](../venues/NVDIA2024/README.md))

  - **Abstract**: Large Language Models (LLMs) show promise in code generation tasks. However, their code-writing abilities are often limited in scope: while they can successfully implement simple functions, they struggle with more complex tasks. A fundamental difference with how an LLM writes code, compared to a hum...
  - **Labels**: [code generation](../../labels/code_generation.md), [debugging](../../labels/debugging.md)


- [Instruct, Not Assist: LLM-based Multi-Turn Planning and Hierarchical Questioning for Socratic Code Debugging](../venues/EMNLP2024/paper_11.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Socratic questioning is an effective teaching strategy, encouraging critical thinking and problem-solving. The conversational capabilities of large language models (LLMs) show great potential for providing scalable, real-time student guidance. However, current LLMs often give away solutions directly...
  - **Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md), [agent design](../../labels/agent_design.md), [planning](../../labels/planning.md)


- [Isolating Compiler Bugs by Generating Effective Witness Programs With Large Language Models](../venues/TSE2024/paper_4.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Compiler bugs pose a significant threat to safety-critical applications, and promptly as well as effectively isolating these bugs is crucial for assuring the quality of compilers. However, the limited availability of debugging information on reported bugs complicates the compiler bug isolation task....
  - **Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


- [LPR: Large Language Models-Aided Program Reduction](../venues/ISSTA2024/paper_5.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Program reduction is a widely used technique to facilitate debugging                compilers by automatically minimizing programs that trigger                compiler bugs. Existing program reduction techniques are either                generic to a wide range of languages (such as Perses and Vulca...
  - **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md), [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md)


- [Large Language Models for Test-Free Fault Localization](../venues/ICSE2024/paper_3.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Fault Localization (FL) aims to automatically localize buggy lines of code, a key first step in many manual and automatic debugging tasks. Previous FL techniques assume the provision of input tests, and often require extensive program analysis, program instrumentation, or data preprocessing. Prior w...
  - **Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


- [Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning](../venues/FSE2024/paper_29.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Program slicing, the process of extracting program statements that influence values at a designated location (known as the slicing criterion), is helpful in both manual and automated debugging. However, such slicing techniques prove ineffective in scenarios where executing specific inputs is prohibi...
  - **Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


- [SelfPiCo: Self-Guided Partial Code Execution with LLMs](../venues/ISSTA2024/paper_16.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Code executability plays a vital role in software debugging and testing (e.g., detecting runtime exceptions or assertion violations). However, code execution, especially partial or arbitrary code execution, is a non-trivial task due to missing definitions and complex third-party dependencies. To mak...
  - **Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md)


- [Teaching large language models to self-debug](../venues/ICLR2024/paper_7.md), ([ICLR2024](../venues/ICLR2024/README.md))

  - **Abstract**: Large language models (LLMs) have achieved impressive performance on code generation. However, for complex programming tasks, generating the correct solution in one go becomes challenging, thus some prior works have designed program repair approaches to improve code generation performance. In this w...
  - **Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md)


## Bug Reproduction

- [Evaluating Diverse Large Language Models for Automatic and General Bug Reproduction](../venues/TSE2024/paper_13.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Bug reproduction is a critical developer activity that is also challenging to automate, as bug reports are often in natural language and thus can be difficult to transform to test cases consistently. As a result, existing techniques mostly focused on crash bugs, which are easier to automatically det...
  - **Labels**: [program testing](../../labels/program_testing.md), [bug reproduction](../../labels/bug_reproduction.md), [empirical study](../../labels/empirical_study.md)


- [Large Language Models are Few-Shot Testers: Exploring LLM-Based General Bug Reproduction](../venues/ICSE2023/paper_5.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Many automated test generation techniques have been developed to aid developers with writing tests. To facilitate full automation, most existing techniques aim to either increase coverage, or generate exploratory inputs. However, existing test generation techniques largely fall short of achieving mo...
  - **Labels**: [program testing](../../labels/program_testing.md), [bug reproduction](../../labels/bug_reproduction.md)


## Vulnerability Exploitation

- [Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models](../venues/arXiv2024/paper_25.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Language Model (LM) agents for cybersecurity that are capable of autonomously identifying vulnerabilities and executing exploits have the potential to cause real-world impact. Policymakers, model providers, and other researchers in the AI and cybersecurity communities are interested in quantifying t...
  - **Labels**: [program testing](../../labels/program_testing.md), [vulnerability exploitation](../../labels/vulnerability_exploitation.md), [benchmark](../../labels/benchmark.md)


- [Evaluating Offensive Security Capabilities of Large Language Models](../venues/Google2024/paper_2.md), ([Google2024](../venues/Google2024/README.md))

  - **Abstract**: At Project Zero, we constantly seek to expand the scope and effectiveness of our vulnerability research. Though much of our work still relies on traditional methods like manual source code audits and reverse engineering, we're always looking for new approaches....
  - **Labels**: [program testing](../../labels/program_testing.md), [vulnerability exploitation](../../labels/vulnerability_exploitation.md)


- [From Naptime to Big Sleep: Using Large Language Models To Catch Vulnerabilities In Real-World Code](../venues/Google2024/paper_1.md), ([Google2024](../venues/Google2024/README.md))

  - **Abstract**: In our previous post, Project Naptime: Evaluating Offensive Security Capabilities of Large Language Models, we introduced our framework for large-language-model-assisted vulnerability research and demonstrated its potential by improving the state-of-the-art performance on Meta's CyberSecEval2 benchm...
  - **Labels**: [program testing](../../labels/program_testing.md), [vulnerability exploitation](../../labels/vulnerability_exploitation.md)


- [Language agents as hackers: Evaluating cybersecurity skills with capture the flag](../venues/NeurIPS2023/paper_1.md), ([NeurIPS2023](../venues/NeurIPS2023/README.md))

  - **Abstract**: Amidst the advent of language models (LMs) and their wide-ranging capabilities, concerns have been raised about their implications with regards to privacy and security. In particular, the emergence of language agents as a promising aid for automating and augmenting digital work poses immediate quest...
  - **Labels**: [program testing](../../labels/program_testing.md), [vulnerability exploitation](../../labels/vulnerability_exploitation.md), [benchmark](../../labels/benchmark.md)


- [Teams of LLM Agents can Exploit Zero-Day Vulnerabilities](../venues/arXiv2024/paper_24.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: LLM agents have become increasingly sophisticated, especially in the realm of cybersecurity. Researchers have shown that LLM agents can exploit real-world vulnerabilities when given a description of the vulnerability and toy capture-the-flag problems. However, these agents still perform poorly on re...
  - **Labels**: [program testing](../../labels/program_testing.md), [vulnerability exploitation](../../labels/vulnerability_exploitation.md)


- [Vulnhuntr: Autonomous AI Finds First 0-Day Vulnerabilities in Wild](../venues/ProtectAI2024/paper_1.md), ([ProtectAI2024](../venues/ProtectAI2024/README.md))

  - **Abstract**: Today, we introduce [Vulnhuntr](https://github.com/protectai/vulnhuntr), a Python static code analyzer that leverages the power of large language models (LLMs) to find and explain complex, multistep vulnerabilities. Thanks to the capabilities of models like Claude 3.5, AI has now uncovered more than...
  - **Labels**: [program testing](../../labels/program_testing.md), [vulnerability exploitation](../../labels/vulnerability_exploitation.md)


