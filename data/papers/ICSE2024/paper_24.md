# GrammarT5: Grammar-Integrated Pretrained Encoder-Decoder Neural Model for Code

**Authors**: Zhu, Qihao and Liang, Qingyuan and Sun, Zeyu and Xiong, Yingfei and Zhang, Lu and Cheng, Shengyu

**Abstract**:

Pretrained models for code have exhibited promising performance across various code-related tasks, such as code summarization, code completion, code translation, and bug detection. However, despite their success, the majority of current models still represent code as a token sequence, which may not adequately capture the essence of the underlying code structure.In this work, we propose GrammarT5, a grammar-integrated encoder-decoder pretrained neural model for code. GrammarT5 employs a novel grammar-integrated representation, Tokenized Grammar Rule Sequence (TGRS), for code. TGRS is constructed based on the grammar rule sequence utilized in syntax-guided code generation and integrates syntax information with code tokens within an appropriate input length. Furthermore, we suggest attaching language flags to help GrammarT5 differentiate between grammar rules of various programming languages. Finally, we introduce two novel pretraining tasks---Edge Prediction (EP), and Sub-Tree Prediction (STP) to learn syntactic information.Experiments were conducted on five code-related tasks using eleven datasets, demonstrating that GrammarT5 achieves state-of-the-art (SOTA) performance on most tasks in comparison to models of the same scale. Additionally, the paper illustrates that the proposed pretraining tasks and language flags can enhance GrammarT5 to better capture the syntax and semantics of code.

**Link**: [Read Paper](https://doi.org/10.1145/3597503.3639125)

**Labels**: general coding task, code model, training, source code model
