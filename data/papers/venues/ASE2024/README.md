# ASE2024

Number of papers: 45

## [A Pair Programming Framework for Code Generation via Multi-Plan Exploration and Feedback-Driven Refinement](paper_21.md)
- **Authors**: Zhang, Huan and Cheng, Wei and Wu, Yuhan and Hu, Wei
- **Abstract**: Large language models (LLMs) have achieved impressive performance on code generation. Although prior studies enhanced LLMs with prompting techniques and code refinement, they still struggle with complex programming problems due to rigid solution plans. In this paper, we draw on pair programming practices to propose PairCoder, a novel LLM-based framework for code generation. PairCoder incorporates two collaborative LLM agents, namely a Navigator agent for high-level planning and a Driver agent fo...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695506)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [agent design](../../labels/agent_design.md), [planning](../../labels/planning.md)


## [ART: A Unified Unsupervised Framework for Incident Management in Microservice Systems](paper_44.md)
- **Authors**: Sun, Yongqian and Shi, Binpeng and Mao, Mingyu and Ma, Minghua and Xia, Sibo and Zhang, Shenglin and Pei, Dan
- **Abstract**: Automated incident management is critical for large-scale microservice systems, including tasks such as anomaly detection (AD), failure triage (FT), and root cause localization (RCL). Currently, most techniques focus only on a single task, overlooking shared knowledge across closely related tasks. However, employing isolated models for managing multiple tasks may result in inefficiencies, delayed responses, a lack of systemic perspective, and complexity in updates and operations. Therefore we pr...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695495)
- **Labels**: [general coding task](../../labels/general_coding_task.md)


## [An Empirical Study to Evaluate AIGC Detectors on Code Content](paper_16.md)
- **Authors**: JianWang and Liu, Shangqing and Xie, Xiaofei and Li, Yi
- **Abstract**: Artificial Intelligence Generated Content (AIGC) has garnered considerable attention for its impressive performance, with Large Language Models (LLMs), like ChatGPT, emerging as a leading AIGC model that produces high-quality responses across various applications, including software development and maintenance. Despite its potential, the misuse of LLMs, especially in security and safety-critical domains, such as academic integrity and answering questions on Stack Overflow, poses significant conc...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695468)
- **Labels**: [general coding task](../../labels/general_coding_task.md), [benchmark](../../labels/benchmark.md)


## [Ansible Lightspeed: A Code Generation Service for IT Automation](paper_30.md)
- **Authors**: Sahoo, Priyam and Pujar, Saurabh and Nalawade, Ganesh and Genhardt, Richard and Mandel, Louis and Buratti, Luca
- **Abstract**: The availability of Large Language Models (LLMs) which can generate code, has made it possible to create tools that improve developer productivity. Integrated development environments or IDEs which developers use to write software are often used as an interface to interact with LLMs. Although many such tools have been released, almost all of them focus on general-purpose programming languages. Domain-specific languages, such as those crucial for Information Technology (IT) automation, have not r...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695277)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [Attacks and Defenses for Large Language Models on Coding Tasks](paper_32.md)
- **Authors**: Zhang, Chi and Wang, Zifan and Zhao, Ruoshi and Mangal, Ravi and Fredrikson, Matt and Jia, Limin and Pasareanu, Corina
- **Abstract**: Modern large language models (LLMs), such as ChatGPT, have demonstrated impressive capabilities for coding tasks, including writing and reasoning about code. They improve upon previous neural network models of code, such as code2seq or seq2seq, that already demonstrated competitive results when performing tasks such as code summarization and identifying code vulnerabilities. However, these previous code models were shown vulnerable to adversarial examples, i.e., small syntactic perturbations des...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695297)
- **Labels**: [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md), [attack](../../labels/attack.md), [defense](../../labels/defense.md)


