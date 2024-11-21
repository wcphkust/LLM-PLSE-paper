# A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization

**Authors**: Kang, Sungmin and An, Gabin and Yoo, Shin

**Abstract**:

Fault Localization (FL), in which a developer seeks to identify which part of the code is malfunctioning and needs to be fixed, is a recurring challenge in debugging. To reduce developer burden, many automated FL techniques have been proposed. However, prior work has noted that existing techniques fail to provide rationales for the suggested locations, hindering developer adoption of these techniques. With this in mind, we propose AutoFL, a Large Language Model (LLM)-based FL technique that generates an explanation of the bug along with a suggested fault location. AutoFL prompts an LLM to use function calls to navigate a repository, so that it can effectively localize faults over a large software repository and overcome the limit of the LLM context length. Extensive experiments on 798 real-world bugs in Java and Python reveal AutoFL improves method-level acc@1 by up to 233.3\% over baselines. Furthermore, developers were interviewed on their impression of AutoFL-generated explanations, showing that developers generally liked the natural language explanations of AutoFL, and that they preferred reading a few, high-quality explanations instead of many.

**Link**: [Read Paper](https://doi.org/10.1145/3660771)

**Labels**: program testing, debugging
