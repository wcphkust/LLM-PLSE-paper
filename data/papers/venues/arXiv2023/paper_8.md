# Do you still need a manual smart contract audit?

**Authors**: David, Isaac and Zhou, Liyi and Qin, Kaihua and Song, Dawn and Cavallaro, Lorenzo and Gervais, Arthur

**Abstract**:

We investigate the feasibility of employing large language models (LLMs) for conducting the security audit of smart contracts, a traditionally time-consuming and costly process. Our research focuses on the optimization of prompt engineering for enhanced security analysis, and we evaluate the performance and accuracy of LLMs using a benchmark dataset comprising 52 Decentralized Finance (DeFi) smart contracts that have previously been compromised.     Our findings reveal that, when applied to vulnerable contracts, both GPT-4 and Claude models correctly identify the vulnerability type in 40% of the cases. However, these models also demonstrate a high false positive rate, necessitating continued involvement from manual auditors. The LLMs tested outperform a random model by 20% in terms of F1-score. To ensure the integrity of our study, we conduct mutation testing on five newly developed and ostensibly secure smart contracts, into which we manually insert two and 15 vulnerabilities each. This testing yielded a remarkable best-case 78.7% true positive rate for the GPT-4-32k model. We tested both, asking the models to perform a binary classification on whether a contract is vulnerable, and a non-binary prompt. We also examined the influence of model temperature variations and context length on the LLM's performance. Despite the potential for many further enhancements, this work lays the groundwork for a more efficient and economical approach to smart contract security audits.

**Link**: [Read Paper](https://arxiv.org/pdf/2306.12338.pdf)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