## [Attribution-guided Adversarial Code Prompt Generation for Code Completion Models](paper_45.md)
- **Authors**: Li, Xueyang and Meng, Guozhu and Liu, Shangqing and Xiang, Lu and Sun, Kun and Chen, Kai and Luo, Xiapu and Liu, Yang
- **Abstract**: Large language models have made significant progress in code completion, which may further remodel future software development. However, these code completion models are found to be highly risky as they may introduce vulnerabilities unintentionally or be induced by a special input, i.e., adversarial code prompt. Prior studies mainly focus on the robustness of these models, but their security has not been fully analyzed.In this paper, we propose a novel approach AdvPro that can automatically gene...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695517)
- **Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md), [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md), [attack](../../labels/attack.md)


## [Automated Validation of COBOL to Java Transformation](paper_38.md)
- **Authors**: Kumar, Atul and Saha, Diptikalyan and Yasue, Toshiaki and Ono, Kohichi and Krishnan, Saravanan and Hans, Sandeep and Satoh, Fumiko and Mitchell, Gerald and Kumar, Sachin
- **Abstract**: Recent advances in Large Language Model (LLM) based Generative AI techniques have made it feasible to translate enterpriselevel code from legacy languages such as COBOL to modern languages such as Java or Python. While the results of LLM-based automatic transformation are encouraging, the resulting code cannot be trusted to correctly translate the original code. We propose a framework and a tool to help validate the equivalence of COBOL and translated Java. The results can also help repair the c...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695365)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [B4: Towards Optimal Assessment of Plausible Code Solutions with Plausible Tests](paper_27.md)
- **Authors**: Chen, Mouxiang and Liu, Zhongxin and Tao, He and Hong, Yusu and Lo, David and Xia, Xin and Sun, Jianling
- **Abstract**: Selecting the best code solution from multiple generated ones is an essential task in code generation, which can be achieved by using some reliable validators (e.g., developer-written test cases) for assistance. Since reliable test cases are not always available and can be expensive to build in practice, researchers propose to automatically generate test cases to assess code solutions. However, when both code solutions and test cases are plausible and not reliable, selecting the best solution be...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695536)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [Bridging Gaps in LLM Code Translation: Reducing Errors with Call Graphs and Bridged Debuggers](paper_40.md)
- **Authors**: Luo, Yang and Yu, Richard and Zhang, Fajun and Liang, Ling and Xiong, Yongqiang
- **Abstract**: When using large language models (LLMs) for code translation of complex software, numerous compilation and runtime errors can occur due to insufficient context awareness. To address this issue, this paper presents a code translation method based on call graphs and bridged debuggers: TransGraph. TransGraph first obtains the call graph of the entire code project using the Language Server Protocol, which provides a detailed description of the function call relationships in the program. Through this...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695322)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [Can Large Language Models Comprehend Code Stylometry?](paper_39.md)
- **Authors**: Dipongkor, Atish
- **Abstract**: Code Authorship Attribution (CAA) has several applications such as copyright disputes, plagiarism detection and criminal prosecution. Existing studies mainly focused on CAA by proposing machine learning (ML) and Deep Learning (DL) based techniques. The main limitations of ML-based techniques are (a) manual feature engineering is required to train these models and (b) they are vulnerable to adversarial attack. In this study, we initially fine-tune five Large Language Models (LLMs) for CAA and eva...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695370)
- **Labels**: [static analysis](../../labels/static_analysis.md), [software composition analysis](../../labels/software_composition_analysis.md)


## [ComplexCodeEval: A Benchmark for Evaluating Large Code Models on More Complex Code](paper_28.md)
- **Authors**: Feng, Jia and Liu, Jiachen and Gao, Cuiyun and Chong, Chun Yong and Wang, Chaozheng and Gao, Shan and Xia, Xin
- **Abstract**: In recent years, with the widespread attention of academia and industry on the application of large language models (LLMs) to code-related tasks, an increasing number of large code models (LCMs) have been proposed and corresponding evaluation benchmarks have continually emerged. Although existing evaluation benchmarks are helpful for comparing different LCMs, they may not reflect the performance of LCMs in various development scenarios. Specifically, they might evaluate model performance in only...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695552)
- **Labels**: [general coding task](../../labels/general_coding_task.md), [benchmark](../../labels/benchmark.md)


