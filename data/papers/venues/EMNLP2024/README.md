# EMNLP2024

Number of papers: 39

## [AMR-Evol: Adaptive Modular Response Evolution Elicits Better Knowledge Distillation for Large Language Models in Code Generation](paper_17.md)
- **Authors**: Luo, Ziyang and Li, Xin and Lin, Hongzhan and Ma, Jing and Bing, Lidong
- **Abstract**: The impressive performance of proprietary LLMs like GPT4 in code generation has led to a trend to replicate these capabilities in open-source models through knowledge distillation (e.g. Code Evol-Instruct). However, these efforts often neglect the crucial aspect of response quality, relying heavily on teacher models for direct response distillation. This paradigm, especially for complex instructions, can degrade the quality of synthesized data, compromising the knowledge distillation process. To...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.66)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [AutoDetect: Towards a Unified Framework for Automated Weakness Detection in Large Language Models](paper_8.md)
- **Authors**: Cheng, Jiale and Lu, Yida and Gu, Xiaotao and Ke, Pei and Liu, Xiao and Dong, Yuxiao and Wang, Hongning and Tang, Jie and Huang, Minlie
- **Abstract**: Although Large Language Models (LLMs) are becoming increasingly powerful, they still exhibit significant but subtle weaknesses, such as mistakes in instruction-following or coding tasks.As these unexpected errors could lead to severe consequences in practical deployments, it is crucial to investigate the limitations within LLMs systematically.Traditional benchmarking approaches cannot thoroughly pinpoint specific model deficiencies, while manual inspections are costly and not scalable. In this p...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.397)
- **Labels**: [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md), [empirical study](../../labels/empirical_study.md)


## [Can LLMs Reason in the Wild with Programs?](paper_11.md)
- **Authors**: Yang, Yuan and Xiong, Siheng and Payani, Ali and Shareghi, Ehsan and Fekri, Faramarz
- **Abstract**: Large Language Models (LLMs) have shown superior capability to solve reasoning problems with programs. While being a promising direction, most of such frameworks are trained and evaluated in settings with a prior knowledge of task requirements. However, as LLMs become more capable, it is necessary to assess their reasoning abilities in more realistic scenarios where many real-world problems are open-ended with ambiguous scope, and often require multiple formalisms to solve. To investigate this, ...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.573)
- **Labels**: [prompt strategy](../../labels/prompt_strategy.md), [reason with code](../../labels/reason_with_code.md)


## [CoCoST: Automatic Complex Code Generation with Online Searching and Correctness Testing](paper_34.md)
- **Authors**: He, Xinyi and Zou, Jiaru and Lin, Yun and Zhou, Mengyu and Han, Shi and Yuan, Zejian and Zhang, Dongmei
- **Abstract**: Large Language Models have revolutionized code generation ability by converting natural language descriptions into executable code. However, generating complex code within real-world scenarios remains challenging due to intricate structures, subtle bugs, understanding of advanced data types, and lack of supplementary contents. To address these challenges, we introduce the CoCoST framework, which enhances complex code generation by online searching for more information with planned queries and co...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.1082)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [benchmark](../../labels/benchmark.md)


## [Code Prompting Elicits Conditional Reasoning Abilities in Text+Code LLMs](paper_25.md)
- **Authors**: Puerto, Haritz and Tutek, Martin and Aditya, Somak and Zhu, Xiaodan and Gurevych, Iryna
- **Abstract**: Reasoning is a fundamental component of language understanding. Recent prompting techniques, such as chain of thought, have consistently improved LLMs’ performance on various reasoning tasks. Nevertheless, there is still little understanding of what triggers reasoning abilities in LLMs in the inference stage. In this paper, we investigate the effect of the input representation on the reasoning abilities of LLMs. We hypothesize that representing natural language tasks as code can enhance specific...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.629)
- **Labels**: [prompt strategy](../../labels/prompt_strategy.md), [reason with code](../../labels/reason_with_code.md)


