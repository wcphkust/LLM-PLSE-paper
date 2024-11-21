# Assisting Static Analysis with Large Language Models: A ChatGPT Experiment

**Authors**: Li, Haonan and Hao, Yu and Zhai, Yizhuo and Qian, Zhiyun

**Abstract**:

Recent advances of Large Language Models (LLMs), e.g., ChatGPT, exhibited strong capabilities of comprehending and responding to questions across a variety of domains. Surprisingly, ChatGPT even possesses a strong understanding of program code. In this paper, we investigate where and how LLMs can assist static analysis by asking appropriate questions. In particular, we target a specific bug-finding tool, which produces many false positives from the static analysis. In our evaluation, we find that these false positives can be effectively pruned by asking carefully constructed questions about function-level behaviors or function summaries. Specifically, with a pilot study of 20 false positives, we can successfully prune 8 out of 20 based on GPT-3.5, whereas GPT-4 had a near-perfect result of 16 out of 20, where the four failed ones are not currently considered/supported by our questions, e.g., involving concurrency. Additionally, it also identified one false negative case (a missed bug). We find LLMs a promising tool that can enable a more effective and efficient program analysis.

**Link**: [Read Paper](https://doi.org/10.1145/3611643.3613078)

**Labels**: static analysis, bug detection
