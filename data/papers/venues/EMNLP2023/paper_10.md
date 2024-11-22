# Prompting with Pseudo-Code Instructions

**Authors**: Mishra, Mayank and Kumar, Prince and Bhat, Riyaz and Murthy, Rudra and Contractor, Danish and Tamilselvam, Srikanth

**Abstract**:

Prompting with natural language instructions has recently emerged as a popular method of harnessing the capabilities of large language models (LLM). Given the inherent ambiguity present in natural language, it is intuitive to consider the possible advantages of prompting with less ambiguous prompt styles, like pseudo-code. In this paper, we explore if prompting via pseudo-code instructions helps improve the performance of pre-trained language models. We manually create a dataset of pseudo-code prompts for 132 different tasks spanning classification, QA, and generative language tasks, sourced from the Super-NaturalInstructions dataset. Using these prompts along with their counterparts in natural language, we study their performance on two LLM families - BLOOM, CodeGen. Our experiments show that using pseudo-code instructions leads to better results, with an average increase (absolute) of 7-16 points in F1 scores for classification tasks and an improvement (relative) of 12-38% in aggregate ROUGE-L scores across all tasks. We include detailed ablation studies which indicate that code comments, docstrings, and the structural clues encoded in pseudo-code all contribute towards the improvement in performance. To the best of our knowledge, our work is the first to demonstrate how pseudo-code prompts can be helpful in improving the performance of pre-trained LMs.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.939)

**Labels**: [prompt strategy](../../labels/prompt_strategy.md), [reason with code](../../labels/reason_with_code.md)
