# Code Summarization

- [Automatic Semantic Augmentation of Language Model Prompts (for Code Summarization)](../venues/ICSE2024/paper_19.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Large Language Models (LLM) are a new class of computation engines, "programmed" via prompt engineering. Researchers are still learning how to best "program" these LLMs to help developers. We start with the intuition that developers tend to consciously and unconsciously collect semantics facts, from the code, while working. Mostly these are shallow, simple facts arising from a quick read. For a function, such facts might include parameter and local variable names, return expressions, simple pre-...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [CoSS: Leveraging Statement Semantics for Code Summarization](../venues/TSE2023/paper_4.md), ([TSE2023](../venues/TSE2023/README.md))

  - **Abstract**: Automated code summarization tools allow generating descriptions for code snippets in natural language, which benefits software development and maintenance. Recent studies demonstrate that the quality of generated summaries can be improved by using additional code representations beyond token sequences. The majority of contemporary approaches mainly focus on extracting code syntactic and structural information from abstract syntax trees (ASTs). However, from the view of macro-structures, it is c...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Code Structure–Guided Transformer for Source Code Summarization](../venues/TOSEM2023/paper_3.md), ([TOSEM2023](../venues/TOSEM2023/README.md))

  - **Abstract**: Code summaries help developers comprehend programs and reduce their time to infer the program functionalities during software maintenance. Recent efforts resort to deep learning techniques such as sequence-to-sequence models for generating accurate code summaries, among which Transformer-based approaches have achieved promising performance. However, effectively integrating the code structure information into the Transformer is under-explored in this task domain. In this article, we propose a nov...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md)


- [EyeTrans: Merging Human and Machine Attention for Neural Code Summarization](../venues/FSE2024/paper_30.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Neural code summarization leverages deep learning models to automatically generate brief natural language summaries of code snippets. The development of Transformer models has led to extensive use of attention during model design. While existing work has primarily and almost exclusively focused on static properties of source code and related structural representations like the Abstract Syntax Tree (AST), few studies have considered human attention — that is, where programmers focus while examini...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [empirical study](empirical_study.md)


- [Learning to Generate Structured Code Summaries From Hybrid Code Context](../venues/TSE2024/paper_11.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Code summarization aims to automatically generate natural language descriptions for code, and has become a rapidly expanding research area in the past decades. Unfortunately, existing approaches mainly focus on the “one-to-one” mapping from methods to short descriptions, which hinders them from becoming practical tools: 1) The program context is ignored, so they have difficulty in predicting labels outside the target method; 2) They are typically trained to generate brief function descriptions w...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [benchmark](benchmark.md)


- [Natural Is the Best: Model-Agnostic Code Simplification for Pre-trained Large Language Models](../venues/FSE2024/paper_17.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Pre-trained Large Language Models (LLM) have achieved remarkable successes in several domains. However, code-oriented LLMs are often heavy in computational complexity, and quadratically with the length of the input code sequence. Toward simplifying the input program of an LLM, the state-of-the-art approach has the strategies to filter the input code tokens based on the attention scores given by the LLM. The decision to simplify the input program should not rely on the attention patterns of an LL...
  - **Labels**: [static analysis](static_analysis.md), [code search](code_search.md), [code summarization](code_summarization.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [SimLLM: Calculating Semantic Similarity in Code Summaries using a Large Language Model-Based Approach](../venues/FSE2024/paper_4.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Code summaries are pivotal in software engineering, serving to improve code readability, maintainability, and collaboration. While recent advancements in Large Language Models (LLMs) have opened new avenues for automatic code summarization, existing metrics for evaluating summary quality, such as BLEU and BERTScore, have notable limitations. Specifically, these existing metrics either fail to capture the nuances of semantic meaning in summaries or are further limited in understanding domain-spec...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md)


- [Understanding Code Changes Practically with Small-Scale Language Models](../venues/ASE2024/paper_3.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Recent studies indicate that traditional techniques for understanding code changes are not as effective as techniques that directly prompt language models (LMs). However, current LM-based techniques heavily rely on expensive, large LMs (LLMs) such as GPT-4 and Llama-13b, which are either commercial or prohibitively costly to deploy on a wide scale, thereby restricting their practical applicability. This paper explores the feasibility of deploying small LMs (SLMs) while maintaining comparable or ...
  - **Labels**: [static analysis](static_analysis.md), [code summarization](code_summarization.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)
