# Fuzzing

- [CodaMosa: Escaping Coverage Plateaus in Test Generation with Pre-Trained Large Language Models](../venues/ICSE2023/paper_1.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Search-based software testing (SBST) generates high-coverage test cases for programs under test with a combination of test case generation and mutation. SBST's performance relies on there being a reasonable probability of generating test cases that exercise the core logic of the program under test. Given such test cases, SBST can then explore the space around them to exercise various parts of the ...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Code-Aware Prompting: A Study of Coverage-Guided Test Generation in Regression Setting using LLM](../venues/FSE2024/paper_25.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Testing plays a pivotal role in ensuring software quality, yet conventional Search Based Software Testing (SBST) methods often struggle with complex software units, achieving suboptimal test coverage. Recent work using large language models (LLMs) for test generation have focused on improving generation quality through optimizing the test generation context and correcting errors in model outputs, ...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Drowzee: Metamorphic Testing for Fact-Conflicting Hallucination Detection in Large Language Models](../venues/OOPSLA2024/paper_4.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Large language models (LLMs) have revolutionized language processing, but face critical challenges with security, privacy, and generating hallucinations — coherent but factually inaccurate outputs. A major issue is fact-conflicting hallucination (FCH), where LLMs produce content contradicting ground truth facts. Addressing FCH is difficult due to two key challenges: 1) Automatically constructing a...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Fuzz4All: Universal Fuzzing with Large Language Models](../venues/ICSE2024/paper_15.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Fuzzing has achieved tremendous success in discovering bugs and vulnerabilities in various software systems. Systems under test (SUTs) that take in programming or formal language as inputs, e.g., compilers, runtime engines, constraint solvers, and software libraries with accessible APIs, are especially important as they are fundamental building blocks of software development. However, existing fuz...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Fuzzing JavaScript Interpreters with Coverage-Guided Reinforcement Learning for LLM-Based Mutation](../venues/ISSTA2024/paper_22.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: JavaScript interpreters, crucial for modern web browsers, require an effective fuzzing method to identify security-related bugs. However, the strict grammatical requirements for input present significant challenges. Recent efforts to integrate language models for context- aware mutation in fuzzing are promising but lack the necessary coverage guidance to be fully effective. This paper presents a n...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)


- [How Effective Are They? Exploring Large Language Model Based Fuzz Driver Generation](../venues/ISSTA2024/paper_14.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Fuzz drivers are essential for library API fuzzing. However, automatically generating fuzz drivers is a complex task, as it demands the creation of high-quality, correct, and robust API usage code. An LLM-based (Large Language Model) approach for generating fuzz drivers is a promising area of research. Unlike traditional program analysis-based generators, this text-based approach is more generaliz...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [LLM-Based Code Generation Method for Golang Compiler Testing](../venues/FSE2023/paper_7.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Modern optimizing compilers are among the most complex software systems humans build. One way to identify subtle compiler bugs is fuzzing. Both the quantity and the quality of testcases are crucial to the performance of fuzzing. Traditional testcase-generation methods, such as Csmith and YARPGen, have been proven successful at discovering compiler bugs. However, such generated testcases have limit...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)


- [LLMIF: Augmented Large Language Model for Fuzzing IoT Devices](../venues/S&P2024/paper_2.md), ([S&P2024](../venues/S&P2024/README.md))

  - **Abstract**: Despite the efficacy of fuzzing in verifying the implementation correctness of network protocols, existing IoT protocol fuzzing approaches grapple with several limitations, including obfuscated message formats, unresolved message dependencies, and a lack of evaluations on the testing cases. These limitations significantly curtail the capabilities of IoT fuzzers in vulnerability identification. In ...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Large Language Model guided Protocol Fuzzing](../venues/NDSS2024/paper_2.md), ([NDSS2024](../venues/NDSS2024/README.md))

  - **Abstract**: How to find security flaws in a protocol implementation without a machine-readable specification of the protocol? Facing the internet, protocol implementations are particularly security-critical software systems where inputs must adhere to a specific structure and order that is often informally specified in hundreds of pages in natural language (RFC). Without some machine-readable version of that ...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [protocol fuzzing](protocol_fuzzing.md)


- [Large Language Models Are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models](../venues/ISSTA2023/paper_2.md), ([ISSTA2023](../venues/ISSTA2023/README.md))

  - **Abstract**: Deep Learning (DL) systems have received exponential growth in popularity and have become ubiquitous in our everyday life. Such systems are built on top of popular DL libraries, e.g., TensorFlow and PyTorch which provide APIs as building blocks for DL systems. Detecting bugs in these DL libraries is critical for almost all downstream DL systems in ensuring effectiveness/safety for end users. Meanw...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [library testing](library_testing.md)


- [Large Language Models are Edge-Case Generators: Crafting Unusual Programs for Fuzzing Deep Learning Libraries](../venues/ICSE2024/paper_5.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Bugs in Deep Learning (DL) libraries may affect almost all downstream DL applications, and it is crucial to ensure the quality of such systems. It is challenging to generate valid input programs for fuzzing DL libraries, since the input programs need to satisfy both the syntax/semantics of the supported languages (e.g., Python) and the tensor/operator constraints for constructing valid computation...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Llm4fuzz: Guided fuzzing of smart contracts with large language models](../venues/arXiv2024/paper_22.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: As blockchain platforms grow exponentially, millions of lines of smart contract code are being deployed to manage extensive digital assets. However, vulnerabilities in this mission-critical code have led to significant exploitations and asset losses. Thorough automated security analysis of smart contracts is thus imperative. This paper introduces LLM4Fuzz to optimize automated smart contract secur...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Prompt Fuzzing for Fuzz Driver Generation](../venues/CCS2023/paper_2.md), ([CCS2023](../venues/CCS2023/README.md))

  - **Abstract**: Writing high-quality fuzz drivers is time-consuming and requires a deep understanding of the library. However, the performance of the state-of-the-art automatic fuzz driver generation techniques leaves a lot to be desired. Fuzz drivers, which are learned from consumer code, can reach deep states but are restricted to their external inputs. On the other hand, interpretative fuzzing can explore most...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [SMT Solver Validation Empowered by Large Pre-Trained Language Models](../venues/ASE2023/paper_3.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: SMT solvers are utilized to check the satisfiability of logic formulas and have been applied in various crucial domains, including software verification, test case generation, and program synthesis. However, bugs hidden in SMT solvers can lead to severe consequences, causing erroneous results in these domains. Therefore, ensuring the reliability and robustness of SMT solvers is of critical importa...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md)


- [Sedar: Obtaining High-Quality Seeds for DBMS Fuzzing via Cross-DBMS SQL Transfer](../venues/ICSE2024/paper_16.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Effective DBMS fuzzing relies on high-quality initial seeds, which serve as the starting point for mutation. These initial seeds should incorporate various DBMS features to explore the state space thoroughly. While built-in test cases are typically used as initial seeds, many DBMSs lack comprehensive test cases, making it difficult to apply state-of-the-art fuzzing techniques directly.To address t...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [DBMS testing](DBMS_testing.md)


- [The Mutators Reloaded: Fuzzing Compilers with Large Language Model Generated Mutation Operators](../venues/ASPLOS2024/paper_1.md), ([ASPLOS2024](../venues/ASPLOS2024/README.md))

  - **Abstract**: Crafting high-quality mutators–the core of mutation-based fuzzing that shapes the search space–is challenging. It requires human expertise and creativity, and their implementation demands knowledge of compiler internals. This paper presents MetaMut framework for developing new, useful mutators for compiler fuzzing. It integrates our compilerdomain knowledge into prompts and processes that can best...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)


- [When fuzzing meets llms: Challenges and opportunities](../venues/FSE2024/paper_27.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Fuzzing, a widely-used technique for bug detection, has seen advancements through Large Language Models (LLMs). Despite their potential, LLMs face specific challenges in fuzzing. In this paper, we identified five major challenges of LLM-assisted fuzzing. To support our findings, we revisited the most recent papers from top-tier conferences, confirming that these challenges are widespread. As a rem...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [survey](survey.md)


- [WhiteFox: White-Box Compiler Fuzzing Empowered by Large Language Models](../venues/OOPSLA2024/paper_3.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Compiler correctness is crucial, as miscompilation can falsify program behaviors, leading to serious consequences over the software supply chain. In the literature, fuzzing has been extensively studied to uncover compiler defects. However, compiler fuzzing remains challenging: Existing arts focus on black- and grey-box fuzzing, which generates test programs without sufficient understanding of inte...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)
