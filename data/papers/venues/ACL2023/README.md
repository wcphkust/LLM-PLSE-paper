# ACL2023

Number of papers: 13

## [A Static Evaluation of Code Completion by Large Language Models](paper_12.md)
- **Authors**: Ding, Hantian and Kumar, Varun and Tian, Yuchen and Wang, Zijian and Kwiatkowski, Rob and Li, Xiaopeng and Ramanathan, Murali Krishna and Ray, Baishakhi and Bhatia, Parminder and Sengupta, Sudipta
- **Abstract**: Large language models trained on code have shown great potential to increase productivity of software developers. Several execution-based benchmarks have been proposed to evaluate functional correctness of model-generated code on simple programming problems. Nevertheless, it is expensive to perform the same evaluation on complex real-world projects considering the execution cost. On the other hand, static analysis tools such as linters, which can detect errors without running the program, haven’...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.acl-industry.34)
[code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md), [empirical study](../../labels/empirical_study.md)

## [Code4Struct: Code Generation for Few-Shot Event Structure Prediction](paper_8.md)
- **Authors**: Wang, Xingyao and Li, Sha and Ji, Heng
- **Abstract**: Large Language Model (LLM) trained on a mixture of text and code has demonstrated impressive capability in translating natural language (NL) into structured code. We observe that semantic structures can be conveniently translated into code and propose Code4Struct to leverage such text-to-structure translation capability to tackle structured prediction tasks. As a case study, we formulate Event Argument Extraction (EAE) as converting text into event-argument structures that can be represented as ...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.acl-long.202)
[code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [empirical study](../../labels/empirical_study.md)

## [CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors](paper_5.md)
- **Authors**: Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng
- **Abstract**: Large language models (LLMs) pre-trained on massive corpora have demonstrated impressive few-shot learning ability on many NLP tasks. A common practice is to recast the task into a text-to-text format such that generative LLMs of natural language (NL-LLMs) like GPT-3 can be prompted to solve it. However, it is nontrivial to perform information extraction (IE) tasks with NL-LLMs since the output of the IE task is usually structured and therefore is hard to be converted into plain text. In this pa...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.acl-long.855)
[code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)

## [Complementary explanations for effective in-context learning](paper_7.md)
- **Authors**: Ye, Xi and Iyer, Srinivasan and Celikyilmaz, Asli and Stoyanov, Ves and Durrett, Greg and Pasunuru, Ramakanth
- **Abstract**: Large language models (LLMs) have exhibited remarkable capabilities in learning from explanations in prompts, but there has been limited understanding of exactly how these explanations function or why they are effective. This work aims to better understand the mechanisms by which explanations are used for in-context learning. We first study the impact of two different factors on the performance of prompts with explanations: the computation trace (the way the solution is decomposed) and the natur...
- **Link**: [Read Paper](https://arxiv.org/abs/2211.13892)
[prompt strategy](../../labels/prompt_strategy.md), [reason with code](../../labels/reason_with_code.md), [empirical study](../../labels/empirical_study.md)

## [Domain-specific transformer models for query translation](paper_11.md)
- **Authors**: Kulkarni, Mandar and Garera, Nikesh and Trivedi, Anusua
- **Abstract**: Due to the democratization of e-commerce, many product companies are listing their goods for online shopping. For periodic buying within a domain such as Grocery, consumers are generally inclined to buy certain brands of products. Due to a large non-English speaking population in India, we observe a significant percentage of code-mix Hinglish search queries e.g., sasta atta. An intuitive approach to dealing with code-mix queries is to train an encoder-decoder model to translate the query to Engl...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.acl-industry.10)
[code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)

## [Fact-Checking Complex Claims with Program-Guided Reasoning](paper_3.md)
- **Authors**: Pan, Liangming and Wu, Xiaobao and Lu, Xinyuan and Luu, Anh Tuan and Wang, William Yang and Kan, Min-Yen and Nakov, Preslav
- **Abstract**: Fact-checking real-world claims often requires collecting multiple pieces of evidence and applying complex multi-step reasoning. In this paper, we present Program-Guided Fact-Checking (ProgramFC), a novel fact-checking model that decomposes complex claims into simpler sub-tasks that can be solved using a shared library of specialized functions. We first leverage the in-context learning ability of large language models to generate reasoning programs to guide the verification process. Afterward, w...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.acl-long.386)
[prompt strategy](../../labels/prompt_strategy.md), [reason with code](../../labels/reason_with_code.md)