## [CodeAgent: Autonomous Communicative Agents for Code Review](paper_26.md)
- **Authors**: Tang, Xunzhu and Kim, Kisub and Song, Yewei and Lothritz, Cedric and Li, Bei and Ezzini, Saad and Tian, Haoye and Klein, Jacques and Bissyandé, Tegawendé F.
- **Abstract**: Code review, which aims at ensuring the overall quality and reliability of software, is a cornerstone of software development. Unfortunately, while crucial, Code review is a labor-intensive process that the research community is looking to automate. Existing automated methods rely on single input-output generative models and thus generally struggle to emulate the collaborative nature of code review. This work introduces CodeAgent, a novel multi-agent Large Language Model (LLM) system for code re...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.632)
- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [code review](../../labels/code_review.md), [agent design](../../labels/agent_design.md)


## [CodeFort: Robust Training for Code Generation Models](paper_39.md)
- **Authors**: Zhang, Yuhao and Wang, Shiqi and Qian, Haifeng and Wang, Zijian and Shang, Mingyue and Liu, Linbo and Gouda, Sanjay Krishna and Ray, Baishakhi and Ramanathan, Murali Krishna and Ma, Xiaofei and others
- **Abstract**: Code generation models are not robust to small perturbations, which often lead to inconsistent and incorrect generations and significantly degrade the performance of these models. Improving the robustness of code generation models is crucial to better user experience when these models are deployed in real-world applications. However, existing efforts have not addressed this issue for code generation models. To fill this gap, we propose CodeFort, a framework to improve the robustness of code gene...
- **Link**: [Read Paper](https://arxiv.org/pdf/2405.01567)
- **Labels**: [code generation](../../labels/code_generation.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [code model](../../labels/code_model.md), [code model robustness](../../labels/code_model_robustness.md)


## [CodeIP: A Grammar-Guided Multi-Bit Watermark for Large Language Models of Code](paper_9.md)
- **Authors**: Guan, Batu and Wan, Yao and Bi, Zhangqian and Wang, Zheng and Zhang, Hongyu and Zhou, Pan and Sun, Lichao
- **Abstract**: Large Language Models (LLMs) have achieved remarkable progress in code generation. It now becomes crucial to identify whether the code is AI-generated and to determine the specific model used, particularly for purposes such as protecting Intellectual Property (IP) in industry and preventing cheating in programming exercises. To this end, several attempts have been made to insert watermarks into machine-generated code. However, existing approaches are limited to inserting only a single bit of inf...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.541)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md)


## [CodeJudge: Evaluating Code Generation with Large Language Models](paper_35.md)
- **Authors**: Tong, Weixi and Zhang, Tianyi
- **Abstract**: Large Language Models (LLMs) have shown promising performance in code generation. However, how to reliably evaluate code generated by LLMs remains an unresolved problem. This paper presents CodeJudge, a code evaluation framework that leverages LLMs to evaluate the semantic correctness of generated code without the need for test cases. We investigate different ways to guide the LLM in performing “slow thinking” to arrive at an in-depth and reliable evaluation. We experimented with four LLMs as ev...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.1118)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [Coffee-Gym: An Environment for Evaluating and Improving Natural Language Feedback on Erroneous Code](paper_38.md)
- **Authors**: Chae, Hyungjoo and Kwon, Taeyoon and Moon, Seungjun and Song, Yongho and Kang, Dongjin and Ong, Kai Tzu-iunn and Kwak, Beong-woo and Bae, Seonghyeon and Hwang, Seung-won and Yeo, Jinyoung
- **Abstract**: This paper presents Coffee-Gym, a comprehensive RL environment for training models that provide feedback on code editing. Coffee-Gym includes two major components: (1) Coffee, a dataset containing humans’ code edit traces for coding questions and human-written feedback for editing erroneous code; (2) CoffeeEval, a reward function that faithfully reflects the helpfulness of feedback by assessing the performance of the revised code in unit tests. With them, Coffee-Gym addresses the unavailability ...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.1254)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [benchmark](../../labels/benchmark.md)


## [DA-Code: Agent Data Science Code Generation Benchmark for Large Language Models](paper_28.md)
- **Authors**: Huang, Yiming and Luo, Jianwen and Yu, Yan and Zhang, Yitong and Lei, Fangyu and Wei, Yifan and He, Shizhu and Huang, Lifu and Liu, Xiao and Zhao, Jun and Liu, Kang
- **Abstract**: We introduce DA-Code, a code generation benchmark specifically designed to assess LLMs on agent-based data science tasks. This benchmark features three core elements: First, the tasks within DA-Code are inherently challenging, setting them apart from traditional code generation tasks and demanding advanced coding skills in grounding and planning. Second, examples in DA-Code are all based on real and diverse data, covering a wide range of complex data wrangling and analytics tasks. Third, to solv...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.748)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [benchmark](../../labels/benchmark.md)


