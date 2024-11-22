# Learning performance-improving code edits

**Authors**: Shypula, Alexander and Madaan, Aman and Zeng, Yimeng and Alon, Uri and Gardner, Jacob and Hashemi, Milad and Neubig, Graham and Ranganathan, Parthasarathy and Bastani, Osbert and Yazdanbakhsh, Amir

**Abstract**:

With the waning of Moore's law, optimizing program performance has become a major focus of software research. However, high-level optimizations such as API and algorithm changes remain elusive due to the difficulty of understanding the semantics of code. Simultaneously, pretrained large language models (LLMs) have demonstrated strong capabilities at solving a wide range of programming tasks. To that end, we introduce a framework for adapting LLMs to high-level program optimization. First, we curate a dataset of performance-improving edits made by human programmers of over 77K competitive C++ programming submission pairs, accompanied by extensive unit tests. A major challenge is the significant variability of measuring performance on commodity hardware, which can lead to spurious "improvements". To isolate and reliably evaluate the impact of program optimizations, we design an environment based on the gem5 full system simulator, the de facto simulator used in academia and industry. Next, we propose a broad range of adaptation strategies for code optimization; for prompting, these include retrieval-based few-shot prompting and chain-of-thought, and for finetuning, these include performance-conditioned generation and synthetic data augmentation based on self-play. A combination of these techniques achieves an average speedup of 5.65X on CodeLlama-13B and 6.86X on GPT-3.5, surpassing the best human performance (4.06X). We find our proposed performance-conditioned generation is particularly effective at improving performance as well as increasing the fraction of optimized programs.

**Link**: [Read Paper](https://arxiv.org/pdf/2302.07867)

**Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)
