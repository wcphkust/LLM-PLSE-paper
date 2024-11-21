# Copiloting the Copilots: Fusing Large Language Models with Completion Engines for Automated Program Repair

**Authors**: Wei, Yuxiang and Xia, Chunqiu Steven and Zhang, Lingming

**Abstract**:

During Automated Program Repair (APR), it can be challenging&nbsp;to synthesize correct patches for real-world systems in general-purpose programming languages. Recent Large Language Models&nbsp;(LLMs) have been shown to be helpful “copilots” in assisting developers with various coding tasks, and have also been directly&nbsp;applied for patch synthesis. However, most LLMs treat programs as&nbsp;sequences of tokens, meaning that they are ignorant of the underlying semantics constraints of the target programming language. This&nbsp;results in plenty of statically invalid generated patches, impeding&nbsp;the practicality of the technique. Therefore, we propose Repilot,&nbsp;a framework to further copilot the AI “copilots” (i.e., LLMs) by&nbsp;synthesizing more valid patches during the repair process. Our key&nbsp;insight is that many LLMs produce outputs autoregressively (i.e.,&nbsp;token by token), resembling human writing programs, which can&nbsp;be significantly boosted and guided through a Completion Engine.&nbsp;Repilot synergistically synthesizes a candidate patch through the&nbsp;interaction between an LLM and a Completion Engine, which 1)&nbsp;prunes away infeasible tokens suggested by the LLM and 2) proactively completes the token based on the suggestions provided by the&nbsp;Completion Engine. Our evaluation on a subset of the widely-used&nbsp;Defects4j 1.2 and 2.0 datasets shows that Repilot fixes 66 and 50&nbsp;bugs, respectively, surpassing the best-performing baseline by 14&nbsp;and 16 bugs fixed. More&nbsp;importantly, Repilot is capable of producing more valid and correct patches than the base LLM when given&nbsp;the same generation budget.

**Link**: [Read Paper](https://doi.org/10.1145/3611643.3616271)

**Labels**: code generation, program repair
