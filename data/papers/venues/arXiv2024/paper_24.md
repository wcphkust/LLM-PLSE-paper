# Llm4fuzz: Guided fuzzing of smart contracts with large language models

**Authors**: Shou, Chaofan and Liu, Jing and Lu, Doudou and Sen, Koushik

**Abstract**:

As blockchain platforms grow exponentially, millions of lines of smart contract code are being deployed to manage extensive digital assets. However, vulnerabilities in this mission-critical code have led to significant exploitations and asset losses. Thorough automated security analysis of smart contracts is thus imperative. This paper introduces LLM4Fuzz to optimize automated smart contract security analysis by leveraging large language models (LLMs) to intelligently guide and prioritize fuzzing campaigns. While traditional fuzzing suffers from low efficiency in exploring the vast state space, LLM4Fuzz employs LLMs to direct fuzzers towards high-value code regions and input sequences more likely to trigger vulnerabilities. Additionally, LLM4Fuzz can leverage LLMs to guide fuzzers based on user-defined invariants, reducing blind exploration overhead. Evaluations of LLM4Fuzz on real-world DeFi projects show substantial gains in efficiency, coverage, and vulnerability detection compared to baseline fuzzing. LLM4Fuzz also uncovered five critical vulnerabilities that can lead to a loss of more than $247k.

**Link**: [Read Paper](https://arxiv.org/pdf/2401.11108.pdf)

**Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)