## [Contextualized Data-Wrangling Code Generation in Computational Notebooks](paper_19.md)
- **Authors**: Huang, Junjie and Guo, Daya and Wang, Chenglong and Gu, Jiazhen and Lu, Shuai and Inala, Jeevana Priya and Yan, Cong and Gao, Jianfeng and Duan, Nan and Lyu, Michael R.
- **Abstract**: Data wrangling, the process of preparing raw data for further analysis in computational notebooks, is a crucial yet time-consuming step in data science. Code generation has the potential to automate the data wrangling process to reduce analysts' overhead by translating user intents into executable code. Precisely generating data wrangling code necessitates a comprehensive consideration of the rich context present in notebooks, including textual context, code context and data context. However, no...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695503)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [ContractTinker: LLM-Empowered Vulnerability Repair for Real-World Smart Contracts](paper_35.md)
- **Authors**: Wang, Che and Zhang, Jiashuo and Gao, Jianbo and Xia, Libin and Guan, Zhi and Chen, Zhong
- **Abstract**: Smart contracts are susceptible to being exploited by attackers, especially when facing real-world vulnerabilities. To mitigate this risk, developers often rely on third-party audit services to identify potential vulnerabilities before project deployment. Nevertheless, repairing the identified vulnerabilities is still complex and laborintensive, particularly for developers lacking security expertise. Moreover, existing pattern-based repair tools mostly fail to address real-world vulnerabilities ...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695349)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [empirical study](../../labels/empirical_study.md)


## [Copilot-in-the-Loop: Fixing Code Smells in Copilot-Generated Python Code using Copilot](paper_31.md)
- **Authors**: Zhang, Beiqi and Liang, Peng and Feng, Qiong and Fu, Yujia and Li, Zengyang
- **Abstract**: As one of the most popular dynamic languages, Python experiences a decrease in readability and maintainability when code smells are present. Recent advancements in Large Language Models have sparked growing interest in AI-enabled tools for both code generation and refactoring. GitHub Copilot is one such tool that has gained widespread usage. Copilot Chat, released in September 2023, functions as an interactive tool aimed at facilitating natural language-powered coding. However, limited attention...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695290)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [CoqPilot, a plugin for LLM-based generation of proofs](paper_36.md)
- **Authors**: Kozyrev, Andrei and Solovev, Gleb and Khramov, Nikita and Podkopaev, Anton
- **Abstract**: We present CoqPilot, a VS Code extension designed to help automate writing of Coq proofs. The plugin collects the parts of proofs marked with the admit tactic in a Coq file, i.e., proof holes, and combines LLMs along with non-machine-learning methods to generate proof candidates for the holes. Then, CoqPilot checks if each proof candidate solves the given subgoal and, if successful, replaces the hole with it. The focus of CoqPilot is twofold. Firstly, we want to allow users to seamlessly combine...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695357)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


## [Cross-lingual Code Clone Detection: When LLMs Fail Short Against Embedding-based Classifier](paper_41.md)
- **Authors**: Moumoula, Micheline Benedicte and Kabore, Abdoul Kader and Klein, Jacques and Bissyande, Tegawende F.
- **Abstract**: Cross-lingual code clone detection has gained attention in software development due to the use of multiple programming languages. Recent advances in machine learning, particularly Large Language Models (LLMs), have motivated a reexamination of this problem.This paper evaluates the performance of four LLMs and eight prompts for detecting cross-lingual code clones, as well as a pretrained embedding model for classifying clone pairs. Both approaches are tested on the XLCoST and CodeNet datasets.Our...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695335)
- **Labels**: [static analysis](../../labels/static_analysis.md), [code similarity analysis](../../labels/code_similarity_analysis.md)


## [DroidCoder: Enhanced Android Code Completion with Context-Enriched Retrieval-Augmented Generation](paper_13.md)
- **Authors**: Yu, Xinran and Li, Chun and Pan, Minxue and Li, Xuandong
- **Abstract**: Android is the most popular mobile operating system. However, Android development requires extensive coding, especially for unique features such as lifecycle callbacks and UI widgets. Existing code completion methods typically utilize Retrieval-Augmented Generation (RAG) to provide contextual information for pre-trained code large language models (Code LLMs) to perform completion. Despite considerable progress in these methods, their effectiveness in Android development remains limited. This is ...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695063)
- **Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md), [prompt strategy](../../labels/prompt_strategy.md), [retrieval-augmented generation](../../labels/retrieval-augmented_generation.md)


