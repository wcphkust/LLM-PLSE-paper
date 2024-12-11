# Program Repair

- [An Empirical Study on Fine-Tuning Large Language Models of Code for Automated Program Repair](../venues/ASE2023/paper_2.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: The advent of large language models (LLMs) has opened up new opportunities for automated program repair (APR). In particular, some recent studies have explored how to leverage large language models of code (LLMCs) for program repair tasks and show promising results. However, most of them adopt the zero/few-shot learning paradigm for APR, which directly use LLMCs to generate the possibly correct code given its surrounding context. Though effective, the repair capabilities of LLMCs based on the fi...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [AutoCodeRover: Autonomous Program Improvement](../venues/ISSTA2024/paper_20.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Researchers have made significant progress in automating the software development process in the past decades. Automated techniques for issue summarization, bug reproduction, fault localization, and program repair have been built to ease the workload of developers. Recent progress in Large Language Models (LLMs) has significantly impacted the development process, where developers can use LLM-based programming assistants to achieve automated coding. Nevertheless, software engineering involves the...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Automated Program Repair in the Era of Large Pre-Trained Language Models](../venues/ICSE2023/paper_4.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Automated Program Repair (APR) aims to help developers automatically patch software bugs. However, current state-of-the-art traditional and learning-based APR techniques face the problem of limited patch variety, failing to fix complicated bugs. This is mainly due to the reliance on bug-fixing datasets to craft fix templates (traditional) or directly predict potential patches (learning-based). Large Pre-Trained Language Models (LLMs), trained using billions of text/code tokens, can potentially h...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Automated Program Repair via Conversation: Fixing 162 out of 337 Bugs for $0.42 Each using ChatGPT](../venues/ISSTA2024/paper_10.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Automated Program Repair (APR) aims to automatically generate patches for buggy programs. Traditional APR techniques suffer from a lack of patch variety as they rely heavily on handcrafted or mined bug fixing patterns and cannot easily generalize to other bug/fix types. To address this limitation, recent APR work has been focused on leveraging modern Large Language Models (LLMs) to directly generate patches for APR. Such LLM-based APR tools work by first constructing an input prompt built using ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Automated Program Repair via Conversation:Fixing 162 out of 337 Bugs for $0.42 Each using ChatGPT](../venues/ISSTA2024/paper_2.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Automated Program Repair (APR) aims to automatically generate patches for buggy programs. Traditional APR techniques suffer from a lack of patch variety as they rely heavily on handcrafted or mined bug fixing patterns and cannot easily generalize to other bug/fix types. To address this limitation, recent APR work has been focused on leveraging modern Large Language Models (LLMs) to directly generate patches for APR. Such LLM-based APR tools work by first constructing an input prompt built using ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Automated Repair of Programs from Large Language Models](../venues/ICSE2023/paper_3.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Large language models such as Codex, have shown the capability to produce code for many programming tasks. However, the success rate of existing models is low, especially for complex programming tasks. One of the reasons is that language models lack awareness of program semantics, resulting in incorrect programs, or even programs which do not compile. In this paper, we systematically study whether automated program repair (APR) techniques can fix the incorrect solutions produced by language mode...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Benchmarking Automated Program Repair: An Extensive Study on Both Real-World and Artificial Bugs](../venues/ISSTA2024/paper_7.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: As bugs are inevitable and prevalent in real-world programs, many Automated Program Repair (APR) techniques have been proposed to generate patches for them. However, due to the lack of a standard for evaluating APR techniques, prior works tend to use different settings and benchmarks in evaluation, threatening the trustworthiness of the evaluation results. Additionally, they typically only adopt plausibility and genuineness as evaluation metrics, which may potentially mask some underlying issues...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [benchmark](benchmark.md)


- [Better Patching Using LLM Prompting, via Self-Consistency](../venues/ASE2023/paper_5.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Large Language models (LLMs) can be induced to solve non-trivial problems with “few-shot” prompts including illustrative problem-solution examples. Now if the few-shots also include “chain of thought” ($\mathcal{C}oT$) explanations, which are of the form problem-explanation-solution, LLMs will generate a “explained” solution, and perform even better. Recently an exciting, substantially better technique, self-consistency [1] ($\mathcal{S}-C$) has emerged, based on the intuition that there are man...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [prompt strategy](prompt_strategy.md)


- [CREF: An LLM-Based Conversational Software Repair Framework for Programming Tutors](../venues/ISSTA2024/paper_11.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: With the proven effectiveness of Large Language Models (LLMs) in code-related tasks, researchers have explored their potential for program repair. However, existing repair benchmarks might have influenced LLM training data, potentially causing data leakage. To evaluate LLMs’ realistic repair capabilities, (i) we introduce an extensive, non-crawled benchmark TutorCode, comprising 1,239 C++ defect codes and associated information such as tutor guidance, solution description, failing test cases, an...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Coffee-Gym: An Environment for Evaluating and Improving Natural Language Feedback on Erroneous Code](../venues/EMNLP2024/paper_38.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: This paper presents Coffee-Gym, a comprehensive RL environment for training models that provide feedback on code editing. Coffee-Gym includes two major components: (1) Coffee, a dataset containing humans’ code edit traces for coding questions and human-written feedback for editing erroneous code; (2) CoffeeEval, a reward function that faithfully reflects the helpfulness of feedback by assessing the performance of the revised code in unit tests. With them, Coffee-Gym addresses the unavailability ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [benchmark](benchmark.md)


- [ContractTinker: LLM-Empowered Vulnerability Repair for Real-World Smart Contracts](../venues/ASE2024/paper_35.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Smart contracts are susceptible to being exploited by attackers, especially when facing real-world vulnerabilities. To mitigate this risk, developers often rely on third-party audit services to identify potential vulnerabilities before project deployment. Nevertheless, repairing the identified vulnerabilities is still complex and laborintensive, particularly for developers lacking security expertise. Moreover, existing pattern-based repair tools mostly fail to address real-world vulnerabilities ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Copilot-in-the-Loop: Fixing Code Smells in Copilot-Generated Python Code using Copilot](../venues/ASE2024/paper_31.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: As one of the most popular dynamic languages, Python experiences a decrease in readability and maintainability when code smells are present. Recent advancements in Large Language Models have sparked growing interest in AI-enabled tools for both code generation and refactoring. GitHub Copilot is one such tool that has gained widespread usage. Copilot Chat, released in September 2023, functions as an interactive tool aimed at facilitating natural language-powered coding. However, limited attention...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Copiloting the Copilots: Fusing Large Language Models with Completion Engines for Automated Program Repair](../venues/FSE2023/paper_1.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: During Automated Program Repair (APR), it can be challenging&nbsp;to synthesize correct patches for real-world systems in general-purpose programming languages. Recent Large Language Models&nbsp;(LLMs) have been shown to be helpful “copilots” in assisting developers with various coding tasks, and have also been directly&nbsp;applied for patch synthesis. However, most LLMs treat programs as&nbsp;sequences of tokens, meaning that they are ignorant of the underlying semantics constraints of the tar...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Exploring Parameter-Efficient Fine-Tuning of Large Language Model on Automated Program Repair](../venues/ASE2024/paper_14.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Automated Program Repair (APR) aims to fix bugs by generating patches. And existing work has demonstrated that "pre-training and fine-tuning" paradigm enables Large Language Models (LLMs) improve fixing capabilities on APR. However, existing work mainly focuses on Full-Model Fine-Tuning (FMFT) for APR and limited research has been conducted on the execution-based evaluation of Parameter-Efficient Fine-Tuning (PEFT) for APR. Comparing to FMFT, PEFT can reduce computing resource consumption withou...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [FastFixer: An Efficient and Effective Approach for Repairing Programming Assignments](../venues/ASE2024/paper_12.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Providing personalized and timely feedback for student's programming assignments is useful for programming education. Automated program repair (APR) techniques have been used to fix the bugs in programming assignments, where the Large Language Models (LLMs) based approaches have shown promising results. Given the growing complexity of identifying and fixing bugs in advanced programming assignments, current fine-tuning strategies for APR are inadequate in guiding the LLM to identify bugs and make...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [How Effective Are Neural Networks for Fixing Security Vulnerabilities](../venues/ISSTA2023/paper_3.md), ([ISSTA2023](../venues/ISSTA2023/README.md))

  - **Abstract**: Security vulnerability repair is a difficult task that is in dire need of automation. Two groups of techniques have shown promise: (1) large code language models (LLMs) that have been pre-trained on source code for tasks such as code completion, and (2) automated program repair (APR) techniques that use deep learning (DL) models to automatically fix software bugs. This paper is the first to study and compare Java vulnerability repair capabilities of LLMs and DL-based APR models. The contribution...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [benchmark](benchmark.md)


- [Improving Automated Program Repair with Domain Adaptation](../venues/TOSEM2024/paper_8.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Automated Program Repair (APR) is defined as the process of fixing a bug/defect in the source code, by an automated tool. APR tools have recently experienced promising results by leveraging state-of-the-art Neural Language Processing (NLP) techniques. APR tools such as TFix and CodeXGLUE that combine text-to-text transformers with software-specific techniques are outperforming alternatives, these days. However, in most APR studies, the train and test sets are chosen from the same set of projects...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Improving Transformer-based Program Repair Model through False Behavior Diagnosis](../venues/EMNLP2023/paper_17.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Research on automated program repairs using transformer-based models has recently gained considerable attention. The comprehension of the erroneous behavior of a model enables the identification of its inherent capacity and provides insights for improvement. However, the current landscape of research on program repair models lacks an investigation of their false behavior. Thus, we propose a methodology for diagnosing and treating the false behaviors of transformer-based program repair models. Sp...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [InferFix: End-to-End Program Repair with LLMs](../venues/FSE2023/paper_5.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Software development life cycle is profoundly influenced by bugs; their introduction, identification, and eventual resolution account for a significant portion of software development cost. This has motivated software engineering researchers and practitioners to propose different approaches for automating the identification and repair of software defects. Large Language Models (LLMs) have been adapted to the program repair task through few-shot demonstration learning and instruction prompting, t...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Is Self-Repair a Silver Bullet for Code Generation?](../venues/ICLR2023/paper_1.md), ([ICLR2023](../venues/ICLR2023/README.md))

  - **Abstract**: Large language models have shown remarkable aptitude in code generation, but still struggle to perform complex tasks. Self-repair---in which the model debugs and repairs its own code---has recently become a popular way to boost performance in these settings. However, despite its increasing popularity, existing studies of self-repair have been limited in scope; in many settings, its efficacy thus remains poorly understood. In this paper, we analyze Code Llama, GPT-3.5 and GPT-4's ability to perfo...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [LLMs Cannot Reliably Identify and Reason About Security Vulnerabilities (Yet?): A Comprehensive Evaluation, Framework, and Benchmarks](../venues/S&P2024/paper_1.md), ([S&P2024](../venues/S&P2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have been suggested for use in automated vulnerability repair, but benchmarks showing they can consistently identify security-related bugs are lacking. We thus develop SecLLMHolmes, a fully automated evaluation framework that performs the most detailed investigation to date on whether LLMs can reliably identify and reason about security-related bugs. We construct a set of 228 code scenarios and analyze eight of the most capable LLMs across eight different investigati...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Mining Action Rules for Defect Reduction Planning](../venues/FSE2024/paper_12.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Defect reduction planning plays a vital role in enhancing software quality and minimizing software maintenance costs. By training a black box machine learning model and “explaining” its predictions, explainable AI for software engineering aims to identify the code characteristics that impact maintenance risks. However, post-hoc explanations do not always faithfully reflect what the original model computes. In this paper, we introduce CounterACT, a Counterfactual ACTion rule mining approach that ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Neurosymbolic Repair of Test Flakiness](../venues/ISSTA2024/paper_17.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Test flakiness, a non-deterministic behavior of builds irrelevant to code changes, is a major and continuing impediment to deliver- ing reliable software. The very few techniques for the automated repair of test flakiness are specifically crafted to repair either Order- Dependent (OD) or Implementation-Dependent (ID) flakiness. They are also all symbolic approaches, i.e., they leverage program analy- sis to detect and repair known test flakiness patterns and root causes, failing to generalize. T...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Out of Context: How important is Local Context in Neural Program Repair?](../venues/ICSE2024/paper_27.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Deep learning source code models have been applied very successfully to the problem of automated program repair. One of the standing issues is the small input window of current models which often cannot fully fit the context code required for a bug fix (e.g., method or class declarations of a project). Instead, input is often restricted to the local context, that is, the lines below and above the bug location. In this work we study the importance of this local context on repair success: how much...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Out of Sight, Out of Mind: Better Automatic Vulnerability Repair by Broadening Input Ranges and Sources](../venues/ICSE2024/paper_28.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: The advances of deep learning (DL) have paved the way for automatic software vulnerability repair approaches, which effectively learn the mapping from the vulnerable code to the fixed code. Nevertheless, existing DL-based vulnerability repair methods face notable limitations: 1) they struggle to handle lengthy vulnerable code, 2) they treat code as natural language texts, neglecting its inherent structure, and 3) they do not tap into the valuable expert knowledge present in the expert system. To...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Programming Assistant for Exception Handling with CodeBERT](../venues/ICSE2024/paper_13.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: With practical code reuse, the code fragments from developers' forums often migrate to applications. Owing to the incomplete nature of such fragments, they often lack the details on exception handling. The adaptation for exception handling to the codebase is not trivial as developers must learn and memorize what API methods could cause exceptions and what exceptions need to be handled. We propose Neurex, an exception handling recommender that learns from complete code, and accepts a given Java c...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [PyDex: Repairing Bugs in Introductory Python Assignments using LLMs](../venues/OOPSLA2024/paper_6.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Students often make mistakes in their introductory programming assignments as part of their learning process. Unfortunately, providing custom repairs for these mistakes can require a substantial amount of time and effort from class instructors. Automated program repair (APR) techniques can be used to synthesize such fixes. Prior work has explored the use of symbolic and neural techniques for APR in the education domain. Both types of approaches require either substantial engineering efforts or l...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [PyTy: Repairing Static Type Errors in Python](../venues/ICSE2024/paper_12.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Gradual typing enables developers to annotate types of their own choosing, offering a flexible middle ground between no type annotations and a fully statically typed language. As more and more code bases get type-annotated, static type checkers detect an increasingly large number of type errors. Unfortunately, fixing these errors requires manual effort, hampering the adoption of gradual typing in practice. This paper presents PyTy, an automated program repair approach targeted at statically dete...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [type inference](type_inference.md)


- [Repairagent: An autonomous, llm-based agent for program repair](../venues/arXiv2024/paper_9.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Automated program repair has emerged as a powerful technique to mitigate the impact of software bugs on system reliability and user experience. This paper introduces RepairAgent, the first work to address the program repair challenge through an autonomous agent based on a large language model (LLM). Unlike existing deep learning-based approaches, which prompt a model with a fixed prompt or in a fixed feedback loop, our work treats the LLM as an agent capable of autonomously planning and executin...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [agent design](agent_design.md), [planning](planning.md)


- [Self-Edit: Fault-Aware Code Editor for Code Generation](../venues/ACL2023/paper_1.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Large language models (LLMs) have demonstrated an impressive ability to generate codes on competitive programming tasks. However, with limited sample numbers, LLMs still suffer from poor accuracy. Inspired by the process of human programming, we propose a generate-and-edit approach named Self-Edit that utilizes execution results of the generated code from LLMs to improve the code quality on the competitive programming task. We execute the generated code on the example test case provided in the q...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [benchmark](benchmark.md)


- [Swe-bench: Can language models resolve real-world github issues?](../venues/ICLR2024/paper_1.md), ([ICLR2024](../venues/ICLR2024/README.md))

  - **Abstract**: Language models have outpaced our ability to evaluate them effectively, but for their future development it is essential to study the frontier of their capabilities. We find real-world software engineering to be a rich, sustainable, and challenging testbed for evaluating the next generation of language models. To this end, we introduce SWE-bench, an evaluation framework consisting of 2,294 software engineering problems drawn from real GitHub issues and corresponding pull requests across 12 popul...
  - **Labels**: [benchmark](benchmark.md), [code generation](code_generation.md), [program repair](program_repair.md)


- [The Best of Both Worlds: Combining Learned Embeddings with Engineered Features for Accurate Prediction of Correct Patches](../venues/TOSEM2023/paper_2.md), ([TOSEM2023](../venues/TOSEM2023/README.md))

  - **Abstract**: A large body of the literature on automated program repair develops approaches where patches are automatically generated to be validated against an oracle (e.g., a test suite). Because such an oracle can be imperfect, the generated patches, although validated by the oracle, may actually be incorrect. While the state-of-the-art explores research directions that require dynamic information or rely on manually-crafted heuristics, we study the benefit of learning code representations in order to lea...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [The Plastic Surgery Hypothesis in the Era of Large Language Models](../venues/ASE2023/paper_9.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Automated Program Repair (APR) aspires to automatically generate patches for an input buggy program. Traditional APR tools typically focus on specific bug types and fixes through the use of templates, heuristics, and formal specifications. However, these techniques are limited in terms of the bug types and patch variety they can produce. As such, researchers have designed various learning-based APR tools with recent work focused on directly using Large Language Models (LLMs) for APR. While LLM-b...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [ThinkRepair: Self-Directed Automated Program Repair](../venues/ISSTA2024/paper_15.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Though many approaches have been proposed for Automated Program Repair (APR) and indeed achieved remarkable performance, they still have limitations in fixing bugs that require analyzing and reasoning about the logic of the buggy program. Recently, large language models (LLMs) instructed by prompt engineering have attracted much attention for their powerful ability to address many kinds of tasks including bug-fixing. However, the quality of the prompt will highly affect the ability of LLMs and m...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [Towards Efficient Fine-Tuning of Language Models With Organizational Data for Automated Software Review](../venues/TSE2024/paper_1.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Large language models like BERT and GPT possess significant capabilities and potential impacts across various applications. Software engineers often use these models for code-related tasks, including generating, debugging, and summarizing code. Nevertheless, large language models still have several flaws, including model hallucination. (e.g., generating erroneous code and producing outdated and inaccurate programs) and the substantial computational resources and energy required for training and ...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Towards Low-Resource Automatic Program Repair with Meta-Learning and Pretrained Language Models](../venues/EMNLP2023/paper_15.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Automatic program repair (APR) has gained increasing attention as an essential technique in software development to reduce manual debugging efforts and boost developers’ productivity. Recent advances in deep learning (DL) based models have demonstrated promising results by learning from large-scale bug-fix examples in a data-driven manner. However, in practical scenarios, software bugs have an imbalanced distribution, and the fixing knowledge learned by APR models often only capture the patterns...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Vision Transformer Inspired Automated Vulnerability Repair](../venues/TOSEM2024/paper_9.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Recently, automated vulnerability repair approaches have been widely adopted to combat increasing software security issues. In particular, transformer-based encoder-decoder models achieve competitive results. Whereas vulnerable programs may only consist of a few vulnerable code areas that need repair, existing AVR approaches lack a mechanism guiding their model to pay more attention to vulnerable code areas during repair generation. In this article, we propose a novel vulnerability repair framew...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md)


- [iSMELL: Assembling LLMs with Expert Toolsets for Code Smell Detection and Refactoring](../venues/ASE2024/paper_22.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Detecting and refactoring code smells is challenging, laborious, and sustaining. Although large language models have demonstrated potential in identifying various types of code smells, they also have limitations such as input-output token restrictions, difficulty in accessing repository-level knowledge, and performing dynamic source code analysis. Existing learning-based methods or commercial expert toolsets have advantages in handling complex smells. They can analyze project structures and cont...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [bug detection](bug_detection.md)
