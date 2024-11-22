# Verified multi-step synthesis using large language models and monte carlo tree search

**Authors**: Brandfonbrener, David and Raja, Sibi and Prasad, Tarun and Loughridge, Chloe and Yang, Jianang and Henniger, Simon and Byrd, William E and Zinkov, Robert and Amin, Nada

**Abstract**:

We present an approach using Monte Carlo Tree Search (MCTS) to guide Large Language Models (LLMs) to generate verified programs in Dafny, Lean and Coq. Our method, which we call VMCTS, leverages the verifier inside the search algorithm by checking partial programs at each step. In combination with the LLM prior, the verifier feedback raises the synthesis capabilities of open source models. On a set of five verified programming problems, we find that in four problems where the base model cannot solve the question even when re-sampling solutions for one hour, VMCTS can solve the problems within 6 minutes. The base model with VMCTS is even competitive with ChatGPT4 augmented with plugins and multiple re-tries on these problems. Our code and benchmarks are available at https://github.com/namin/llm-verified-with-monte-carlo-tree-search.

**Link**: [Read Paper](https://openreview.net/pdf?id=HmB9uZTzaD)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)