## [Dynamic Scoring Code Token Tree: A Novel Decoding Strategy for Generating High-Performance Code](paper_20.md)
- **Authors**: Qu, Muzi and Liu, Jie and Kang, Liangyi and Wang, Shuai and Ye, Dan and Huang, Tao
- **Abstract**: Within the realms of scientific computing, large-scale data processing, and artificial intelligence-powered computation, disparities in performance, which originate from differing code implementations, directly influence the practicality of the code. Although existing works tried to utilize code knowledge to enhance the execution performance of codes generated by large language models, they neglect code evaluation outcomes which directly refer to the code execution details, resulting in ineffici...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695505)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [Effective Vulnerable Function Identification based on CVE Description Empowered by Large Language Models](paper_6.md)
- **Authors**: Wu, Yulun and Wen, Ming and Yu, Zeliang and Guo, Xiaochen and Jin, Hai
- **Abstract**: Open-source software (OSS) has profoundly transformed the software development paradigm by facilitating effortless code reuse. However, in recent years, there has been an alarming increase in disclosed vulnerabilities within OSS, posing significant security risks to downstream users. Therefore, analyzing existing vulnerabilities and precisely assessing their threats to downstream applications become pivotal. Plenty of efforts have been made recently towards this problem, such as vulnerability re...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695013)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [Exploring Parameter-Efficient Fine-Tuning of Large Language Model on Automated Program Repair](paper_14.md)
- **Authors**: Li, Guochang and Zhi, Chen and Chen, Jialiang and Han, Junxiao and Deng, Shuiguang
- **Abstract**: Automated Program Repair (APR) aims to fix bugs by generating patches. And existing work has demonstrated that "pre-training and fine-tuning" paradigm enables Large Language Models (LLMs) improve fixing capabilities on APR. However, existing work mainly focuses on Full-Model Fine-Tuning (FMFT) for APR and limited research has been conducted on the execution-based evaluation of Parameter-Efficient Fine-Tuning (PEFT) for APR. Comparing to FMFT, PEFT can reduce computing resource consumption withou...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695066)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [FastFixer: An Efficient and Effective Approach for Repairing Programming Assignments](paper_12.md)
- **Authors**: Liu, Fang and Liu, Zhenwei and Zhao, Qianhui and Jiang, Jing and Zhang, Li and Sun, Zian and Li, Ge and Li, Zhongqi and Ma, Yuchi
- **Abstract**: Providing personalized and timely feedback for student's programming assignments is useful for programming education. Automated program repair (APR) techniques have been used to fix the bugs in programming assignments, where the Large Language Models (LLMs) based approaches have shown promising results. Given the growing complexity of identifying and fixing bugs in advanced programming assignments, current fine-tuning strategies for APR are inadequate in guiding the LLM to identify bugs and make...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695062)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph](paper_10.md)
- **Authors**: Liu, Wei and Yu, Ailun and Zan, Daoguang and Shen, Bo and Zhang, Wei and Zhao, Haiyan and Jin, Zhi and Wang, Qianxiang
- **Abstract**: The performance of repository-level code completion depends upon the effective leverage of both general and repository-specific knowledge. Despite the impressive capability of code LLMs in general code completion tasks, they often exhibit less satisfactory performance on repository-level completion due to the lack of repository-specific knowledge in these LLMs. To address this problem, we propose GraphCoder, a retrieval-augmented code completion framework that leverages LLMs' general code knowle...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695054)
- **Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md)


## [Instructive Code Retriever: Learn from Large Language Model's Feedback for Code Intelligence Tasks](paper_2.md)
- **Authors**: Lu, Jiawei and Wang, Haoye and Liu, Zhongxin and Liang, Keyu and Bao, Lingfeng and Yang, Xiaohu
- **Abstract**: Recent studies proposed to leverage large language models (LLMs) with In-Context Learning (ICL) to handle code intelligence tasks without fine-tuning. ICL employs task instructions and a set of examples as demonstrations to guide the model in generating accurate answers without updating its parameters. While ICL has proven effective for code intelligence tasks, its performance heavily relies on the selected examples. Previous work has achieved some success in using BM25 to retrieve examples for ...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3694997)
- **Labels**: [prompt strategy](../../labels/prompt_strategy.md), [retrieval-augmented generation](../../labels/retrieval-augmented_generation.md)


