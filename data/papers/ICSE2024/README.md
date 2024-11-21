# ICSE2024

Number of papers: 32

## [UniLog: Automatic Logging via LLM and In-Context Learning](paper_1.md)
- **Authors**: Xu, Junjielong and Cui, Ziang and Zhao, Yuan and Zhang, Xu and He, Shilin and He, Pinjia and Li, Liqun and Kang, Yu and Lin, Qingwei and Dang, Yingnong and Rajmohan, Saravan and Zhang, Dongmei
- **Abstract**: Logging, which aims to determine the position of logging statements, the verbosity levels, and the log messages, is a crucial process for software reliability enhancement. In recent years, numerous automatic logging tools have been designed to assist developers in one of the logging tasks (e.g., pro...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3623326)
- **Labels**: software maintenance and deployment, system log analysis

## [Dataflow Analysis-Inspired Deep Learning for Efficient Vulnerability Detection](paper_2.md)
- **Authors**: Steenhoek, Benjamin and Gao, Hongyang and Le, Wei
- **Abstract**: Deep learning-based vulnerability detection has shown great performance and, in some studies, outperformed static analysis tools. However, the highest-performing approaches use token-based transformer models, which are not the most efficient to capture code semantics required for vulnerability detec...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3623345)
- **Labels**: static analysis, bug detection, code model, training, source code model

## [Large Language Models for Test-Free Fault Localization](paper_3.md)
- **Authors**: Yang, Aidan Z. H. and Le Goues, Claire and Martins, Ruben and Hellendoorn, Vincent
- **Abstract**: Fault Localization (FL) aims to automatically localize buggy lines of code, a key first step in many manual and automatic debugging tasks. Previous FL techniques assume the provision of input tests, and often require extensive program analysis, program instrumentation, or data preprocessing. Prior w...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3623342)
- **Labels**: program testing, debugging, code model, training, source code model

## [Large Language Models are Few-Shot Summarizers: Multi-Intent Comment Generation via In-Context Learning](paper_4.md)
- **Authors**: Geng, Mingyang and Wang, Shangwen and Dong, Dezun and Wang, Haotian and Li, Ge and Jin, Zhi and Mao, Xiaoguang and Liao, Xiangke
- **Abstract**: Code comment generation aims at generating natural language descriptions for a code snippet to facilitate developers' program comprehension activities. Despite being studied for a long time, a bottleneck for existing approaches is that given a code snippet, they can only generate one comment while d...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3608134)
- **Labels**: software maintenance and deployment, commit message generation

## [Large Language Models are Edge-Case Generators: Crafting Unusual Programs for Fuzzing Deep Learning Libraries](paper_5.md)
- **Authors**: Deng, Yinlin and Xia, Chunqiu Steven and Yang, Chenyuan and Zhang, Shizhuo Dylan and Yang, Shujing and Zhang, Lingming
- **Abstract**: Bugs in Deep Learning (DL) libraries may affect almost all downstream DL applications, and it is crucial to ensure the quality of such systems. It is challenging to generate valid input programs for fuzzing DL libraries, since the input programs need to satisfy both the syntax/semantics of the suppo...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3623343)
- **Labels**: program testing, fuzzing

## [On Extracting Specialized Code Abilities from Large Language Models: A Feasibility Study](paper_6.md)
- **Authors**: Li, Zongjie and Wang, Chaozheng and Ma, Pingchuan and Liu, Chaowei and Wang, Shuai and Wu, Daoyuan and Gao, Cuiyun and Liu, Yang
- **Abstract**: Recent advances in large language models (LLMs) significantly boost their usage in software engineering. However, training a well-performing LLM demands a substantial workforce for data collection and annotation. Moreover, training datasets may be proprietary or partially open, and the process often...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639091)
- **Labels**: code generation, program synthesis

## [When Neural Code Completion Models Size up the Situation: Attaining Cheaper and Faster Completion through Dynamic Model Inference](paper_7.md)
- **Authors**: Sun, Zhensu and Du, Xiaoning and Song, Fu and Wang, Shangwen and Li, Li
- **Abstract**: Leveraging recent advancements in large language models, modern neural code completion models have demonstrated the capability to generate highly accurate code suggestions. However, their massive size poses challenges in terms of computational costs and environmental impact, hindering their widespre...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639120)
- **Labels**: code generation, code completion, empirical study

## [Traces of Memorisation in Large Language Models for Code](paper_8.md)
- **Authors**: Al-Kaswan, Ali and Izadi, Maliheh and van Deursen, Arie
- **Abstract**: Large language models have gained significant popularity because of their ability to generate human-like text and potential applications in various fields, such as Software Engineering. Large language models for code are commonly trained on large unsanitised corpora of source code scraped from the i...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639133)
- **Labels**: code model, security, attack, benchmark

