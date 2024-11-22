# Exploring Distributional Shifts in Large Language Models for Code Analysis

**Authors**: Arakelyan, Shushan and Das, Rocktim and Mao, Yi and Ren, Xiang

**Abstract**:

We systematically study how three large language models with code capabilities - CodeT5, Codex, and ChatGPT - generalize to out-of-domain data. We consider two fundamental applications - code summarization, and code generation. We split data into domains following its natural boundaries - by an organization, by a project, and by a module within the software project. We establish that samples from each new domain present all the models with a significant challenge of distribution shift. We study how established methods adapt models to better generalize to new domains. Our experiments show that while multitask learning alone is a reasonable baseline, combining it with few-shot finetuning on examples retrieved from training data can achieve very strong performance. Moreover, this solution can outperform direct finetuning for very low-data scenarios. Finally, we consider variations of this approach to create a more broadly applicable method to adapt to multiple domains at once. We find that for code generation, a model adapted to multiple domains simultaneously performs on par with those adapted to a single domain.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.1013)

**Labels**: [general coding task](../../labels/general_coding_task.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md), [empirical study](../../labels/empirical_study.md)
