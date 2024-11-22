# Large language model-powered smart contract vulnerability detection: New perspectives

**Authors**: Hu, Sihao and Huang, Tiansheng and {\.I}lhan, Fatih and Tekin, Selim Furkan and Liu, Ling

**Abstract**:

This paper provides a systematic analysis of the opportunities, challenges, and potential solutions of harnessing Large Language Models (LLMs) such as GPT-4 to dig out vulnerabilities within smart contracts based on our ongoing research. For the task of smart contract vulnerability detection, achieving practical usability hinges on identifying as many true vulnerabilities as possible while minimizing the number of false positives. Nonetheless, our empirical study reveals contradictory yet interesting findings: generating more answers with higher randomness largely boosts the likelihood of producing a correct answer but inevitably leads to a higher number of false positives. To mitigate this tension, we propose an adversarial framework dubbed GPTL ENS that breaks the conventional one-stage detection into two synergistic stages - generation and discrimination, for progressive detection and refinement, wherein the LLM plays dual roles, i.e., AUDITOR and CRITIC, respectively. The goal of AUDITOR is to yield a broad spectrum of vulnerabilities with the hope of encompassing the correct answer, whereas the goal of CRITIC that evaluates the validity of identified vulnerabilities is to minimize the number of false positives. Experimental results and illustrative examples demonstrate that AUDITOR and CRITIC work together harmoniously to yield pronounced improvements over the conventional one-stage detection. GPTL ENS is intuitive, strategic, and entirely LLM-driven without relying on specialist expertise in smart contracts, showcasing its methodical generality and potential to detect a broad spectrum of vulnerabilities. Our code is available at: https://github.com/git-disl/GPTLens.

**Link**: [Read Paper](https://arxiv.org/pdf/2310.01152.pdf)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
