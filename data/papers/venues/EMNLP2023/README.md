# EMNLP2023

Number of papers: 18

## [API-Assisted Code Generation for Question Answering on Varied Table Structures](paper_9.md)
- **Authors**: Cao, Yihan and Chen, Shuyi and Liu, Ryan and Wang, Zhiruo and Fried, Daniel
- **Abstract**: A persistent challenge to table question answering (TableQA) by generating executable programs has been adapting to varied table structures, typically requiring domain-specific logical forms. In response, this paper introduces a unified TableQA framework that: (1) provides a unified representation for structured tables as multi-index Pandas data frames, (2) uses Python as a powerful querying language, and (3) uses few-shot prompting to translate NL questions into Python programs, which are execu...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.897)
[code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)

## [Benchmarking and Improving Text-to-SQL Generation under Ambiguity](paper_3.md)
- **Authors**: Bhaskar, Adithya and Tomar, Tushar and Sathe, Ashutosh and Sarawagi, Sunita
- **Abstract**: Research in Text-to-SQL conversion has been largely benchmarked against datasets where each text query corresponds to one correct SQL. However, natural language queries over real-life databases frequently involve significant ambiguity about the intended SQL due to overlapping schema names and multiple confusing relationship paths. To bridge this gap, we develop a novel benchmark called AmbiQT with over 3000 examples where each text is interpretable as two plausible SQLs due to lexical and/or str...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.436)
[code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [benchmark](../../labels/benchmark.md)

## [CRUSH4SQL: Collective Retrieval Using Schema Hallucination For Text2SQL](paper_8.md)
- **Authors**: Kothyari, Mayank and Dhingra, Dhruva and Sarawagi, Sunita and Chakrabarti, Soumen
- **Abstract**: Existing Text-to-SQL generators require the entire schema to be encoded with the user text. This is expensive or impractical for large databases with tens of thousands of columns. Standard dense retrieval techniques are inadequate for schema subsetting of a large structured database, where the correct semantics of retrieval demands that we rank sets of schema elements rather than individual documents. In response, we propose a two-stage process for effective coverage during retrieval. First, we ...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.868)
[code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)

## [CodeBERTScore: Evaluating Code Generation with Pretrained Models of Code](paper_16.md)
- **Authors**: Zhou, Shuyan and Alon, Uri and Agarwal, Sumit and Neubig, Graham
- **Abstract**: Since the rise of neural natural-language-to-code models (NL\rightarrowCode) that can generate long expressions and statements rather than a single next-token, one of the major problems has been reliably evaluating their generated output. In this paper, we propose CodeBERTScore: an evaluation metric for code generation, which builds on BERTScore (Zhang et al., 2020). Instead of encoding only the generated tokens as in BERTScore, CodeBERTScore also encodes the natural language input preceding the...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.859)
[code generation](../../labels/code_generation.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

## [CodeT5+: Open Code Large Language Models for Code Understanding and Generation](paper_1.md)
- **Authors**: Wang, Yue and Le, Hung and Gotmare, Akhilesh and Bui, Nghi and Li, Junnan and Hoi, Steven
- **Abstract**: Large language models (LLMs) pretrained on vast source code have achieved prominent progress in code intelligence. However, existing code LLMs have two main limitations. First, they often adopt a specific architecture (encoder-only or decoder-only) or rely on a unified encoder-decoder network for different downstream tasks, lacking the flexibility to operate in the optimal architecture for a specific task. Secondly, they often employ a limited set of pretraining objectives which might not be rel...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.68)
[general coding task](../../labels/general_coding_task.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

## [Explanation selection using unlabeled data for chain-of-thought prompting](paper_14.md)
- **Authors**: Ye, Xi and Durrett, Greg
- **Abstract**: Recent work has shown how to prompt large language models with explanations to obtain strong performance on textual reasoning tasks, i.e., the chain-of-thought paradigm. However, subtly different explanations can yield widely varying downstream task accuracy. Explanations that have not been "tuned" for a task, such as off-the-shelf explanations written by nonexperts, may lead to mediocre performance. This paper tackles the problem of how to optimize explanation-infused prompts in a blackbox fash...
- **Link**: [Read Paper](https://arxiv.org/abs/2302.04813)
[prompt strategy](../../labels/prompt_strategy.md), [reason with code](../../labels/reason_with_code.md), [empirical study](../../labels/empirical_study.md)

## [Exploring Distributional Shifts in Large Language Models for Code Analysis](paper_11.md)
- **Authors**: Arakelyan, Shushan and Das, Rocktim and Mao, Yi and Ren, Xiang
- **Abstract**: We systematically study how three large language models with code capabilities - CodeT5, Codex, and ChatGPT - generalize to out-of-domain data. We consider two fundamental applications - code summarization, and code generation. We split data into domains following its natural boundaries - by an organization, by a project, and by a module within the software project. We establish that samples from each new domain present all the models with a significant challenge of distribution shift. We study ...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.1013)
[general coding task](../../labels/general_coding_task.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md), [empirical study](../../labels/empirical_study.md)

## [Generating Data for Symbolic Language with Large Language Models](paper_5.md)
- **Authors**: Ye, Jiacheng and Li, Chengzu and Kong, Lingpeng and Yu, Tao
- **Abstract**: While large language models (LLMs) bring not only performance but also complexity, recent work has started to turn LLMs into data generators rather than task inferencers, where another affordable task model is trained for efficient deployment and inference. However, such an approach has primarily been applied to natural language tasks, and has not yet been explored for symbolic language tasks with complex structured outputs (e.g., semantic parsing and code generation). In this paper, we propose ...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.523)
[code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

## [Improving Transformer-based Program Repair Model through False Behavior Diagnosis](paper_17.md)
- **Authors**: Kim, Youngkyoung and Kim, Misoo and Lee, Eunseok
- **Abstract**: Research on automated program repairs using transformer-based models has recently gained considerable attention. The comprehension of the erroneous behavior of a model enables the identification of its inherent capacity and provides insights for improvement. However, the current landscape of research on program repair models lacks an investigation of their false behavior. Thus, we propose a methodology for diagnosing and treating the false behaviors of transformer-based program repair models. Sp...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.865)
[code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)