## [Evaluating Large Language Models in Class-Level Code Generation](paper_9.md)
- **Authors**: Du, Xueying and Liu, Mingwei and Wang, Kaixin and Wang, Hanlin and Liu, Junwei and Chen, Yixuan and Feng, Jiayi and Sha, Chaofeng and Peng, Xin and Lou, Yiling
- **Abstract**: Recently, many large language models (LLMs) have been proposed, showing advanced proficiency in code generation. Meanwhile, many efforts have been dedicated to evaluating LLMs on code generation benchmarks such as HumanEval. Although being very helpful for comparing different LLMs, existing evaluati...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639219)
- **Labels**: code generation, benchmark

## [Lost in Translation: A Study of Bugs Introduced by Large Language Models while Translating Code](paper_10.md)
- **Authors**: Pan, Rangeet and Ibrahimzada, Ali Reza and Krishna, Rahul and Sankar, Divya and Wassi, Lambert Pouguem and Merler, Michele and Sobolev, Boris and Pavuluri, Raju and Sinha, Saurabh and Jabbarvand, Reyhaneh
- **Abstract**: Code translation aims to convert source code from one programming language (PL) to another. Given the promising abilities of large language models (LLMs) in code synthesis, researchers are exploring their potential to automate code translation. The prerequisite for advancing the state of LLM-based c...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639226)
- **Labels**: code generation, program transformation, empirical study

## [Rust-lancet: Automated Ownership-Rule-Violation Fixing with Behavior Preservation](paper_11.md)
- **Authors**: Yang, Wenzhang and Song, Linhai and Xue, Yinxing
- **Abstract**: As a relatively new programming language, Rust is designed to provide both memory safety and runtime performance. To achieve this goal, Rust conducts rigorous static checks against its safety rules during compilation, effectively eliminating memory safety issues that plague C/C++ programs. Although ...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639103)
- **Labels**: code generation, program transformation

## [PyTy: Repairing Static Type Errors in Python](paper_12.md)
- **Authors**: Chow, Yiu Wai and Di Grazia, Luca and Pradel, Michael
- **Abstract**: Gradual typing enables developers to annotate types of their own choosing, offering a flexible middle ground between no type annotations and a fully statically typed language. As more and more code bases get type-annotated, static type checkers detect an increasingly large number of type errors. Unf...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639184)
- **Labels**: code generation, program repair, static analysis, type inference

## [Programming Assistant for Exception Handling with CodeBERT](paper_13.md)
- **Authors**: Cai, Yuchen and Yadavally, Aashish and Mishra, Abhishek and Montejo, Genesis and Nguyen, Tien
- **Abstract**: With practical code reuse, the code fragments from developers' forums often migrate to applications. Owing to the incomplete nature of such fragments, they often lack the details on exception handling. The adaptation for exception handling to the codebase is not trivial as developers must learn and ...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639188)
- **Labels**: code generation, program repair, empirical study

## [Using an LLM to Help With Code Understanding](paper_14.md)
- **Authors**: Nam, Daye and Macvean, Andrew and Hellendoorn, Vincent and Vasilescu, Bogdan and Myers, Brad
- **Abstract**: Understanding code is challenging, especially when working in new and complex development environments. Code comments and documentation can help, but are typically scarce or hard to navigate. Large language models (LLMs) are revolutionizing the process of writing code. Can they do the same for helpi...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639187)
- **Labels**: software maintenance and deployment

## [Fuzz4All: Universal Fuzzing with Large Language Models](paper_15.md)
- **Authors**: Xia, Chunqiu Steven and Paltenghi, Matteo and Le Tian, Jia and Pradel, Michael and Zhang, Lingming
- **Abstract**: Fuzzing has achieved tremendous success in discovering bugs and vulnerabilities in various software systems. Systems under test (SUTs) that take in programming or formal language as inputs, e.g., compilers, runtime engines, constraint solvers, and software libraries with accessible APIs, are especia...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639121)
- **Labels**: program testing, fuzzing

## [Sedar: Obtaining High-Quality Seeds for DBMS Fuzzing via Cross-DBMS SQL Transfer](paper_16.md)
- **Authors**: Fu, Jingzhou and Liang, Jie and Wu, Zhiyong and Jiang, Yu
- **Abstract**: Effective DBMS fuzzing relies on high-quality initial seeds, which serve as the starting point for mutation. These initial seeds should incorporate various DBMS features to explore the state space thoroughly. While built-in test cases are typically used as initial seeds, many DBMSs lack comprehensiv...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639210)
- **Labels**: program testing, fuzzing, DBMS testing

