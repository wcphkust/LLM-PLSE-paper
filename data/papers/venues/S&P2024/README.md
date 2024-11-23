# S&P2024

Number of papers: 4

## [LLMIF: Augmented Large Language Model for Fuzzing IoT Devices](paper_2.md)
- **Authors**: Wang, Jincheng and Yu, Le and Luo, Xiapu
- **Abstract**: Despite the efficacy of fuzzing in verifying the implementation correctness of network protocols, existing IoT protocol fuzzing approaches grapple with several limitations, including obfuscated message formats, unresolved message dependencies, and a lack of evaluations on the testing cases. These limitations significantly curtail the capabilities of IoT fuzzers in vulnerability identification. In this work, we show that the protocol specification contains fruitful descriptions of protocol messag...
- **Link**: [Read Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10646659)
[program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)

## [LLMs Cannot Reliably Identify and Reason About Security Vulnerabilities (Yet?): A Comprehensive Evaluation, Framework, and Benchmarks](paper_1.md)
- **Authors**: Ullah, Saad and Han, Mingji and Pujar, Saurabh and Pearce, Hammond and Coskun, Ayse and Stringhini, Gianluca
- **Abstract**: Large Language Models (LLMs) have been suggested for use in automated vulnerability repair, but benchmarks showing they can consistently identify security-related bugs are lacking. We thus develop SecLLMHolmes, a fully automated evaluation framework that performs the most detailed investigation to date on whether LLMs can reliably identify and reason about security-related bugs. We construct a set of 228 code scenarios and analyze eight of the most capable LLMs across eight different investigati...
- **Link**: [Read Paper](https://arxiv.org/pdf/2312.12575)
[static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [empirical study](../../labels/empirical_study.md)

## [Smartinv: Multimodal learning for smart contract invariant inference](paper_4.md)
- **Authors**: Wang, Sally Junsong and Pei, Kexin and Yang, Junfeng
- **Abstract**: Smart contracts are software programs that enable diverse business activities on the blockchain. Recent research has identified new classes of "machine un-auditable" bugs that arise from source code not meeting underlying transaction contexts. Existing detection methods require human understanding of underlying transaction logic and manual reasoning across different sources of context (i.e., modalities), such as code and natural language specifying the expected transaction behavior.To automate t...
- **Link**: [Read Paper](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a126/1Ub23GNTAeQ)
[static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)

## [TrojanPuzzle: Covertly Poisoning Code-Suggestion Models](paper_3.md)
- **Authors**: Aghakhani, Hojjat and Dai, Wei and Manoel, Andre and Fernandes, Xavier and Kharkar, Anant and Kruegel, Christopher and Vigna, Giovanni and Evans, David and Zorn, Ben and Sim, Robert
- **Abstract**: With tools like GitHub Copilot, automatic code suggestion is no longer a dream in software engineering. These tools, based on large language models, are typically trained on massive corpora of code mined from unvetted public sources. As a result, these models are susceptible to data poisoning attacks where an adversary manipulates the model’s training by injecting malicious data. Poisoning attacks could be designed to influence the model’s suggestions at run time for chosen contexts, such as ind...
- **Link**: [Read Paper](https://arxiv.org/pdf/2301.02344)
[code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md), [attack](../../labels/attack.md), [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md)