# TOSEM2024

Number of papers: 10

## [Harnessing the power of llm to support binary taint analysis](paper_7.md)
- **Authors**: Liu, Puzhuo and Sun, Chengnian and Zheng, Yaowen and Feng, Xuan and Qin, Chuan and Wang, Yuncheng and Li, Zhi and Sun, Limin
- **Abstract**: This paper proposes LATTE, the first static binary taint analysis that is powered by a large language model (LLM). LATTE is superior to the state of the art (e.g., Emtaint, Arbiter, Karonte) in three aspects. First, LATTE is fully automated while prior static binary taint analyzers need rely on human expertise to manually customize taint propagation rules and vulnerability inspection rules. Second, LATTE is significantly effective in vulnerability detection, demonstrated by our comprehensive eva...
- **Link**: [Read Paper](https://arxiv.org/abs/2310.08275)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [Improving Automated Program Repair with Domain Adaptation](paper_8.md)
- **Authors**: Zirak, Armin and Hemmati, Hadi
- **Abstract**: Automated Program Repair (APR) is defined as the process of fixing a bug/defect in the source code, by an automated tool. APR tools have recently experienced promising results by leveraging state-of-the-art Neural Language Processing (NLP) techniques. APR tools such as TFix and CodeXGLUE that combine text-to-text transformers with software-specific techniques are outperforming alternatives, these days. However, in most APR studies, the train and test sets are chosen from the same set of projects...
- **Link**: [Read Paper](https://doi.org/10.1145/3631972)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [LLMEffiChecker: Understanding and Testing Efficiency Degradation of Large Language Models](paper_4.md)
- **Authors**: Feng, Xiaoning and Han, Xiaohong and Chen, Simin and Yang, Wei
- **Abstract**: Large Language Models (LLMs) have received much recent attention due to their human-level accuracy. While existing works mostly focus on either improving accuracy or testing accuracy robustness, the computation efficiency of LLMs, which is of paramount importance due to often vast generation demands and real-time requirements, has surprisingly received little attention. In this article, we make the first attempt to understand and test potential computation efficiency robustness in state-of-the-a...
- **Link**: [Read Paper](https://doi.org/10.1145/3664812)
- **Labels**: [code model](../../labels/code_model.md), [code model robustness](../../labels/code_model_robustness.md)


## [Revealing the Unseen: AI Chain on LLMs for Predicting Implicit Dataflows to Generate Dataflow Graphs in Dynamically Typed Code](paper_3.md)
- **Authors**: Huang, Qing and Luo, Zhiwen and Xing, Zhenchang and Zeng, Jinshan and Chen, Jieshan and Xu, Xiwei and Chen, Yong
- **Abstract**: Dataflow graphs (DFGs) capture definitions (defs) and uses across program blocks, which is a fundamental program representation for program analysis, testing and maintenance. However, dynamically typed programming languages like Python present implicit dataflow issues that make it challenging to determine def-use flow information at compile time. Static analysis methods like Soot and WALA are inadequate for handling these issues, and manually enumerating comprehensive heuristic rules is impracti...
- **Link**: [Read Paper](https://doi.org/10.1145/3672458)
- **Labels**: [static analysis](../../labels/static_analysis.md), [data-flow analysis](../../labels/data-flow_analysis.md)


## [Risky Dynamic Typing-related Practices in Python: An Empirical Study](paper_6.md)
- **Authors**: Chen, Zhifei and Chen, Lin and Yang, Yibiao and Feng, Qiong and Li, Xuansong and Song, Wei
- **Abstract**: Python’s dynamic typing nature provides developers with powerful programming abstractions. However, many type-related bugs are accumulated in code bases of Python due to the misuse of dynamic typing. The goal of this article is to aid in the understanding of developers’ high-risk practices toward dynamic typing and the early detection of type-related bugs. We first formulate the rules of six types of risky dynamic typing-related practices (type smells for short) in Python. We then develop a rule...
- **Link**: [Read Paper](https://doi.org/10.1145/3649593)
- **Labels**: [static analysis](../../labels/static_analysis.md), [type inference](../../labels/type_inference.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)


## [Self-Collaboration Code Generation via ChatGPT](paper_5.md)
- **Authors**: Dong, Yihong and Jiang, Xue and Jin, Zhi and Li, Ge
- **Abstract**: Although large language models (LLMs) have demonstrated remarkable code-generation ability, they still struggle with complex tasks. In real-world software development, humans usually tackle complex tasks through collaborative teamwork, a strategy that significantly controls development complexity and enhances software quality. Inspired by this, we present a self-collaboration framework for code generation employing LLMs, exemplified by ChatGPT. Specifically, through role instructions, (1) Multip...
- **Link**: [Read Paper](https://doi.org/10.1145/3672459)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [Self-Planning Code Generation with Large Language Models](paper_2.md)
- **Authors**: Jiang, Xue and Dong, Yihong and Wang, Lecheng and Fang, Zheng and Shang, Qiwei and Li, Ge and Jin, Zhi and Jiao, Wenpin
- **Abstract**: Although large language models (LLMs) have demonstrated impressive ability in code generation, they are still struggling to address the complicated intent provided by humans. It is widely acknowledged that humans typically employ planning to decompose complex problems and schedule solution steps prior to implementation. To this end, we introduce planning into code generation to help the model understand complex intent and reduce the difficulty of problem-solving. This paper proposes a self-plann...
- **Link**: [Read Paper](https://doi.org/10.1145/3672456)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [agent design](../../labels/agent_design.md), [planning](../../labels/planning.md), [empirical study](../../labels/empirical_study.md)


## [Survey of Code Search Based on Deep Learning](paper_10.md)
- **Authors**: Xie, Yutao and Lin, Jiayi and Dong, Hande and Zhang, Lei and Wu, Zhonghai
- **Abstract**: Code writing is repetitive and predictable, inspiring us to develop various code intelligence techniques. This survey focuses on code search, that is, to retrieve code that matches a given natural language query by effectively capturing the semantic similarity between the query and code. Deep learning, being able to extract complex semantics information, has achieved great success in this field. Recently, various deep learning methods, such as graph neural networks and pretraining models, have b...
- **Link**: [Read Paper](https://doi.org/10.1145/3628161)
- **Labels**: [survey](../../labels/survey.md), [static analysis](../../labels/static_analysis.md), [code search](../../labels/code_search.md)


## [Unveiling Code Pre-Trained Models: Investigating Syntax and Semantics Capacities](paper_1.md)
- **Authors**: Ma, Wei and Liu, Shangqing and Zhao, Mengjie and Xie, Xiaofei and Wang, Wenhang and Hu, Qiang and Zhang, Jie and Liu, Yang
- **Abstract**: Code models have made significant advancements in code intelligence by encoding knowledge about programming languages. While previous studies have explored the capabilities of these models in learning code syntax, there has been limited investigation on their ability to understand code semantics. Additionally, existing analyses assume that the number of edges between nodes at the abstract syntax tree&nbsp;(AST) is related to syntax distance, and also often require transforming the high-dimension...
- **Link**: [Read Paper](https://doi.org/10.1145/3664606)
- **Labels**: [static analysis](../../labels/static_analysis.md), [pointer analysis](../../labels/pointer_analysis.md), [data-flow analysis](../../labels/data-flow_analysis.md), [empirical study](../../labels/empirical_study.md)


## [Vision Transformer Inspired Automated Vulnerability Repair](paper_9.md)
- **Authors**: Fu, Michael and Nguyen, Van and Tantithamthavorn, Chakkrit and Phung, Dinh and Le, Trung
- **Abstract**: Recently, automated vulnerability repair approaches have been widely adopted to combat increasing software security issues. In particular, transformer-based encoder-decoder models achieve competitive results. Whereas vulnerable programs may only consist of a few vulnerable code areas that need repair, existing AVR approaches lack a mechanism guiding their model to pay more attention to vulnerable code areas during repair generation. In this article, we propose a novel vulnerability repair framew...
- **Link**: [Read Paper](https://doi.org/10.1145/3632746)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)
