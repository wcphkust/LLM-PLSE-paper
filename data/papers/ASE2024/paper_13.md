# DroidCoder: Enhanced Android Code Completion with Context-Enriched Retrieval-Augmented Generation

**Authors**: Yu, Xinran and Li, Chun and Pan, Minxue and Li, Xuandong

**Abstract**:

Android is the most popular mobile operating system. However, Android development requires extensive coding, especially for unique features such as lifecycle callbacks and UI widgets. Existing code completion methods typically utilize Retrieval-Augmented Generation (RAG) to provide contextual information for pre-trained code large language models (Code LLMs) to perform completion. Despite considerable progress in these methods, their effectiveness in Android development remains limited. This is because the features of Android development make it challenging for existing retrieval mechanisms to extract sufficient context effectively. In response, we propose DroidCoder, a novel Android code completion framework that employs Android development features and contextual information of code snippets to enrich RAG. It also incorporates a specifically designed loss function to fine-tune the model, enabling it to better utilize context-enhanced RAG for Android code completion. We evaluated our method on three base models and different types of applications, comparing it with two state-of-the-art code completion methods. The experimental results demonstrate that our method significantly outperforms the baselines at line-level and multi-line-level code completion and improves the quality of the completed code.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695063)

**Labels**: code generation, code completion, prompt strategy, RAG
