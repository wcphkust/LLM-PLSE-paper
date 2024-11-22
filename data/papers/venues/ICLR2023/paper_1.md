# Is Self-Repair a Silver Bullet for Code Generation?

**Authors**: Olausson, Theo X and Inala, Jeevana Priya and Wang, Chenglong and Gao, Jianfeng and Solar-Lezama, Armando

**Abstract**:

Large language models have shown remarkable aptitude in code generation, but still struggle to perform complex tasks. Self-repair---in which the model debugs and repairs its own code---has recently become a popular way to boost performance in these settings. However, despite its increasing popularity, existing studies of self-repair have been limited in scope; in many settings, its efficacy thus remains poorly understood. In this paper, we analyze Code Llama, GPT-3.5 and GPT-4's ability to perform self-repair on problems taken from HumanEval and APPS. We find that when the cost of carrying out repair is taken into account, performance gains are often modest, vary a lot between subsets of the data, and are sometimes not present at all. We hypothesize that this is because self-repair is bottlenecked by the model's ability to provide feedback on its own code; using a stronger model to artificially boost the quality of the feedback, we observe substantially larger performance gains. Similarly, a small-scale study in which we provide GPT-4 with feedback from human participants suggests that even for the strongest models, self-repair still lags far behind what can be achieved with human-level debugging.

**Link**: [Read Paper](https://openreview.net/forum?id=y0GJXRungR)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)