## [JavaBench: A Benchmark of Object-Oriented Code Generation for Evaluating Large Language Models](paper_17.md)
- **Authors**: Cao, Jialun and Chen, Zhiyong and Wu, Jiarong and Cheung, Shing-Chi and Xu, Chang
- **Abstract**: Code generation benchmarks such as HumanEval are widely adopted to evaluate LLMs' capabilities. However, after consolidating the latest 24 benchmarks, we noticed three significant imbalances. First, imbalanced programming language. 95.8\% of benchmarks involve Python, while only 5 benchmarks involve Java, resulting in an insufficient understanding of LLMs' capability to generate Java code. Second, imbalanced code granularity. Function-/statement-level benchmarks account for over 83.3\% of benchm...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695470)
- **Labels**: [benchmark](../../labels/benchmark.md), [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [LLM Meets Bounded Model Checking: Neuro-symbolic Loop Invariant Inference](paper_7.md)
- **Authors**: Wu, Guangyuan and Cao, Weining and Yao, Yuan and Wei, Hengfeng and Chen, Taolue and Ma, Xiaoxing
- **Abstract**: Loop invariant inference, a key component in program verification, is a challenging task due to the inherent undecidability and complex loop behaviors in practice. Recently, machine learning based techniques have demonstrated impressive performance in generating loop invariants automatically. However, these methods highly rely on the labeled training data, and are intrinsically random and uncertain, leading to unstable performance. In this paper, we investigate a synergy of large language models...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695014)
- **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


## [LLM-Based Java Concurrent Program to ArkTS Converter](paper_37.md)
- **Authors**: Liu, Runlin and Lin, Yuhang and Hu, Yunge and Zhang, Zhe and Gao, Xiang
- **Abstract**: HarmonyOS NEXT is a distributed operating system developed to support HarmonyOS native apps. To support the new and independent Harmony ecosystem, developers are required to migrate their applications from Android to HarmonyOS. However, HarmonyOS utilizes ArkTS, a superset of TypeScript, as the programming language for application development. Hence, migrating applications to HarmonyOS requires translating programs across different program languages, e.g., Java, which is known to be very challen...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695362)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [LLM-Generated Invariants for Bounded Model Checking Without Loop Unrolling](paper_23.md)
- **Authors**: Pirzada, Muhammad A. A. and Reger, Giles and Bhayat, Ahmed and Cordeiro, Lucas C.
- **Abstract**: We investigate a modification of the classical Bounded Model Checking (BMC) procedure that does not handle loops through unrolling but via modifications to the control flow graph (CFG). A portion of the CFG representing a loop is replaced by a node asserting invariants of the loop. We generate these invariants using Large Language Models (LLMs) and use a first-order theorem prover to ensure the correctness of the generated statements. We thus transform programs to loop-free variants in a sound m...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695512)
- **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md), [invariant generation](../../labels/invariant_generation.md)


## [Leveraging Large Language Model to Assist Detecting Rust Code Comment Inconsistency](paper_5.md)
- **Authors**: Zhang, Yichi and Liu, Zixi and Feng, Yang and Xu, Baowen
- **Abstract**: Rust is renowned for its robust memory safety capabilities, yet its distinctive memory management model poses substantial challenges in both writing and understanding programs. Within Rust source code, comments are employed to clearly delineate conditions that might cause panic behavior, thereby warning developers about potential hazards associated with specific operations. Therefore, comments are particularly crucial for documenting Rust's program logic and design. Nevertheless, as modern softw...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695010)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [On the Evaluation of Large Language Models in Unit Test Generation](paper_26.md)
- **Authors**: Yang, Lin and Yang, Chen and Gao, Shutao and Wang, Weijing and Wang, Bo and Zhu, Qihao and Chu, Xiao and Zhou, Jianyi and Liang, Guangtai and Wang, Qianxiang and Chen, Junjie
- **Abstract**: Unit testing is an essential activity in software development for verifying the correctness of software components. However, manually writing unit tests is challenging and time-consuming. The emergence of Large Language Models (LLMs) offers a new direction for automating unit test generation. Existing research primarily focuses on closed-source LLMs (e.g., ChatGPT and CodeX) with fixed prompting strategies, leaving the capabilities of advanced open-source LLMs with various prompting settings une...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695529)
- **Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md), [empirical study](../../labels/empirical_study.md)


