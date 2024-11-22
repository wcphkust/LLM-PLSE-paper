# RepoSim: Evaluating Prompt Strategies for Code Completion via User Behavior Simulation

**Authors**: Peng, Chao and Wu, Qinyun and Liu, Jiangchao and Liu, Jierui and Jiang, Bo and Xu, Mengqian and Wang, Yinghao and Liu, Xia and Yang, Ping

**Abstract**:

Large language models (LLMs) have revolutionized code completion tasks. IDE plugins such as MarsCode can generate code recommendations, saving developers significant time and effort. However, current evaluation methods for code completion are limited by their reliance on static code benchmarks, which do not consider human interactions and evolving repositories. This paper proposes RepoSim, a novel benchmark designed to evaluate code completion tasks by simulating the evolving process of repositories and incorporating user behaviors. RepoSim leverages data from an IDE plugin, by recording and replaying user behaviors to provide a realistic programming context for evaluation. This allows for the assessment of more complex prompt strategies, such as utilizing recently visited files and incorporating user editing history. Additionally, RepoSim proposes a new metric based on users' acceptance or rejection of predictions, offering a user-centric evaluation criterion. Our preliminary evaluation demonstrates that incorporating users' recent edit history into prompts significantly improves the quality of LLM-generated code, highlighting the importance of temporal context in code completion. RepoSim represents a significant advancement in benchmarking tools, offering a realistic and user-focused framework for evaluating code completion performance.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695299)

**Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md)
