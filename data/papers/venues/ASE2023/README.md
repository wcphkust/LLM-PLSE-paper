# ASE2023

Number of papers: 18

- **Labels**: [code generation](../../labels/code_generation.md), [source code model](../../labels/source_code_model.md)

- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [empirical study](../../labels/empirical_study.md)

- **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)

- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [prompt strategy](../../labels/prompt_strategy.md)

- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [empirical study](../../labels/empirical_study.md)

- **Labels**: [program testing](../../labels/program_testing.md), [differential testing](../../labels/differential_testing.md)

- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [code review](../../labels/code_review.md)

- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)

- **Labels**: [general coding task](../../labels/general_coding_task.md)

- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)

- **Labels**: [static analysis](../../labels/static_analysis.md), [type inference](../../labels/type_inference.md)

- **Labels**: [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

- **Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md), [empirical study](../../labels/empirical_study.md)

- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)

- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)

- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [documentation generation](../../labels/documentation_generation.md)

- **Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

## [A Closer Look at Different Difficulty Levels Code Generation Abilities of ChatGPT](paper_6.md)
- **Authors**: Yan, Dapeng and Gao, Zhipeng and Liu, Zhiming
- **Abstract**: Code generation aims to generate source code implementing human requirements illustrated with natural language specifications. With the rapid development of intelligent software engineering, automated code generation has become a hot research topic in both artificial intelligence and software engineering, and researchers have made significant achievements on code generation. More recently, large language models (LLMs) have demonstrated outstanding performance on code generation tasks, such as Ch...
- **Link**: [Read Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10298505)


## [An Empirical Study on Fine-Tuning Large Language Models of Code for Automated Program Repair](paper_2.md)
- **Authors**: Huang, Kai and Meng, Xiangxin and Zhang, Jian and Liu, Yang and Wang, Wenjie and Li, Shuhao and Zhang, Yuqing
- **Abstract**: The advent of large language models (LLMs) has opened up new opportunities for automated program repair (APR). In particular, some recent studies have explored how to leverage large language models of code (LLMCs) for program repair tasks and show promising results. However, most of them adopt the zero/few-shot learning paradigm for APR, which directly use LLMCs to generate the possibly correct code given its surrounding context. Though effective, the repair capabilities of LLMCs based on the fi...
- **Link**: [Read Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10298532)


