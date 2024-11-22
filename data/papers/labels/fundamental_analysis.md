# Fundamental Analysis

- [A Learning-Based Approach to Static Program Slicing](../venues/OOPSLA2024/paper_7.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Traditional program slicing techniques are crucial for early bug detection and manual/automated debugging of online code snippets. Nevertheless, their inability to handle incomplete code hinders their real-world applicability in such scenarios. To overcome these challenges, we present NS-Slicer, a novel learning-based approach that predicts static program slices for both complete and partial code Our tool leverages a pre-trained language model to exploit its understanding of fine-grained variabl...
  - **Labels**: [static analysis](static_analysis.md), [fundamental analysis](fundamental_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Evaluating the effectiveness of deep learning models for foundational program analysis tasks](../venues/OOPSLA2024/paper_8.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: While deep neural networks provide state-of-the-art solutions to a wide range of programming language tasks, their effectiveness in dealing with foundational program analysis tasks remains under explored. In this paper, we present an empirical study that evaluates four prominent models of code (i.e., CuBERT, CodeBERT, GGNN, and Graph Sandwiches) in two such foundational tasks: (1) alias prediction, in which models predict whether two pointers must alias, may alias or must not alias; and (2) equi...
  - **Labels**: [static analysis](static_analysis.md), [fundamental analysis](fundamental_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Function Argument Nullability Using an LLM](../venues/Galois2024/paper_1.md), ([Galois2024](../venues/Galois2024/README.md))

  - **Abstract**: We think that Rust is a great language, and maybe you agree! Unfortunately, even if you do, there’s a good chance whatever application you’re working on is written in some older language such as C. To help with this, Galois has been developing c2rust, an automated transpiler (source-to-source translator) from C code into Rust code. c2rust can take almost any C and turn it into C-like Rust code, the first step in creating a new Rust application. And we’re building more features to turn C into saf...
  - **Labels**: [static analysis](static_analysis.md), [fundamental analysis](fundamental_analysis.md)


- [LLMs: Understanding Code Syntax and Semantics for Code Analysis](../venues/arXiv2023/paper_1.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Large language models~(LLMs) demonstrate significant potential to revolutionize software engineering (SE) by exhibiting outstanding performance in SE tasks such as code and document generation. However, the high reliability and risk control requirements in software engineering raise concerns about the lack of interpretability of LLMs. To address this concern, we conducted a study to evaluate the capabilities of LLMs and their limitations for code analysis in SE. We break down the abilities neede...
  - **Labels**: [static analysis](static_analysis.md), [fundamental analysis](fundamental_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [empirical study](empirical_study.md)


- [NormTab: Improving Symbolic Reasoning in LLMs Through Tabular Data Normalization](../venues/EMNLP2024/paper_4.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: In recent years, Large Language Models (LLMs) have demonstrated remarkable capabilities in parsing textual data and generating code. However, their performance in tasks involving tabular data, especially those requiring symbolic reasoning, faces challenges due to the structural variance and inconsistency in table cell values often found in web tables. In this paper, we introduce NormTab, a novel framework aimed at enhancing the symbolic reasoning performance of LLMs by normalizing web tables. We...
  - **Labels**: [static analysis](static_analysis.md), [fundamental analysis](fundamental_analysis.md)


- [Program Slicing in the Era of Large Language Models](../venues/arXiv2024/paper_21.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Program slicing is a critical technique in software engineering, enabling developers to isolate relevant portions of code for tasks such as bug detection, code comprehension, and debugging. In this study, we investigate the application of large language models (LLMs) to both static and dynamic program slicing, with a focus on Java programs. We evaluate the performance of four state-of-the-art LLMs- GPT-4o, GPT-3.5 Turbo, Llama-2, and Gemma-7B leveraging advanced prompting techniques, including f...
  - **Labels**: [static analysis](static_analysis.md), [fundamental analysis](fundamental_analysis.md)


- [Programl: A graph-based program representation for data flow analysis and compiler optimizations](../venues/ICML2021/paper_2.md), ([ICML2021](../venues/ICML2021/README.md))

  - **Abstract**: Machine learning (ML) is increasingly seen as a viable approach for building compiler optimization heuristics, but many ML methods cannot replicate even the simplest of the data flow analyses that are critical to making good optimization decisions. We posit that if ML cannot do that, then it is insufficiently able to reason about programs. We formulate data flow analyses as supervised learning tasks and introduce a large open dataset of programs and their corresponding labels from several analys...
  - **Labels**: [static analysis](static_analysis.md), [fundamental analysis](fundamental_analysis.md), [compiler optimization](compiler_optimization.md), [code model](code_model.md), [code model training](code_model_training.md), [IR code model](IR_code_model.md)


- [Revealing the Unseen: AI Chain on LLMs for Predicting Implicit Dataflows to Generate Dataflow Graphs in Dynamically Typed Code](../venues/TOSEM2024/paper_3.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Dataflow graphs (DFGs) capture definitions (defs) and uses across program blocks, which is a fundamental program representation for program analysis, testing and maintenance. However, dynamically typed programming languages like Python present implicit dataflow issues that make it challenging to determine def-use flow information at compile time. Static analysis methods like Soot and WALA are inadequate for handling these issues, and manually enumerating comprehensive heuristic rules is impracti...
  - **Labels**: [static analysis](static_analysis.md), [fundamental analysis](fundamental_analysis.md)


- [Sanitizing Large Language Models in Bug Detection with Data-Flow](../venues/EMNLP2024/paper_5.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large language models (LLMs) show potential in code reasoning tasks, facilitating the customization of detecting bugs in software development. However, the hallucination effect can significantly compromise the reliability of bug reports. This work formulates a new schema of bug detection and presents a novel sanitization technique that detects false positives for hallucination mitigation. Our key idea is to enforce LLMs to emit data-flow paths in few-shot chain-of-thought prompting and validate ...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [fundamental analysis](fundamental_analysis.md)


- [Semantic-Enhanced Indirect Call Analysis with Large Language Models](../venues/ASE2024/paper_8.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: In contemporary software development, the widespread use of indirect calls to achieve dynamic features poses challenges in constructing precise control flow graphs (CFGs), which further impacts the performance of downstream static analysis tasks. To tackle this issue, various types of indirect call analyzers have been proposed. However, they do not fully leverage the semantic information of the program, limiting their effectiveness in real-world scenarios.To address these issues, this paper prop...
  - **Labels**: [static analysis](static_analysis.md), [fundamental analysis](fundamental_analysis.md)


- [Unveiling Code Pre-Trained Models: Investigating Syntax and Semantics Capacities](../venues/TOSEM2024/paper_1.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Code models have made significant advancements in code intelligence by encoding knowledge about programming languages. While previous studies have explored the capabilities of these models in learning code syntax, there has been limited investigation on their ability to understand code semantics. Additionally, existing analyses assume that the number of edges between nodes at the abstract syntax tree&nbsp;(AST) is related to syntax distance, and also often require transforming the high-dimension...
  - **Labels**: [static analysis](static_analysis.md), [fundamental analysis](fundamental_analysis.md), [empirical study](empirical_study.md)


- [Which Syntactic Capabilities Are Statistically Learned by Masked Language Models for Code?](../venues/ICSE2024/paper_20.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: This paper discusses the limitations of evaluating Masked Language Models (MLMs) in code completion tasks. We highlight that relying on accuracy-based measurements may lead to an overestimation of models' capabilities by neglecting the syntax rules of programming languages. To address these issues, we introduce a technique called SyntaxEval in which Syntactic Capabilities are used to enhance the evaluation of MLMs. SyntaxEval automates the process of masking elements in the model input based on ...
  - **Labels**: [static analysis](static_analysis.md), [fundamental analysis](fundamental_analysis.md), [empirical study](empirical_study.md)