## [Defending Large Language Models Against Jailbreak Attacks via Layer-specific Editing](paper_6.md)
- **Authors**: Zhao, Wei and Li, Zhe and Li, Yige and Zhang, Ye and Sun, Jun
- **Abstract**: Large language models (LLMs) are increasingly being adopted in a wide range of real-world applications. Despite their impressive performance, recent studies have shown that LLMs are vulnerable to deliberately crafted adversarial prompts even when aligned via Reinforcement Learning from Human Feedback or supervised fine-tuning. While existing defense methods focus on either detecting harmful prompts or reducing the likelihood of harmful responses through various means, defending LLMs against jail...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.293)
- **Labels**: [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md)


## [DocCGen: Document-based Controlled Code Generation](paper_33.md)
- **Authors**: Pimparkhede, Sameer and Kammakomati, Mehant and Tamilselvam, Srikanth G. and Kumar, Prince and Kumar, Ashok Pon and Bhattacharyya, Pushpak
- **Abstract**: Recent developments show that Large Language Models (LLMs) produce state-of-the-art performance on natural language (NL) to code generation for resource-rich general-purpose languages like C++, Java, and Python. However, their practical usage for structured domain-specific languages (DSLs) such as YAML, JSON is limited due to domain-specific schema, grammar, and customizations generally unseen by LLMs during pre-training. Efforts have been made to mitigate this challenge via in-context learning ...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.1040)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [ECCO: Can We Improve Model-Generated Code Efficiency Without Sacrificing Functional Correctness?](paper_31.md)
- **Authors**: Waghjale, Siddhant and Veerendranath, Vishruth and Wang, Zhiruo and Fried, Daniel
- **Abstract**: Although large language models (LLMs) have been largely successful in generating functionally correct programs, conditioning models to produce efficient solutions while ensuring correctness remains a challenge. Further, unreliability in benchmarking code efficiency is a hurdle across varying hardware specifications for popular interpreted languages such as Python. In this paper, we present ECCO, a reproducible benchmark for evaluating program efficiency via two paradigms: natural language (NL) b...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.859)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [EHRAgent: Code Empowers Large Language Models for Few-shot Complex Tabular Reasoning on Electronic Health Records](paper_36.md)
- **Authors**: Shi, Wenqi and Xu, Ran and Zhuang, Yuchen and Yu, Yue and Zhang, Jieyu and Wu, Hang and Zhu, Yuanda and Ho, Joyce C. and Yang, Carl and Wang, May Dongmei
- **Abstract**: Clinicians often rely on data engineers to retrieve complex patient information from electronic health record (EHR) systems, a process that is both inefficient and time-consuming. We propose EHRAgent, a large language model (LLM) agent empowered with accumulative domain knowledge and robust coding capability. EHRAgent enables autonomous code generation and execution to facilitate clinicians in directly interacting with EHRs using natural language. Specifically, we formulate a multi-tabular reaso...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.1245)
- **Labels**: [prompt strategy](../../labels/prompt_strategy.md), [reason with code](../../labels/reason_with_code.md)


## [Empowering Multi-step Reasoning across Languages via Program-Aided Language Models](paper_27.md)
- **Authors**: Ranaldi, Leonardo and Pucci, Giulia and Haddow, Barry and Birch, Alexandra
- **Abstract**: In-context learning methods are popular inference strategies where Large Language Models (LLMs) are elicited to solve a task using provided demonstrations without parameter updates. Among these approaches are the reasoning methods, best exemplified by Chain-of-Thought (CoT) and Program-Aided Language Models (PAL), which elicit LLMs to generate reasoning paths, thus promoting accuracy and attracting increasing attention. However, despite the success of these methods, the ability to deliver multi-...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.678)
- **Labels**: [prompt strategy](../../labels/prompt_strategy.md), [reason with code](../../labels/reason_with_code.md)


