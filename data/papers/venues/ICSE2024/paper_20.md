# Which Syntactic Capabilities Are Statistically Learned by Masked Language Models for Code?

**Authors**: Velasco, Alejandro and Palacio, David N and Rodriguez-Cardenas, Daniel and Poshyvanyk, Denys

**Abstract**:

This paper discusses the limitations of evaluating Masked Language Models (MLMs) in code completion tasks. We highlight that relying on accuracy-based measurements may lead to an overestimation of models' capabilities by neglecting the syntax rules of programming languages. To address these issues, we introduce a technique called SyntaxEval in which Syntactic Capabilities are used to enhance the evaluation of MLMs. SyntaxEval automates the process of masking elements in the model input based on their Abstract Syntax Trees (ASTs). We conducted a case study on two popular MLMs using data from GitHub repositories. Our results showed negative causal effects between the node types and MLMs' accuracy. We conclude that MLMs under study fail to predict some syntactic capabilities.

**Link**: [Read Paper](https://arxiv.org/pdf/2401.01512)

**Labels**: [static analysis](../../labels/static_analysis.md), [syntactic analysis](../../labels/syntactic_analysis.md), [empirical study](../../labels/empirical_study.md)