## [GPTScan: Detecting Logic Vulnerabilities in Smart Contracts by Combining GPT with Program Analysis](paper_17.md)
- **Authors**: Sun, Yuqiang and Wu, Daoyuan and Xue, Yue and Liu, Han and Wang, Haijun and Xu, Zhengzi and Xie, Xiaofei and Liu, Yang
- **Abstract**: Smart contracts are prone to various vulnerabilities, leading to substantial financial losses over time. Current analysis tools mainly target vulnerabilities with fixed control- or data-flow patterns, such as re-entrancy and integer overflow. However, a recent study on Web3 security bugs revealed th...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639117)
- **Labels**: static analysis, bug detection

## [Where is it? Tracing the Vulnerability-relevant Files from Vulnerability Reports](paper_18.md)
- **Authors**: Sun, Jiamou and Chen, Jieshan and Xing, Zhenchang and Lu, Qinghua and Xu, Xiwei and Zhu, Liming
- **Abstract**: With the widely usage of open-source software, supply-chain-based vulnerability attacks, including SolarWind and Log4Shell, have posed significant risks to software security. Currently, people rely on vulnerability advisory databases or commercial software bill of materials (SBOM) to defend against ...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639202)
- **Labels**: static analysis, bug detection

## [Automatic Semantic Augmentation of Language Model Prompts (for Code Summarization)](paper_19.md)
- **Authors**: Ahmed, Toufique and Pai, Kunal Suresh and Devanbu, Premkumar and Barr, Earl
- **Abstract**: Large Language Models (LLM) are a new class of computation engines, "programmed" via prompt engineering. Researchers are still learning how to best "program" these LLMs to help developers. We start with the intuition that developers tend to consciously and unconsciously collect semantics facts, from...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639183)
- **Labels**: static analysis, code summarization, prompt strategy, RAG

## [Which Syntactic Capabilities Are Statistically Learned by Masked Language Models for Code?](paper_20.md)
- **Authors**: Velasco, Alejandro and Palacio, David N and Rodriguez-Cardenas, Daniel and Poshyvanyk, Denys
- **Abstract**: This paper discusses the limitations of evaluating Masked Language Models (MLMs) in code completion tasks. We highlight that relying on accuracy-based measurements may lead to an overestimation of models' capabilities by neglecting the syntax rules of programming languages. To address these issues, ...
- **Link**: [Read Paper](No Link Available)
- **Labels**: static analysis, fundamental analysis, empirical study

## [Fair: Flow type-aware pre-training of compiler intermediate representations](paper_21.md)
- **Authors**: Niu, Changan and Li, Chuanyi and Ng, Vincent and Lo, David and Luo, Bin
- **Abstract**: While the majority of existing pre-trained models from code learn source code features such as code tokens and abstract syntax trees, there are some other works that focus on learning from compiler intermediate representations (IRs). Existing IR-based models typically utilize IR features such as ins...
- **Link**: [Read Paper](No Link Available)
- **Labels**: general coding task, code model, training, IR code model

## [Gptscan: Detecting logic vulnerabilities in smart contracts by combining gpt with program analysis](paper_22.md)
- **Authors**: Sun, Yuqiang and Wu, Daoyuan and Xue, Yue and Liu, Han and Wang, Haijun and Xu, Zhengzi and Xie, Xiaofei and Liu, Yang
- **Abstract**: Smart contracts are prone to various vulnerabilities, leading to substantial financial losses over time. Current analysis tools mainly target vulnerabilities with fixed control- or data-flow patterns, such as re-entrancy and integer overflow. However, a recent study on Web3 security bugs revealed th...
- **Link**: [Read Paper](No Link Available)
- **Labels**: static analysis, bug detection

## [EGFE: End-to-end Grouping of Fragmented Elements in UI Designs with Multimodal Learning](paper_23.md)
- **Authors**: Chen, Liuqing and Chen, Yunnong and Xiao, Shuhong and Song, Yaxuan and Sun, Lingyun and Zhen, Yankun and Zhou, Tingting and Chang, Yanfang
- **Abstract**: When translating UI design prototypes to code in industry, automatically generating code from design prototypes can expedite the development of applications and GUI iterations. However, in design prototypes without strict design specifications, UI components may be composed of fragmented elements. G...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3623313)
- **Labels**: code generation, program synthesis

## [GrammarT5: Grammar-Integrated Pretrained Encoder-Decoder Neural Model for Code](paper_24.md)
- **Authors**: Zhu, Qihao and Liang, Qingyuan and Sun, Zeyu and Xiong, Yingfei and Zhang, Lu and Cheng, Shengyu
- **Abstract**: Pretrained models for code have exhibited promising performance across various code-related tasks, such as code summarization, code completion, code translation, and bug detection. However, despite their success, the majority of current models still represent code as a token sequence, which may not ...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639125)
- **Labels**: general coding task, code model, training, source code model

