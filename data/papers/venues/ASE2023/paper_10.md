# What Makes Good In-Context Demonstrations for Code Intelligence Tasks with LLMs?

**Authors**: Gao, Shuzheng and Wen, Xin-Cheng and Gao, Cuiyun and Wang, Wenxuan and Zhang, Hongyu and Lyu, Michael R.

**Abstract**:

Pre-trained models of source code have gained widespread popularity in many code intelligence tasks. Recently, with the scaling of the model and corpus size, large language models have shown the ability of in-context learning (ICL). ICL employs task instructions and a few examples as demonstrations, and then inputs the demonstrations to the language models for making predictions. This new learning paradigm is training-free and has shown impressive performance in various natural language processing and code intelligence tasks. However, the performance of ICL heavily relies on the quality of demonstrations, e.g., the selected examples. It is important to systematically investigate how to construct a good demonstration for code-related tasks. In this paper, we empirically explore the impact of three key factors on the performance of ICL in code intelligence tasks: the selection, order, and number of demonstration examples. We conduct extensive experiments on three code intelligence tasks including code summarization, bug fixing, and program synthesis. Our experimental results demonstrate that all the above three factors dramatically impact the performance of ICL in code intelligence tasks. Additionally, we summarize our findings and provide takeaway suggestions on how to construct effective demonstrations, taking into account these three perspectives. We also show that a carefully-designed demonstration based on our findings can lead to substantial improvements over widely-used demonstration construction methods, e.g., improving BLEU-4, EM, and EM by at least 9.90%, 175.96%, and 50.81% on code summarization, bug fixing, and program synthesis, respectively.

**Link**: [Read Paper](https://arxiv.org/pdf/2304.07575)

**Labels**: [general coding task](../../labels/general_coding_task.md)
