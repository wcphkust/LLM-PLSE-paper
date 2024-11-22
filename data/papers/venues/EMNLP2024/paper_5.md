# Sanitizing Large Language Models in Bug Detection with Data-Flow

**Authors**: Wang, Chengpeng and Zhang, Wuqi and Su, Zian and Xu, Xiangzhe and Zhang, Xiangyu

**Abstract**:

Large language models (LLMs) show potential in code reasoning tasks, facilitating the customization of detecting bugs in software development. However, the hallucination effect can significantly compromise the reliability of bug reports. This work formulates a new schema of bug detection and presents a novel sanitization technique that detects false positives for hallucination mitigation. Our key idea is to enforce LLMs to emit data-flow paths in few-shot chain-of-thought prompting and validate them via the program-property decomposition. Specifically, we dissect data-flow paths into basic properties upon concise code snippets and leverage parsing-based analysis and LLMs for validation. Our approach averagely achieves 91.03% precision and 74.00% recall upon synthetic benchmarks and boosts the precision by 21.99% with the sanitization. The evaluation upon real-world Android malware applications also demonstrates the superiority over an industrial analyzer, surpassing the precision and recall by 15.36% and 3.61%, respectively.

**Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.217)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [fundamental analysis](../../labels/fundamental_analysis.md)