## [Enhancing Discourse Dependency Parsing with Sentence Dependency Parsing: A Unified Generative Method Based on Code Representation](paper_14.md)
- **Authors**: Shen, Zizhuo and Shao, Yanqiu and Li, Wei
- **Abstract**: Due to the high complexity of Discourse Dependency Parsing (DDP) tasks, their existing annotation resources are relatively scarce compared to other NLP tasks, and different DDP tasks also have significant differences in annotation schema. These issues have led to the dilemma of low resources for DDP tasks. Thanks to the powerful capabilities of Large Language Models (LLMs) in cross-task learning, we can use LLMs to model dependency parsing under different annotation schema in an unified manner, ...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.729)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [EvoR: Evolving Retrieval for Code Generation](paper_3.md)
- **Authors**: Su, Hongjin and Jiang, Shuyang and Lai, Yuhang and Wu, Haoyuan and Shi, Boao and Liu, Che and Liu, Qian and Yu, Tao
- **Abstract**: Recently the retrieval-augmented generation (RAG) has been successfully applied in code generation. However, existing pipelines for retrieval-augmented code generation (RACG) employ static knowledge bases with a single source, limiting the adaptation capabilities of Large Language Models (LLMs) to domains they have insufficient knowledge of. In this work, we develop a novel pipeline, EVOR, that employs the synchronous evolution of both queries and diverse knowledge bases. On two realistic settin...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.143)
- **Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md), [source code model](../../labels/source_code_model.md), [prompt strategy](../../labels/prompt_strategy.md), [retrieval-augmented generation](../../labels/retrieval-augmented_generation.md)


## [How Do Humans Write Code? Large Models Do It the Same Way Too](paper_20.md)
- **Authors**: Li, Long and He, Xuzheng and Wang, Haozhe and Wang, Linlin and He, Liang
- **Abstract**: Program-of-Thought (PoT) replaces natural language-based Chain-of-Thought (CoT) as the most popular method in Large Language Models (LLMs) mathematical reasoning tasks by utilizing external tool calls to circumvent computational errors. However, our evaluation of the GPT-4 and Llama series reveals that using PoT introduces more reasoning errors, such as incorrect formulas or flawed logic, compared to CoT. To address this issue, we propose Human-Think Language (HTL), which leverages a suite of st...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.267)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [empirical study](../../labels/empirical_study.md)


## [How Do Your Code LLMs perform? Empowering Code Instruction Tuning with Really Good Data](paper_30.md)
- **Authors**: Wang, Yejie and He, Keqing and Fu, Dayuan and GongQue, Zhuoma and Xu, Heyang and Chen, Yanxu and Wang, Zhexu and Fu, Yujia and Dong, Guanting and Diao, Muxi and Wang, Jingang and Zhang, Mengdi and Cai, Xunliang and Xu, Weiran
- **Abstract**: Recently, there has been a growing interest in studying how to construct better code instruction tuning data. However, we observe Code models trained with these datasets exhibit high performance on HumanEval but perform worse on other benchmarks such as LiveCodeBench. Upon further investigation, we find that many datasets suffer from severe data leakage. After cleaning up most of the leaked data, some well-known high-quality datasets perform poorly. This discovery reveals a new challenge: identi...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.777)
- **Labels**: [code generation](../../labels/code_generation.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [Impeding LLM-assisted Cheating in Introductory Programming Assignments via Adversarial Perturbation](paper_16.md)
- **Authors**: Salim, Saiful Islam and Yang, Rubin Yuchan and Cooper, Alexander and Ray, Suryashree and Debray, Saumya and Rahaman, Sazzadur
- **Abstract**: While Large language model (LLM)-based programming assistants such as CoPilot and ChatGPT can help improve the productivity of professional software developers, they can also facilitate cheating in introductory computer programming courses. Assuming instructors have limited control over the industrial-strength models, this paper investigates the baseline performance of 5 widely used LLMs on a collection of introductory programming problems, examines adversarial perturbations to degrade their per...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.27)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [empirical study](../../labels/empirical_study.md)


## [Instruct, Not Assist: LLM-based Multi-Turn Planning and Hierarchical Questioning for Socratic Code Debugging](paper_10.md)
- **Authors**: Kargupta, Priyanka and Agarwal, Ishika and Tur, Dilek Hakkani and Han, Jiawei
- **Abstract**: Socratic questioning is an effective teaching strategy, encouraging critical thinking and problem-solving. The conversational capabilities of large language models (LLMs) show great potential for providing scalable, real-time student guidance. However, current LLMs often give away solutions directly, making them ineffective instructors. We tackle this issue in the code debugging domain with TreeInstruct, an Instructor agent guided by a novel state space-based planning algorithm. TreeInstruct ask...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.553)
- **Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md), [agent design](../../labels/agent_design.md), [planning](../../labels/planning.md)


