# Harnessing the power of llm to support binary taint analysis

**Authors**: Liu, Puzhuo and Sun, Chengnian and Zheng, Yaowen and Feng, Xuan and Qin, Chuan and Wang, Yuncheng and Li, Zhi and Sun, Limin

**Abstract**:

This paper proposes LATTE, the first static binary taint analysis that is powered by a large language model (LLM). LATTE is superior to the state of the art (e.g., Emtaint, Arbiter, Karonte) in three aspects. First, LATTE is fully automated while prior static binary taint analyzers need rely on human expertise to manually customize taint propagation rules and vulnerability inspection rules. Second, LATTE is significantly effective in vulnerability detection, demonstrated by our comprehensive evaluations. For example, LATTE has found 37 new bugs in real-world firmware which the baselines failed to find, and 7 of them have been assigned CVE numbers. Lastly, LATTE incurs remarkably low engineering cost, making it a cost-efficient and scalable solution for security researchers and practitioners. We strongly believe that LATTE opens up a new direction to harness the recent advance in LLMs to improve vulnerability analysis for binary programs.

**Link**: [Read Paper](https://arxiv.org/abs/2310.08275)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