## [PACGBI: A Pipeline for Automated Code Generation from Backlog Items](paper_34.md)
- **Authors**: Sarschar, Mahja and Zhang, Gefei and Nowak, Annika
- **Abstract**: While there exist several tools to leverage Large Language Models (LLMs) for code generation, their capabilities are limited to the source code editor and are disconnected from the overall software development process. These tools typically generate standalone code snippets that still require manual integration into the codebase. There is still a lack of integrated solutions that seamlessly automate the entire development cycle, from backlog items to code generation and merge requests. We presen...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695346)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [Preference-Guided Refactored Tuning for Retrieval Augmented Code Generation](paper_1.md)
- **Authors**: Gao, Xinyu and Xiong, Yun and Wang, Deze and Guan, Zhenhan and Shi, Zejian and Wang, Haofen and Li, Shanshan
- **Abstract**: Retrieval-augmented code generation utilizes Large Language Models as the generator and significantly expands their code generation capabilities by providing relevant code, documentation, and more via the retriever. The current approach suffers from two primary limitations: 1) information redundancy. The indiscriminate inclusion of redundant information can result in resource wastage and may misguide generators, affecting their effectiveness and efficiency. 2) preference gap. Due to different op...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3694987)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [RCFG2Vec: Considering Long-Distance Dependency for Binary Code Similarity Detection](paper_43.md)
- **Authors**: Li, Weilong and Lu, Jintian and Xiao, Ruizhi and Shao, Pengfei and Jin, Shuyuan
- **Abstract**: Binary code similarity detection(BCSD), as a fundamental technique in software security, has various applications, including malware family detection, known vulnerability detection and code plagiarism detection. Recent deep learning-based BCSD approaches have demonstrated promising performance. However, they face two significant challenges that limit detection performance. First, most approaches that use sequence networks (like RNN and Transformer) utilize coarse-grained tokenization methods, wh...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695070)
- **Labels**: [static analysis](../../labels/static_analysis.md), [code similarity analysis](../../labels/code_similarity_analysis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md)


## [RMCBench: Benchmarking Large Language Models' Resistance to Malicious Code](paper_18.md)
- **Authors**: Chen, Jiachi and Zhong, Qingyuan and Wang, Yanlin and Ning, Kaiwen and Liu, Yongkun and Xu, Zenan and Zhao, Zhe and Chen, Ting and Zheng, Zibin
- **Abstract**: Warning: Please note that this article contains potential harmful or offensive content. This content is only for the evaluating and analysis of LLMs and does not imply any intention to promote criminal activities.The emergence of Large Language Models (LLMs) has significantly influenced various aspects of software development activities. Despite their benefits, LLMs also pose notable risks, including the potential to generate harmful content and being abused by malicious developers to create mal...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695480)
- **Labels**: [code generation](../../labels/code_generation.md), [benchmark](../../labels/benchmark.md), [code model](../../labels/code_model.md), [code model robustness](../../labels/code_model_robustness.md), [attack](../../labels/attack.md)


## [RepoSim: Evaluating Prompt Strategies for Code Completion via User Behavior Simulation](paper_33.md)
- **Authors**: Peng, Chao and Wu, Qinyun and Liu, Jiangchao and Liu, Jierui and Jiang, Bo and Xu, Mengqian and Wang, Yinghao and Liu, Xia and Yang, Ping
- **Abstract**: Large language models (LLMs) have revolutionized code completion tasks. IDE plugins such as MarsCode can generate code recommendations, saving developers significant time and effort. However, current evaluation methods for code completion are limited by their reliance on static code benchmarks, which do not consider human interactions and evolving repositories. This paper proposes RepoSim, a novel benchmark designed to evaluate code completion tasks by simulating the evolving process of reposito...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695299)
- **Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md)


