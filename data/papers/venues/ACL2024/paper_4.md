# Quantifying Contamination in Evaluating Code Generation Capabilities of Language Models

**Authors**: Riddell, Martin and Ni, Ansong and Cohan, Arman

**Abstract**:

While large language models have achieved remarkable performance on various code generation benchmarks, there have been growing concerns regarding potential contamination of these benchmarks as they may be leaked into pretraining and finetuning data. While recent work has investigated contamination in natural language generation and understanding tasks, there has been less extensive research into how data contamination impacts the evaluation of code generation, which is critical for understanding the robustness and reliability of LLMs in programming contexts. In this work, we perform a comprehensive study of data contamination of popular code generation benchmarks, and precisely quantify their overlap with pretraining corpus through both surface-level and semantic-level matching. In our experiments, we show that there are substantial overlap between popular code generation benchmarks and open training corpus, and models perform significantly better on the subset of the benchmarks where similar solutions are seen during training. We also conduct extensive analysis on the factors that affect model memorization and generalization, such as model size, problem difficulty, and question length. We release all resulting files from our matching pipeline for future research.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.761)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [empirical study](../../labels/empirical_study.md)
