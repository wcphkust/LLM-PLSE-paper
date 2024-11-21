# On Extracting Specialized Code Abilities from Large Language Models: A Feasibility Study

**Authors**: Li, Zongjie and Wang, Chaozheng and Ma, Pingchuan and Liu, Chaowei and Wang, Shuai and Wu, Daoyuan and Gao, Cuiyun and Liu, Yang

**Abstract**:

Recent advances in large language models (LLMs) significantly boost their usage in software engineering. However, training a well-performing LLM demands a substantial workforce for data collection and annotation. Moreover, training datasets may be proprietary or partially open, and the process often requires a costly GPU cluster. The intellectual property value of commercial LLMs makes them attractive targets for imitation attacks, but creating an imitation model with comparable parameters still incurs high costs. This motivates us to explore a practical and novel direction: slicing commercial black-box LLMs using medium-sized backbone models.In this paper, we explore the feasibility of launching imitation attacks on LLMs to extract their specialized code abilities, such as "code synthesis" and "code translation." We systematically investigate the effectiveness of launching code ability extraction attacks under different code-related tasks with multiple query schemes, including zero-shot, in-context, and Chain-of-Thought. We also design response checks to refine the outputs, leading to an effective imitation training process. Our results show promising outcomes, demonstrating that with a reasonable number of queries, attackers can train a medium-sized backbone model to replicate specialized code behaviors similar to the target LLMs. We summarize our findings and insights to help researchers better understand the threats posed by imitation attacks, including revealing a practical attack surface for generating adversarial code examples against LLMs.

**Link**: [Read Paper](https://doi.org/10.1145/3597503.3639091)

**Labels**: code generation, program synthesis