## [Let’s Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs](paper_6.md)
- **Authors**: Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam
- **Abstract**: A popular approach for improving the correctness of output from large language models (LLMs) is Self-Consistency - poll the LLM multiple times and output the most frequent solution. Existing Self-Consistency techniques always generate a constant number of samples per question, where a better approach will be to non-uniformly distribute the available budget based on the amount of agreement in the samples generated so far. In response, we introduce Adaptive-Consistency, a cost-efficient, model-agn...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.761)
[prompt strategy](../../labels/prompt_strategy.md), [sampling and ranking](../../labels/sampling_and_ranking.md)

## [MiniChain: A Small Library for Coding with Large Language Models](paper_12.md)
- **Authors**: Rush, Alexander
- **Abstract**: Programming augmented by large language models (LLMs) opens up many new application areas, but also requires care. LLMs are accurate enough, on average, to replace core functionality, yet make basic mistakes that demonstrate a lack of robustness. An ecosystem of prompting tools, from intelligent agents to new programming languages, have emerged with different solutions for patching LLMs with other tools. In this work, we introduce MiniChain, an opinionated tool for LLM augmented programming, wit...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-demo.27)
[general coding task](../../labels/general_coding_task.md)

## [On Sample-Efficient Code Generation](paper_18.md)
- **Authors**: Han, Hojae and Kim, Yu Jin and Kim, Byoungjip and Lee, Youngwon and Lee, Kyungjae and Lee, Kyungmin and Lee, Moontae and Bae, Kyunghoon and Hwang, Seung-won
- **Abstract**: Large language models often struggle to predict runtime behavior in code generation tasks, leading to a reliance on rejection sampling (best-of-n) to generate multiple code snippets then select the best. Our distinction is reducing sampling costs, without compromising generation quality. We introduce EFFICODE, a novel framework that prioritizes sampling on test problems that models can solve. We show how EFFICODE estimates solvability to optimize computational costs during multiple sampling. Bas...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-industry.73)
[code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)