## [Introducing Compiler Semantics into Large Language Models as Programming Language Translators: A Case Study of C to x86 Assembly](paper_2.md)
- **Authors**: Zhang, Shuoming and Zhao, Jiacheng and Xia, Chunwei and Wang, Zheng and Chen, Yunji and Cui, Huimin
- **Abstract**: Compilers are complex software containing millions of lines of code, taking years to develop. This paper investigates to what extent Large Language Models (LLMs) can replace hand-crafted compilers in translating high-level programming languages to machine instructions, using C to x86 assembly as a case study. We identify two challenges of using LLMs for code translation and introduce two novel data pre-processing techniques to address the challenges: numerical value conversion and training data ...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.55)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [LLM4Decompile: Decompiling Binary Code with Large Language Models](paper_18.md)
- **Authors**: Tan, Hanzhuo and Luo, Qi and Li, Jing and Zhang, Yuqun
- **Abstract**: Decompilation aims to convert binary code to high-level source code, but traditional tools like Ghidra often produce results that are difficult to read and execute. Motivated by the advancements in Large Language Models (LLMs), we propose LLM4Decompile, the first and largest open-source LLM series (1.3B to 33B) trained to decompile binary code. We optimize the LLM training process and introduce the LLM4Decompile-End models to decompile binary directly. The resulting models significantly outperfo...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.203)
- **Labels**: [static analysis](../../labels/static_analysis.md), [program decompilation](../../labels/program_decompilation.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md)


## [Language Models as Compilers: Simulating Pseudocode Execution Improves Algorithmic Reasoning in Language Models](paper_37.md)
- **Authors**: Chae, Hyungjoo and Kim, Yeonghyeon and Kim, Seungone and Ong, Kai Tzu-iunn and Kwak, Beong-woo and Kim, Moohyeon and Kim, Sunghwan and Kwon, Taeyoon and Chung, Jiwan and Yu, Youngjae and Yeo, Jinyoung
- **Abstract**: Algorithmic reasoning tasks that involve complex logical patterns, such as completing Dyck language, pose challenges for large language models (LLMs), despite their recent success. Prior work has used LLMs to generate programming language and applied external compilers for such tasks. Yet, when on the fly, it is hard to generate an executable code with the correct logic for the solution. Even so, code for one instance cannot be reused for others, although they might require the same logic to sol...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.1253)
- **Labels**: [prompt strategy](../../labels/prompt_strategy.md), [reason with code](../../labels/reason_with_code.md)


## [Language-to-Code Translation with a Single Labeled Example](paper_23.md)
- **Authors**: Bostrom, Kaj and Jhamtani, Harsh and Fang, Hao and Thomson, Sam and Shin, Richard and Xia, Patrick and Van Durme, Benjamin and Eisner, Jason and Andreas, Jacob
- **Abstract**: Tools for translating natural language into code promise natural, open-ended interaction with databases, web APIs, and other software systems. However, this promise is complicated by the diversity and continual development of these systems, each with its own interface and distinct set of features. Building a new language-to-code translator, even starting with a large language model (LM), typically requires annotating a large set of natural language commands with their associated programs. In thi...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.462)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [benchmark](../../labels/benchmark.md)


## [Leveraging Context-Aware Prompting for Commit Message Generation](paper_29.md)
- **Authors**: Jiang, Zhihua and Chen, Jianwei and Rao, Dongning and Ye, Guanghui
- **Abstract**: Writing comprehensive commit messages is tedious yet important, because these messages describe changes of code, such as fixing bugs or adding new features. However, most existing methods focus on either only the changed lines or nearest context lines, without considering the effectiveness of selecting useful contexts. On the other hand, it is possible that introducing excessive contexts can lead to noise. To this end, we propose a code model COMMIT (Context-aware prOMpting based comMIt-message ...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.749)
- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [commit message generation](../../labels/commit_message_generation.md)


