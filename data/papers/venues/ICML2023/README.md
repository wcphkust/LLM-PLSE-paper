# ICML2023

Number of papers: 3

## [Can large language models reason about program invariants?](paper_3.md)
- **Authors**: Pei, Kexin and Bieber, David and Shi, Kensen and Sutton, Charles and Yin, Pengcheng
- **Abstract**: Identifying invariants is an important program analysis task with applications towards program understanding, bug finding, vulnerability analysis, and formal verification. Existing tools for identifying program invariants rely on dynamic analysis, requiring traces collected from multiple executions in order to produce reliable invariants. We study the application of large language models to invariant prediction, finding that models trained on source code and fine-tuned for invariant generation c...
- **Link**: [Read Paper](https://openreview.net/pdf?id=mXv2aVqUGG)
- **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


## [LongCoder: {A} Long-Range Pre-trained Language Model for Code Completion](paper_1.md)
- **Authors**: Daya Guo and Canwen Xu and Nan Duan and Jian Yin and Julian J. McAuley
- **Abstract**: In this paper, we introduce a new task for code completion that focuses on handling long code input and propose a sparse Transformer model, called LongCoder, to address this task. LongCoder employs a sliding window mechanism for self-attention and introduces two types of globally accessible tokens-bridge tokens and memory tokens-to improve performance and efficiency. Bridge tokens are inserted throughout the input sequence to aggregate local information and facilitate global interaction, while m...
- **Link**: [Read Paper](https://proceedings.mlr.press/v202/guo23j.html)
- **Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [Repository-Level Prompt Generation for Large Language Models of Code](paper_2.md)
- **Authors**: Disha Shrivastava and Hugo Larochelle and Daniel Tarlow
- **Abstract**: With the success of large language models (LLMs) of code and their use as code assistants (e.g. Codex used in GitHub Copilot), techniques for introducing domain-specific knowledge in the prompt design process become important. In this work, we propose a framework called Repo-Level Prompt Generator that learns to generate example-specific prompts using prompt proposals. The prompt proposals take context from the entire repository, thereby incorporating both the structure of the repository and the...
- **Link**: [Read Paper](https://proceedings.mlr.press/v202/shrivastava23a.html)
- **Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md), [prompt strategy](../../labels/prompt_strategy.md), [retrieval-augmented generation](../../labels/retrieval-augmented_generation.md)
