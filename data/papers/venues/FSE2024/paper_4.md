# SimLLM: Calculating Semantic Similarity in Code Summaries using a Large Language Model-Based Approach

**Authors**: Jin, Xin and Lin, Zhiqiang

**Abstract**:

Code summaries are pivotal in software engineering, serving to improve code readability, maintainability, and collaboration. While recent advancements in Large Language Models (LLMs) have opened new avenues for automatic code summarization, existing metrics for evaluating summary quality, such as BLEU and BERTScore, have notable limitations. Specifically, these existing metrics either fail to capture the nuances of semantic meaning in summaries or are further limited in understanding domain-specific terminologies and expressions prevalent in code summaries. In this paper, we present SimLLM, a novel LLM-based approach designed to more precisely evaluate the semantic similarity of code summaries. Built upon an autoregressive LLM using a specialized pretraining task on permutated inputs and a pooling-based pairwise similarity measure, SimLLM overcomes the shortcomings of existing metrics. Our empirical evaluations demonstrate that SimLLM not only outperforms existing metrics but also shows a significantly high correlation with human ratings.

**Link**: [Read Paper](https://doi.org/10.1145/3660769)

**Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md)
