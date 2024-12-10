# Pointer Analysis

- [Evaluating the effectiveness of deep learning models for foundational program analysis tasks](../venues/OOPSLA2024/paper_8.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: While deep neural networks provide state-of-the-art solutions to a wide range of programming language tasks, their effectiveness in dealing with foundational program analysis tasks remains under explored. In this paper, we present an empirical study that evaluates four prominent models of code (i.e., CuBERT, CodeBERT, GGNN, and Graph Sandwiches) in two such foundational tasks: (1) alias prediction, in which models predict whether two pointers must alias, may alias or must not alias; and (2) equi...
  - **Labels**: [static analysis](static_analysis.md), [pointer analysis](pointer_analysis.md), [equivalence checking](equivalence_checking.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Function Argument Nullability Using an LLM](../venues/Galois2024/paper_1.md), ([Galois2024](../venues/Galois2024/README.md))

  - **Abstract**: We think that Rust is a great language, and maybe you agree! Unfortunately, even if you do, there’s a good chance whatever application you’re working on is written in some older language such as C. To help with this, Galois has been developing c2rust, an automated transpiler (source-to-source translator) from C code into Rust code. c2rust can take almost any C and turn it into C-like Rust code, the first step in creating a new Rust application. And we’re building more features to turn C into saf...
  - **Labels**: [static analysis](static_analysis.md), [pointer analysis](pointer_analysis.md)


- [Unveiling Code Pre-Trained Models: Investigating Syntax and Semantics Capacities](../venues/TOSEM2024/paper_1.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Code models have made significant advancements in code intelligence by encoding knowledge about programming languages. While previous studies have explored the capabilities of these models in learning code syntax, there has been limited investigation on their ability to understand code semantics. Additionally, existing analyses assume that the number of edges between nodes at the abstract syntax tree&nbsp;(AST) is related to syntax distance, and also often require transforming the high-dimension...
  - **Labels**: [static analysis](static_analysis.md), [pointer analysis](pointer_analysis.md), [data-flow analysis](data-flow_analysis.md), [empirical study](empirical_study.md)
