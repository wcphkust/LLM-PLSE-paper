# Complementary explanations for effective in-context learning

**Authors**: Ye, Xi and Iyer, Srinivasan and Celikyilmaz, Asli and Stoyanov, Ves and Durrett, Greg and Pasunuru, Ramakanth

**Abstract**:

Large language models (LLMs) have exhibited remarkable capabilities in learning from explanations in prompts, but there has been limited understanding of exactly how these explanations function or why they are effective. This work aims to better understand the mechanisms by which explanations are used for in-context learning. We first study the impact of two different factors on the performance of prompts with explanations: the computation trace (the way the solution is decomposed) and the natural language used to express the prompt. By perturbing explanations on three controlled tasks, we show that both factors contribute to the effectiveness of explanations. We further study how to form maximally effective sets of explanations for solving a given test query. We find that LLMs can benefit from the complementarity of the explanation set: diverse reasoning skills shown by different exemplars can lead to better performance. Therefore, we propose a maximal marginal relevance-based exemplar selection approach for constructing exemplar sets that are both relevant as well as complementary, which successfully improves the in-context learning performance across three real-world tasks on multiple LLMs.

**Link**: [Read Paper](https://arxiv.org/abs/2211.13892)

**Labels**: [prompt strategy](../../labels/prompt_strategy.md), [reason with code](../../labels/reason_with_code.md), [empirical study](../../labels/empirical_study.md)
