# FSE2023

Number of papers: 13

## [Copiloting the Copilots: Fusing Large Language Models with Completion Engines for Automated Program Repair](paper_1.md)
- **Authors**: Wei, Yuxiang and Xia, Chunqiu Steven and Zhang, Lingming
- **Abstract**: During Automated Program Repair (APR), it can be challenging&nbsp;to synthesize correct patches for real-world systems in general-purpose programming languages. Recent Large Language Models&nbsp;(LLMs) have been shown to be helpful “copilots” in assisting developers with various coding tasks, and have also been directly&nbsp;applied for patch synthesis. However, most LLMs treat programs as&nbsp;se...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616271)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)

## [Multilingual Code Co-evolution using Large Language Models](paper_2.md)
- **Authors**: Zhang, Jiyang and Nie, Pengyu and Li, Junyi Jessy and Gligoric, Milos
- **Abstract**: Many software projects implement APIs and algorithms in multiple programming languages. Maintaining such projects is tiresome, as developers have to ensure that any change (e.g., a bug fix or a new feature) is being propagated, timely and without errors, to implementations in other programming languages. In the world of ever-changing software, using rule-based translation tools (i.e., transpilers)...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616350)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

## [Baldur: Whole-Proof Generation and Repair with Large Language Models](paper_3.md)
- **Authors**: First, Emily and Rabe, Markus N. and Ringer, Talia and Brun, Yuriy
- **Abstract**: Formally verifying software is a highly desirable but labor-intensive task.  Recent work has developed methods to automate formal verification using proof assistants, such as Coq and Isabelle/HOL, e.g., by training a model to predict one proof step at a time and using that model to search through the space of possible proofs.  This paper introduces a new method to automate formal verification: We ...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616243)
- **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)

## [Grace: Language Models Meet Code Edits](paper_4.md)
- **Authors**: Gupta, Priyanshu and Khare, Avishree and Bajpai, Yasharth and Chakraborty, Saikat and Gulwani, Sumit and Kanade, Aditya and Radhakrishna, Arjun and Soares, Gustavo and Tiwari, Ashish
- **Abstract**: Developers spend a significant amount of time in editing code for a variety of reasons such as bug fixing or adding new features. Designing effective methods to predict code edits has been an active yet challenging area of research due to the diversity of code edits and the difficulty of capturing the developer intent. In this work, we address these challenges by endowing pre-trained large languag...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616253)
- **Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

## [InferFix: End-to-End Program Repair with LLMs](paper_5.md)
- **Authors**: Jin, Matthew and Shahriar, Syed and Tufano, Michele and Shi, Xin and Lu, Shuai and Sundaresan, Neel and Svyatkovskiy, Alexey
- **Abstract**: Software development life cycle is profoundly influenced by bugs; their introduction, identification, and eventual resolution account for a significant portion of software development cost. This has motivated software engineering researchers and practitioners to propose different approaches for automating the identification and repair of software defects. Large Language Models (LLMs) have been ada...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3613892)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)

## [Assisting Static Analysis with Large Language Models: A ChatGPT Experiment](paper_6.md)
- **Authors**: Li, Haonan and Hao, Yu and Zhai, Yizhuo and Qian, Zhiyun
- **Abstract**: Recent advances of Large Language Models (LLMs), e.g., ChatGPT, exhibited strong capabilities of comprehending and responding to questions across a variety of domains. Surprisingly, ChatGPT even possesses a strong understanding of program code. In this paper, we investigate where and how LLMs can assist static analysis by asking appropriate questions. In particular, we target a specific bug-findin...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3613078)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)

## [LLM-Based Code Generation Method for Golang Compiler Testing](paper_7.md)
- **Authors**: Gu, Qiuhan
- **Abstract**: Modern optimizing compilers are among the most complex software systems humans build. One way to identify subtle compiler bugs is fuzzing. Both the quantity and the quality of testcases are crucial to the performance of fuzzing. Traditional testcase-generation methods, such as Csmith and YARPGen, have been proven successful at discovering compiler bugs. However, such generated testcases have limit...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3617850)
- **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [compiler testing](../../labels/compiler_testing.md)

