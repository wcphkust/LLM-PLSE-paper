# A Pair Programming Framework for Code Generation via Multi-Plan Exploration and Feedback-Driven Refinement

**Authors**: Zhang, Huan and Cheng, Wei and Wu, Yuhan and Hu, Wei

**Abstract**:

Large language models (LLMs) have achieved impressive performance on code generation. Although prior studies enhanced LLMs with prompting techniques and code refinement, they still struggle with complex programming problems due to rigid solution plans. In this paper, we draw on pair programming practices to propose PairCoder, a novel LLM-based framework for code generation. PairCoder incorporates two collaborative LLM agents, namely a Navigator agent for high-level planning and a Driver agent for specific implementation. The Navigator is responsible for proposing promising solution plans, selecting the current optimal plan, and directing the next iteration round based on execution feedback. The Driver follows the guidance of Navigator to undertake initial code generation, code testing, and refinement. This interleaved and iterative workflow involves multi-plan exploration and feedback-based refinement, which mimics the collaboration of pair programmers. We evaluate PairCoder with both open-source and closed-source LLMs on various code generation benchmarks. Extensive experimental results demonstrate the superior accuracy of PairCoder, achieving relative pass@1 improvements of 12.00\%--162.43\% compared to prompting LLMs directly.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695506)

**Labels**: code generation, program synthesis, agent design, planning
