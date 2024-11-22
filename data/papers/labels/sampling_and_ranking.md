# Sampling And Ranking

- [Let’s Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs](../venues/EMNLP2023/paper_6.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: A popular approach for improving the correctness of output from large language models (LLMs) is Self-Consistency - poll the LLM multiple times and output the most frequent solution. Existing Self-Consistency techniques always generate a constant number of samples per question, where a better approach will be to non-uniformly distribute the available budget based on the amount of agreement in the samples generated so far. In response, we introduce Adaptive-Consistency, a cost-efficient, model-agn...
  - **Labels**: [prompt strategy](prompt_strategy.md), [sampling and ranking](sampling_and_ranking.md)


- [Making Language Models Better Reasoners with Step-Aware Verifier](../venues/ACL2023/paper_2.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Few-shot learning is a challenging task that requires language models to generalize from limited examples. Large language models like GPT-3 and PaLM have made impressive progress in this area, but they still face difficulties in reasoning tasks such as GSM8K, a benchmark for arithmetic problems. To improve their reasoning skills, previous work has proposed to guide the language model with prompts that elicit a series of reasoning steps before giving the final answer, achieving a significant impr...
  - **Labels**: [prompt strategy](prompt_strategy.md), [sampling and ranking](sampling_and_ranking.md)


- [Ranking llm-generated loop invariants for program verification](../venues/EMNLP2023/paper_13.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Synthesizing inductive loop invariants is fundamental to automating program verification. In this work, we observe that Large Language Models (such as gpt-3.5 or gpt-4) are capable of synthesizing loop invariants for a class of programs in a 0-shot setting, yet require several samples to generate the correct invariants. This can lead to a large number of calls to a program verifier to establish an invariant. To address this issue, we propose a {\it re-ranking} approach for the generated results ...
  - **Labels**: [static analysis](static_analysis.md), [program verification](program_verification.md), [invariant generation](invariant_generation.md), [prompt strategy](prompt_strategy.md), [sampling and ranking](sampling_and_ranking.md)
