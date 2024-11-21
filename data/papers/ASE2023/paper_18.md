# Domain Adaptive Code Completion via Language Models and Decoupled Domain Databases

**Authors**: Tang, Ze and Ge, Jidong and Liu, Shangqing and Zhu, Tingwei and Xu, Tongtong and Huang, Liguo and Luo, Bin

**Abstract**:

Large Language Models (LLMs) have demonstrated remarkable performance in code completion. However, due to the lack of domain-specific knowledge, they may not be optimal in completing code that requires intensive domain knowledge for example completing the library names. Although there are several works that have confirmed the effectiveness of fine-tuning techniques to adapt language models for code completion in specific domains. They are limited by the need for constant fine-tuning of the model when the project is in constant iteration. To address this limitation, in this paper, we propose $k$ NM-LM, a retrieval-augmented language model (R-LM), that integrates domain knowledge into language models without fine-tuning. Different from previous techniques, our approach is able to automatically adapt to different language models and domains. Specifically, it utilizes the in-domain code to build the retrieval-based database decoupled from LM, and then combines it with LM through Bayesian inference to complete the code. The extensive experiments on the completion of intra-project and intra-scenario have confirmed that $k$ NM-LM brings about appreciable enhancements when compared to CodeGPT and UnixCoder. A deep analysis of our tool including the responding speed, storage usage, specific type code completion, and API invocation completion has confirmed that $k$ NM-LM provides satisfactory performance, which renders it highly appropriate for domain adaptive code completion. Furthermore, our approach operates without the requirement for direct access to the language model's parameters. As a result, it can seamlessly integrate with black-box code completion models, making it easy to integrate our approach as a plugin to further enhance the performance of these models.

**Link**: [Read Paper](No Link Available)

**Labels**: code generation, code completion, code model, training, source code model
