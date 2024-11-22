# FSE2023

Number of papers: 13

## [Copiloting the Copilots: Fusing Large Language Models with Completion Engines for Automated Program Repair](paper_1.md)
- **Authors**: Wei, Yuxiang and Xia, Chunqiu Steven and Zhang, Lingming
- **Abstract**: During Automated Program Repair (APR), it can be challenging&nbsp;to synthesize correct patches for real-world systems in general-purpose programming languages. Recent Large Language Models&nbsp;(LLMs) have been shown to be helpful “copilots” in assisting developers with various coding tasks, and ha...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616271)
- **Labels**: code generation, program repair

## [Multilingual Code Co-evolution using Large Language Models](paper_2.md)
- **Authors**: Zhang, Jiyang and Nie, Pengyu and Li, Junyi Jessy and Gligoric, Milos
- **Abstract**: Many software projects implement APIs and algorithms in multiple programming languages. Maintaining such projects is tiresome, as developers have to ensure that any change (e.g., a bug fix or a new feature) is being propagated, timely and without errors, to implementations in other programming langu...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616350)
- **Labels**: code generation, program transformation, code model, code model training, source code model

## [Baldur: Whole-Proof Generation and Repair with Large Language Models](paper_3.md)
- **Authors**: First, Emily and Rabe, Markus N. and Ringer, Talia and Brun, Yuriy
- **Abstract**: Formally verifying software is a highly desirable but labor-intensive task.  Recent work has developed methods to automate formal verification using proof assistants, such as Coq and Isabelle/HOL, e.g., by training a model to predict one proof step at a time and using that model to search through th...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616243)
- **Labels**: static analysis, program verification

## [Grace: Language Models Meet Code Edits](paper_4.md)
- **Authors**: Gupta, Priyanshu and Khare, Avishree and Bajpai, Yasharth and Chakraborty, Saikat and Gulwani, Sumit and Kanade, Aditya and Radhakrishna, Arjun and Soares, Gustavo and Tiwari, Ashish
- **Abstract**: Developers spend a significant amount of time in editing code for a variety of reasons such as bug fixing or adding new features. Designing effective methods to predict code edits has been an active yet challenging area of research due to the diversity of code edits and the difficulty of capturing t...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616253)
- **Labels**: code generation, code completion, code model, code model training, source code model

## [InferFix: End-to-End Program Repair with LLMs](paper_5.md)
- **Authors**: Jin, Matthew and Shahriar, Syed and Tufano, Michele and Shi, Xin and Lu, Shuai and Sundaresan, Neel and Svyatkovskiy, Alexey
- **Abstract**: Software development life cycle is profoundly influenced by bugs; their introduction, identification, and eventual resolution account for a significant portion of software development cost. This has motivated software engineering researchers and practitioners to propose different approaches for auto...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3613892)
- **Labels**: code generation, program repair

## [Assisting Static Analysis with Large Language Models: A ChatGPT Experiment](paper_6.md)
- **Authors**: Li, Haonan and Hao, Yu and Zhai, Yizhuo and Qian, Zhiyun
- **Abstract**: Recent advances of Large Language Models (LLMs), e.g., ChatGPT, exhibited strong capabilities of comprehending and responding to questions across a variety of domains. Surprisingly, ChatGPT even possesses a strong understanding of program code. In this paper, we investigate where and how LLMs can as...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3613078)
- **Labels**: static analysis, bug detection

## [LLM-Based Code Generation Method for Golang Compiler Testing](paper_7.md)
- **Authors**: Gu, Qiuhan
- **Abstract**: Modern optimizing compilers are among the most complex software systems humans build. One way to identify subtle compiler bugs is fuzzing. Both the quantity and the quality of testcases are crucial to the performance of fuzzing. Traditional testcase-generation methods, such as Csmith and YARPGen, ha...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3617850)
- **Labels**: program testing, fuzzing, compiler testing

## [Towards Greener Yet Powerful Code Generation via Quantization: An Empirical Study](paper_8.md)
- **Authors**: Wei, Xiaokai and Gonugondla, Sujan Kumar and Wang, Shiqi and Ahmad, Wasi and Ray, Baishakhi and Qian, Haifeng and Li, Xiaopeng and Kumar, Varun and Wang, Zijian and Tian, Yuchen and Sun, Qing and Athiwaratkun, Ben and Shang, Mingyue and Ramanathan, Murali Krishna and Bhatia, Parminder and Xiang, Bing
- **Abstract**: ML-powered code generation aims to assist developers to write code in a more productive manner by intelligently generating code blocks based on natural language prompts. Recently, large pretrained deep learning models have pushed the boundary of code generation and achieved impressive performance. H...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616302)
- **Labels**: code generation, program synthesis, empirical study

## [Self-Supervised Query Reformulation for Code Search](paper_9.md)
- **Authors**: Mao, Yuetian and Wan, Chengcheng and Jiang, Yuze and Gu, Xiaodong
- **Abstract**: Automatic query reformulation is a widely utilized technology for enriching user requirements and enhancing the outcomes of code search. It can be conceptualized as a machine translation task, wherein the objective is to rephrase a given query into a more comprehensive alternative. While showing pro...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616306)
- **Labels**: static analysis, code search

## [Log Parsing with Generalization Ability under New Log Types](paper_10.md)
- **Authors**: Yu, Siyu and Wu, Yifan and Li, Zhijing and He, Pinjia and Chen, Ningjiang and Liu, Changjian
- **Abstract**: Log parsing, which converts semi-structured logs into structured logs, is the first step for automated log analysis.  Existing parsers are still unsatisfactory in real-world systems due to new log types in new-coming logs.  In practice, available logs collected during system runtime often do not con...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616355)
- **Labels**: software maintenance and deployment, system log analysis

## [An Extensive Study on Adversarial Attack against Pre-trained Models of Code](paper_11.md)
- **Authors**: Du, Xiaohu and Wen, Ming and Wei, Zichao and Wang, Shangwen and Jin, Hai
- **Abstract**: Transformer-based pre-trained models of code (PTMC) have been widely utilized and have achieved state-of-the-art performance in many mission-critical applications. However, they can be vulnerable to adversarial attacks through identifier substitution or coding style transformation, which can signifi...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616356)
- **Labels**: code model, code model security, attack, empirical study

## [The EarlyBIRD Catches the Bug: On Exploiting Early Layers of Encoder Models for More Efficient Code Classification](paper_12.md)
- **Authors**: Grishina, Anastasiia and Hort, Max and Moonen, Leon
- **Abstract**: The use of modern Natural Language Processing (NLP) techniques has shown to be beneficial for software engineering tasks, such as vulnerability detection and type inference. However, training deep NLP models requires significant computational resources. This paper explores techniques that aim at ach...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616304)
- **Labels**: static analysis, bug detection, code model, code model training, source code model, empirical study

## [Evaluating Transfer Learning for Simplifying GitHub READMEs](paper_13.md)
- **Authors**: Gao, Haoyu and Treude, Christoph and Zahedi, Mansooreh
- **Abstract**: Software documentation captures detailed knowledge about a software product, e.g., code, technologies, and design. It plays an important role in the coordination of development teams and in conveying ideas to various stakeholders. However, software documentation can be hard to comprehend if it is wr...
- **Link**: [Read Paper](https://doi.org/10.1145/3611643.3616291)
- **Labels**: software maintenance and deployment, documentation generation

