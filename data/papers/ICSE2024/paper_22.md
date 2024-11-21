# Gptscan: Detecting logic vulnerabilities in smart contracts by combining gpt with program analysis

**Authors**: Sun, Yuqiang and Wu, Daoyuan and Xue, Yue and Liu, Han and Wang, Haijun and Xu, Zhengzi and Xie, Xiaofei and Liu, Yang

**Abstract**:

Smart contracts are prone to various vulnerabilities, leading to substantial financial losses over time. Current analysis tools mainly target vulnerabilities with fixed control- or data-flow patterns, such as re-entrancy and integer overflow. However, a recent study on Web3 security bugs revealed that about 80% of these bugs cannot be audited by existing tools due to the lack of domain-specific property description and checking. Given recent advances in Large Language Models (LLMs), it is worth exploring how Generative Pre-training Transformer (GPT) could aid in detecting logic vulnerabilities.In this paper, we propose GPTScan, the first tool combining GPT with static analysis for smart contract logic vulnerability detection. Instead of relying solely on GPT to identify vulnerabilities, which can lead to high false positives and is limited by GPT's pre-trained knowledge, we utilize GPT as a versatile code understanding tool. By breaking down each logic vulnerability type into scenarios and properties, GPTScan matches candidate vulnerabilities with GPT. To enhance accuracy, GPTScan further instructs GPT to intelligently recognize key variables and statements, which are then validated by static confirmation. Evaluation on diverse datasets with around 400 contract projects and 3K Solidity files shows that GPTScan achieves high precision (over 90%) for token contracts and acceptable precision (57.14%) for large projects like Web3Bugs. It effectively detects ground-truth logic vulnerabilities with a recall of over 70%, including 9 new vulnerabilities missed by human auditors. GPTScan is fast and cost-effective, taking an average of 14.39 seconds and 0.01 USD to scan per thousand lines of Solidity code. Moreover, static confirmation helps GPTScan reduce two-thirds of false positives.

**Link**: [Read Paper](No Link Available)

**Labels**: static analysis, bug detection
