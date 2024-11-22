# FSE2024

Number of papers: 31

## [AI-Assisted Code Authoring at Scale: Fine-Tuning, Deploying, and Mixed Methods Evaluation](paper_1.md)
- **Authors**: Murali, Vijayaraghavan and Maddila, Chandra and Ahmad, Imad and Bolin, Michael and Cheng, Daniel and Ghorbani, Negar and Fernandez, Renuka and Nagappan, Nachiappan and Rigby, Peter C.
- **Abstract**: Generative LLMs have been shown to effectively power AI-based code authoring tools that can suggest entire statements or blocks of code during code authoring. In this paper we present CodeCompose, an AI-assisted code authoring tool developed and deployed at Meta internally. CodeCompose is based on the InCoder LLM that merges generative capabilities with bi-directionality. We have scaled up CodeCompose to serve tens of thousands of developers at Meta, across 9 programming languages and several co...
- **Link**: [Read Paper](https://doi.org/10.1145/3643774)
- **Labels**: [code generation](../../labels/code_generation.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

## [Refactoring to Pythonic Idioms: A Hybrid Knowledge-Driven Approach Leveraging Large Language Models](paper_2.md)
- **Authors**: Zhang, Zejun and Xing, Zhenchang and Ren, Xiaoxue and Lu, Qinghua and Xu, Xiwei
- **Abstract**: Pythonic idioms are highly valued and widely used in the Python programming community. However, many  Python users find it challenging to use Pythonic idioms. Adopting rule-based approach or LLM-only approach is not sufficient to overcome three persistent challenges of code idiomatization including code miss, wrong detection and wrong refactoring. Motivated by the determinism of rules and adaptability of LLMs, we propose a hybrid approach consisting of three modules. We not only write prompts to...
- **Link**: [Read Paper](https://doi.org/10.1145/3643776)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)

## [Can GPT-4 Replicate Empirical Software Engineering Research?](paper_3.md)
- **Authors**: Liang, Jenny T. and Badea, Carmen and Bird, Christian and DeLine, Robert and Ford, Denae and Forsgren, Nicole and Zimmermann, Thomas
- **Abstract**: Empirical software engineering research on production systems has brought forth a better understanding of the software engineering process for practitioners and researchers alike. However, only a small subset of production systems is studied, limiting the impact of this research. While software engineering practitioners could benefit from replicating research on their own data, this poses its own set of challenges, since performing replications requires a deep understanding of research methodolo...
- **Link**: [Read Paper](https://doi.org/10.1145/3660767)
- **Labels**: [empirical study](../../labels/empirical_study.md), [agent design](../../labels/agent_design.md)

## [SimLLM: Calculating Semantic Similarity in Code Summaries using a Large Language Model-Based Approach](paper_4.md)
- **Authors**: Jin, Xin and Lin, Zhiqiang
- **Abstract**: Code summaries are pivotal in software engineering, serving to improve code readability, maintainability, and collaboration. While recent advancements in Large Language Models (LLMs) have opened new avenues for automatic code summarization, existing metrics for evaluating summary quality, such as BLEU and BERTScore, have notable limitations. Specifically, these existing metrics either fail to capture the nuances of semantic meaning in summaries or are further limited in understanding domain-spec...
- **Link**: [Read Paper](https://doi.org/10.1145/3660769)
- **Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md)

## [A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization](paper_5.md)
- **Authors**: Kang, Sungmin and An, Gabin and Yoo, Shin
- **Abstract**: Fault Localization (FL), in which a developer seeks to identify which part of the code is malfunctioning and needs to be fixed, is a recurring challenge in debugging. To reduce developer burden, many automated FL techniques have been proposed. However, prior work has noted that existing techniques fail to provide rationales for the suggested locations, hindering developer adoption of these techniques. With this in mind, we propose AutoFL, a Large Language Model (LLM)-based FL technique that gene...
- **Link**: [Read Paper](https://doi.org/10.1145/3660771)
- **Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md)

## [Exploring and Unleashing the Power of Large Language Models in Automated Code Translation](paper_6.md)
- **Authors**: Yang, Zhen and Liu, Fang and Yu, Zhongxing and Keung, Jacky Wai and Li, Jia and Liu, Shuo and Hong, Yifan and Ma, Xiaoxue and Jin, Zhi and Li, Ge
- **Abstract**: Code translation tools, namely transpilers, are developed for automatic source-to-source translation. Latest learning-based transpilers have shown impressive enhancement against rule-based counterparts in both translation accuracy and readability, owing to their task-specific pre-training on extensive monolingual corpora. Nevertheless, their current performance still remains unsatisfactory for practical deployment, and the associated training resources are also prohibitively expensive. Large Lan...
- **Link**: [Read Paper](https://doi.org/10.1145/3660778)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [empirical study](../../labels/empirical_study.md)

## [Evaluating and Improving ChatGPT for Unit Test Generation](paper_7.md)
- **Authors**: Yuan, Zhiqiang and Liu, Mingwei and Ding, Shiji and Wang, Kaixin and Chen, Yixuan and Peng, Xin and Lou, Yiling
- **Abstract**: Unit testing plays an essential role in detecting bugs in functionally-discrete program units (e.g., methods). Manually writing high-quality unit tests is time-consuming and laborious. Although the traditional techniques are able to generate tests with reasonable coverage, they are shown to exhibit low readability and still cannot be directly adopted by developers in practice. Recent work has shown the large potential of large language models (LLMs) in unit test generation. By being pre-trained ...
- **Link**: [Read Paper](https://doi.org/10.1145/3660783)
- **Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md), [empirical study](../../labels/empirical_study.md), [code generation](../../labels/code_generation.md)

## [Beyond Code Generation: An Observational Study of ChatGPT Usage in Software Engineering Practice](paper_8.md)
- **Authors**: Khojah, Ranim and Mohamad, Mazen and Leitner, Philipp and de Oliveira Neto, Francisco Gomes
- **Abstract**: Large Language Models (LLMs) are frequently discussed in academia and the general public as support tools for virtually any use case that relies on the production of text, including software engineering. Currently, there is much debate, but little empirical evidence, regarding the practical usefulness of LLM-based tools such as ChatGPT for engineers in industry. We conduct an observational study of 24 professional software engineers who have been using ChatGPT over a period of one week in their ...
- **Link**: [Read Paper](https://doi.org/10.1145/3660788)
- **Labels**: [empirical study](../../labels/empirical_study.md)

## [Can Large Language Models Transform Natural Language Intent into Formal Method Postconditions?](paper_9.md)
- **Authors**: Endres, Madeline and Fakhoury, Sarah and Chakraborty, Saikat and Lahiri, Shuvendu K.
- **Abstract**: Informal natural language that describes code functionality, such as code comments or function documentation, may contain substantial information about a program’s intent. However, there is typically no guarantee that a program’s implementation and natural language documentation are aligned. In the case of a conflict, leveraging information in code-adjacent natural language has the potential to enhance fault localization, debugging, and code trustworthiness. In practice, however, this informatio...
- **Link**: [Read Paper](https://doi.org/10.1145/3660791)
- **Labels**: [static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md), [empirical study](../../labels/empirical_study.md)

## [An Empirical Study on Code Review Activity Prediction and Its Impact in Practice](paper_10.md)
- **Authors**: Olewicki, Doriane and Habchi, Sarra and Adams, Bram
- **Abstract**: During code reviews, an essential step in software quality assurance, reviewers have the difficult task of understanding and evaluating code changes to validate their quality and prevent introducing faults to the codebase. This is a tedious process where the effort needed is highly dependent on the code submitted, as well as the author’s and the reviewer’s experience, leading to median wait times for review feedback of 15-64 hours. Through an initial user study carried with 29 experts, we found ...
- **Link**: [Read Paper](https://doi.org/10.1145/3660806)
- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [code review](../../labels/code_review.md), [empirical study](../../labels/empirical_study.md)

## [Do Large Language Models Pay Similar Attention Like Human Programmers When Generating Code?](paper_11.md)
- **Authors**: Kou, Bonan and Chen, Shengmai and Wang, Zhijie and Ma, Lei and Zhang, Tianyi
- **Abstract**: Large Language Models (LLMs) have recently been widely used for code generation. Due to the complexity and opacity of LLMs, little is known about how these models generate code. We made the first attempt to bridge this knowledge gap by investigating whether LLMs attend to the same parts of a task description as human programmers during code generation. An analysis of six LLMs, including GPT-4, on two popular code generation benchmarks revealed a consistent misalignment between LLMs' and programm...
- **Link**: [Read Paper](https://doi.org/10.1145/3660807)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [empirical study](../../labels/empirical_study.md)

## [Mining Action Rules for Defect Reduction Planning](paper_12.md)
- **Authors**: Oueslati, Khouloud and Laberge, Gabriel and Lamothe, Maxime and Khomh, Foutse
- **Abstract**: Defect reduction planning plays a vital role in enhancing software quality and minimizing software maintenance costs. By training a black box machine learning model and “explaining” its predictions, explainable AI for software engineering aims to identify the code characteristics that impact maintenance risks. However, post-hoc explanations do not always faithfully reflect what the original model computes. In this paper, we introduce CounterACT, a Counterfactual ACTion rule mining approach that ...
- **Link**: [Read Paper](https://doi.org/10.1145/3660809)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [empirical study](../../labels/empirical_study.md)

## [ClarifyGPT: A Framework for Enhancing LLM-Based Code Generation via Requirements Clarification](paper_13.md)
- **Authors**: Mu, Fangwen and Shi, Lin and Wang, Song and Yu, Zhuohao and Zhang, Binquan and Wang, ChenXue and Liu, Shichao and Wang, Qing
- **Abstract**: Large Language Models (LLMs), such as ChatGPT, have demonstrated impressive capabilities in automatically generating code from provided natural language requirements. However, in real-world practice, it is inevitable that the requirements written by users might be ambiguous or insufficient. Current LLMs will directly generate programs according to those unclear requirements, regardless of interactive clarification, which will likely deviate from the original user intents. To bridge that gap, we ...
- **Link**: [Read Paper](https://doi.org/10.1145/3660810)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)

## [Are Human Rules Necessary? Generating Reusable APIs with CoT Reasoning and In-Context Learning](paper_14.md)
- **Authors**: Mai, Yubo and Gao, Zhipeng and Hu, Xing and Bao, Lingfeng and Liu, Yu and Sun, JianLing
- **Abstract**: Inspired by the great potential of Large Language Models (LLMs) for solving complex coding tasks, in this paper, we propose a novel approach, named Code2API, to automatically perform APIzation for Stack Overflow code snippets. Code2API does not require additional model training or any manual crafting rules and can be easily deployed on personal computers without relying on other external tools. Specifically, Code2API guides the LLMs through well-designed prompts to generate well-formed APIs for ...
- **Link**: [Read Paper](https://doi.org/10.1145/3660811)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [source code model](../../labels/source_code_model.md)

## [LILAC: Log Parsing using LLMs with Adaptive Parsing Cache](paper_15.md)
- **Authors**: Jiang, Zhihan and Liu, Jinyang and Chen, Zhuangbin and Li, Yichen and Huang, Junjie and Huo, Yintong and He, Pinjia and Gu, Jiazhen and Lyu, Michael R.
- **Abstract**: Log parsing transforms log messages into structured formats, serving as the prerequisite step for various log analysis tasks. Although a variety of log parsing approaches have been proposed, their performance on complicated log data remains compromised due to the use of human-crafted rules or learning-based models with limited training data. The recent emergence of powerful large language models (LLMs) demonstrates their vast pre-trained knowledge related to code and logging, making it promising...
- **Link**: [Read Paper](https://doi.org/10.1145/3643733)
- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [system log analysis](../../labels/system_log_analysis.md)

## [DiffCoder: Enhancing Large Language Model on API Invocation via Analogical Code Exercises](paper_16.md)
- **Authors**: Zan, Daoguang and Yu, Ailun and Shen, Bo and Chen, Bei and Li, Wei and Gong, Yongshun and Chen, Xiaolin and Yao, Yafen and Luo, Weihua and Guan, Bei and Liu, Yan and Wang, Yongji and Wang, Qianxiang and Cui, Lizhen
- **Abstract**: The task of code generation aims to generate code solutions based on given programming problems. Recently, code large language models (code LLMs) have shed new light on this task, owing to their formidable code generation capabilities. While these models are powerful, they seldom focus on further improving the accuracy of library-oriented API invocation. Nonetheless, programmers frequently invoke APIs in routine coding tasks. In this paper, we aim to enhance the proficiency of existing code LLMs...
- **Link**: [Read Paper](https://doi.org/10.1145/3643745)
- **Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md)

## [Natural Is the Best: Model-Agnostic Code Simplification for Pre-trained Large Language Models](paper_17.md)
- **Authors**: Wang, Yan and Li, Xiaoning and Nguyen, Tien N. and Wang, Shaohua and Ni, Chao and Ding, Ling
- **Abstract**: Pre-trained Large Language Models (LLM) have achieved remarkable successes in several domains. However, code-oriented LLMs are often heavy in computational complexity, and quadratically with the length of the input code sequence. Toward simplifying the input program of an LLM, the state-of-the-art approach has the strategies to filter the input code tokens based on the attention scores given by the LLM. The decision to simplify the input program should not rely on the attention patterns of an LL...
- **Link**: [Read Paper](https://doi.org/10.1145/3643753)
- **Labels**: [static analysis](../../labels/static_analysis.md), [code search](../../labels/code_search.md), [code summarization](../../labels/code_summarization.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

## [Go Static: Contextualized Logging Statement Generation](paper_18.md)
- **Authors**: Li, Yichen and Huo, Yintong and Zhong, Renyi and Jiang, Zhihan and Liu, Jinyang and Huang, Junjie and Gu, Jiazhen and He, Pinjia and Lyu, Michael R.
- **Abstract**: Logging practices have been extensively investigated to assist developers in writing appropriate logging statements for documenting software behaviors. Although numerous automatic logging approaches have been proposed, their performance remains unsatisfactory due to the constraint of the single-method input, without informative programming context outside the method. Specifically, we identify three inherent limitations with single-method context: limited static scope of logging statements, incon...
- **Link**: [Read Paper](https://doi.org/10.1145/3643754)
- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [system log analysis](../../labels/system_log_analysis.md)

## [Unprecedented Code Change Automation: The Fusion of LLMs and Transformation by Example](paper_19.md)
- **Authors**: Dilhara, Malinda and Bellur, Abhiram and Bryksin, Timofey and Dig, Danny
- **Abstract**: Software developers often repeat the same code changes within a project or across different projects. These repetitive changes are known as “code change patterns” (CPATs). Automating CPATs is crucial to expedite the software development process. While current Transformation by Example (TBE) techniques can automate CPATs, they are limited by the quality and quantity of the provided input examples. Thus, they miss transforming code variations that do not have the exact syntax, data-, or control-fl...
- **Link**: [Read Paper](https://doi.org/10.1145/3643755)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)

## [CodePlan: Repository-Level Coding using LLMs and Planning](paper_20.md)
- **Authors**: Bairi, Ramakrishna and Sonwane, Atharv and Kanade, Aditya and C., Vageesh D. and Iyer, Arun and Parthasarathy, Suresh and Rajamani, Sriram and Ashok, B. and Shet, Shashank
- **Abstract**: Software engineering activities such as package migration, fixing error reports from static analysis or testing, and adding type annotations or other specifications to a codebase, involve pervasively editing the entire repository of code.     We formulate these activities as repository-level coding tasks.         Recent tools like GitHub Copilot, which are powered by Large Language Models (LLMs), have succeeded in offering high-quality solutions to localized coding problems.     Repository-level...
- **Link**: [Read Paper](https://doi.org/10.1145/3643757)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [agent design](../../labels/agent_design.md), [planning](../../labels/planning.md)

## [Only diff Is Not Enough: Generating Commit Messages Leveraging Reasoning and Action of Large Language Model](paper_21.md)
- **Authors**: Li, Jiawei and Farag\'{o}, David and Petrov, Christian and Ahmed, Iftekhar
- **Abstract**: Commit messages play a vital role in software development and maintenance. While previous research has introduced various Commit Message Generation (CMG) approaches, they often suffer from a lack of consideration for the broader software context associated with code changes. This limitation resulted in generated commit messages that contained insufficient information and were poorly readable. To address these shortcomings, we approached CMG as a knowledge-intensive reasoning task. We employed Re...
- **Link**: [Read Paper](https://doi.org/10.1145/3643760)
- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [commit message generation](../../labels/commit_message_generation.md)

## [CORE: Resolving Code Quality Issues using LLMs](paper_22.md)
- **Authors**: Wadhwa, Nalin and Pradhan, Jui and Sonwane, Atharv and Sahu, Surya Prakash and Natarajan, Nagarajan and Kanade, Aditya and Parthasarathy, Suresh and Rajamani, Sriram
- **Abstract**: As software projects progress, quality of code assumes paramount importance as it affects reliability, maintainability and security of software. For this reason, static analysis tools are used in developer workflows to flag code quality issues. However, developers need to spend extra efforts to revise their code to improve code quality based on the tool findings. In this work, we investigate the use of (instruction-following) large language models (LLMs) to assist developers in revising code to ...
- **Link**: [Read Paper](https://doi.org/10.1145/3643762)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)

## [Towards AI-Assisted Synthesis of Verified Dafny Methods](paper_23.md)
- **Authors**: Misu, Md Rakib Hossain and Lopes, Cristina V. and Ma, Iris and Noble, James
- **Abstract**: Large language models show great promise in many domains, including programming. A promise is easy to make but hard to keep, and language models often fail to keep their promises, generating erroneous code. A promising avenue to keep models honest is to incorporate formal verification: generating programs’ specifications as well as code so that the code can be proved correct with respect to the specifications. Unfortunately, existing large language models show a severe lack of proficiency in ver...
- **Link**: [Read Paper](https://doi.org/10.1145/3643763)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)

## [COSTELLO: Contrastive Testing for Embedding-Based Large Language Model as a Service Embeddings](paper_24.md)
- **Authors**: Jiang, Weipeng and Zhai, Juan and Ma, Shiqing and Zhang, Xiaoyu and Shen, Chao
- **Abstract**: Large language models have gained significant popularity and are often provided as a service (i.e., LLMaaS).  Companies like OpenAI and Google provide online APIs of LLMs to allow downstream users to create innovative applications.  Despite its popularity, LLM safety and quality assurance is a well-recognized concern in the real world, requiring extra efforts for testing these LLMs.  Unfortunately, while end-to-end services like ChatGPT have garnered rising attention in terms of testing, the LLM...
- **Link**: [Read Paper](https://doi.org/10.1145/3643767)
- **Labels**: [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

## [Code-Aware Prompting: A Study of Coverage-Guided Test Generation in Regression Setting using LLM](paper_25.md)
- **Authors**: Ryan, Gabriel and Jain, Siddhartha and Shang, Mingyue and Wang, Shiqi and Ma, Xiaofei and Ramanathan, Murali Krishna and Ray, Baishakhi
- **Abstract**: Testing plays a pivotal role in ensuring software quality, yet conventional Search Based Software Testing (SBST) methods often struggle with complex software units, achieving suboptimal test coverage. Recent work using large language models (LLMs) for test generation have focused on improving generation quality through optimizing the test generation context and correcting errors in model outputs, but use fixed prompting strategies that prompt the model to generate tests without additional guidan...
- **Link**: [Read Paper](https://doi.org/10.1145/3643769)
- **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)

## [Codeart: Better code models by attention regularization when symbols are lacking](paper_26.md)
- **Authors**: Su, Zian and Xu, Xiangzhe and Huang, Ziyang and Zhang, Zhuo and Ye, Yapeng and Huang, Jianjun and Zhang, Xiangyu
- **Abstract**: Transformer based code models have impressive performance in many software engineering tasks. However, their effectiveness degrades when symbols are missing or not informative. The reason is that the model may not learn to pay attention to the right correlations/contexts without the help of symbols. We propose a new method to pre-train general code models when symbols are lacking. We observe that in such cases, programs degenerate to something written in a very primitive language. We hence propo...
- **Link**: [Read Paper](https://dl.acm.org/doi/pdf/10.1145/3643752)
- **Labels**: [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md)

## [When fuzzing meets llms: Challenges and opportunities](paper_27.md)
- **Authors**: Jiang, Yu and Liang, Jie and Ma, Fuchen and Chen, Yuanliang and Zhou, Chijin and Shen, Yuheng and Wu, Zhiyong and Fu, Jingzhou and Wang, Mingzhe and Li, Shanshan and others
- **Abstract**: Fuzzing, a widely-used technique for bug detection, has seen advancements through Large Language Models (LLMs). Despite their potential, LLMs face specific challenges in fuzzing. In this paper, we identified five major challenges of LLM-assisted fuzzing. To support our findings, we revisited the most recent papers from top-tier conferences, confirming that these challenges are widespread. As a remedy, we propose some actionable recommendations to help improve applying LLM in Fuzzing and conduct ...
- **Link**: [Read Paper](https://dl.acm.org/doi/pdf/10.1145/3663529.3663784)
- **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [survey](../../labels/survey.md)

## [DAInfer: Inferring API Aliasing Specifications from Library Documentation via Neurosymbolic Optimization](paper_28.md)
- **Authors**: Wang, Chengpeng and Zhang, Jipeng and Wu, Rongxin and Zhang, Charles
- **Abstract**: Modern software systems heavily rely on various libraries, necessitating understanding API semantics in static analysis. However, summarizing API semantics remains challenging due to complex implementations or the unavailability of library code. This paper presents DAInfer, a novel approach for inferring API aliasing specifications from library documentation. Specifically, we employ Natural Language Processing (NLP) models to interpret informal semantic information provided by the documentation,...
- **Link**: [Read Paper](https://dl.acm.org/doi/pdf/10.1145/3660816)
- **Labels**: [static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md)

## [Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning](paper_29.md)
- **Authors**: Yadavally, Aashish and Li, Yi and Nguyen, Tien N
- **Abstract**: Program slicing, the process of extracting program statements that influence values at a designated location (known as the slicing criterion), is helpful in both manual and automated debugging. However, such slicing techniques prove ineffective in scenarios where executing specific inputs is prohibitively expensive, or even impossible, as with partial code. In this paper, we introduce ND-Slicer, a predictive slicing methodology that caters to specific executions based on a particular input, over...
- **Link**: [Read Paper](https://aashishyadavally.github.io/assets/pdf/pub-fse2024.pdf)
- **Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

## [EyeTrans: Merging Human and Machine Attention for Neural Code Summarization](paper_30.md)
- **Authors**: Zhang, Yifan and Li, Jiliang and Karas, Zachary and Bansal, Aakash and Li, Toby Jia-Jun and McMillan, Collin and Leach, Kevin and Huang, Yu
- **Abstract**: Neural code summarization leverages deep learning models to automatically generate brief natural language summaries of code snippets. The development of Transformer models has led to extensive use of attention during model design. While existing work has primarily and almost exclusively focused on static properties of source code and related structural representations like the Abstract Syntax Tree (AST), few studies have considered human attention — that is, where programmers focus while examini...
- **Link**: [Read Paper](https://doi.org/10.1145/3643732)
- **Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md), [empirical study](../../labels/empirical_study.md)

## [Learning to Detect and Localize Multilingual Bugs](paper_31.md)
- **Authors**: Yang, Haoran and Nong, Yu and Zhang, Tao and Luo, Xiapu and Cai, Haipeng
- **Abstract**: Increasing studies have shown bugs in multi-language software as a critical loophole in modern software quality assurance, especially those induced by language interactions (i.e., multilingual bugs). Yet existing tool support for bug detection/localization remains largely limited to single-language software, despite the long-standing prevalence of multi-language systems in various real-world software domains. Extant static/dynamic analysis and deep learning (DL) based approaches all face major c...
- **Link**: [Read Paper](https://doi.org/10.1145/3660804)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

