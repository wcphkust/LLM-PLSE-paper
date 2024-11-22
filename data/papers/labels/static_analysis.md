# Static Analysis

## Fundamental Analysis

- [A Learning-Based Approach to Static Program Slicing](../venues/OOPSLA2024/paper_7.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Traditional program slicing techniques are crucial for early bug detection and manual/automated debugging of online code snippets. Nevertheless, their inability to handle incomplete code hinders their real-world applicability in such scenarios. To overcome these challenges, we present NS-Slicer, a n...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [fundamental analysis](../../labels/fundamental_analysis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


- [Evaluating the effectiveness of deep learning models for foundational program analysis tasks](../venues/OOPSLA2024/paper_8.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: While deep neural networks provide state-of-the-art solutions to a wide range of programming language tasks, their effectiveness in dealing with foundational program analysis tasks remains under explored. In this paper, we present an empirical study that evaluates four prominent models of code (i.e....
  - **Labels**: [static analysis](../../labels/static_analysis.md), [fundamental analysis](../../labels/fundamental_analysis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


- [Function Argument Nullability Using an LLM](../venues/Galois2024/paper_1.md), ([Galois2024](../venues/Galois2024/README.md))

  - **Abstract**: We think that Rust is a great language, and maybe you agree! Unfortunately, even if you do, there’s a good chance whatever application you’re working on is written in some older language such as C. To help with this, Galois has been developing c2rust, an automated transpiler (source-to-source transl...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [fundamental analysis](../../labels/fundamental_analysis.md)


- [LLMs: Understanding Code Syntax and Semantics for Code Analysis](../venues/arXiv2023/paper_1.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Large language models~(LLMs) demonstrate significant potential to revolutionize software engineering (SE) by exhibiting outstanding performance in SE tasks such as code and document generation. However, the high reliability and risk control requirements in software engineering raise concerns about t...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [fundamental analysis](../../labels/fundamental_analysis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md), [empirical study](../../labels/empirical_study.md)


- [NormTab: Improving Symbolic Reasoning in LLMs Through Tabular Data Normalization](../venues/EMNLP2024/paper_4.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: In recent years, Large Language Models (LLMs) have demonstrated remarkable capabilities in parsing textual data and generating code. However, their performance in tasks involving tabular data, especially those requiring symbolic reasoning, faces challenges due to the structural variance and inconsis...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [fundamental analysis](../../labels/fundamental_analysis.md)


- [Program Slicing in the Era of Large Language Models](../venues/arXiv2024/paper_21.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Program slicing is a critical technique in software engineering, enabling developers to isolate relevant portions of code for tasks such as bug detection, code comprehension, and debugging. In this study, we investigate the application of large language models (LLMs) to both static and dynamic progr...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [fundamental analysis](../../labels/fundamental_analysis.md)


- [Programl: A graph-based program representation for data flow analysis and compiler optimizations](../venues/ICML2021/paper_2.md), ([ICML2021](../venues/ICML2021/README.md))

  - **Abstract**: Machine learning (ML) is increasingly seen as a viable approach for building compiler optimization heuristics, but many ML methods cannot replicate even the simplest of the data flow analyses that are critical to making good optimization decisions. We posit that if ML cannot do that, then it is insu...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [fundamental analysis](../../labels/fundamental_analysis.md), [compiler optimization](../../labels/compiler_optimization.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [IR code model](../../labels/IR_code_model.md)


- [Revealing the Unseen: AI Chain on LLMs for Predicting Implicit Dataflows to Generate Dataflow Graphs in Dynamically Typed Code](../venues/TOSEM2024/paper_3.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Dataflow graphs (DFGs) capture definitions (defs) and uses across program blocks, which is a fundamental program representation for program analysis, testing and maintenance. However, dynamically typed programming languages like Python present implicit dataflow issues that make it challenging to det...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [fundamental analysis](../../labels/fundamental_analysis.md)


- [Sanitizing Large Language Models in Bug Detection with Data-Flow](../venues/EMNLP2024/paper_5.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large language models (LLMs) show potential in code reasoning tasks, facilitating the customization of detecting bugs in software development. However, the hallucination effect can significantly compromise the reliability of bug reports. This work formulates a new schema of bug detection and present...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [fundamental analysis](../../labels/fundamental_analysis.md)


- [Semantic-Enhanced Indirect Call Analysis with Large Language Models](../venues/ASE2024/paper_8.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: In contemporary software development, the widespread use of indirect calls to achieve dynamic features poses challenges in constructing precise control flow graphs (CFGs), which further impacts the performance of downstream static analysis tasks. To tackle this issue, various types of indirect call ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [fundamental analysis](../../labels/fundamental_analysis.md)


- [Unveiling Code Pre-Trained Models: Investigating Syntax and Semantics Capacities](../venues/TOSEM2024/paper_1.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Code models have made significant advancements in code intelligence by encoding knowledge about programming languages. While previous studies have explored the capabilities of these models in learning code syntax, there has been limited investigation on their ability to understand code semantics. Ad...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [fundamental analysis](../../labels/fundamental_analysis.md), [empirical study](../../labels/empirical_study.md)


- [Which Syntactic Capabilities Are Statistically Learned by Masked Language Models for Code?](../venues/ICSE2024/paper_20.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: This paper discusses the limitations of evaluating Masked Language Models (MLMs) in code completion tasks. We highlight that relying on accuracy-based measurements may lead to an overestimation of models' capabilities by neglecting the syntax rules of programming languages. To address these issues, ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [fundamental analysis](../../labels/fundamental_analysis.md), [empirical study](../../labels/empirical_study.md)


## Specification Inference

- [Can Large Language Models Transform Natural Language Intent into Formal Method Postconditions?](../venues/FSE2024/paper_9.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Informal natural language that describes code functionality, such as code comments or function documentation, may contain substantial information about a program’s intent. However, there is typically no guarantee that a program’s implementation and natural language documentation are aligned. In the ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md), [empirical study](../../labels/empirical_study.md)


- [DAInfer: Inferring API Aliasing Specifications from Library Documentation via Neurosymbolic Optimization](../venues/FSE2024/paper_28.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Modern software systems heavily rely on various libraries, necessitating understanding API semantics in static analysis. However, summarizing API semantics remains challenging due to complex implementations or the unavailability of library code. This paper presents DAInfer, a novel approach for infe...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md)


- [Enchanting program specification synthesis by large language models using static analysis and program verification](../venues/CAV2024/paper_1.md), ([CAV2024](../venues/CAV2024/README.md))

  - **Abstract**: Formal verification provides a rigorous and systematic approach to ensure the correctness and reliability of software systems. Yet, constructing specifications for the full proof relies on domain expertise and non-trivial manpower. In view of such needs, an automated approach for specification synth...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md), [specification inference](../../labels/specification_inference.md)


- [Generating API Parameter Security Rules with LLM for API Misuse Detection](../venues/arXiv2024/paper_17.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: In this paper, we present a new framework, named GPTAid, for automatic APSRs generation by analyzing API source code with LLM and detecting API misuse caused by incorrect parameter use. To validate the correctness of the LLM-generated APSRs, we propose an execution feedback-checking approach based o...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md)


- [Impact of large language models on generating software specifications](../venues/arXiv2023/paper_11.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Software specifications are essential for ensuring the reliability of software systems. Existing specification extraction approaches, however, suffer from limited generalizability and require manual efforts. The recent emergence of Large Language Models (LLMs), which have been successfully applied t...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md)


- [SpecEval: Evaluating Code Comprehension in Large Language Models via Program Specifications](../venues/arXiv2024/paper_20.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Large Language models have achieved impressive performance in automated software engineering. Extensive efforts have been made to evaluate the abilities of code LLMs in various aspects, with an increasing number of benchmarks and evaluation frameworks proposed. Apart from the most sought-after capab...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md)


- [SpecGen: Automated Generation of Formal Program Specifications via Large Language Models](../venues/arXiv2024/paper_19.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: In software development, formal program specifications play a crucial role in various stages. However, manually crafting formal program specifications is rather difficult, making the job time-consuming and labor-intensive. Moreover, it is even more challenging to write specifications that correctly ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md)


## Bug Detection

- [A Comprehensive Study of the Capabilities of Large Language Models for Vulnerability Detection](../venues/arXiv2024/paper_12.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated great potential for code generation and other software engineering tasks. Vulnerability detection is of crucial importance to maintaining the security, integrity, and trustworthiness of software systems. Precise vulnerability detection requires reasonin...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)


- [Assisting Static Analysis with Large Language Models: A ChatGPT Experiment](../venues/FSE2023/paper_6.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Recent advances of Large Language Models (LLMs), e.g., ChatGPT, exhibited strong capabilities of comprehending and responding to questions across a variety of domains. Surprisingly, ChatGPT even possesses a strong understanding of program code. In this paper, we investigate where and how LLMs can as...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [Beware of the unexpected: Bimodal taint analysis](../venues/ISSTA2023/paper_4.md), ([ISSTA2023](../venues/ISSTA2023/README.md))

  - **Abstract**: Static analysis is a powerful tool for detecting security vulnerabilities and other programming problems. Global taint tracking, in particular, can spot vulnerabilities arising from complicated data flow across multiple functions. However, precisely identifying which flows are problematic is challen...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [CORE: Resolving Code Quality Issues using LLMs](../venues/FSE2024/paper_22.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: As software projects progress, quality of code assumes paramount importance as it affects reliability, maintainability and security of software. For this reason, static analysis tools are used in developer workflows to flag code quality issues. However, developers need to spend extra efforts to revi...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [CoderUJB: An Executable and Unified Java Benchmark for Practical Programming Scenarios](../venues/ISSTA2024/paper_3.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: In the evolving landscape of large language models (LLMs) tailored for software engineering, the need for benchmarks that accurately reflect real-world development scenarios is paramount. Current benchmarks are either too simplistic or fail to capture the multi-tasking nature of software development...
  - **Labels**: [code generation](../../labels/code_generation.md), [program testing](../../labels/program_testing.md), [bug detection](../../labels/bug_detection.md), [benchmark](../../labels/benchmark.md)


- [Collaboration to Repository-Level Vulnerability Detection](../venues/ISSTA2024/paper_26.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Large Language Model (LLM)-based methods have proven to be effective for many software engineering domains, with a potential for substantial productivity effective for software vulnerability detection.    However, due to the limitation of the length of input contexts of LLM, the existing LLM-based m...
  - **Labels**: [code generation](../../labels/code_generation.md), [bug detection](../../labels/bug_detection.md)


- [Combining Fine-Tuning and LLM-based Agents for Intuitive Smart Contract Auditing with Justifications](../venues/ICSE2025/paper_3.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Smart contracts are decentralized applications built atop blockchains like Ethereum. Recent research has shown that large language models (LLMs) have potential in auditing smart contracts, but the state-of-the-art indicates that even GPT-4 can achieve only 30% precision (when both decision and justi...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [agent design](../../labels/agent_design.md)


- [Continuous learning for android malware detection](../venues/USENIXSec2023/paper_2.md), ([USENIXSec2023](../venues/USENIXSec2023/README.md))

  - **Abstract**: Machine learning methods can detect Android malware with very high accuracy. However, these classifiers have an Achilles heel, concept drift: they rapidly become out of date and ineffective, due to the evolution of malware apps and benign apps. Our research finds that, after training an Android malw...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)


- [Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection](../venues/ICSE2024/paper_2.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Deep learning-based vulnerability detection has shown great performance and, in some studies, outperformed static analysis tools. However, the highest-performing approaches use token-based transformer models, which are not the most efficient to capture code semantics required for vulnerability detec...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


- [DiverseVul: {A} New Vulnerable Source Code Dataset for Deep Learning Based Vulnerability Detection](../venues/RAID2023/paper_1.md), ([RAID2023](../venues/RAID2023/README.md))

  - **Abstract**: We propose and release a new vulnerable source code dataset. We curate the dataset by crawling security issue websites, extracting vulnerability-fixing commits and source codes from the corresponding projects. Our new dataset contains 18,945 vulnerable functions spanning 150 CWEs and 330,492 non-vul...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [benchmark](../../labels/benchmark.md)


- [Do Language Models Learn Semantics of Code? {A} Case Study in Vulnerability Detection](../venues/arXiv2023/paper_5.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Recently, pretrained language models have shown state-of-the-art performance on the vulnerability detection task. These models are pretrained on a large corpus of source code, then fine-tuned on a smaller supervised vulnerability dataset. Due to the different training objectives and the performance ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)


- [Do you still need a manual smart contract audit?](../venues/arXiv2023/paper_8.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: We investigate the feasibility of employing large language models (LLMs) for conducting the security audit of smart contracts, a traditionally time-consuming and costly process. Our research focuses on the optimization of prompt engineering for enhanced security analysis, and we evaluate the perform...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [Effective Vulnerable Function Identification based on CVE Description Empowered by Large Language Models](../venues/ASE2024/paper_6.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Open-source software (OSS) has profoundly transformed the software development paradigm by facilitating effortless code reuse. However, in recent years, there has been an alarming increase in disclosed vulnerabilities within OSS, posing significant security risks to downstream users. Therefore, anal...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [Enhancing Static Analysis for Practical Bug Detection: An LLM-Integrated Approach](../venues/OOPSLA2024/paper_5.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: While static analysis is instrumental in uncovering software bugs, its precision in analyzing large and intricate codebases remains challenging. The emerging prowess of Large Language Models (LLMs) offers a promising avenue to address these complexities. In this paper, we present LLift, a pioneering...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [Examining Zero-Shot Vulnerability Repair with Large Language Models](../venues/S&P2023/paper_1.md), ([S&P2023](../venues/S&P2023/README.md))

  - **Abstract**: Human developers can produce code with cybersecurity bugs. Can emerging ‘smart’ code completion tools help repair those bugs? In this work, we examine the use of large language models (LLMs) for code (such as OpenAI’s Codex and AI21’s Jurassic J-1) for zero-shot vulnerability repair. We investigate ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)


- [Explaining Software Bugs Leveraging Code Structures in Neural Machine Translation](../venues/ICSE2023/paper_6.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Software bugs claim ≈ 50\% of development time and cost the global economy billions of dollars. Once a bug is reported, the assigned developer attempts to identify and understand the source code responsible for the bug and then corrects the code. Over the last five decades, there has been significan...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [E{\&}V: Prompting Large Language Models to Perform Static Analysis by Pseudo-code Execution and Verification](../venues/Microsoft2023/paper_2.md), ([Microsoft2023](../venues/Microsoft2023/README.md))

  - **Abstract**: Static analysis, the process of examining code without executing it, is crucial for identifying software issues. Yet, static analysis is hampered by its complexity and the need for customization for different targets. Traditional static analysis tools require extensive human effort and are often lim...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [GPTScan: Detecting Logic Vulnerabilities in Smart Contracts by Combining GPT with Program Analysis](../venues/ICSE2024/paper_17.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Smart contracts are prone to various vulnerabilities, leading to substantial financial losses over time. Current analysis tools mainly target vulnerabilities with fixed control- or data-flow patterns, such as re-entrancy and integer overflow. However, a recent study on Web3 security bugs revealed th...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [Gptscan: Detecting logic vulnerabilities in smart contracts by combining gpt with program analysis](../venues/ICSE2024/paper_22.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Smart contracts are prone to various vulnerabilities, leading to substantial financial losses over time. Current analysis tools mainly target vulnerabilities with fixed control- or data-flow patterns, such as re-entrancy and integer overflow. However, a recent study on Web3 security bugs revealed th...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [Harnessing the power of llm to support binary taint analysis](../venues/arXiv2023/paper_7.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: This paper proposes LATTE, the first static binary taint analysis that is powered by a large language model (LLM). LATTE is superior to the state of the art (e.g., Emtaint, Arbiter, Karonte) in three aspects. First, LATTE is fully automated while prior static binary taint analyzers need rely on huma...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [How Far Have We Gone in Vulnerability Detection Using Large Language Models](../venues/arXiv2023/paper_3.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: As software becomes increasingly complex and prone to vulnerabilities, automated vulnerability detection is critically important, yet challenging. Given the significant successes of large language models (LLMs) in various tasks, there is growing anticipation of their efficacy in vulnerability detect...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [benchmark](../../labels/benchmark.md)


- [Interleaving Static Analysis and LLM Prompting](../venues/SOAP2024/paper_1.md), ([SOAP2024](../venues/SOAP2024/README.md))

  - **Abstract**: This paper presents a new approach for using Large Language Models (LLMs) to improve static program analysis. Specifically, during program analysis, we interleave calls to the static analyzer and queries to the LLM: the prompt used to query the LLM is constructed using intermediate results from the ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [Jtrans: Jump-aware transformer for binary code similarity detection](../venues/ISSTA2022/paper_1.md), ([ISSTA2022](../venues/ISSTA2022/README.md))

  - **Abstract**: Binary code similarity detection (BCSD) has important applications in various fields such as vulnerabilities detection, software component analysis, and reverse engineering. Recent studies have shown that deep neural networks (DNNs) can comprehend instructions or control-flow graphs (CFG) of binary ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md)


- [LLM-Assisted Static Analysis for Detecting Security Vulnerabilities](../venues/arXiv2024/paper_18.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Software is prone to security vulnerabilities. Program analysis tools to detect them have limited effectiveness in practice due to their reliance on human labeled specifications. Large language models (or LLMs) have shown impressive code generation capabilities but they cannot do complex reasoning o...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [LLM-based Resource-Oriented Intention Inference for Static Resource Detection](../venues/ICSE2025/paper_2.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Resource leaks, caused by resources not being released after acquisition, often lead to performance issues and system crashes. Existing static detection techniques rely on mechanical matching of predefined resource acquisition/release APIs and null-checking conditions to find unreleased resources, s...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [LLM4Vuln: {A} Unified Evaluation Framework for Decoupling and Enhancing LLMs' Vulnerability Reasoning](../venues/arXiv2024/paper_15.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Large language models (LLMs) have demonstrated significant potential in various tasks, including vulnerability detection. However, current efforts in this area are preliminary, lacking clarity on whether LLMs' vulnerability reasoning capabilities stem from the models themselves or external aids such...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [benchmark](../../labels/benchmark.md)


- [LLMDFA: Analyzing Dataflow in Code with Large Language Model](../venues/NeurIPS2024/paper_6.md), ([NeurIPS2024](../venues/NeurIPS2024/README.md))

  - **Abstract**: Dataflow analysis is a fundamental code analysis technique that identifies dependencies between program values. Traditional approaches typically necessitate successful compilation and expert customization, hindering their applicability and usability for analyzing uncompilable programs with evolving ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [LLMs Cannot Reliably Identify and Reason About Security Vulnerabilities (Yet?): A Comprehensive Evaluation, Framework, and Benchmarks](../venues/S&P2024/paper_1.md), ([S&P2024](../venues/S&P2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have been suggested for use in automated vulnerability repair, but benchmarks showing they can consistently identify security-related bugs are lacking. We thus develop SecLLMHolmes, a fully automated evaluation framework that performs the most detailed investigation to d...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [empirical study](../../labels/empirical_study.md)


- [Large Language Models for Code Analysis: Do LLMs Really Do Their Job?](../venues/USENIXSec2024/paper_1.md), ([USENIXSec2024](../venues/USENIXSec2024/README.md))

  - **Abstract**: Large language models (LLMs) have demonstrated significant potential in the realm of natural language understanding and programming code processing tasks. Their capacity to comprehend and generate human-like code has spurred research into harnessing LLMs for code analysis purposes. However, the exis...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)


- [Large language model-powered smart contract vulnerability detection: New perspectives](../venues/arXiv2023/paper_9.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: This paper provides a systematic analysis of the opportunities, challenges, and potential solutions of harnessing Large Language Models (LLMs) such as GPT-4 to dig out vulnerabilities within smart contracts based on our ongoing research. For the task of smart contract vulnerability detection, achiev...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [Learning to Detect and Localize Multilingual Bugs](../venues/FSE2024/paper_31.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Increasing studies have shown bugs in multi-language software as a critical loophole in modern software quality assurance, especially those induced by language interactions (i.e., multilingual bugs). Yet existing tool support for bug detection/localization remains largely limited to single-language ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


- [Leveraging Large Language Model to Assist Detecting Rust Code Comment Inconsistency](../venues/ASE2024/paper_5.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Rust is renowned for its robust memory safety capabilities, yet its distinctive memory management model poses substantial challenges in both writing and understanding programs. Within Rust source code, comments are employed to clearly delineate conditions that might cause panic behavior, thereby war...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [Leveraging Semantic Relations in Code and Data to Enhance Taint Analysis of Embedded Systems](../venues/USENIXSec2024/paper_2.md), ([USENIXSec2024](../venues/USENIXSec2024/README.md))

  - **Abstract**: IoT devices have significantly impacted our daily lives, and detecting vulnerabilities in embedded systems early on is critical for ensuring their security. Among the existing vulnerability detection techniques for embedded systems, static taint analysis has been proven effective in detecting severe...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


- [Pre-training by Predicting Program Dependencies for Vulnerability Analysis Tasks](../venues/ICSE2024/paper_30.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Vulnerability analysis is crucial for software security. Inspired by the success of pre-trained models on software engineering tasks, this work focuses on using pre-training techniques to enhance the understanding of vulnerable code and boost vulnerability analysis. The code understanding ability of...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


- [RealVul: Can We Detect Vulnerabilities in Web Applications with LLM?](../venues/EMNLP2024/paper_25.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: The latest advancements in large language models (LLMs) have sparked interest in their potential for software vulnerability detection. However, there is currently a lack of research specifically focused on vulnerabilities in the PHP language, and challenges in data sampling and processing persist, h...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [Risky Dynamic Typing-related Practices in Python: An Empirical Study](../venues/TOSEM2024/paper_6.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Python’s dynamic typing nature provides developers with powerful programming abstractions. However, many type-related bugs are accumulated in code bases of Python due to the misuse of dynamic typing. The goal of this article is to aid in the understanding of developers’ high-risk practices toward dy...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [type inference](../../labels/type_inference.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)


- [SCALE: Constructing Structured Natural Language Comment Trees for Software Vulnerability Detection](../venues/ISSTA2024/paper_4.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Recently, there has been a growing interest in automatic software vulnerability detection.     Pre-trained model-based approaches have demonstrated superior performance than other Deep Learning (DL)-based approaches in detecting vulnerabilities.     However, the existing pre-trained model-based appr...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [Sanitizing Large Language Models in Bug Detection with Data-Flow](../venues/EMNLP2024/paper_5.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large language models (LLMs) show potential in code reasoning tasks, facilitating the customization of detecting bugs in software development. However, the hallucination effect can significantly compromise the reliability of bug reports. This work formulates a new schema of bug detection and present...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [fundamental analysis](../../labels/fundamental_analysis.md)


- [Semantic Sleuth: Identifying Ponzi Contracts via Large Language Models](../venues/ASE2024/paper_11.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Smart contracts, self-executing agreements directly encoded in code, are fundamental to blockchain technology, especially in decentralized finance (DeFi) and Web3. However, the rise of Ponzi schemes in smart contracts poses significant risks, leading to substantial financial losses and eroding trust...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [SkipAnalyzer: An Embodied Agent for Code Analysis with Large Language Models](../venues/arXiv2023/paper_6.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: We introduce SkipAnalyzer, a large language model (LLM)-powered tool for static code analysis. SkipAnalyzer has three components: 1) an LLM-based static bug detector that scans source code and reports specific types of bugs, 2) an LLM-based false-positive filter that can identify false-positive bugs...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [agent design](../../labels/agent_design.md)


- [Smartinv: Multimodal learning for smart contract invariant inference](../venues/S&P2024/paper_4.md), ([S&P2024](../venues/S&P2024/README.md))

  - **Abstract**: Smart contracts are software programs that enable diverse business activities on the blockchain. Recent research has identified new classes of "machine un-auditable" bugs that arise from source code not meeting underlying transaction contexts. Existing detection methods require human understanding o...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [Source Code Vulnerability Detection: Combining Code Language Models and Code Property Graphs](../venues/arXiv2024/paper_13.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Currently, deep learning successfully applies to code vulnerability detection by learning from code sequences or property graphs. However, sequence-based methods often overlook essential code attributes such as syntax, control flow, and data dependencies, whereas graph-based approaches might underes...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


- [Stanceformer: Target-Aware Transformer for Stance Detection](../venues/EMNLP2024/paper_6.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: The task of Stance Detection involves discerning the stance expressed in a text towards a specific subject or target. Prior works have relied on existing transformer models that lack the capability to prioritize targets effectively. Consequently, these models yield similar performance regardless of ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)


- [The EarlyBIRD Catches the Bug: On Exploiting Early Layers of Encoder Models for More Efficient Code Classification](../venues/FSE2023/paper_12.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: The use of modern Natural Language Processing (NLP) techniques has shown to be beneficial for software engineering tasks, such as vulnerability detection and type inference. However, training deep NLP models requires significant computational resources. This paper explores techniques that aim at ach...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md), [empirical study](../../labels/empirical_study.md)


- [The Emergence of Large Language Models in Static Analysis: A First Look through Micro-Benchmarks](../venues/Forge2024/paper_1.md), ([Forge2024](../venues/Forge2024/README.md))

  - **Abstract**: Binary code similarity detection(BCSD), as a fundamental technique in software security, has various applications, including malware family detection, known vulnerability detection and code plagiarism detection. Recent deep learning-based BCSD approaches have demonstrated promising performance. Howe...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)


- [Top Score on the Wrong Exam: On Benchmarking in Machine Learning for Vulnerability Detection](../venues/arXiv2024/paper_16.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: According to our survey of the machine learning for vulnerability detection (ML4VD) literature published in the top Software Engineering conferences, every paper in the past 5 years defines ML4VD as a binary classification problem: Given a function, does it contain a security flaw?In this paper, we ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)


- [Twin Graph-Based Anomaly Detection via Attentive Multi-Modal Learning for Microservice System](../venues/ASE2023/paper_16.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Microservice architecture has sprung up over recent years for managing enterprise applications, due to its ability to independently deploy and scale services. Despite its benefits, ensuring the reliability and safety of a microservice system remains highly challenging. Existing anomaly detection alg...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [Understanding the Effectiveness of Large Language Models in Detecting Security Vulnerabilities](../venues/arXiv2023/paper_4.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: While automated vulnerability detection techniques have made promising progress in detecting security vulnerabilities, their scalability and applicability remain challenging. The remarkable performance of Large Language Models (LLMs), such as GPT-4 and CodeLlama, on code-related tasks has prompted r...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)


- [VALAR: Streamlining Alarm Ranking in Static Analysis with Value-Flow Assisted Active Learning](../venues/ASE2023/paper_15.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Static analyzers play a critical role in program defects and security vulnerabilities detection. Despite their importance, the widespread adoption of static analysis techniques in industrial development faces numerous obstacles, among which the high rate of false alarms constitutes a significant one...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [VGX: Large-Scale Sample Generation for Boosting Learning-Based Software Vulnerability Analyses](../venues/ICSE2024/paper_29.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Accompanying the successes of learning-based defensive software vulnerability analyses is the lack of large and quality sets of labeled vulnerable program samples, which impedes further advancement of those defenses. Existing automated sample generation approaches have shown potentials yet still fal...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


- [VULGEN: Realistic Vulnerability Generation Via Pattern Mining and Deep Learning](../venues/ICSE2023/paper_11.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Building new, powerful data-driven defenses against prevalent software vulnerabilities needs sizable, quality vulnerability datasets, so does large-scale benchmarking of existing defense solutions. Automatic data generation would promisingly meet the need, yet there is little work aimed to generate ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [benchmark](../../labels/benchmark.md)


- [VulEval: Towards Repository-Level Evaluation of Software Vulnerability Detection](../venues/arXiv2024/paper_11.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Deep Learning (DL)-based methods have proven to be effective for software vulnerability detection, with a potential for substantial productivity enhancements for detecting vulnerabilities. Current methods mainly focus on detecting single functions (i.e., intra-procedural vulnerabilities), ignoring t...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [benchmark](../../labels/benchmark.md)


- [VulExplainer: A Transformer-Based Hierarchical Distillation for Explaining Vulnerability Types](../venues/TSE2023/paper_1.md), ([TSE2023](../venues/TSE2023/README.md))

  - **Abstract**: Deep learning-based vulnerability prediction approaches are proposed to help under-resourced security practitioners to detect vulnerable functions. However, security practitioners still do not know what type of vulnerabilities correspond to a given prediction (aka CWE-ID). Thus, a novel approach to ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [Vulnerability Detection with Code Language Models: How Far Are We?](../venues/ICSE2025/paper_1.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: In the context of the rising interest in code language models (code LMs) and vulnerability detection, we study the effectiveness of code LMs for detecting vulnerabilities. Our analysis reveals significant shortcomings in existing vulnerability datasets, including poor data quality, low label accurac...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [benchmark](../../labels/benchmark.md)


- [Where is it? Tracing the Vulnerability-relevant Files from Vulnerability Reports](../venues/ICSE2024/paper_18.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: With the widely usage of open-source software, supply-chain-based vulnerability attacks, including SolarWind and Log4Shell, have posed significant risks to software security. Currently, people rely on vulnerability advisory databases or commercial software bill of materials (SBOM) to defend against ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [Who Judges the Judge: An Empirical Study on Online Judge Tests](../venues/ISSTA2023/paper_1.md), ([ISSTA2023](../venues/ISSTA2023/README.md))

  - **Abstract**: Online Judge platforms play a pivotal role in education, competitive programming, recruitment, career training, and large language model training. They rely on predefined test suites to judge the correctness of submitted solutions. It is therefore important that the solution judgement is reliable an...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


- [Your Instructions Are Not Always Helpful: Assessing the Efficacy of Instruction Fine-tuning for Software Vulnerability Detection](../venues/arXiv2024/paper_14.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Software, while beneficial, poses potential cybersecurity risks due to inherent vulnerabilities. Detecting these vulnerabilities is crucial, and deep learning has shown promise as an effective tool for this task due to its ability to perform well without extensive feature engineering. However, a cha...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


- [iSMELL: Assembling LLMs with Expert Toolsets for Code Smell Detection and Refactoring](../venues/ASE2024/paper_22.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Detecting and refactoring code smells is challenging, laborious, and sustaining. Although large language models have demonstrated potential in identifying various types of code smells, they also have limitations such as input-output token restrictions, difficulty in accessing repository-level knowle...
  - **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## Program Verification

- [Automated Program Refinement: Guide and Verify Code Large Language Model with Refinement Calculus](../venues/POPL2025/paper_1.md), ([POPL2025](../venues/POPL2025/README.md))

  - **Abstract**: Recently, the rise of code-centric large language models (LLMs) appears to have reshaped the software engineering world with low-barrier tools like Copilot that can generate code easily. However, there is no correctness guarantee for the code generated by LLMs, which suffer from the hallucination pr...
  - **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md), [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


- [Baldur: Whole-Proof Generation and Repair with Large Language Models](../venues/FSE2023/paper_3.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Formally verifying software is a highly desirable but labor-intensive task.  Recent work has developed methods to automate formal verification using proof assistants, such as Coq and Isabelle/HOL, e.g., by training a model to predict one proof step at a time and using that model to search through th...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


- [Can ChatGPT support software verification?](../venues/FASE2024/paper_1.md), ([FASE2024](../venues/FASE2024/README.md))

  - **Abstract**: Large language models have become increasingly effective in software engineering tasks such as code generation, debugging and repair. Language models like ChatGPT can not only generate code, but also explain its inner workings and in particular its correctness. This raises the question whether we ca...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


- [Can large language models reason about program invariants?](../venues/ICML2023/paper_3.md), ([ICML2023](../venues/ICML2023/README.md))

  - **Abstract**: Identifying invariants is an important program analysis task with applications towards program understanding, bug finding, vulnerability analysis, and formal verification. Existing tools for identifying program invariants rely on dynamic analysis, requiring traces collected from multiple executions ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


- [CoqPilot, a plugin for LLM-based generation of proofs](../venues/ASE2024/paper_36.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: We present CoqPilot, a VS Code extension designed to help automate writing of Coq proofs. The plugin collects the parts of proofs marked with the admit tactic in a Coq file, i.e., proof holes, and combines LLMs along with non-machine-learning methods to generate proof candidates for the holes. Then,...
  - **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


- [Enchanting program specification synthesis by large language models using static analysis and program verification](../venues/CAV2024/paper_1.md), ([CAV2024](../venues/CAV2024/README.md))

  - **Abstract**: Formal verification provides a rigorous and systematic approach to ensure the correctness and reliability of software systems. Yet, constructing specifications for the full proof relies on domain expertise and non-trivial manpower. In view of such needs, an automated approach for specification synth...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md), [specification inference](../../labels/specification_inference.md)


- [Finding inductive loop invariants using large language models](../venues/arXiv2023/paper_10.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**:     Loop invariants are fundamental to reasoning about programs with loops. They establish properties about a given loop's behavior. When they additionally are inductive, they become useful for the task of formal verification that seeks to establish strong mathematical guarantees about program's run...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md), [invariant generation](../../labels/invariant_generation.md)


- [Hypothesis search: Inductive reasoning with language models](../venues/ICLR2024/paper_2.md), ([ICLR2024](../venues/ICLR2024/README.md))

  - **Abstract**: Inductive reasoning is a core problem-solving capacity: humans can identify underlying principles from a few examples, which can then be robustly generalized to novel scenarios. Recent work has evaluated large language models (LLMs) on inductive reasoning tasks by directly prompting them yielding "i...
  - **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


- [LLM Meets Bounded Model Checking: Neuro-symbolic Loop Invariant Inference](../venues/ASE2024/paper_7.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Loop invariant inference, a key component in program verification, is a challenging task due to the inherent undecidability and complex loop behaviors in practice. Recently, machine learning based techniques have demonstrated impressive performance in generating loop invariants automatically. Howeve...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


- [LLM-Generated Invariants for Bounded Model Checking Without Loop Unrolling](../venues/ASE2024/paper_23.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: We investigate a modification of the classical Bounded Model Checking (BMC) procedure that does not handle loops through unrolling but via modifications to the control flow graph (CFG). A portion of the CFG representing a loop is replaced by a node asserting invariants of the loop. We generate these...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md), [invariant generation](../../labels/invariant_generation.md)


- [Lemur: Integrating large language models in automated program verification](../venues/ICLR2024/paper_6.md), ([ICLR2024](../venues/ICLR2024/README.md))

  - **Abstract**: The demonstrated code-understanding capability of LLMs raises the question of whether they can be used for automated program verification, a task that typically demands high-level abstract reasoning about program properties that is challenging for verification tools. We propose a general methodology...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


- [Ranking llm-generated loop invariants for program verification](../venues/EMNLP2023/paper_13.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Synthesizing inductive loop invariants is fundamental to automating program verification. In this work, we observe that Large Language Models (such as gpt-3.5 or gpt-4) are capable of synthesizing loop invariants for a class of programs in a 0-shot setting, yet require several samples to generate th...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md), [invariant generation](../../labels/invariant_generation.md), [prompt strategy](../../labels/prompt_strategy.md), [sampling and ranking](../../labels/sampling_and_ranking.md)


- [Towards AI-Assisted Synthesis of Verified Dafny Methods](../venues/FSE2024/paper_23.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Large language models show great promise in many domains, including programming. A promise is easy to make but hard to keep, and language models often fail to keep their promises, generating erroneous code. A promising avenue to keep models honest is to incorporate formal verification: generating pr...
  - **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


- [Towards General Loop Invariant Generation: A Benchmark of Programs with Memory Manipulation](../venues/NeurIPS2024/paper_7.md), ([NeurIPS2024](../venues/NeurIPS2024/README.md))

  - **Abstract**: Program verification is vital for ensuring software reliability, especially in the context of increasingly complex systems. Loop invariants, remaining true before and after each iteration of loops, are crucial for this verification process. Traditional provers and machine learning based methods for ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md), [benchmark](../../labels/benchmark.md)


- [Verified Code Transpilation with LLMs](../venues/NeurIPS2024/paper_4.md), ([NeurIPS2024](../venues/NeurIPS2024/README.md))

  - **Abstract**: Domain-specific languages (DSLs) are integral to various software workflows. Such languages offer domain-specific optimizations and abstractions that improve code readability and maintainability. However, leveraging these languages requires developers to rewrite existing code using the specific DSL'...
  - **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


## Code Search

- [Natural Is the Best: Model-Agnostic Code Simplification for Pre-trained Large Language Models](../venues/FSE2024/paper_17.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Pre-trained Large Language Models (LLM) have achieved remarkable successes in several domains. However, code-oriented LLMs are often heavy in computational complexity, and quadratically with the length of the input code sequence. Toward simplifying the input program of an LLM, the state-of-the-art a...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [code search](../../labels/code_search.md), [code summarization](../../labels/code_summarization.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


- [On the Effectiveness of Transfer Learning for Code Search](../venues/TSE2023/paper_6.md), ([TSE2023](../venues/TSE2023/README.md))

  - **Abstract**: The Transformer architecture and transfer learning have marked a quantum leap in natural language processing, improving the state of the art across a range of text-based tasks. This paper examines how these advancements can be applied to and improve code search. To this end, we pre-train a BERT-base...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [code search](../../labels/code_search.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


- [Self-Supervised Query Reformulation for Code Search](../venues/FSE2023/paper_9.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Automatic query reformulation is a widely utilized technology for enriching user requirements and enhancing the outcomes of code search. It can be conceptualized as a machine translation task, wherein the objective is to rephrase a given query into a more comprehensive alternative. While showing pro...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [code search](../../labels/code_search.md)


- [Survey of Code Search Based on Deep Learning](../venues/TOSEM2024/paper_9.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Code writing is repetitive and predictable, inspiring us to develop various code intelligence techniques. This survey focuses on code search, that is, to retrieve code that matches a given natural language query by effectively capturing the semantic similarity between the query and code. Deep learni...
  - **Labels**: [survey](../../labels/survey.md), [static analysis](../../labels/static_analysis.md), [code search](../../labels/code_search.md)


- [Virtual Compiler Is All You Need For Assembly Code Search](../venues/ACL2024/paper_11.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Assembly code search is vital for reducing the burden on reverse engineers, allowing them to quickly identify specific functions using natural language within vast binary programs.Despite its significance, this critical task is impeded by the complexities involved in building high-quality datasets. ...
  - **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md), [static analysis](../../labels/static_analysis.md), [code search](../../labels/code_search.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## Code Similarity Analysis

- [BinCola: Diversity-Sensitive Contrastive Learning for Binary Code Similarity Detection](../venues/TSE2024/paper_14.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Binary Code Similarity Detection (BCSD) is a fundamental binary analysis technique in the area of software security. Recently, advanced deep learning algorithms are integrated into BCSD platforms to achieve superior performance on well-known benchmarks. However, real-world large programs embed more ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [code similarity analysis](../../labels/code_similarity_analysis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md)


- [Cross-lingual Code Clone Detection: When LLMs Fail Short Against Embedding-based Classifier](../venues/ASE2024/paper_41.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Cross-lingual code clone detection has gained attention in software development due to the use of multiple programming languages. Recent advances in machine learning, particularly Large Language Models (LLMs), have motivated a reexamination of this problem.This paper evaluates the performance of fou...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [code similarity analysis](../../labels/code_similarity_analysis.md)


- [Improving Binary Code Similarity Transformer Models by Semantics-Driven Instruction Deemphasis](../venues/ISSTA2023/paper_5.md), ([ISSTA2023](../venues/ISSTA2023/README.md))

  - **Abstract**: Given a function in the binary executable form, binary code similarity analysis determines a set of similar functions from a large pool of candidate functions. These similar functions are usually compiled from the same source code with different compilation setups. Such analysis has a large number o...
  - **Labels**: [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md), [static analysis](../../labels/static_analysis.md), [code similarity analysis](../../labels/code_similarity_analysis.md)


- [RCFG2Vec: Considering Long-Distance Dependency for Binary Code Similarity Detection](../venues/ASE2024/paper_43.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Binary code similarity detection(BCSD), as a fundamental technique in software security, has various applications, including malware family detection, known vulnerability detection and code plagiarism detection. Recent deep learning-based BCSD approaches have demonstrated promising performance. Howe...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [code similarity analysis](../../labels/code_similarity_analysis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md)


## Software Composition Analysis

- [BinaryAI: Binary Software Composition Analysis via Intelligent Binary Source Code Matching](../venues/ICSE2024/paper_31.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: While third-party libraries (TPLs) are extensively reused to enhance productivity during software development, they can also introduce potential security risks such as vulnerability propagation. Software composition analysis (SCA), proposed to identify reused TPLs for reducing such risks, has become...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [software composition analysis](../../labels/software_composition_analysis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md)


- [Can Large Language Models Comprehend Code Stylometry?](../venues/ASE2024/paper_39.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Code Authorship Attribution (CAA) has several applications such as copyright disputes, plagiarism detection and criminal prosecution. Existing studies mainly focused on CAA by proposing machine learning (ML) and Deep Learning (DL) based techniques. The main limitations of ML-based techniques are (a)...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [software composition analysis](../../labels/software_composition_analysis.md)


- [Maltracker: A Fine-Grained NPM Malware Tracker Copiloted by LLM-Enhanced Dataset](../venues/ISSTA2024/paper_24.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: As the largest package registry, Node Package Manager (NPM) has become the prime target for various supply chain attacks recently and has been flooded with numerous malicious packages, posing significant security risks to end-users. Learning-based methods have demonstrated promising performance with...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [software composition analysis](../../labels/software_composition_analysis.md)


## Code Summarization

- [Automatic Semantic Augmentation of Language Model Prompts (for Code Summarization)](../venues/ICSE2024/paper_19.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Large Language Models (LLM) are a new class of computation engines, "programmed" via prompt engineering. Researchers are still learning how to best "program" these LLMs to help developers. We start with the intuition that developers tend to consciously and unconsciously collect semantics facts, from...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md), [prompt strategy](../../labels/prompt_strategy.md), [retrieval-augmented generation](../../labels/retrieval-augmented_generation.md)


- [CoSS: Leveraging Statement Semantics for Code Summarization](../venues/TSE2023/paper_4.md), ([TSE2023](../venues/TSE2023/README.md))

  - **Abstract**: Automated code summarization tools allow generating descriptions for code snippets in natural language, which benefits software development and maintenance. Recent studies demonstrate that the quality of generated summaries can be improved by using additional code representations beyond token sequen...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


- [Code Structure–Guided Transformer for Source Code Summarization](../venues/TOSEM2023/paper_3.md), ([TOSEM2023](../venues/TOSEM2023/README.md))

  - **Abstract**: Code summaries help developers comprehend programs and reduce their time to infer the program functionalities during software maintenance. Recent efforts resort to deep learning techniques such as sequence-to-sequence models for generating accurate code summaries, among which Transformer-based appro...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md)


- [EyeTrans: Merging Human and Machine Attention for Neural Code Summarization](../venues/FSE2024/paper_30.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Neural code summarization leverages deep learning models to automatically generate brief natural language summaries of code snippets. The development of Transformer models has led to extensive use of attention during model design. While existing work has primarily and almost exclusively focused on s...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md), [empirical study](../../labels/empirical_study.md)


- [Learning to Generate Structured Code Summaries From Hybrid Code Context](../venues/TSE2024/paper_11.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Code summarization aims to automatically generate natural language descriptions for code, and has become a rapidly expanding research area in the past decades. Unfortunately, existing approaches mainly focus on the “one-to-one” mapping from methods to short descriptions, which hinders them from beco...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md), [benchmark](../../labels/benchmark.md)


- [Natural Is the Best: Model-Agnostic Code Simplification for Pre-trained Large Language Models](../venues/FSE2024/paper_17.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Pre-trained Large Language Models (LLM) have achieved remarkable successes in several domains. However, code-oriented LLMs are often heavy in computational complexity, and quadratically with the length of the input code sequence. Toward simplifying the input program of an LLM, the state-of-the-art a...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [code search](../../labels/code_search.md), [code summarization](../../labels/code_summarization.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


- [SimLLM: Calculating Semantic Similarity in Code Summaries using a Large Language Model-Based Approach](../venues/FSE2024/paper_4.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Code summaries are pivotal in software engineering, serving to improve code readability, maintainability, and collaboration. While recent advancements in Large Language Models (LLMs) have opened new avenues for automatic code summarization, existing metrics for evaluating summary quality, such as BL...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md)


- [Understanding Code Changes Practically with Small-Scale Language Models](../venues/ASE2024/paper_3.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Recent studies indicate that traditional techniques for understanding code changes are not as effective as techniques that directly prompt language models (LMs). However, current LM-based techniques heavily rely on expensive, large LMs (LLMs) such as GPT-4 and Llama-13b, which are either commercial ...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## Compiler Optimization

- [Meta large language model compiler: Foundation models of compiler optimization](../venues/Meta2024/paper_1.md), ([Meta2024](../venues/Meta2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated remarkable capabilities across a variety of software engineering and coding tasks. However, their application in the domain of code and compiler optimization remains underexplored. Training LLMs is resource-intensive, requiring substantial GPU hours and...
  - **Labels**: [code generation](../../labels/code_generation.md), [compiler optimization](../../labels/compiler_optimization.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [IR code model](../../labels/IR_code_model.md)


- [Programl: A graph-based program representation for data flow analysis and compiler optimizations](../venues/ICML2021/paper_2.md), ([ICML2021](../venues/ICML2021/README.md))

  - **Abstract**: Machine learning (ML) is increasingly seen as a viable approach for building compiler optimization heuristics, but many ML methods cannot replicate even the simplest of the data flow analyses that are critical to making good optimization decisions. We posit that if ML cannot do that, then it is insu...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [fundamental analysis](../../labels/fundamental_analysis.md), [compiler optimization](../../labels/compiler_optimization.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [IR code model](../../labels/IR_code_model.md)


## Type Inference

- [Generative Type Inference for Python](../venues/ASE2023/paper_12.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Python is a popular dynamic programming language, evidenced by its ranking as the second most commonly used language on GitHub. However, its dynamic type system can lead to potential type errors, leading researchers to explore automatic type inference approaches for Python programs. Existing type in...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [type inference](../../labels/type_inference.md)


- [PyTy: Repairing Static Type Errors in Python](../venues/ICSE2024/paper_12.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Gradual typing enables developers to annotate types of their own choosing, offering a flexible middle ground between no type annotations and a fully statically typed language. As more and more code bases get type-annotated, static type checkers detect an increasingly large number of type errors. Unf...
  - **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [static analysis](../../labels/static_analysis.md), [type inference](../../labels/type_inference.md)


- [Risky Dynamic Typing-related Practices in Python: An Empirical Study](../venues/TOSEM2024/paper_6.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Python’s dynamic typing nature provides developers with powerful programming abstractions. However, many type-related bugs are accumulated in code bases of Python due to the misuse of dynamic typing. The goal of this article is to aid in the understanding of developers’ high-risk practices toward dy...
  - **Labels**: [static analysis](../../labels/static_analysis.md), [type inference](../../labels/type_inference.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)