## [Personalized Distillation: Empowering Open-Sourced LLMs with Adaptive Learning for Code Generation](paper_2.md)
- **Authors**: Chen, Hailin and Saha, Amrita and Hoi, Steven and Joty, Shafiq
- **Abstract**: With the rise of powerful closed-sourced LLMs (ChatGPT, GPT-4), there are increasing interests in distilling the capabilies of close-sourced LLMs to smaller open-sourced LLMs. Previous distillation methods usually prompt ChatGPT to generate a set of instructions and answers, for the student model to learn. However, such standard distillation approach neglects the merits and conditions of the student model. Inspired by modern teaching principles, we design a personalised distillation process, in ...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.417)
[code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

## [Prompting with Pseudo-Code Instructions](paper_10.md)
- **Authors**: Mishra, Mayank and Kumar, Prince and Bhat, Riyaz and Murthy, Rudra and Contractor, Danish and Tamilselvam, Srikanth
- **Abstract**: Prompting with natural language instructions has recently emerged as a popular method of harnessing the capabilities of large language models (LLM). Given the inherent ambiguity present in natural language, it is intuitive to consider the possible advantages of prompting with less ambiguous prompt styles, like pseudo-code. In this paper, we explore if prompting via pseudo-code instructions helps improve the performance of pre-trained language models. We manually create a dataset of pseudo-code p...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.939)
[prompt strategy](../../labels/prompt_strategy.md), [reason with code](../../labels/reason_with_code.md)

## [Question Answering as Programming for Solving Time-Sensitive Questions](paper_7.md)
- **Authors**: Zhu, Xinyu and Yang, Cheng and Chen, Bei and Li, Siheng and Lou, Jian-Guang and Yang, Yujiu
- **Abstract**: Question answering plays a pivotal role in human daily life because it involves our acquisition of knowledge about the world. However, due to the dynamic and ever-changing nature of real-world facts, the answer can be completely different when the time constraint in the question changes. Recently, Large Language Models (LLMs) have shown remarkable intelligence in question answering, while our experiments reveal that the aforementioned problems still pose a significant challenge to existing LLMs....
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.787)
[prompt strategy](../../labels/prompt_strategy.md), [reason with code](../../labels/reason_with_code.md)

## [Ranking llm-generated loop invariants for program verification](paper_13.md)
- **Authors**: Chakraborty, Saikat and Lahiri, Shuvendu K and Fakhoury, Sarah and Musuvathi, Madanlal and Lal, Akash and Rastogi, Aseem and Senthilnathan, Aditya and Sharma, Rahul and Swamy, Nikhil
- **Abstract**: Synthesizing inductive loop invariants is fundamental to automating program verification. In this work, we observe that Large Language Models (such as gpt-3.5 or gpt-4) are capable of synthesizing loop invariants for a class of programs in a 0-shot setting, yet require several samples to generate the correct invariants. This can lead to a large number of calls to a program verifier to establish an invariant. To address this issue, we propose a {\it re-ranking} approach for the generated results ...
- **Link**: [Read Paper](https://aclanthology.org/2023.findings-emnlp.614.pdf)
[static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md), [invariant generation](../../labels/invariant_generation.md), [prompt strategy](../../labels/prompt_strategy.md), [sampling and ranking](../../labels/sampling_and_ranking.md)

## [Symbolic Planning and Code Generation for Grounded Dialogue](paper_4.md)
- **Authors**: Chiu, Justin and Zhao, Wenting and Chen, Derek and Vaduguru, Saujas and Rush, Alexander and Fried, Daniel
- **Abstract**: Large language models (LLMs) excel at processing and generating text and code. However, LLMs have had limited applicability in grounded task-oriented dialogue as they are difficult to steer toward task objectives and fail to handle novel grounding. We present a modular and interpretable grounded dialogue system that addresses these shortcomings by composing LLMs with a symbolic planner and grounded code execution. Our system, consists of a reader and planner: the reader leverages an LLM to conve...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.460)
[code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [agent design](../../labels/agent_design.md), [planning](../../labels/planning.md)

## [Towards Low-Resource Automatic Program Repair with Meta-Learning and Pretrained Language Models](paper_15.md)
- **Authors**: Wang, Weishi and Wang, Yue and Hoi, Steven and Joty, Shafiq
- **Abstract**: Automatic program repair (APR) has gained increasing attention as an essential technique in software development to reduce manual debugging efforts and boost developers’ productivity. Recent advances in deep learning (DL) based models have demonstrated promising results by learning from large-scale bug-fix examples in a data-driven manner. However, in practical scenarios, software bugs have an imbalanced distribution, and the fixing knowledge learned by APR models often only capture the patterns...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.430)
[code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)