## [Towards Greener Yet Powerful Code Generation via Quantization: An Empirical Study](paper_8.md)
- **Authors**: Wei, Xiaokai and Gonugondla, Sujan Kumar and Wang, Shiqi and Ahmad, Wasi and Ray, Baishakhi and Qian, Haifeng and Li, Xiaopeng and Kumar, Varun and Wang, Zijian and Tian, Yuchen and Sun, Qing and Athiwaratkun, Ben and Shang, Mingyue and Ramanathan, Murali Krishna and Bhatia, Parminder and Xiang, Bing
- **Abstract**: ML-powered code generation aims to assist developers to write code in a more productive manner by intelligently generating code blocks based on natural language prompts. Recently, large pretrained deep learning models have pushed the boundary of code generation and achieved impressive performance. However, the huge number of model parameters poses a significant challenge to their adoption in a typ...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616302)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [empirical study](../../labels/empirical_study.md)

## [Self-Supervised Query Reformulation for Code Search](paper_9.md)
- **Authors**: Mao, Yuetian and Wan, Chengcheng and Jiang, Yuze and Gu, Xiaodong
- **Abstract**: Automatic query reformulation is a widely utilized technology for enriching user requirements and enhancing the outcomes of code search. It can be conceptualized as a machine translation task, wherein the objective is to rephrase a given query into a more comprehensive alternative. While showing promising results, training such a model typically requires a large parallel corpus of query pairs (i.e...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616306)
- **Labels**: [static analysis](../../labels/static_analysis.md), [code search](../../labels/code_search.md)

## [Log Parsing with Generalization Ability under New Log Types](paper_10.md)
- **Authors**: Yu, Siyu and Wu, Yifan and Li, Zhijing and He, Pinjia and Chen, Ningjiang and Liu, Changjian
- **Abstract**: Log parsing, which converts semi-structured logs into structured logs, is the first step for automated log analysis.  Existing parsers are still unsatisfactory in real-world systems due to new log types in new-coming logs.  In practice, available logs collected during system runtime often do not contain all the possible log types of a system because log types related to infrequently activated syst...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616355)
- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [system log analysis](../../labels/system_log_analysis.md)

## [An Extensive Study on Adversarial Attack against Pre-trained Models of Code](paper_11.md)
- **Authors**: Du, Xiaohu and Wen, Ming and Wei, Zichao and Wang, Shangwen and Jin, Hai
- **Abstract**: Transformer-based pre-trained models of code (PTMC) have been widely utilized and have achieved state-of-the-art performance in many mission-critical applications. However, they can be vulnerable to adversarial attacks through identifier substitution or coding style transformation, which can significantly degrade accuracy and may further incur security concerns. Although several approaches have be...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616356)
- **Labels**: [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md), [attack](../../labels/attack.md), [empirical study](../../labels/empirical_study.md)

## [The EarlyBIRD Catches the Bug: On Exploiting Early Layers of Encoder Models for More Efficient Code Classification](paper_12.md)
- **Authors**: Grishina, Anastasiia and Hort, Max and Moonen, Leon
- **Abstract**: The use of modern Natural Language Processing (NLP) techniques has shown to be beneficial for software engineering tasks, such as vulnerability detection and type inference. However, training deep NLP models requires significant computational resources. This paper explores techniques that aim at achieving the best usage of resources and available information in these models.  We propose a generic ...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616304)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md), [empirical study](../../labels/empirical_study.md)

## [Evaluating Transfer Learning for Simplifying GitHub READMEs](paper_13.md)
- **Authors**: Gao, Haoyu and Treude, Christoph and Zahedi, Mansooreh
- **Abstract**: Software documentation captures detailed knowledge about a software product, e.g., code, technologies, and design. It plays an important role in the coordination of development teams and in conveying ideas to various stakeholders. However, software documentation can be hard to comprehend if it is written with jargon and complicated sentence structure. In this study, we explored the potential of te...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616291)
- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [documentation generation](../../labels/documentation_generation.md)