## [On Leakage of Code Generation Evaluation Datasets](paper_15.md)
- **Authors**: Matton, Alexandre and Sherborne, Tom and Aumiller, Dennis and Tommasone, Elena and Alizadeh, Milad and He, Jingyi and Ma, Raymond and Voisin, Maxime and Gilsenan-McMahon, Ellen and Gallé, Matthias
- **Abstract**: In this paper, we consider contamination by code generation test sets, in particular in their use in modern large language models.We discuss three possible sources of such contamination and show findings supporting each of them: (i) direct data leakage, (ii) indirect data leakage through the use of synthetic data and (iii) overfitting to evaluation sets during model selection.To address this, we release Less Basic Python Problems (LBPP): an uncontaminated new benchmark of 161 prompts with their ...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.772)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [benchmark](../../labels/benchmark.md)


## [PTD-SQL: Partitioning and Targeted Drilling with LLMs in Text-to-SQL](paper_19.md)
- **Authors**: Luo, Ruilin and Wang, Liyuan and Lin, Binghuai and Lin, Zicheng and Yang, Yujiu
- **Abstract**: Large Language Models (LLMs) have emerged as powerful tools for Text-to-SQL tasks, exhibiting remarkable reasoning capabilities. Different from tasks such as math word problem and commonsense reasoning, SQL solutions have a relatively fixed pattern. This facilitates the investigation of whether LLMs can benefit from categorical thinking, mirroring how humans acquire knowledge through inductive reasoning based on comparable examples. In this study, we propose that employing query group partitioni...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.221)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [empirical study](../../labels/empirical_study.md)


## [PythonSaga: Redefining the Benchmark to Evaluate Code Generating LLMs](paper_22.md)
- **Authors**: Yadav, Ankit and Beniwal, Himanshu and Singh, Mayank
- **Abstract**: Driven by the surge in code generation using large language models (LLMs), numerous benchmarks have emerged to evaluate these LLMs capabilities. We conducted a large-scale human evaluation of *HumanEval* and *MBPP*, two popular benchmarks for Python code generation, analyzing their diversity and difficulty. Our findings unveil a critical bias towards a limited set of programming concepts, neglecting most of the other concepts entirely. Furthermore, we uncover a worrying prevalence of easy tasks ...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.996)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [benchmark](../../labels/benchmark.md)


## [Re-Reading Improves Reasoning in Large Language Models](paper_32.md)
- **Authors**: Xu, Xiaohan and Tao, Chongyang and Shen, Tao and Xu, Can and Xu, Hongbo and Long, Guodong and Lou, Jian-Guang and Ma, Shuai
- **Abstract**: To enhance the reasoning capabilities of off-the-shelf Large Language Models (LLMs), we introduce a simple, yet general and effective prompting method, RE2, i.e., Re-Reading the question as input. Unlike most thought-eliciting prompting methods, such as Chain-of-Thought (CoT), which aim to elicit the reasoning process in the output, RE2 shifts the focus to the input by processing questions twice, thereby enhancing the understanding process. Consequently, RE2 demonstrates strong generality and co...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.871)
- **Labels**: [prompt strategy](../../labels/prompt_strategy.md)


## [RealVul: Can We Detect Vulnerabilities in Web Applications with LLM?](paper_24.md)
- **Authors**: Cao, Di and Liao, Yong and Shang, Xiuwei
- **Abstract**: The latest advancements in large language models (LLMs) have sparked interest in their potential for software vulnerability detection. However, there is currently a lack of research specifically focused on vulnerabilities in the PHP language, and challenges in data sampling and processing persist, hindering the model’s ability to effectively capture the characteristics of specific vulnerabilities. In this paper, we present RealVul, the first LLM-based framework designed for PHP vulnerability det...
- **Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.472)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [Rethinking Code Refinement: Learning to Judge Code Efficiency](paper_12.md)
- **Authors**: Seo, Minju and Baek, Jinheon and Hwang, Sung Ju
- **Abstract**: Large Language Models (LLMs) have demonstrated impressive capabilities in understanding and generating codes. Due to these capabilities, many recent methods are proposed to automatically refine the codes with LLMs. However, we should rethink that the refined codes (from LLMs and even humans) are not always more efficient than their original versions. On the other hand, running two different versions of codes and comparing them every time is not ideal and time-consuming. Therefore, in this work, ...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.645)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [Revisiting the Impact of Pursuing Modularity for Code Generation](paper_13.md)
- **Authors**: Kang, Deokyeong and Seo, KiJung and Kim, Taeuk
- **Abstract**: Modular programming, which aims to construct the final program by integrating smaller, independent building blocks, has been regarded as a desirable practice in software development. However, with the rise of recent code generation agents built upon large language models (LLMs), a question emerges: is this traditional practice equally effective for these new tools? In this work, we assess the impact of modularity in code generation by introducing a novel metric for its quantitative measurement. ...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.676)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [empirical study](../../labels/empirical_study.md)


