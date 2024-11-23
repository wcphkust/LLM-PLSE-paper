# arXiv2023

Number of papers: 15

## [A survey on hallucination in large language models: Principles, taxonomy, challenges, and open questions](paper_12.md)
- **Authors**: Huang, Lei and Yu, Weijiang and Ma, Weitao and Zhong, Weihong and Feng, Zhangyin and Wang, Haotian and Chen, Qianglong and Peng, Weihua and Feng, Xiaocheng and Qin, Bing and others
- **Abstract**: The emergence of large language models (LLMs) has marked a significant breakthrough in natural language processing (NLP), leading to remarkable advancements in text understanding and generation. Nevertheless, alongside these strides, LLMs exhibit a critical tendency to produce hallucinations, resulting in content that is inconsistent with real-world facts or user inputs. This phenomenon poses substantial challenges to their practical deployment and raises concerns over the reliability of LLMs in...
- **Link**: [Read Paper](https://arxiv.org/pdf/2406.19508)
[hallucination in reasoning](../../labels/hallucination_in_reasoning.md), [survey](../../labels/survey.md)

## [Cognitive architectures for language agents](paper_14.md)
- **Authors**: Sumers, Theodore R and Yao, Shunyu and Narasimhan, Karthik and Griffiths, Thomas L
- **Abstract**: The prominent large language models (LLMs) of today differ from past language models not only in size, but also in the fact that they are trained on a combination of natural language and formal language (code). As a medium between humans and computers, code translates high-level goals into executable steps, featuring standard syntax, logical consistency, abstraction, and modularity. In this survey, we present an overview of the various benefits of integrating code into LLMs' training data. Speci...
- **Link**: [Read Paper](https://arxiv.org/pdf/2309.02427.pdf)
[agent design](../../labels/agent_design.md), [survey](../../labels/survey.md)

## [Cumulative reasoning with large language models](paper_13.md)
- **Authors**: Zhang, Yifan and Yang, Jingqin and Yuan, Yang and Yao, Andrew Chi-Chih
- **Abstract**: While language models are powerful and versatile, they often fail to address highly complex problems. This is because solving complex problems requires deliberate thinking, which has been only minimally guided during training. In this paper, we propose a new method called Cumulative Reasoning (CR), which employs language models in a cumulative and iterative manner to emulate human thought processes. By decomposing tasks into smaller components, \ournameb streamlines the problem-solving process, ...
- **Link**: [Read Paper](https://arxiv.org/pdf/2308.04371.pdf)
[hallucination in reasoning](../../labels/hallucination_in_reasoning.md), [prompt strategy](../../labels/prompt_strategy.md)

## [Do Language Models Learn Semantics of Code? {A} Case Study in Vulnerability Detection](paper_5.md)
- **Authors**: Benjamin Steenhoek and Md Mahbubur Rahman and Shaila Sharmin and Wei Le
- **Abstract**: Recently, pretrained language models have shown state-of-the-art performance on the vulnerability detection task. These models are pretrained on a large corpus of source code, then fine-tuned on a smaller supervised vulnerability dataset. Due to the different training objectives and the performance of the models, it is interesting to consider whether the models have learned the semantics of code relevant to vulnerability detection, namely bug semantics, and if so, how the alignment to bug semant...
- **Link**: [Read Paper](https://doi.org/10.48550/arXiv.2311.04109)
[static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)

## [Do you still need a manual smart contract audit?](paper_8.md)
- **Authors**: David, Isaac and Zhou, Liyi and Qin, Kaihua and Song, Dawn and Cavallaro, Lorenzo and Gervais, Arthur
- **Abstract**: We investigate the feasibility of employing large language models (LLMs) for conducting the security audit of smart contracts, a traditionally time-consuming and costly process. Our research focuses on the optimization of prompt engineering for enhanced security analysis, and we evaluate the performance and accuracy of LLMs using a benchmark dataset comprising 52 Decentralized Finance (DeFi) smart contracts that have previously been compromised.     Our findings reveal that, when applied to vuln...
- **Link**: [Read Paper](https://arxiv.org/pdf/2306.12338.pdf)
[static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)

## [Finding inductive loop invariants using large language models](paper_10.md)
- **Authors**: Kamath, Adharsh and Senthilnathan, Aditya and Chakraborty, Saikat and Deligiannis, Pantazis and Lahiri, Shuvendu K and Lal, Akash and Rastogi, Aseem and Roy, Subhajit and Sharma, Rahul
- **Abstract**:     Loop invariants are fundamental to reasoning about programs with loops. They establish properties about a given loop's behavior. When they additionally are inductive, they become useful for the task of formal verification that seeks to establish strong mathematical guarantees about program's runtime behavior. The inductiveness ensures that the invariants can be checked locally without consulting the entire program, thus are indispensable artifacts in a formal proof of correctness. Finding in...
- **Link**: [Read Paper](https://arxiv.org/abs/2311.07948)
[static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md), [invariant generation](../../labels/invariant_generation.md)

## [Harnessing the power of llm to support binary taint analysis](paper_7.md)
- **Authors**: Liu, Puzhuo and Sun, Chengnian and Zheng, Yaowen and Feng, Xuan and Qin, Chuan and Wang, Yuncheng and Li, Zhi and Sun, Limin
- **Abstract**: This paper proposes LATTE, the first static binary taint analysis that is powered by a large language model (LLM). LATTE is superior to the state of the art (e.g., Emtaint, Arbiter, Karonte) in three aspects. First, LATTE is fully automated while prior static binary taint analyzers need rely on human expertise to manually customize taint propagation rules and vulnerability inspection rules. Second, LATTE is significantly effective in vulnerability detection, demonstrated by our comprehensive eva...
- **Link**: [Read Paper](https://arxiv.org/abs/2310.08275)
[static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)

## [How Far Have We Gone in Vulnerability Detection Using Large Language Models](paper_3.md)
- **Authors**: Zeyu Gao and Hao Wang and Yuchen Zhou and Wenyu Zhu and Chao Zhang
- **Abstract**: As software becomes increasingly complex and prone to vulnerabilities, automated vulnerability detection is critically important, yet challenging. Given the significant successes of large language models (LLMs) in various tasks, there is growing anticipation of their efficacy in vulnerability detection. However, a quantitative understanding of their potential in vulnerability detection is still missing. To bridge this gap, we introduce a comprehensive vulnerability benchmark VulBench. This bench...
- **Link**: [Read Paper](https://doi.org/10.48550/arXiv.2311.12420)
[static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [benchmark](../../labels/benchmark.md)

## [Impact of large language models on generating software specifications](paper_11.md)
- **Authors**: Xie, Danning and Yoo, Byungwoo and Jiang, Nan and Kim, Mijung and Tan, Lin and Zhang, Xiangyu and Lee, Judy S
- **Abstract**: Software specifications are essential for ensuring the reliability of software systems. Existing specification extraction approaches, however, suffer from limited generalizability and require manual efforts. The recent emergence of Large Language Models (LLMs), which have been successfully applied to numerous software engineering tasks, offers a promising avenue for automating this process. In this paper, we conduct the first empirical study to evaluate the capabilities of LLMs for generating so...
- **Link**: [Read Paper](https://arxiv.org/pdf/2306.03324.pdf)
[static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md)

## [LLMs: Understanding Code Syntax and Semantics for Code Analysis](paper_1.md)
- **Authors**: Ma, Wei and Liu, Shangqing and Lin, Zhihao and Wang, Wenhan and Hu, Qiang and Liu, Ye and Zhang, Cen and Nie, Liming and Li, Li and Liu, Yang
- **Abstract**: Large language models~(LLMs) demonstrate significant potential to revolutionize software engineering (SE) by exhibiting outstanding performance in SE tasks such as code and document generation. However, the high reliability and risk control requirements in software engineering raise concerns about the lack of interpretability of LLMs. To address this concern, we conducted a study to evaluate the capabilities of LLMs and their limitations for code analysis in SE. We break down the abilities neede...
- **Link**: [Read Paper](https://arxiv.org/pdf/2410.15631)
[static analysis](../../labels/static_analysis.md), [fundamental analysis](../../labels/fundamental_analysis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md), [empirical study](../../labels/empirical_study.md)

## [Large language model-powered smart contract vulnerability detection: New perspectives](paper_9.md)
- **Authors**: Hu, Sihao and Huang, Tiansheng and {\.I}lhan, Fatih and Tekin, Selim Furkan and Liu, Ling
- **Abstract**: This paper provides a systematic analysis of the opportunities, challenges, and potential solutions of harnessing Large Language Models (LLMs) such as GPT-4 to dig out vulnerabilities within smart contracts based on our ongoing research. For the task of smart contract vulnerability detection, achieving practical usability hinges on identifying as many true vulnerabilities as possible while minimizing the number of false positives. Nonetheless, our empirical study reveals contradictory yet intere...
- **Link**: [Read Paper](https://arxiv.org/pdf/2310.01152.pdf)
[static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)

## [Lmpa: Improving decompilation by synergy of large language model and program analysis](paper_2.md)
- **Authors**: Xu, Xiangzhe and Zhang, Zhuo and Feng, Shiwei and Ye, Yapeng and Su, Zian and Jiang, Nan and Cheng, Siyuan and Tan, Lin and Zhang, Xiangyu
- **Abstract**: Decompilation aims to recover the source code form of a binary executable. It has many applications in security and software engineering such as malware analysis, vulnerability detection and code reuse. A prominent challenge in decompilation is to recover variable names. We propose a novel method that leverages the synergy of large language model (LLM) and program analysis. Language models encode rich multi-modal knowledge, but its limited input size prevents providing sufficient global context ...
- **Link**: [Read Paper](https://arxiv.org/pdf/2306.02546v1)
[code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md)

## [SkipAnalyzer: An Embodied Agent for Code Analysis with Large Language Models](paper_6.md)
- **Authors**: Mohammad Mahdi Mohajer and Reem Aleithan and Nima Shiri Harzevili and Moshi Wei and Alvine Boaye Belle and Hung Viet Pham and Song Wang
- **Abstract**: We introduce SkipAnalyzer, a large language model (LLM)-powered tool for static code analysis. SkipAnalyzer has three components: 1) an LLM-based static bug detector that scans source code and reports specific types of bugs, 2) an LLM-based false-positive filter that can identify false-positive bugs in the results of static bug detectors (e.g., the result of step 1) to improve detection accuracy, and 3) an LLM-based patch generator that can generate patches for the detected bugs above. As a proo...
- **Link**: [Read Paper](https://doi.org/10.48550/arXiv.2310.18532)
[static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [agent design](../../labels/agent_design.md)

## [The rise and potential of large language model based agents: A survey](paper_15.md)
- **Authors**: Xi, Zhiheng and Chen, Wenxiang and Guo, Xin and He, Wei and Ding, Yiwen and Hong, Boyang and Zhang, Ming and Wang, Junzhe and Jin, Senjie and Zhou, Enyu and others
- **Abstract**: For a long time, humanity has pursued artificial intelligence (AI) equivalent to or surpassing the human level, with AI agents considered a promising vehicle for this pursuit. AI agents are artificial entities that sense their environment, make decisions, and take actions. Many efforts have been made to develop intelligent agents, but they mainly focus on advancement in algorithms or training strategies to enhance specific capabilities or performance on particular tasks. Actually, what the commu...
- **Link**: [Read Paper](https://arxiv.org/abs/2309.07864)
[survey](../../labels/survey.md), [agent design](../../labels/agent_design.md)

## [Understanding the Effectiveness of Large Language Models in Detecting Security Vulnerabilities](paper_4.md)
- **Authors**: Avishree Khare and Saikat Dutta and Ziyang Li and Alaia Solko{-}Breslin and Rajeev Alur and Mayur Naik
- **Abstract**: While automated vulnerability detection techniques have made promising progress in detecting security vulnerabilities, their scalability and applicability remain challenging. The remarkable performance of Large Language Models (LLMs), such as GPT-4 and CodeLlama, on code-related tasks has prompted recent works to explore if LLMs can be used to detect vulnerabilities. In this paper, we perform a more comprehensive study by concurrently examining a higher number of datasets, languages and LLMs, an...
- **Link**: [Read Paper](https://doi.org/10.48550/arXiv.2311.16169)
[static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)