## [On Calibration of Pre-trained Code Models](paper_25.md)
- **Authors**: Zhou, Zhenhao and Sha, Chaofeng and Peng, Xin
- **Abstract**: Pre-trained code models have achieved notable success in the field of Software Engineering (SE). However, existing studies have predominantly focused on improving model performance, with limited attention given to other critical aspects such as model calibration. Model calibration, which refers to t...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639126)
- **Labels**: general coding task, code model, training, source code model

## [Language Models for Code Completion: A Practical Evaluation](paper_26.md)
- **Authors**: Izadi, Maliheh and Katzy, Jonathan and Van Dam, Tim and Otten, Marc and Popescu, Razvan Mihai and Van Deursen, Arie
- **Abstract**: Transformer-based language models for automatic code completion have shown great promise so far, yet the evaluation of these models rarely uses real data. This study provides both quantitative and qualitative assessments of three public code language models when completing real-world code. We first ...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639138)
- **Labels**: code generation, code completion

## [Out of Context: How important is Local Context in Neural Program Repair?](paper_27.md)
- **Authors**: Prenner, Julian Aron and Robbes, Romain
- **Abstract**: Deep learning source code models have been applied very successfully to the problem of automated program repair. One of the standing issues is the small input window of current models which often cannot fully fit the context code required for a bug fix (e.g., method or class declarations of a projec...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639086)
- **Labels**: code generation, program repair, empirical study

## [Out of Sight, Out of Mind: Better Automatic Vulnerability Repair by Broadening Input Ranges and Sources](paper_28.md)
- **Authors**: Zhou, Xin and Kim, Kisub and Xu, Bowen and Han, Donggyun and Lo, David
- **Abstract**: The advances of deep learning (DL) have paved the way for automatic software vulnerability repair approaches, which effectively learn the mapping from the vulnerable code to the fixed code. Nevertheless, existing DL-based vulnerability repair methods face notable limitations: 1) they struggle to han...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639222)
- **Labels**: code generation, program repair

## [VGX: Large-Scale Sample Generation for Boosting Learning-Based Software Vulnerability Analyses](paper_29.md)
- **Authors**: Nong, Yu and Fang, Richard and Yi, Guangbei and Zhao, Kunsong and Luo, Xiapu and Chen, Feng and Cai, Haipeng
- **Abstract**: Accompanying the successes of learning-based defensive software vulnerability analyses is the lack of large and quality sets of labeled vulnerable program samples, which impedes further advancement of those defenses. Existing automated sample generation approaches have shown potentials yet still fal...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639116)
- **Labels**: static analysis, bug detection, code model, training, source code model

## [Pre-training by Predicting Program Dependencies for Vulnerability Analysis Tasks](paper_30.md)
- **Authors**: Liu, Zhongxin and Tang, Zhijie and Zhang, Junwei and Xia, Xin and Yang, Xiaohu
- **Abstract**: Vulnerability analysis is crucial for software security. Inspired by the success of pre-trained models on software engineering tasks, this work focuses on using pre-training techniques to enhance the understanding of vulnerable code and boost vulnerability analysis. The code understanding ability of...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639142)
- **Labels**: static analysis, bug detection, code model, training, source code model

## [BinaryAI: Binary Software Composition Analysis via Intelligent Binary Source Code Matching](paper_31.md)
- **Authors**: Jiang, Ling and An, Junwen and Huang, Huihui and Tang, Qiyi and Nie, Sen and Wu, Shi and Zhang, Yuqun
- **Abstract**: While third-party libraries (TPLs) are extensively reused to enhance productivity during software development, they can also introduce potential security risks such as vulnerability propagation. Software composition analysis (SCA), proposed to identify reused TPLs for reducing such risks, has become...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639100)
- **Labels**: static analysis, software composition analysis, code model, training, binary code model

## [Semantic GUI Scene Learning and Video Alignment for Detecting Duplicate Video-based Bug Reports](paper_32.md)
- **Authors**: Yan, Yanfu and Cooper, Nathan and Chaparro, Oscar and Moran, Kevin and Poshyvanyk, Denys
- **Abstract**: Video-based bug reports are increasingly being used to document bugs for programs centered around a graphical user interface (GUI). However, developing automated techniques to manage video-based reports is challenging as it requires identifying and understanding often nuanced visual patterns that ca...
- **Link**: [Read Paper](https://doi.org/10.1145/3597503.3639163)
- **Labels**: software maintenance and deployment, code review

