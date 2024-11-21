# Grace: Language Models Meet Code Edits

**Authors**: Gupta, Priyanshu and Khare, Avishree and Bajpai, Yasharth and Chakraborty, Saikat and Gulwani, Sumit and Kanade, Aditya and Radhakrishna, Arjun and Soares, Gustavo and Tiwari, Ashish

**Abstract**:

Developers spend a significant amount of time in editing code for a variety of reasons such as bug fixing or adding new features. Designing effective methods to predict code edits has been an active yet challenging area of research due to the diversity of code edits and the difficulty of capturing the developer intent. In this work, we address these challenges by endowing pre-trained large language models (LLMs) with the knowledge of relevant prior associated edits, which we call the Grace (Generation conditioned on Associated Code Edits) method. The generative capability of the LLMs helps address the diversity in code changes and conditioning code generation on prior edits helps capture the latent developer intent. We evaluate two well-known LLMs, codex and CodeT5, in zero-shot and fine-tuning settings respectively. In our experiments with two datasets, Grace boosts the performance of the LLMs significantly, enabling them to generate 29\% and 54\% more correctly edited code in top-1 suggestions relative to the current state-of-the-art symbolic and neural approaches, respectively.

**Link**: [Read Paper](https://doi.org/10.1145/3611643.3616253)

**Labels**: code generation, code completion, code model, training, source code model