## [Better Patching Using LLM Prompting, via Self-Consistency](paper_5.md)
- **Authors**: Ahmed, Toufique and Devanbu, Premkumar
- **Abstract**: Large Language models (LLMs) can be induced to solve non-trivial problems with “few-shot” prompts including illustrative problem-solution examples. Now if the few-shots also include “chain of thought” ($\mathcal{C}oT$) explanations, which are of the form problem-explanation-solution, LLMs will generate a “explained” solution, and perform even better. Recently an exciting, substantially better technique, self-consistency [1] ($\mathcal{S}-C$) has emerged, based on the intuition that there are man...
- **Link**: [Read Paper](https://arxiv.org/pdf/2306.00108)


## [CAT-LM training language models on aligned code and tests](paper_13.md)
- **Authors**: Rao, Nikitha and Jain, Kush and Alon, Uri and Le Goues, Claire and Hellendoorn, Vincent J
- **Abstract**: Testing is an integral but often neglected part of the software development process. Classical test generation tools such as EvoSuite generate behavioral test suites by optimizing for coverage, but tend to produce tests that are hard to understand. Language models trained on code can generate code that is highly similar to that written by humans, but current models are trained to generate each file separately, as is standard practice in natural language processing, and thus fail to consider the ...
- **Link**: [Read Paper](https://arxiv.org/pdf/2310.01602)


## [COMEX: A Tool for Generating Customized Source Code Representations](paper_1.md)
- **Authors**: Das, Debeshee and Mathews, Noble Saji and Mathai, Alex and Tamilselvam, Srikanth and Sedamaki, Kranthi and Chimalakonda, Sridhar and Kumar, Atul
- **Abstract**: Learning effective representations of source code is critical for any Machine Learning for Software Engineering (ML4SE) system. Inspired by natural language processing, large language models (LLMs) like Codex and CodeGen treat code as generic sequences of text and are trained on huge corpora of code data, achieving state of the art performance on several software engineering (SE) tasks. However, valid source code, unlike natural language, follows a strict structure and pattern governed by the un...
- **Link**: [Read Paper](https://arxiv.org/pdf/2307.04693)


## [Cell2Doc: ML Pipeline for Generating Documentation in Computational Notebooks](paper_17.md)
- **Authors**: Mondal, Tamal and Barnett, Scott and Lal, Akash and Vedurada, Jyothi
- **Abstract**: Computational notebooks have become the go-to way for solving data-science problems. While they are designed to combine code and documentation, prior work shows that documentation is largely ignored by the developers because of the manual effort. Automated documentation generation can help, but existing techniques fail to capture algorithmic details and developers often end up editing the generated text to provide more explanation and sub-steps. This paper proposes a novel machine-learning pipel...
- **Link**: [Read Paper](https://dl.acm.org/doi/pdf/10.1109/ASE56229.2023.00200)


## [Domain Adaptive Code Completion via Language Models and Decoupled Domain Databases](paper_18.md)
- **Authors**: Tang, Ze and Ge, Jidong and Liu, Shangqing and Zhu, Tingwei and Xu, Tongtong and Huang, Liguo and Luo, Bin
- **Abstract**: Large Language Models (LLMs) have demonstrated remarkable performance in code completion. However, due to the lack of domain-specific knowledge, they may not be optimal in completing code that requires intensive domain knowledge for example completing the library names. Although there are several works that have confirmed the effectiveness of fine-tuning techniques to adapt language models for code completion in specific domains. They are limited by the need for constant fine-tuning of the model...
- **Link**: [Read Paper](https://arxiv.org/pdf/2308.09313)


## [From Misuse to Mastery: Enhancing Code Generation with Knowledge-Driven AI Chaining](paper_11.md)
- **Authors**: Ren, Xiaoxue and Ye, Xinyuan and Zhao, Dehai and Xing, Zhenchang and Yang, Xiaohu
- **Abstract**: Large Language Models (LLMs) have shown promising results in automatic code generation by improving coding efficiency to a certain extent. However, generating high-quality and reliable code remains a formidable task because of LLMs' lack of good programming practice, especially in exception handling. In this paper, we first conduct an empirical study and summarize three crucial challenges of LLMs in exception handling, i.e., incomplete exception handling, incorrect exception handling and abuse o...
- **Link**: [Read Paper](https://arxiv.org/pdf/2309.15606)


## [Generative Type Inference for Python](paper_12.md)
- **Authors**: Peng, Yun and Wang, Chaozheng and Wang, Wenxuan and Gao, Cuiyun and Lyu, Michael R.
- **Abstract**: Python is a popular dynamic programming language, evidenced by its ranking as the second most commonly used language on GitHub. However, its dynamic type system can lead to potential type errors, leading researchers to explore automatic type inference approaches for Python programs. Existing type inference approaches can be generally grouped into three categories, i.e., rule-based, supervised, and cloze- style approaches. The rule-based type inference approaches can ensure the accuracy of predic...
- **Link**: [Read Paper](https://arxiv.org/pdf/2307.09163)


## [Improving Code Extraction from Coding Screencasts Using a Code-Aware Encoder-Decoder Model](paper_4.md)
- **Authors**: Malkadi, Abdulkarim and Tayeb, Ahmad and Haiduc, Sonia
- **Abstract**: Accurate automatic code extraction from tutorial videos is crucial for software developers seeking to reuse the code contained in these videos. Current methods using optical character recognition (OCR) often yield inaccurate results due to code complexity and variations in screencast formats. To address this issue, we introduce CodeT5-OCRfix, an approach that leverages the pre-trained code-aware large language model CodeT5 to enhance code extraction accuracy by post-processing OCRed code. We fir...
- **Link**: [Read Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10298433)


## [Nuances are the Key: Unlocking ChatGPT to Find Failure-Inducing Tests with Differential Prompting](paper_7.md)
- **Authors**: Li, Tsz-On and Zong, Wenxi and Wang, Yibo and Tian, Haoye and Wang, Ying and Cheung, Shing-Chi and Kramer, Jeff
- **Abstract**: Automated detection of software failures is an important but challenging software engineering task. It involves finding in a vast search space the failure-inducing test cases that contain an input triggering the software fault and an oracle asserting the incorrect execution. We are motivated to study how far this outstanding challenge can be solved by recent advances in large language models (LLMs) such as ChatGPT. However, our study reveals that ChatGPT has a relatively low success rate (28.8%)...
- **Link**: [Read Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10298538)


## [On the Evaluation of Neural Code Translation: Taxonomy and Benchmark](paper_14.md)
- **Authors**: Jiao, Mingsheng and Yu, Tingrui and Li, Xuan and Qiu, Guanjie and Gu, Xiaodong and Shen, Beijun
- **Abstract**: In recent years, neural code translation has gained increasing attention. While most of the research focuses on improving model architectures and training processes, we notice that the evaluation process and benchmark for code translation models are severely limited: they primarily treat source code as natural languages and provide a holistic accuracy score while disregarding the full spectrum of model capabilities across different translation types and complexity. In this paper, we present a co...
- **Link**: [Read Paper](https://arxiv.org/pdf/2308.08961)


## [SCPatcher: Mining Crowd Security Discussions to Enrich Secure Coding Practices](paper_8.md)
- **Authors**: Jiang, Ziyou and Shi, Lin and Yang, Guowei and Wang, Qing
- **Abstract**: Secure coding practices (SCPs) have been proposed to guide software developers to write code securely to prevent potential security vulnerabilities. Yet, they are typically one-sentence principles without detailed specifications, e.g., “Properly free allocated memory upon the completion of functions and at all exit points.”, which makes them difficult to follow in practice, especially for software developers who are not yet experienced in secure programming. To address this problem, this paper p...
- **Link**: [Read Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10298463)


## [SMT Solver Validation Empowered by Large Pre-Trained Language Models](paper_3.md)
- **Authors**: Sun, Maolin and Yang, Yibiao and Wang, Yang and Wen, Ming and Jia, Haoxiang and Zhou, Yuming
- **Abstract**: SMT solvers are utilized to check the satisfiability of logic formulas and have been applied in various crucial domains, including software verification, test case generation, and program synthesis. However, bugs hidden in SMT solvers can lead to severe consequences, causing erroneous results in these domains. Therefore, ensuring the reliability and robustness of SMT solvers is of critical importance. Despite several testing approaches proposed for SMT solvers, generating effective test formulas...
- **Link**: [Read Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10298442)


## [The Plastic Surgery Hypothesis in the Era of Large Language Models](paper_9.md)
- **Authors**: Xia, Chunqiu Steven and Ding, Yifeng and Zhang, Lingming
- **Abstract**: Automated Program Repair (APR) aspires to automatically generate patches for an input buggy program. Traditional APR tools typically focus on specific bug types and fixes through the use of templates, heuristics, and formal specifications. However, these techniques are limited in terms of the bug types and patch variety they can produce. As such, researchers have designed various learning-based APR tools with recent work focused on directly using Large Language Models (LLMs) for APR. While LLM-b...
- **Link**: [Read Paper](https://dl.acm.org/doi/pdf/10.1109/ASE56229.2023.00047)


## [Twin Graph-Based Anomaly Detection via Attentive Multi-Modal Learning for Microservice System](paper_16.md)
- **Authors**: Huang, Jun and Yang, Yang and Yu, Hang and Li, Jianguo and Zheng, Xiao
- **Abstract**: Microservice architecture has sprung up over recent years for managing enterprise applications, due to its ability to independently deploy and scale services. Despite its benefits, ensuring the reliability and safety of a microservice system remains highly challenging. Existing anomaly detection algorithms based on a single data modality (i.e., metrics, logs, or traces) fail to fully account for the complex correlations and interactions between different modalities, leading to false negatives an...
- **Link**: [Read Paper](https://arxiv.org/pdf/2310.04701)


## [VALAR: Streamlining Alarm Ranking in Static Analysis with Value-Flow Assisted Active Learning](paper_15.md)
- **Authors**: Liu, Pengcheng and Lu, Yifei and Yang, Wenhua and Pan, Minxue
- **Abstract**: Static analyzers play a critical role in program defects and security vulnerabilities detection. Despite their importance, the widespread adoption of static analysis techniques in industrial development faces numerous obstacles, among which the high rate of false alarms constitutes a significant one. To address this issue, we propose a novel approach called Valar, which performs alarm ranking for advanced value-flow analysis using the active learning technique. Active learning algorithms minimiz...
- **Link**: [Read Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10298558)


## [What Makes Good In-Context Demonstrations for Code Intelligence Tasks with LLMs?](paper_10.md)
- **Authors**: Gao, Shuzheng and Wen, Xin-Cheng and Gao, Cuiyun and Wang, Wenxuan and Zhang, Hongyu and Lyu, Michael R.
- **Abstract**: Pre-trained models of source code have gained widespread popularity in many code intelligence tasks. Recently, with the scaling of the model and corpus size, large language models have shown the ability of in-context learning (ICL). ICL employs task instructions and a few examples as demonstrations, and then inputs the demonstrations to the language models for making predictions. This new learning paradigm is training-free and has shown impressive performance in various natural language processi...
- **Link**: [Read Paper](https://arxiv.org/pdf/2304.07575)
