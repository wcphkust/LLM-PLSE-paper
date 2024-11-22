# EMNLP2023

Number of papers: 18

## [CodeT5+: Open Code Large Language Models for Code Understanding and Generation](paper_1.md)
- **Authors**: Wang, Yue and Le, Hung and Gotmare, Akhilesh and Bui, Nghi and Li, Junnan and Hoi, Steven
- **Abstract**: Large language models (LLMs) pretrained on vast source code have achieved prominent progress in code intelligence. However, existing code LLMs have two main limitations. First, they often adopt a specific architecture (encoder-only or decoder-only) or rely on a unified encoder-decoder network for di...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.68)
- **Labels**: general coding task, code model, code model training, source code model

## [Personalized Distillation: Empowering Open-Sourced LLMs with Adaptive Learning for Code Generation](paper_2.md)
- **Authors**: Chen, Hailin and Saha, Amrita and Hoi, Steven and Joty, Shafiq
- **Abstract**: With the rise of powerful closed-sourced LLMs (ChatGPT, GPT-4), there are increasing interests in distilling the capabilies of close-sourced LLMs to smaller open-sourced LLMs. Previous distillation methods usually prompt ChatGPT to generate a set of instructions and answers, for the student model to...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.417)
- **Labels**: code generation, program synthesis, code model, code model training, source code model

## [Benchmarking and Improving Text-to-SQL Generation under Ambiguity](paper_3.md)
- **Authors**: Bhaskar, Adithya and Tomar, Tushar and Sathe, Ashutosh and Sarawagi, Sunita
- **Abstract**: Research in Text-to-SQL conversion has been largely benchmarked against datasets where each text query corresponds to one correct SQL. However, natural language queries over real-life databases frequently involve significant ambiguity about the intended SQL due to overlapping schema names and multip...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.436)
- **Labels**: code generation, program synthesis, benchmark

## [Symbolic Planning and Code Generation for Grounded Dialogue](paper_4.md)
- **Authors**: Chiu, Justin and Zhao, Wenting and Chen, Derek and Vaduguru, Saujas and Rush, Alexander and Fried, Daniel
- **Abstract**: Large language models (LLMs) excel at processing and generating text and code. However, LLMs have had limited applicability in grounded task-oriented dialogue as they are difficult to steer toward task objectives and fail to handle novel grounding. We present a modular and interpretable grounded dia...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.460)
- **Labels**: code generation, program synthesis, agent design, planning

## [Generating Data for Symbolic Language with Large Language Models](paper_5.md)
- **Authors**: Ye, Jiacheng and Li, Chengzu and Kong, Lingpeng and Yu, Tao
- **Abstract**: While large language models (LLMs) bring not only performance but also complexity, recent work has started to turn LLMs into data generators rather than task inferencers, where another affordable task model is trained for efficient deployment and inference. However, such an approach has primarily be...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.523)
- **Labels**: code model, code model training, source code model

## [Let’s Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs](paper_6.md)
- **Authors**: Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam
- **Abstract**: A popular approach for improving the correctness of output from large language models (LLMs) is Self-Consistency - poll the LLM multiple times and output the most frequent solution. Existing Self-Consistency techniques always generate a constant number of samples per question, where a better approac...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.761)
- **Labels**: prompt strategy, sampling and ranking

## [Question Answering as Programming for Solving Time-Sensitive Questions](paper_7.md)
- **Authors**: Zhu, Xinyu and Yang, Cheng and Chen, Bei and Li, Siheng and Lou, Jian-Guang and Yang, Yujiu
- **Abstract**: Question answering plays a pivotal role in human daily life because it involves our acquisition of knowledge about the world. However, due to the dynamic and ever-changing nature of real-world facts, the answer can be completely different when the time constraint in the question changes. Recently, L...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.787)
- **Labels**: prompt strategy, reason with code

## [CRUSH4SQL: Collective Retrieval Using Schema Hallucination For Text2SQL](paper_8.md)
- **Authors**: Kothyari, Mayank and Dhingra, Dhruva and Sarawagi, Sunita and Chakrabarti, Soumen
- **Abstract**: Existing Text-to-SQL generators require the entire schema to be encoded with the user text. This is expensive or impractical for large databases with tens of thousands of columns. Standard dense retrieval techniques are inadequate for schema subsetting of a large structured database, where the corre...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.868)
- **Labels**: code generation, program synthesis

## [API-Assisted Code Generation for Question Answering on Varied Table Structures](paper_9.md)
- **Authors**: Cao, Yihan and Chen, Shuyi and Liu, Ryan and Wang, Zhiruo and Fried, Daniel
- **Abstract**: A persistent challenge to table question answering (TableQA) by generating executable programs has been adapting to varied table structures, typically requiring domain-specific logical forms. In response, this paper introduces a unified TableQA framework that: (1) provides a unified representation f...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.897)
- **Labels**: code generation, program synthesis

