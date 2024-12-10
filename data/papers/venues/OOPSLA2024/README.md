# OOPSLA2024

Number of papers: 8

## [A Learning-Based Approach to Static Program Slicing](paper_7.md)
- **Authors**: Yadavally, Aashish and Li, Yi and Wang, Shaohua and Nguyen, Tien N
- **Abstract**: Traditional program slicing techniques are crucial for early bug detection and manual/automated debugging of online code snippets. Nevertheless, their inability to handle incomplete code hinders their real-world applicability in such scenarios. To overcome these challenges, we present NS-Slicer, a novel learning-based approach that predicts static program slices for both complete and partial code Our tool leverages a pre-trained language model to exploit its understanding of fine-grained variabl...
- **Link**: [Read Paper](https://aashishyadavally.github.io/assets/pdf/pub-oopsla2024.pdf)
- **Labels**: [static analysis](../../labels/static_analysis.md), [data-flow analysis](../../labels/data-flow_analysis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [Drowzee: Metamorphic Testing for Fact-Conflicting Hallucination Detection in Large Language Models](paper_4.md)
- **Authors**: Li, Ningke and Li, Yuekang and Liu, Yi and Shi, Ling and Wang, Kailong and Wang, Haoyu
- **Abstract**: Large language models (LLMs) have revolutionized language processing, but face critical challenges with security, privacy, and generating hallucinations — coherent but factually inaccurate outputs. A major issue is fact-conflicting hallucination (FCH), where LLMs produce content contradicting ground truth facts. Addressing FCH is difficult due to two key challenges: 1) Automatically constructing and updating benchmark datasets is hard, as existing methods rely on manually curated static benchmar...
- **Link**: [Read Paper](https://doi.org/10.1145/3689776)
- **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


## [Enhancing Static Analysis for Practical Bug Detection: An LLM-Integrated Approach](paper_5.md)
- **Authors**: Li, Haonan and Hao, Yu and Zhai, Yizhuo and Qian, Zhiyun
- **Abstract**: While static analysis is instrumental in uncovering software bugs, its precision in analyzing large and intricate codebases remains challenging. The emerging prowess of Large Language Models (LLMs) offers a promising avenue to address these complexities. In this paper, we present LLift, a pioneering framework that synergizes static analysis and LLMs, with a spotlight on identifying use-before-initialization (UBI) bugs within the Linux kernel. Drawing from our insights into variable usage convent...
- **Link**: [Read Paper](https://doi.org/10.1145/3649828)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [Evaluating the effectiveness of deep learning models for foundational program analysis tasks](paper_8.md)
- **Authors**: Chen, Qian and Yu, Chenyang and Liu, Ruyan and Zhang, Chi and Wang, Yu and Wang, Ke and Su, Ting and Wang, Linzhang
- **Abstract**: While deep neural networks provide state-of-the-art solutions to a wide range of programming language tasks, their effectiveness in dealing with foundational program analysis tasks remains under explored. In this paper, we present an empirical study that evaluates four prominent models of code (i.e., CuBERT, CodeBERT, GGNN, and Graph Sandwiches) in two such foundational tasks: (1) alias prediction, in which models predict whether two pointers must alias, may alias or must not alias; and (2) equi...
- **Link**: [Read Paper](https://dl.acm.org/doi/pdf/10.1145/3649829)
- **Labels**: [static analysis](../../labels/static_analysis.md), [pointer analysis](../../labels/pointer_analysis.md), [equivalence checking](../../labels/equivalence_checking.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [Knowledge Transfer from High-Resource to Low-Resource Programming Languages for Code LLMs](paper_2.md)
- **Authors**: Cassano, Federico and Gouwar, John and Lucchetti, Francesca and Schlesinger, Claire and Freeman, Anders and Anderson, Carolyn Jane and Feldman, Molly Q and Greenberg, Michael and Jangda, Abhinav and Guha, Arjun
- **Abstract**: Over the past few years, Large Language Models of Code (Code LLMs) have started to have a significant impact on programming practice. Code LLMs are also emerging as building blocks for research in programming languages and software engineering. However, the quality of code produced by a Code LLM varies significantly by programming language. Code LLMs produce impressive results on high-resource programming languages that are well represented in their training data (e.g., Java, Python, or JavaScri...
- **Link**: [Read Paper](https://doi.org/10.1145/3689735)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [PyDex: Repairing Bugs in Introductory Python Assignments using LLMs](paper_6.md)
- **Authors**: Zhang, Jialu and Cambronero, Jos\'{e} Pablo and Gulwani, Sumit and Le, Vu and Piskac, Ruzica and Soares, Gustavo and Verbruggen, Gust
- **Abstract**: Students often make mistakes in their introductory programming assignments as part of their learning process. Unfortunately, providing custom repairs for these mistakes can require a substantial amount of time and effort from class instructors. Automated program repair (APR) techniques can be used to synthesize such fixes. Prior work has explored the use of symbolic and neural techniques for APR in the education domain. Both types of approaches require either substantial engineering efforts or l...
- **Link**: [Read Paper](https://doi.org/10.1145/3649850)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [Statically Contextualizing Large Language Models with Typed Holes](paper_1.md)
- **Authors**: Blinn, Andrew and Li, Xiang and Kim, June Hyung and Omar, Cyrus
- **Abstract**: Large language models (LLMs) have reshaped the landscape of program synthesis. However, contemporary LLM-based code completion systems often hallucinate broken code because they lack appropriate code context, particularly when working with definitions that are neither in the training data nor near the cursor. This paper demonstrates that tighter integration with the type and binding structure of the programming language in use, as exposed by its language server, can help address this contextuali...
- **Link**: [Read Paper](https://doi.org/10.1145/3689728)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [benchmark](../../labels/benchmark.md), [empirical study](../../labels/empirical_study.md)


## [WhiteFox: White-Box Compiler Fuzzing Empowered by Large Language Models](paper_3.md)
- **Authors**: Yang, Chenyuan and Deng, Yinlin and Lu, Runyu and Yao, Jiayi and Liu, Jiawei and Jabbarvand, Reyhaneh and Zhang, Lingming
- **Abstract**: Compiler correctness is crucial, as miscompilation can falsify program behaviors, leading to serious consequences over the software supply chain. In the literature, fuzzing has been extensively studied to uncover compiler defects. However, compiler fuzzing remains challenging: Existing arts focus on black- and grey-box fuzzing, which generates test programs without sufficient understanding of internal compiler behaviors. As such, they often fail to construct test programs to exercise intricate o...
- **Link**: [Read Paper](https://doi.org/10.1145/3689736)
- **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md), [compiler testing](../../labels/compiler_testing.md)
