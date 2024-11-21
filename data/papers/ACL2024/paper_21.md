# Lightweight reranking for language model generations

**Authors**: Jain, Siddhartha and Ma, Xiaofei and Deoras, Anoop and Xiang, Bing

**Abstract**:

Large Language Models (LLMs) can exhibit considerable variation in the quality of their sampled outputs. Reranking and selecting the best generation from the sampled set is a popular way of obtaining strong gains in generation quality. In this paper, we present a novel approach for reranking LLM generations. Unlike other techniques that might involve additional inferences or training a specialized reranker, our approach relies on easy to compute pairwise statistics between the generations that have minimal compute overhead. We show that our approach can be formalized as an extension of self-consistency and analyze its performance in that framework, theoretically as well as via simulations. We show strong improvements for selecting the best k generations for code generation tasks as well as robust improvements for the best generation for the tasks of autoformalization, summarization, and translation. While our approach only assumes black-box access to LLMs, we show that additional access to token probabilities can improve performance even further.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.376)

**Labels**: code generation, program synthesis