## [Prompting with Pseudo-Code Instructions](paper_10.md)
- **Authors**: Mishra, Mayank and Kumar, Prince and Bhat, Riyaz and Murthy, Rudra and Contractor, Danish and Tamilselvam, Srikanth
- **Abstract**: Prompting with natural language instructions has recently emerged as a popular method of harnessing the capabilities of large language models (LLM). Given the inherent ambiguity present in natural language, it is intuitive to consider the possible advantages of prompting with less ambiguous prompt s...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.939)
- **Labels**: prompt strategy, reason with code

## [Exploring Distributional Shifts in Large Language Models for Code Analysis](paper_11.md)
- **Authors**: Arakelyan, Shushan and Das, Rocktim and Mao, Yi and Ren, Xiang
- **Abstract**: We systematically study how three large language models with code capabilities - CodeT5, Codex, and ChatGPT - generalize to out-of-domain data. We consider two fundamental applications - code summarization, and code generation. We split data into domains following its natural boundaries - by an orga...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.1013)
- **Labels**: general coding task, code model, code model training, source code model, empirical study

## [MiniChain: A Small Library for Coding with Large Language Models](paper_12.md)
- **Authors**: Rush, Alexander
- **Abstract**: Programming augmented by large language models (LLMs) opens up many new application areas, but also requires care. LLMs are accurate enough, on average, to replace core functionality, yet make basic mistakes that demonstrate a lack of robustness. An ecosystem of prompting tools, from intelligent age...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-demo.27)
- **Labels**: general coding task

## [Ranking llm-generated loop invariants for program verification](paper_13.md)
- **Authors**: Chakraborty, Saikat and Lahiri, Shuvendu K and Fakhoury, Sarah and Musuvathi, Madanlal and Lal, Akash and Rastogi, Aseem and Senthilnathan, Aditya and Sharma, Rahul and Swamy, Nikhil
- **Abstract**: Synthesizing inductive loop invariants is fundamental to automating program verification. In this work, we observe that Large Language Models (such as gpt-3.5 or gpt-4) are capable of synthesizing loop invariants for a class of programs in a 0-shot setting, yet require several samples to generate th...
- **Link**: [Read Paper](https://aclanthology.org/2023.findings-emnlp.614.pdf)
- **Labels**: static analysis, program verification, invariant generation, prompt strategy, sampling and ranking

## [Explanation selection using unlabeled data for chain-of-thought prompting](paper_14.md)
- **Authors**: Ye, Xi and Durrett, Greg
- **Abstract**: Recent work has shown how to prompt large language models with explanations to obtain strong performance on textual reasoning tasks, i.e., the chain-of-thought paradigm. However, subtly different explanations can yield widely varying downstream task accuracy. Explanations that have not been "tuned" ...
- **Link**: [Read Paper](https://arxiv.org/abs/2302.04813)
- **Labels**: prompt strategy, reason with code, empirical study

## [Towards Low-Resource Automatic Program Repair with Meta-Learning and Pretrained Language Models](paper_15.md)
- **Authors**: Wang, Weishi and Wang, Yue and Hoi, Steven and Joty, Shafiq
- **Abstract**: Automatic program repair (APR) has gained increasing attention as an essential technique in software development to reduce manual debugging efforts and boost developers’ productivity. Recent advances in deep learning (DL) based models have demonstrated promising results by learning from large-scale ...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.430)
- **Labels**: code generation, program repair, code model, code model training, source code model

## [CodeBERTScore: Evaluating Code Generation with Pretrained Models of Code](paper_16.md)
- **Authors**: Zhou, Shuyan and Alon, Uri and Agarwal, Sumit and Neubig, Graham
- **Abstract**: Since the rise of neural natural-language-to-code models (NL\rightarrowCode) that can generate long expressions and statements rather than a single next-token, one of the major problems has been reliably evaluating their generated output. In this paper, we propose CodeBERTScore: an evaluation metric...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.859)
- **Labels**: code generation, code model, code model training, source code model

## [Improving Transformer-based Program Repair Model through False Behavior Diagnosis](paper_17.md)
- **Authors**: Kim, Youngkyoung and Kim, Misoo and Lee, Eunseok
- **Abstract**: Research on automated program repairs using transformer-based models has recently gained considerable attention. The comprehension of the erroneous behavior of a model enables the identification of its inherent capacity and provides insights for improvement. However, the current landscape of researc...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.865)
- **Labels**: code generation, program repair

## [On Sample-Efficient Code Generation](paper_18.md)
- **Authors**: Han, Hojae and Kim, Yu Jin and Kim, Byoungjip and Lee, Youngwon and Lee, Kyungjae and Lee, Kyungmin and Lee, Moontae and Bae, Kyunghoon and Hwang, Seung-won
- **Abstract**: Large language models often struggle to predict runtime behavior in code generation tasks, leading to a reliance on rejection sampling (best-of-n) to generate multiple code snippets then select the best. Our distinction is reducing sampling costs, without compromising generation quality. We introduc...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-industry.73)
- **Labels**: code generation, program synthesis

