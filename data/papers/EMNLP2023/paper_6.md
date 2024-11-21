# Let’s Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs

**Authors**: Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam

**Abstract**:

A popular approach for improving the correctness of output from large language models (LLMs) is Self-Consistency - poll the LLM multiple times and output the most frequent solution. Existing Self-Consistency techniques always generate a constant number of samples per question, where a better approach will be to non-uniformly distribute the available budget based on the amount of agreement in the samples generated so far. In response, we introduce Adaptive-Consistency, a cost-efficient, model-agnostic technique that dynamically adjusts the number of samples per question using a lightweight stopping criterion. Our experiments over 17 reasoning and code generation datasets and three LLMs demonstrate that Adaptive-Consistency reduces sample budget by up to 7.9 times with an average accuracy drop of less than 0.1%

**Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.761)

**Labels**: prompt strategy, sampling and ranking
