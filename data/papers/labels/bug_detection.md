# Bug Detection

- [A Comprehensive Study of the Capabilities of Large Language Models for Vulnerability Detection](../venues/arXiv2024/paper_12.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated great potential for code generation and other software engineering tasks. Vulnerability detection is of crucial importance to maintaining the security, integrity, and trustworthiness of software systems. Precise vulnerability detection requires reasoning about the code, making it a good case study for exploring the limits of LLMs' reasoning capabilities. Although recent work has applied LLMs to vulnerability detection using generic prompting techniq...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [Assisting Static Analysis with Large Language Models: A ChatGPT Experiment](../venues/FSE2023/paper_6.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Recent advances of Large Language Models (LLMs), e.g., ChatGPT, exhibited strong capabilities of comprehending and responding to questions across a variety of domains. Surprisingly, ChatGPT even possesses a strong understanding of program code. In this paper, we investigate where and how LLMs can assist static analysis by asking appropriate questions. In particular, we target a specific bug-finding tool, which produces many false positives from the static analysis. In our evaluation, we find tha...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Beware of the unexpected: Bimodal taint analysis](../venues/ISSTA2023/paper_4.md), ([ISSTA2023](../venues/ISSTA2023/README.md))

  - **Abstract**: Static analysis is a powerful tool for detecting security vulnerabilities and other programming problems. Global taint tracking, in particular, can spot vulnerabilities arising from complicated data flow across multiple functions. However, precisely identifying which flows are problematic is challenging, and sometimes depends on factors beyond the reach of pure program analysis, such as conventions and informal knowledge. For example, learning that a parameter name of an API function locale ends...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [CORE: Resolving Code Quality Issues using LLMs](../venues/FSE2024/paper_22.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: As software projects progress, quality of code assumes paramount importance as it affects reliability, maintainability and security of software. For this reason, static analysis tools are used in developer workflows to flag code quality issues. However, developers need to spend extra efforts to revise their code to improve code quality based on the tool findings. In this work, we investigate the use of (instruction-following) large language models (LLMs) to assist developers in revising code to ...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [CoderUJB: An Executable and Unified Java Benchmark for Practical Programming Scenarios](../venues/ISSTA2024/paper_3.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: In the evolving landscape of large language models (LLMs) tailored for software engineering, the need for benchmarks that accurately reflect real-world development scenarios is paramount. Current benchmarks are either too simplistic or fail to capture the multi-tasking nature of software development. To address this, we introduce CoderUJB, a new benchmark designed to evaluate LLMs across diverse Java programming tasks that are executable and reflective of actual development scenarios, acknowledg...
  - **Labels**: [code generation](code_generation.md), [program testing](program_testing.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)


- [Collaboration to Repository-Level Vulnerability Detection](../venues/ISSTA2024/paper_26.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Large Language Model (LLM)-based methods have proven to be effective for many software engineering domains, with a potential for substantial productivity effective for software vulnerability detection.    However, due to the limitation of the length of input contexts of LLM, the existing LLM-based methods mainly focus on detecting function-level and leveraging the in-file context information for vulnerability detection (i.e., intra-procedural vulnerabilities), ignoring the more complex inter-pro...
  - **Labels**: [code generation](code_generation.md), [bug detection](bug_detection.md)


- [Combining Fine-Tuning and LLM-based Agents for Intuitive Smart Contract Auditing with Justifications](../venues/ICSE2025/paper_3.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Smart contracts are decentralized applications built atop blockchains like Ethereum. Recent research has shown that large language models (LLMs) have potential in auditing smart contracts, but the state-of-the-art indicates that even GPT-4 can achieve only 30% precision (when both decision and justification are correct). This is likely because off-the-shelf LLMs were primarily pre-trained on a general text/code corpus and not fine-tuned on the specific domain of Solidity smart contract auditing....
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [agent design](agent_design.md)


- [Continuous learning for android malware detection](../venues/USENIXSec2023/paper_2.md), ([USENIXSec2023](../venues/USENIXSec2023/README.md))

  - **Abstract**: Machine learning methods can detect Android malware with very high accuracy. However, these classifiers have an Achilles heel, concept drift: they rapidly become out of date and ineffective, due to the evolution of malware apps and benign apps. Our research finds that, after training an Android malware classifier on one year's worth of data, the F1 score quickly dropped from 0.99 to 0.76 after 6 months of deployment on new test samples....
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection](../venues/ICSE2024/paper_2.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Deep learning-based vulnerability detection has shown great performance and, in some studies, outperformed static analysis tools. However, the highest-performing approaches use token-based transformer models, which are not the most efficient to capture code semantics required for vulnerability detection. Classical program analysis techniques such as dataflow analysis can detect many types of bugs based on their root causes. In this paper, we propose to combine such causal-based vulnerability det...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [DiverseVul: {A} New Vulnerable Source Code Dataset for Deep Learning Based Vulnerability Detection](../venues/RAID2023/paper_1.md), ([RAID2023](../venues/RAID2023/README.md))

  - **Abstract**: We propose and release a new vulnerable source code dataset. We curate the dataset by crawling security issue websites, extracting vulnerability-fixing commits and source codes from the corresponding projects. Our new dataset contains 18,945 vulnerable functions spanning 150 CWEs and 330,492 non-vulnerable functions extracted from 7,514 commits. Our dataset covers 295 more projects than all previous datasets combined.Combining our new dataset with previous datasets, we present an analysis of the...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)


- [Do Language Models Learn Semantics of Code? {A} Case Study in Vulnerability Detection](../venues/arXiv2023/paper_7.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Recently, pretrained language models have shown state-of-the-art performance on the vulnerability detection task. These models are pretrained on a large corpus of source code, then fine-tuned on a smaller supervised vulnerability dataset. Due to the different training objectives and the performance of the models, it is interesting to consider whether the models have learned the semantics of code relevant to vulnerability detection, namely bug semantics, and if so, how the alignment to bug semant...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [Do you still need a manual smart contract audit?](../venues/arXiv2023/paper_10.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: We investigate the feasibility of employing large language models (LLMs) for conducting the security audit of smart contracts, a traditionally time-consuming and costly process. Our research focuses on the optimization of prompt engineering for enhanced security analysis, and we evaluate the performance and accuracy of LLMs using a benchmark dataset comprising 52 Decentralized Finance (DeFi) smart contracts that have previously been compromised.     Our findings reveal that, when applied to vuln...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Effective Vulnerable Function Identification based on CVE Description Empowered by Large Language Models](../venues/ASE2024/paper_6.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Open-source software (OSS) has profoundly transformed the software development paradigm by facilitating effortless code reuse. However, in recent years, there has been an alarming increase in disclosed vulnerabilities within OSS, posing significant security risks to downstream users. Therefore, analyzing existing vulnerabilities and precisely assessing their threats to downstream applications become pivotal. Plenty of efforts have been made recently towards this problem, such as vulnerability re...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Enhancing Static Analysis for Practical Bug Detection: An LLM-Integrated Approach](../venues/OOPSLA2024/paper_5.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: While static analysis is instrumental in uncovering software bugs, its precision in analyzing large and intricate codebases remains challenging. The emerging prowess of Large Language Models (LLMs) offers a promising avenue to address these complexities. In this paper, we present LLift, a pioneering framework that synergizes static analysis and LLMs, with a spotlight on identifying use-before-initialization (UBI) bugs within the Linux kernel. Drawing from our insights into variable usage convent...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Examining Zero-Shot Vulnerability Repair with Large Language Models](../venues/S&P2023/paper_1.md), ([S&P2023](../venues/S&P2023/README.md))

  - **Abstract**: Human developers can produce code with cybersecurity bugs. Can emerging ‘smart’ code completion tools help repair those bugs? In this work, we examine the use of large language models (LLMs) for code (such as OpenAI’s Codex and AI21’s Jurassic J-1) for zero-shot vulnerability repair. We investigate challenges in the design of prompts that coax LLMs into generating repaired versions of insecure code. This is difficult due to the numerous ways to phrase key information— both semantically and synta...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [Explaining Software Bugs Leveraging Code Structures in Neural Machine Translation](../venues/ICSE2023/paper_6.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Software bugs claim ≈ 50\% of development time and cost the global economy billions of dollars. Once a bug is reported, the assigned developer attempts to identify and understand the source code responsible for the bug and then corrects the code. Over the last five decades, there has been significant research on automatically finding or correcting software bugs. However, there has been little research on automatically explaining the bugs to the developers, which is essential but a highly challen...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [E{\&}V: Prompting Large Language Models to Perform Static Analysis by Pseudo-code Execution and Verification](../venues/Microsoft2023/paper_2.md), ([Microsoft2023](../venues/Microsoft2023/README.md))

  - **Abstract**: Static analysis, the process of examining code without executing it, is crucial for identifying software issues. Yet, static analysis is hampered by its complexity and the need for customization for different targets. Traditional static analysis tools require extensive human effort and are often limited to specific target programs and programming languages. Recent advancements in Large Language Models (LLMs), such as GPT-4 and Llama, offer new capabilities for software engineering tasks. However...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [GPTScan: Detecting Logic Vulnerabilities in Smart Contracts by Combining GPT with Program Analysis](../venues/ICSE2024/paper_17.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Smart contracts are prone to various vulnerabilities, leading to substantial financial losses over time. Current analysis tools mainly target vulnerabilities with fixed control- or data-flow patterns, such as re-entrancy and integer overflow. However, a recent study on Web3 security bugs revealed that about 80\% of these bugs cannot be audited by existing tools due to the lack of domain-specific property description and checking. Given recent advances in Large Language Models (LLMs), it is worth...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Gptscan: Detecting logic vulnerabilities in smart contracts by combining gpt with program analysis](../venues/ICSE2024/paper_22.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Smart contracts are prone to various vulnerabilities, leading to substantial financial losses over time. Current analysis tools mainly target vulnerabilities with fixed control- or data-flow patterns, such as re-entrancy and integer overflow. However, a recent study on Web3 security bugs revealed that about 80% of these bugs cannot be audited by existing tools due to the lack of domain-specific property description and checking. Given recent advances in Large Language Models (LLMs), it is worth ...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Harnessing the power of llm to support binary taint analysis](../venues/arXiv2023/paper_9.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: This paper proposes LATTE, the first static binary taint analysis that is powered by a large language model (LLM). LATTE is superior to the state of the art (e.g., Emtaint, Arbiter, Karonte) in three aspects. First, LATTE is fully automated while prior static binary taint analyzers need rely on human expertise to manually customize taint propagation rules and vulnerability inspection rules. Second, LATTE is significantly effective in vulnerability detection, demonstrated by our comprehensive eva...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [How Far Have We Gone in Vulnerability Detection Using Large Language Models](../venues/arXiv2023/paper_5.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: As software becomes increasingly complex and prone to vulnerabilities, automated vulnerability detection is critically important, yet challenging. Given the significant successes of large language models (LLMs) in various tasks, there is growing anticipation of their efficacy in vulnerability detection. However, a quantitative understanding of their potential in vulnerability detection is still missing. To bridge this gap, we introduce a comprehensive vulnerability benchmark VulBench. This bench...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)


- [Interleaving Static Analysis and LLM Prompting](../venues/SOAP2024/paper_1.md), ([SOAP2024](../venues/SOAP2024/README.md))

  - **Abstract**: This paper presents a new approach for using Large Language Models (LLMs) to improve static program analysis. Specifically, during program analysis, we interleave calls to the static analyzer and queries to the LLM: the prompt used to query the LLM is constructed using intermediate results from the static analysis, and the result from the LLM query is used for subsequent analysis of the program. We apply this novel approach to the problem of error-specification inference of functions in systems ...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Jtrans: Jump-aware transformer for binary code similarity detection](../venues/ISSTA2022/paper_1.md), ([ISSTA2022](../venues/ISSTA2022/README.md))

  - **Abstract**: Binary code similarity detection (BCSD) has important applications in various fields such as vulnerabilities detection, software component analysis, and reverse engineering. Recent studies have shown that deep neural networks (DNNs) can comprehend instructions or control-flow graphs (CFG) of binary code and support BCSD. In this study, we propose a novel Transformer-based approach, namely jTrans, to learn representations of binary code. It is the first solution that embeds control flow informati...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [LLM-Assisted Static Analysis for Detecting Security Vulnerabilities](../venues/arXiv2024/paper_18.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Software is prone to security vulnerabilities. Program analysis tools to detect them have limited effectiveness in practice due to their reliance on human labeled specifications. Large language models (or LLMs) have shown impressive code generation capabilities but they cannot do complex reasoning over code to detect such vulnerabilities especially since this task requires whole-repository analysis. We propose IRIS, a neuro-symbolic approach that systematically combines LLMs with static analysis...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [LLM-based Resource-Oriented Intention Inference for Static Resource Detection](../venues/ICSE2025/paper_2.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Resource leaks, caused by resources not being released after acquisition, often lead to performance issues and system crashes. Existing static detection techniques rely on mechanical matching of predefined resource acquisition/release APIs and null-checking conditions to find unreleased resources, suffering from both (1) false negatives caused by the incompleteness of predefined resource acquisition/release APIs and (2) false positives caused by the unsoundness of resource reachability validatio...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [LLM4Vuln: {A} Unified Evaluation Framework for Decoupling and Enhancing LLMs' Vulnerability Reasoning](../venues/arXiv2024/paper_15.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Large language models (LLMs) have demonstrated significant potential in various tasks, including vulnerability detection. However, current efforts in this area are preliminary, lacking clarity on whether LLMs' vulnerability reasoning capabilities stem from the models themselves or external aids such as knowledge retrieval and tooling support.This paper aims to isolate LLMs' vulnerability reasoning from other capabilities, such as vulnerability knowledge adoption, context information retrieval, a...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)


- [LLMDFA: Analyzing Dataflow in Code with Large Language Model](../venues/NeurIPS2024/paper_6.md), ([NeurIPS2024](../venues/NeurIPS2024/README.md))

  - **Abstract**: Dataflow analysis is a fundamental code analysis technique that identifies dependencies between program values. Traditional approaches typically necessitate successful compilation and expert customization, hindering their applicability and usability for analyzing uncompilable programs with evolving analysis needs in realworld scenarios. This paper presents LLMDFA, an LLM-powered compilation-free and customizable dataflow analysis framework. To address hallucinations for reliable results, we deco...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [LLMs Cannot Reliably Identify and Reason About Security Vulnerabilities (Yet?): A Comprehensive Evaluation, Framework, and Benchmarks](../venues/S&P2024/paper_1.md), ([S&P2024](../venues/S&P2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have been suggested for use in automated vulnerability repair, but benchmarks showing they can consistently identify security-related bugs are lacking. We thus develop SecLLMHolmes, a fully automated evaluation framework that performs the most detailed investigation to date on whether LLMs can reliably identify and reason about security-related bugs. We construct a set of 228 code scenarios and analyze eight of the most capable LLMs across eight different investigati...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code generation](code_generation.md), [program repair](program_repair.md), [empirical study](empirical_study.md)


- [Large Language Models for Code Analysis: Do LLMs Really Do Their Job?](../venues/USENIXSec2024/paper_1.md), ([USENIXSec2024](../venues/USENIXSec2024/README.md))

  - **Abstract**: Large language models (LLMs) have demonstrated significant potential in the realm of natural language understanding and programming code processing tasks. Their capacity to comprehend and generate human-like code has spurred research into harnessing LLMs for code analysis purposes. However, the existing body of literature falls short in delivering a systematic evaluation and assessment of LLMs' effectiveness in code analysis, particularly in the context of obfuscated code.This paper seeks to bri...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [Large language model-powered smart contract vulnerability detection: New perspectives](../venues/arXiv2023/paper_11.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: This paper provides a systematic analysis of the opportunities, challenges, and potential solutions of harnessing Large Language Models (LLMs) such as GPT-4 to dig out vulnerabilities within smart contracts based on our ongoing research. For the task of smart contract vulnerability detection, achieving practical usability hinges on identifying as many true vulnerabilities as possible while minimizing the number of false positives. Nonetheless, our empirical study reveals contradictory yet intere...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Learning to Detect and Localize Multilingual Bugs](../venues/FSE2024/paper_31.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Increasing studies have shown bugs in multi-language software as a critical loophole in modern software quality assurance, especially those induced by language interactions (i.e., multilingual bugs). Yet existing tool support for bug detection/localization remains largely limited to single-language software, despite the long-standing prevalence of multi-language systems in various real-world software domains. Extant static/dynamic analysis and deep learning (DL) based approaches all face major c...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Leveraging Large Language Model to Assist Detecting Rust Code Comment Inconsistency](../venues/ASE2024/paper_5.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Rust is renowned for its robust memory safety capabilities, yet its distinctive memory management model poses substantial challenges in both writing and understanding programs. Within Rust source code, comments are employed to clearly delineate conditions that might cause panic behavior, thereby warning developers about potential hazards associated with specific operations. Therefore, comments are particularly crucial for documenting Rust's program logic and design. Nevertheless, as modern softw...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Leveraging Semantic Relations in Code and Data to Enhance Taint Analysis of Embedded Systems](../venues/USENIXSec2024/paper_2.md), ([USENIXSec2024](../venues/USENIXSec2024/README.md))

  - **Abstract**: IoT devices have significantly impacted our daily lives, and detecting vulnerabilities in embedded systems early on is critical for ensuring their security. Among the existing vulnerability detection techniques for embedded systems, static taint analysis has been proven effective in detecting severe vulnerabilities, such as command injection vulnerabilities, which can cause remote code execution. Nevertheless, static taint analysis is faced with the problem of identifying sources comprehensively...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Pre-training by Predicting Program Dependencies for Vulnerability Analysis Tasks](../venues/ICSE2024/paper_30.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Vulnerability analysis is crucial for software security. Inspired by the success of pre-trained models on software engineering tasks, this work focuses on using pre-training techniques to enhance the understanding of vulnerable code and boost vulnerability analysis. The code understanding ability of a pre-trained model is highly related to its pre-training objectives. The semantic structure, e.g., control and data dependencies, of code is important for vulnerability analysis. However, existing p...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [RealVul: Can We Detect Vulnerabilities in Web Applications with LLM?](../venues/EMNLP2024/paper_25.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: The latest advancements in large language models (LLMs) have sparked interest in their potential for software vulnerability detection. However, there is currently a lack of research specifically focused on vulnerabilities in the PHP language, and challenges in data sampling and processing persist, hindering the model’s ability to effectively capture the characteristics of specific vulnerabilities. In this paper, we present RealVul, the first LLM-based framework designed for PHP vulnerability det...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Risky Dynamic Typing-related Practices in Python: An Empirical Study](../venues/TOSEM2024/paper_6.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Python’s dynamic typing nature provides developers with powerful programming abstractions. However, many type-related bugs are accumulated in code bases of Python due to the misuse of dynamic typing. The goal of this article is to aid in the understanding of developers’ high-risk practices toward dynamic typing and the early detection of type-related bugs. We first formulate the rules of six types of risky dynamic typing-related practices (type smells for short) in Python. We then develop a rule...
  - **Labels**: [static analysis](static_analysis.md), [type inference](type_inference.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [SCALE: Constructing Structured Natural Language Comment Trees for Software Vulnerability Detection](../venues/ISSTA2024/paper_4.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Recently, there has been a growing interest in automatic software vulnerability detection.     Pre-trained model-based approaches have demonstrated superior performance than other Deep Learning (DL)-based approaches in detecting vulnerabilities.     However, the existing pre-trained model-based approaches generally employ code sequences as input during prediction, and may ignore vulnerability-related structural information, as reflected in the following two aspects.     First, they tend to fail ...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Sanitizing Large Language Models in Bug Detection with Data-Flow](../venues/EMNLP2024/paper_5.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large language models (LLMs) show potential in code reasoning tasks, facilitating the customization of detecting bugs in software development. However, the hallucination effect can significantly compromise the reliability of bug reports. This work formulates a new schema of bug detection and presents a novel sanitization technique that detects false positives for hallucination mitigation. Our key idea is to enforce LLMs to emit data-flow paths in few-shot chain-of-thought prompting and validate ...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [fundamental analysis](fundamental_analysis.md)


- [Semantic Sleuth: Identifying Ponzi Contracts via Large Language Models](../venues/ASE2024/paper_11.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Smart contracts, self-executing agreements directly encoded in code, are fundamental to blockchain technology, especially in decentralized finance (DeFi) and Web3. However, the rise of Ponzi schemes in smart contracts poses significant risks, leading to substantial financial losses and eroding trust in blockchain systems. Existing detection methods, such as PonziGuard, depend on large amounts of labeled data and struggle to identify unseen Ponzi schemes, limiting their reliability and generaliza...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [SkipAnalyzer: An Embodied Agent for Code Analysis with Large Language Models](../venues/arXiv2023/paper_8.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: We introduce SkipAnalyzer, a large language model (LLM)-powered tool for static code analysis. SkipAnalyzer has three components: 1) an LLM-based static bug detector that scans source code and reports specific types of bugs, 2) an LLM-based false-positive filter that can identify false-positive bugs in the results of static bug detectors (e.g., the result of step 1) to improve detection accuracy, and 3) an LLM-based patch generator that can generate patches for the detected bugs above. As a proo...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [agent design](agent_design.md)


- [Smartinv: Multimodal learning for smart contract invariant inference](../venues/S&P2024/paper_4.md), ([S&P2024](../venues/S&P2024/README.md))

  - **Abstract**: Smart contracts are software programs that enable diverse business activities on the blockchain. Recent research has identified new classes of "machine un-auditable" bugs that arise from source code not meeting underlying transaction contexts. Existing detection methods require human understanding of underlying transaction logic and manual reasoning across different sources of context (i.e., modalities), such as code and natural language specifying the expected transaction behavior.To automate t...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Source Code Vulnerability Detection: Combining Code Language Models and Code Property Graphs](../venues/arXiv2024/paper_13.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Currently, deep learning successfully applies to code vulnerability detection by learning from code sequences or property graphs. However, sequence-based methods often overlook essential code attributes such as syntax, control flow, and data dependencies, whereas graph-based approaches might underestimate the semantics of code and face challenges in capturing long-distance contextual information.To address this gap, we propose Vul-LMGNN, a unified model that combines pre-trained code language mo...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Stanceformer: Target-Aware Transformer for Stance Detection](../venues/EMNLP2024/paper_6.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: The task of Stance Detection involves discerning the stance expressed in a text towards a specific subject or target. Prior works have relied on existing transformer models that lack the capability to prioritize targets effectively. Consequently, these models yield similar performance regardless of whether we utilize or disregard target information, undermining the task’s significance. To address this challenge, we introduce Stanceformer, a target-aware transformer model that incorporates enhanc...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [The EarlyBIRD Catches the Bug: On Exploiting Early Layers of Encoder Models for More Efficient Code Classification](../venues/FSE2023/paper_12.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: The use of modern Natural Language Processing (NLP) techniques has shown to be beneficial for software engineering tasks, such as vulnerability detection and type inference. However, training deep NLP models requires significant computational resources. This paper explores techniques that aim at achieving the best usage of resources and available information in these models.  We propose a generic approach, EarlyBIRD, to build composite representations of code from the early layers of a pre-train...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)


- [The Emergence of Large Language Models in Static Analysis: A First Look through Micro-Benchmarks](../venues/Forge2024/paper_1.md), ([Forge2024](../venues/Forge2024/README.md))

  - **Abstract**: Binary code similarity detection(BCSD), as a fundamental technique in software security, has various applications, including malware family detection, known vulnerability detection and code plagiarism detection. Recent deep learning-based BCSD approaches have demonstrated promising performance. However, they face two significant challenges that limit detection performance. First, most approaches that use sequence networks (like RNN and Transformer) utilize coarse-grained tokenization methods, wh...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [Top Score on the Wrong Exam: On Benchmarking in Machine Learning for Vulnerability Detection](../venues/arXiv2024/paper_16.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: According to our survey of the machine learning for vulnerability detection (ML4VD) literature published in the top Software Engineering conferences, every paper in the past 5 years defines ML4VD as a binary classification problem: Given a function, does it contain a security flaw?In this paper, we ask whether this decision can really be made without further context and study both vulnerable and non-vulnerable functions in the most popular ML4VD datasets. A function is vulnerable if it was invol...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [Twin Graph-Based Anomaly Detection via Attentive Multi-Modal Learning for Microservice System](../venues/ASE2023/paper_16.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Microservice architecture has sprung up over recent years for managing enterprise applications, due to its ability to independently deploy and scale services. Despite its benefits, ensuring the reliability and safety of a microservice system remains highly challenging. Existing anomaly detection algorithms based on a single data modality (i.e., metrics, logs, or traces) fail to fully account for the complex correlations and interactions between different modalities, leading to false negatives an...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Understanding the Effectiveness of Large Language Models in Detecting Security Vulnerabilities](../venues/arXiv2023/paper_6.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: While automated vulnerability detection techniques have made promising progress in detecting security vulnerabilities, their scalability and applicability remain challenging. The remarkable performance of Large Language Models (LLMs), such as GPT-4 and CodeLlama, on code-related tasks has prompted recent works to explore if LLMs can be used to detect vulnerabilities. In this paper, we perform a more comprehensive study by concurrently examining a higher number of datasets, languages and LLMs, an...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)


- [VALAR: Streamlining Alarm Ranking in Static Analysis with Value-Flow Assisted Active Learning](../venues/ASE2023/paper_15.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Static analyzers play a critical role in program defects and security vulnerabilities detection. Despite their importance, the widespread adoption of static analysis techniques in industrial development faces numerous obstacles, among which the high rate of false alarms constitutes a significant one. To address this issue, we propose a novel approach called Valar, which performs alarm ranking for advanced value-flow analysis using the active learning technique. Active learning algorithms minimiz...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [VGX: Large-Scale Sample Generation for Boosting Learning-Based Software Vulnerability Analyses](../venues/ICSE2024/paper_29.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Accompanying the successes of learning-based defensive software vulnerability analyses is the lack of large and quality sets of labeled vulnerable program samples, which impedes further advancement of those defenses. Existing automated sample generation approaches have shown potentials yet still fall short of practical expectations due to the high noise in the generated samples. This paper proposes VGX, a new technique aimed for large-scale generation of high-quality vulnerability datasets. Give...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [VULGEN: Realistic Vulnerability Generation Via Pattern Mining and Deep Learning](../venues/ICSE2023/paper_11.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Building new, powerful data-driven defenses against prevalent software vulnerabilities needs sizable, quality vulnerability datasets, so does large-scale benchmarking of existing defense solutions. Automatic data generation would promisingly meet the need, yet there is little work aimed to generate much-needed quality vulnerable samples. Meanwhile, existing similar and adaptable techniques suffer critical limitations for that purpose. In this paper, we present VULGEN, the first injection-based v...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)


- [VulEval: Towards Repository-Level Evaluation of Software Vulnerability Detection](../venues/arXiv2024/paper_11.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Deep Learning (DL)-based methods have proven to be effective for software vulnerability detection, with a potential for substantial productivity enhancements for detecting vulnerabilities. Current methods mainly focus on detecting single functions (i.e., intra-procedural vulnerabilities), ignoring the more complex inter-procedural vulnerability detection scenarios in practice. For example, developers routinely engage with program analysis to detect vulnerabilities that span multiple functions wi...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)


- [VulExplainer: A Transformer-Based Hierarchical Distillation for Explaining Vulnerability Types](../venues/TSE2023/paper_1.md), ([TSE2023](../venues/TSE2023/README.md))

  - **Abstract**: Deep learning-based vulnerability prediction approaches are proposed to help under-resourced security practitioners to detect vulnerable functions. However, security practitioners still do not know what type of vulnerabilities correspond to a given prediction (aka CWE-ID). Thus, a novel approach to explain the type of vulnerabilities for a given prediction is imperative. In this paper, we propose &lt;italic&gt;VulExplainer&lt;/italic&gt;, an approach to explain the type of vulnerabilities. We re...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Vulnerability Detection with Code Language Models: How Far Are We?](../venues/ICSE2025/paper_1.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: In the context of the rising interest in code language models (code LMs) and vulnerability detection, we study the effectiveness of code LMs for detecting vulnerabilities. Our analysis reveals significant shortcomings in existing vulnerability datasets, including poor data quality, low label accuracy, and high duplication rates, leading to unreliable model performance in realistic vulnerability detection scenarios. Additionally, the evaluation methods used with these datasets are not representat...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [benchmark](benchmark.md)


- [Where is it? Tracing the Vulnerability-relevant Files from Vulnerability Reports](../venues/ICSE2024/paper_18.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: With the widely usage of open-source software, supply-chain-based vulnerability attacks, including SolarWind and Log4Shell, have posed significant risks to software security. Currently, people rely on vulnerability advisory databases or commercial software bill of materials (SBOM) to defend against potential risks. Unfortunately, these datasets do not provide finer-grained file-level vulnerability information, compromising their effectiveness. Previous works have not adequately addressed this is...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Who Judges the Judge: An Empirical Study on Online Judge Tests](../venues/ISSTA2023/paper_1.md), ([ISSTA2023](../venues/ISSTA2023/README.md))

  - **Abstract**: Online Judge platforms play a pivotal role in education, competitive programming, recruitment, career training, and large language model training. They rely on predefined test suites to judge the correctness of submitted solutions. It is therefore important that the solution judgement is reliable and free from potentially misleading false positives (i.e., incorrect solutions that are judged as correct). In this paper, we conduct an empirical study of 939 coding problems with 541,552 solutions, a...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md)


- [Your Instructions Are Not Always Helpful: Assessing the Efficacy of Instruction Fine-tuning for Software Vulnerability Detection](../venues/arXiv2024/paper_14.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Software, while beneficial, poses potential cybersecurity risks due to inherent vulnerabilities. Detecting these vulnerabilities is crucial, and deep learning has shown promise as an effective tool for this task due to its ability to perform well without extensive feature engineering. However, a challenge in deploying deep learning for vulnerability detection is the limited availability of training data. Recent research highlights the deep learning efficacy in diverse tasks. This success is attr...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [iSMELL: Assembling LLMs with Expert Toolsets for Code Smell Detection and Refactoring](../venues/ASE2024/paper_22.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Detecting and refactoring code smells is challenging, laborious, and sustaining. Although large language models have demonstrated potential in identifying various types of code smells, they also have limitations such as input-output token restrictions, difficulty in accessing repository-level knowledge, and performing dynamic source code analysis. Existing learning-based methods or commercial expert toolsets have advantages in handling complex smells. They can analyze project structures and cont...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [bug detection](bug_detection.md)