## [Sanitizing Large Language Models in Bug Detection with Data-Flow](paper_4.md)
- **Authors**: Wang, Chengpeng and Zhang, Wuqi and Su, Zian and Xu, Xiangzhe and Zhang, Xiangyu
- **Abstract**: Large language models (LLMs) show potential in code reasoning tasks, facilitating the customization of detecting bugs in software development. However, the hallucination effect can significantly compromise the reliability of bug reports. This work formulates a new schema of bug detection and presents a novel sanitization technique that detects false positives for hallucination mitigation. Our key idea is to enforce LLMs to emit data-flow paths in few-shot chain-of-thought prompting and validate ...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.217)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [data-flow analysis](../../labels/data-flow_analysis.md)


## [Self-Constructed Context Decompilation with Fined-grained Alignment Enhancement](paper_7.md)
- **Authors**: Feng, Yunlong and Teng, Dechuan and Xu, Yang and Mu, Honglin and Xu, Xiao and Qin, Libo and Zhu, Qingfu and Che, Wanxiang
- **Abstract**: Decompilation transforms compiled code back into a high-level programming language for analysis when source code is unavailable. Previous work has primarily focused on enhancing decompilation performance by increasing the scale of model parameters or training data for pre-training. Based on the characteristics of the decompilation task, we propose two methods: (1) Without fine-tuning, the Self-Constructed Context Decompilation (sc²dec) method recompiles the LLM’s decompilation results to constru...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.385)
- **Labels**: [static analysis](../../labels/static_analysis.md), [program decompilation](../../labels/program_decompilation.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md), [benchmark](../../labels/benchmark.md)


## [Socratic Human Feedback (SoHF): Expert Steering Strategies for LLM Code Generation](paper_21.md)
- **Authors**: Chidambaram, Subramanian and Li, Li Erran and Bai, Min and Li, Xiaopeng and Lin, Kaixiang and Zhou, Xiong and Williams, Alex C.
- **Abstract**: Large Language Models (LLMs) are increasingly used for generating code solutions, empowered by features like self-debugging and self-reflection. However, LLMs often struggle with complex programming problems without human guidance. This paper investigates the strategies employed by expert programmers to steer code-generating LLMs toward successful outcomes. Through a study involving experts using natural language to guide GPT-4, Gemini Ultra, and, Claude 3.5 Sonnet on highly difficult programmin...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.908)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [empirical study](../../labels/empirical_study.md)


## [Stanceformer: Target-Aware Transformer for Stance Detection](paper_5.md)
- **Authors**: Garg, Krishna and Caragea, Cornelia
- **Abstract**: The task of Stance Detection involves discerning the stance expressed in a text towards a specific subject or target. Prior works have relied on existing transformer models that lack the capability to prioritize targets effectively. Consequently, these models yield similar performance regardless of whether we utilize or disregard target information, undermining the task’s significance. To address this challenge, we introduce Stanceformer, a target-aware transformer model that incorporates enhanc...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.286)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)


## [TransLLaMa: LLM-based Simultaneous Translation System](paper_1.md)
- **Authors**: Koshkin, Roman and Sudoh, Katsuhito and Nakamura, Satoshi
- **Abstract**: Decoder-only large language models (LLMs) have recently demonstrated impressive capabilities in text generation and reasoning. Nonetheless, they have limited applications in simultaneous machine translation (SiMT), currently dominated by encoder-decoder transformers. This study demonstrates that, after fine-tuning on a small dataset comprising causally aligned source and target sentence pairs, a pre-trained open-source LLM can control input segmentation directly by generating a special “wait” to...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.27)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md), [empirical study](../../labels/empirical_study.md)