## [Semantic Sleuth: Identifying Ponzi Contracts via Large Language Models](paper_11.md)
- **Authors**: Wu, Cong and Chen, Jing and Wang, Ziwei and Liang, Ruichao and Du, Ruiying
- **Abstract**: Smart contracts, self-executing agreements directly encoded in code, are fundamental to blockchain technology, especially in decentralized finance (DeFi) and Web3. However, the rise of Ponzi schemes in smart contracts poses significant risks, leading to substantial financial losses and eroding trust in blockchain systems. Existing detection methods, such as PonziGuard, depend on large amounts of labeled data and struggle to identify unseen Ponzi schemes, limiting their reliability and generaliza...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695055)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [Semantic-Enhanced Indirect Call Analysis with Large Language Models](paper_8.md)
- **Authors**: Cheng, Baijun and Zhang, Cen and Wang, Kailong and Shi, Ling and Liu, Yang and Wang, Haoyu and Guo, Yao and Li, Ding and Chen, Xiangqun
- **Abstract**: In contemporary software development, the widespread use of indirect calls to achieve dynamic features poses challenges in constructing precise control flow graphs (CFGs), which further impacts the performance of downstream static analysis tasks. To tackle this issue, various types of indirect call analyzers have been proposed. However, they do not fully leverage the semantic information of the program, limiting their effectiveness in real-world scenarios.To address these issues, this paper prop...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695016)
- **Labels**: [static analysis](../../labels/static_analysis.md), [fundamental analysis](../../labels/fundamental_analysis.md)


## [Semi-Supervised Code Translation Overcoming the Scarcity of Parallel Code Data](paper_24.md)
- **Authors**: Zhu, Ming and Karim, Mohimenul and Lourentzou, Ismini and Yao, Daphne
- **Abstract**: Neural code translation is the task of converting source code from one programming language to another. One of the main challenges is the scarcity of parallel code data, which hinders the ability of translation models to learn accurate cross-language alignments. In this paper, we introduce MIRACLE, a semi-supervised approach that improves code translation through synthesizing high-quality parallel code data and curriculum learning on code data with ascending alignment levels. MIRACLE leverages s...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695524)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [Sifting through the Chaff: On Utilizing Execution Feedback for Ranking the Generated Code Candidates](paper_4.md)
- **Authors**: Sun, Zhihong and Wan, Yao and Li, Jia and Zhang, Hongyu and Jin, Zhi and Li, Ge and Lyu, Chen
- **Abstract**: Large Language Models (LLMs), such as GPT-4, StarCoder, and Code Llama, are transforming the way developers approach programming by automatically generating code based on given contexts, such as natural language descriptions or incomplete surrounding code. Despite advancements, generating syntactically and semantically correct code remains challenging, especially for complex programming tasks. Existing approaches typically generate multiple candidate solutions using LLMs to increase the likeliho...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695000)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [Test-Driven Development and LLM-based Code Generation](paper_25.md)
- **Authors**: Mathews, Noble Saji and Nagappan, Meiyappan
- **Abstract**: Recent Large Language Models (LLMs) have demonstrated significant capabilities in generating code snippets directly from problem statements. This increasingly automated process mirrors traditional human-led software development, where code is often written in response to a requirement. Historically, Test-Driven Development (TDD) has proven its merit, requiring developers to write tests before the functional code, ensuring alignment with the initial problem statements. Applying TDD principles to ...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695527)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [Three Heads Are Better Than One: Suggesting Move Method Refactoring Opportunities with Inter-class Code Entity Dependency Enhanced Hybrid Hypergraph Neural Network](paper_15.md)
- **Authors**: Cui, Di and Wang, Jiaqi and Wang, Qiangqiang and Ji, Peng and Qiao, Minglang and Zhao, Yutong and Hu, Jingzhao and Wang, Luqiao and Li, Qingshan
- **Abstract**: Methods implemented in incorrect classes will cause excessive reliance on other classes than their own, known as a typical code smell symptom: feature envy, which makes it difficult to maintain increased coupling between classes. Addressing this issue, several Move Method refactoring tools have been proposed, employing a two-phase process: identifying misplaced methods to move and appropriate classes to receive, and implementing the mechanics of refactoring. These tools traditionally use hard-co...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695068)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [Towards Understanding the Effectiveness of Large Language Models on Directed Test Input Generation](paper_42.md)
- **Authors**: Jiang, Zongze and Wen, Ming and Cao, Jialun and Shi, Xuanhua and Jin, Hai
- **Abstract**: Automatic testing has garnered significant attention and success over the past few decades. Techniques such as unit testing and coverage-guided fuzzing have revealed numerous critical software bugs and vulnerabilities. However, a long-standing, formidable challenge for existing techniques is how to achieve higher testing coverage. Constraint-based techniques, such as symbolic execution and concolic testing, have been well-explored and integrated into the existing approaches. With the popularity ...
- **Link**: [Read Paper](https://dl.acm.org/doi/pdf/10.1145/3691620.3695513e)
- **Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md), [empirical study](../../labels/empirical_study.md)


