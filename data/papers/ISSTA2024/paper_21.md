# Fuzzing JavaScript Interpreters with Coverage-Guided Reinforcement Learning for LLM-Based Mutation

**Authors**: Eom, Jueon and Jeong, Seyeon and Kwon, Taekyoung

**Abstract**:

JavaScript interpreters, crucial for modern web browsers, require an effective fuzzing method to identify security-related bugs. However, the strict grammatical requirements for input present significant challenges. Recent efforts to integrate language models for context- aware mutation in fuzzing are promising but lack the necessary coverage guidance to be fully effective. This paper presents a novel technique called CovRL (Coverage-guided Reinforcement Learning) that combines Large Language Models (LLMs) with Reinforcement Learning (RL) from coverage feedback. Our fuzzer, CovRL-Fuzz, integrates coverage feedback directly into the LLM by leveraging the Term Frequency-Inverse Document Frequency (TF-IDF) method to construct a weighted coverage map. This map is key in calculating the fuzzing reward, which is then applied to the LLM-based mutator through reinforcement learning. CovRL-Fuzz, through this approach, enables the generation of test cases that are more likely to discover new coverage areas, thus improving bug detection while minimizing syntax and semantic errors, all without needing extra post-processing. Our evaluation results show that CovRL-Fuzz outperforms the state-of-the-art fuzzers in enhancing code coverage and identifying bugs in JavaScript interpreters: CovRL-Fuzz identified 58 real-world security-related bugs in the latest JavaScript interpreters, including 50 previously unknown bugs and 15 CVEs.

**Link**: [Read Paper](https://doi.org/10.1145/3650212.3680389)

**Labels**: program testing, fuzzing, compiler testing