## [Large Language Models Meet NL2Code: A Survey](paper_4.md)
- **Authors**: Zan, Daoguang and Chen, Bei and Zhang, Fengji and Lu, Dianjie and Wu, Bingchao and Guan, Bei and Yongji, Wang and Lou, Jian-Guang
- **Abstract**: The task of generating code from a natural language description, or NL2Code, is considered a pressing and significant challenge in code intelligence. Thanks to the rapid development of pre-training techniques, surging large language models are being proposed for code, sparking the advances in NL2Code. To facilitate further research and applications in this field, in this paper, we present a comprehensive survey of 27 existing large language models for NL2Code, and also review benchmarks and metr...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.acl-long.411)
[survey](../../labels/survey.md), [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)

## [Making Language Models Better Reasoners with Step-Aware Verifier](paper_2.md)
- **Authors**: Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu
- **Abstract**: Few-shot learning is a challenging task that requires language models to generalize from limited examples. Large language models like GPT-3 and PaLM have made impressive progress in this area, but they still face difficulties in reasoning tasks such as GSM8K, a benchmark for arithmetic problems. To improve their reasoning skills, previous work has proposed to guide the language model with prompts that elicit a series of reasoning steps before giving the final answer, achieving a significant impr...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.acl-long.291)
[prompt strategy](../../labels/prompt_strategy.md), [sampling and ranking](../../labels/sampling_and_ranking.md)

## [Multitask Pretraining with Structured Knowledge for Text-to-SQL Generation](paper_9.md)
- **Authors**: Giaquinto, Robert and Zhang, Dejiao and Kleiner, Benjamin and Li, Yang and Tan, Ming and Bhatia, Parminder and Nallapati, Ramesh and Ma, Xiaofei
- **Abstract**: Many machine learning-based low-code or no-code applications involve generating code that interacts with structured knowledge. For example, one of the most studied tasks in this area is generating SQL code from a natural language statement. Prior work shows that incorporating context information from the database schema, such as table and column names, is beneficial to model performance on this task. In this work we present a large pretraining dataset and strategy for learning representations of...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.acl-long.620)
[code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [benchmark](../../labels/benchmark.md)

## [Python Code Generation by Asking Clarification Questions](paper_10.md)
- **Authors**: Li, Haau-Sing (Xiaocheng) and Mesgar, Mohsen and Martins, André and Gurevych, Iryna
- **Abstract**: Code generation from text requires understanding the user’s intent from a natural languagedescription and generating an executable code snippet that satisfies this intent. While recent pretrained language models demonstrate remarkable performance for this task, these models fail when the given natural language description is under-specified. In this work, we introduce a novel and more realistic setup for this task. We hypothesize that the under-specification of a natural language description can...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.acl-long.799)
[code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)

## [ReCode: Robustness Evaluation of Code Generation Models](paper_13.md)
- **Authors**: Wang, Shiqi and Li, Zheng and Qian, Haifeng and Yang, Chenghao and Wang, Zijian and Shang, Mingyue and Kumar, Varun and Tan, Samson and Ray, Baishakhi and Bhatia, Parminder and Nallapati, Ramesh and Ramanathan, Murali Krishna and Roth, Dan and Xiang, Bing
- **Abstract**: Code generation models have achieved impressive performance. However, they tend to be brittle as slight edits to a prompt could lead to very different generations; these robustness properties, critical for user experience when deployed in real-life applications, are not well understood. Most existing works on robustness in text or code tasks have focused on classification, while robustness in generation tasks is an uncharted area and to date there is no comprehensive benchmark for robustness in ...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.acl-long.773)
[code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md), [code model](../../labels/code_model.md), [code model robustness](../../labels/code_model_robustness.md)

## [Self-Edit: Fault-Aware Code Editor for Code Generation](paper_1.md)
- **Authors**: Zhang, Kechi and Li, Zhuo and Li, Jia and Li, Ge and Jin, Zhi
- **Abstract**: Large language models (LLMs) have demonstrated an impressive ability to generate codes on competitive programming tasks. However, with limited sample numbers, LLMs still suffer from poor accuracy. Inspired by the process of human programming, we propose a generate-and-edit approach named Self-Edit that utilizes execution results of the generated code from LLMs to improve the code quality on the competitive programming task. We execute the generated code on the example test case provided in the q...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.acl-long.45)
[code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [benchmark](../../labels/benchmark.md)

## [XSemPLR: Cross-Lingual Semantic Parsing in Multiple Natural Languages and Meaning Representations](paper_6.md)
- **Authors**: Zhang, Yusen and Wang, Jun and Wang, Zhiguo and Zhang, Rui
- **Abstract**: Cross-Lingual Semantic Parsing (CLSP) aims to translate queries in multiple natural languages (NLs) into meaning representations (MRs) such as SQL, lambda calculus, and logic forms. However, existing CLSP models are separately proposed and evaluated on datasets of limited tasks and applications, impeding a comprehensive and unified evaluation of CLSP on a diverse range of NLs and MRs. To this end, we present XSemPLR, a unified benchmark for cross-lingual semantic parsing featured with 22 natural...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.acl-long.887)
[code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)