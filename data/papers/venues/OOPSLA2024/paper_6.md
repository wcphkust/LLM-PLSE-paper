# PyDex: Repairing Bugs in Introductory Python Assignments using LLMs

**Authors**: Zhang, Jialu and Cambronero, Jos\'{e} Pablo and Gulwani, Sumit and Le, Vu and Piskac, Ruzica and Soares, Gustavo and Verbruggen, Gust

**Abstract**:

Students often make mistakes in their introductory programming assignments as part of their learning process. Unfortunately, providing custom repairs for these mistakes can require a substantial amount of time and effort from class instructors. Automated program repair (APR) techniques can be used to synthesize such fixes. Prior work has explored the use of symbolic and neural techniques for APR in the education domain. Both types of approaches require either substantial engineering efforts or large amounts of data and training. We propose to use a large language model trained on code, such as Codex (a version of GPT), to build an APR system -- PyDex -- for introductory Python programming assignments. Our system can fix both syntactic and semantic mistakes by combining multi-modal prompts, iterative querying, test-case-based selection of few-shots, and program chunking. We evaluate PyDex on 286 real student programs and compare to three baselines, including one that combines a state-of-the-art Python syntax repair engine, BIFI, and a state-of-the-art Python semantic repair engine for student assignments, Refactory. We find that PyDex can fix more programs and produce smaller patches on average.

**Link**: [Read Paper](https://doi.org/10.1145/3649850)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)
