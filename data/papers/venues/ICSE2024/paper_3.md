# Large Language Models for Test-Free Fault Localization

**Authors**: Yang, Aidan Z. H. and Le Goues, Claire and Martins, Ruben and Hellendoorn, Vincent

**Abstract**:

Fault Localization (FL) aims to automatically localize buggy lines of code, a key first step in many manual and automatic debugging tasks. Previous FL techniques assume the provision of input tests, and often require extensive program analysis, program instrumentation, or data preprocessing. Prior work on deep learning for APR struggles to learn from small datasets and produces limited results on real-world programs. Inspired by the ability of large language models (LLMs) of code to adapt to new tasks based on very few examples, we investigate the applicability of LLMs to line level fault localization. Specifically, we propose to overcome the left-to-right nature of LLMs by fine-tuning a small set of bidirectional adapter layers on top of the representations learned by LLMs to produce LLMAO, the first language model based fault localization approach that locates buggy lines of code without any test coverage information. We fine-tune LLMs with 350 million, 6 billion, and 16 billion parameters on small, manually curated corpora of buggy programs such as the Defects4J corpus. We observe that our technique achieves substantially more confidence in fault localization when built on the larger models, with bug localization performance scaling consistently with the LLM size. Our empirical evaluation shows that LLMAO improves the Top-1 results over the state-of-the-art machine learning fault localization (MLFL) baselines by 2.3\%--54.4\%, and Top-5 results by 14.4\%-35.6\%. LLMAO is also the first FL technique trained using a language model architecture that can detect security vulnerabilities down to the code line level.

**Link**: [Read Paper](https://doi.org/10.1145/3597503.3623342)

**Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)