## [Understanding Code Changes Practically with Small-Scale Language Models](paper_3.md)
- **Authors**: Li, Cong and Xu, Zhaogui and Di, Peng and Wang, Dongxia and Li, Zheng and Zheng, Qian
- **Abstract**: Recent studies indicate that traditional techniques for understanding code changes are not as effective as techniques that directly prompt language models (LMs). However, current LM-based techniques heavily rely on expensive, large LMs (LLMs) such as GPT-4 and Llama-13b, which are either commercial or prohibitively costly to deploy on a wide scale, thereby restricting their practical applicability. This paper explores the feasibility of deploying small LMs (SLMs) while maintaining comparable or ...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3694999)
- **Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [Understanding Developer-Analyzer Interactions in Code Reviews](paper_29.md)
- **Authors**: Schaef, Martin and Cirisci, Berk and Luo, Linghui and Mansur, Muhammad Numair and Tripp, Omer and Sanchez, Daniel and Zhou, Qiang and Zafar, Muhammad Bilal
- **Abstract**: Static code analyzers are now a common part of the codereview process. These automated tools integrate into the code review process by commenting on code changes and suggesting improvements, in the same way as human reviewers. The comments made by static analyzers often trigger a conversation between developers to align on if and how the issue should be fixed. Because developers rarely give feedback directly to the tool, understanding the sentiment and intent in the conversation triggered by the...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695257)
- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [code review](../../labels/code_review.md), [empirical study](../../labels/empirical_study.md)


## [WaDec: Decompiling WebAssembly Using Large Language Model](paper_9.md)
- **Authors**: She, Xinyu and Zhao, Yanjie and Wang, Haoyu
- **Abstract**: WebAssembly (abbreviated Wasm) has emerged as a cornerstone of web development, offering a compact binary format that allows high-performance applications to run at near-native speeds in web browsers. Despite its advantages, Wasm's binary nature presents significant challenges for developers and researchers, particularly regarding readability when debugging or analyzing web applications. Therefore, effective decompilation becomes crucial. Unfortunately, traditional decompilers often struggle wit...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695020)
- **Labels**: [code generation](../../labels/code_generation.md), [program decompilation](../../labels/program_decompilation.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md)


## [iSMELL: Assembling LLMs with Expert Toolsets for Code Smell Detection and Refactoring](paper_22.md)
- **Authors**: Wu, Di and Mu, Fangwen and Shi, Lin and Guo, Zhaoqiang and Liu, Kui and Zhuang, Weiguang and Zhong, Yuqi and Zhang, Li
- **Abstract**: Detecting and refactoring code smells is challenging, laborious, and sustaining. Although large language models have demonstrated potential in identifying various types of code smells, they also have limitations such as input-output token restrictions, difficulty in accessing repository-level knowledge, and performing dynamic source code analysis. Existing learning-based methods or commercial expert toolsets have advantages in handling complex smells. They can analyze project structures and cont...
- **Link**: [Read Paper](https://doi.org/10.1145/3691620.3695508)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
