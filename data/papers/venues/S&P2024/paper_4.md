# Smartinv: Multimodal learning for smart contract invariant inference

**Authors**: Wang, Sally Junsong and Pei, Kexin and Yang, Junfeng

**Abstract**:

Smart contracts are software programs that enable diverse business activities on the blockchain. Recent research has identified new classes of "machine un-auditable" bugs that arise from source code not meeting underlying transaction contexts. Existing detection methods require human understanding of underlying transaction logic and manual reasoning across different sources of context (i.e., modalities), such as code and natural language specifying the expected transaction behavior.To automate the detection of "machine un-auditable" bugs, we present SmartInv, an accurate and fast smart contract invariant inference framework. Our key insight is that the expected behavior of smart contracts, as specified by invariants, relies on understanding and reasoning across multimodal information, such as source code and natural language. We propose a new finetuning and prompting strategy to foundation models, Tier of Thought (ToT), to reason across multiple modalities of smart contracts and to generate invariants. SmartInv then localizes potential vulnerabilities by checking the violation of those generated invariants.We evaluate SmartInv on real-world smart contract bugs that resulted in financial losses over the past 2.5 years (from January 1, 2021 to May 31, 2023). Extensive evaluation shows that SmartInv can generate useful invariants to effectively localize "machine un-auditable" bugs, from which SmartInv uncovers 119 zero-day bugs. We sampled eight bugs and reported them to the respective developers. Six vulnerabilities were quickly fixed by the developers, five of which are confirmed as "high severity.

**Link**: [Read Paper](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a126/1Ub23GNTAeQ)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
