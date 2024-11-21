# Large Language Models are Few-Shot Summarizers: Multi-Intent Comment Generation via In-Context Learning

**Authors**: Geng, Mingyang and Wang, Shangwen and Dong, Dezun and Wang, Haotian and Li, Ge and Jin, Zhi and Mao, Xiaoguang and Liao, Xiangke

**Abstract**:

Code comment generation aims at generating natural language descriptions for a code snippet to facilitate developers' program comprehension activities. Despite being studied for a long time, a bottleneck for existing approaches is that given a code snippet, they can only generate one comment while developers usually need to know information from diverse perspectives such as what is the functionality of this code snippet and how to use it. To tackle this limitation, this study empirically investigates the feasibility of utilizing large language models (LLMs) to generate comments that can fulfill developers' diverse intents. Our intuition is based on the facts that (1) the code and its pairwise comment are used during the pre-training process of LLMs to build the semantic connection between the natural language and programming language, and (2) comments in the real-world projects, which are collected for the pre-training, usually contain different developers' intents. We thus postulate that the LLMs can already understand the code from different perspectives after the pre-training. Indeed, experiments on two large-scale datasets demonstrate the rationale of our insights: by adopting the in-context learning paradigm and giving adequate prompts to the LLM (e.g., providing it with ten or more examples), the LLM can significantly outperform a state-of-the-art supervised learning approach on generating comments with multiple intents. Results also show that customized strategies for constructing the prompts and post-processing strategies for reranking the results can both boost the LLM's performances, which shed light on future research directions for using LLMs to achieve comment generation.

**Link**: [Read Paper](https://doi.org/10.1145/3597503.3608134)

**Labels**: software maintenance and deployment, commit message generation
