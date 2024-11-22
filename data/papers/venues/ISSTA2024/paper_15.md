# ThinkRepair: Self-Directed Automated Program Repair

**Authors**: Yin, Xin and Ni, Chao and Wang, Shaohua and Li, Zhenhao and Zeng, Limin and Yang, Xiaohu

**Abstract**:

Though many approaches have been proposed for Automated Program Repair (APR) and indeed achieved remarkable performance, they still have limitations in fixing bugs that require analyzing and reasoning about the logic of the buggy program. Recently, large language models (LLMs) instructed by prompt engineering have attracted much attention for their powerful ability to address many kinds of tasks including bug-fixing. However, the quality of the prompt will highly affect the ability of LLMs and manually constructing high-quality prompts is a costly endeavor.   To address this limitation, we propose a self-directed LLM-based automated program repair, ThinkRepair, with two main phases: collection phase and fixing phase. The former phase automatically collects various chains of thoughts that constitute pre-fixed knowledge by instructing LLMs with the Chain-of-Thought (CoT) prompt. The latter phase targets fixing a bug by first selecting examples for few-shot learning and second automatically interacting with LLMs, optionally appending with feedback of testing information.   Evaluations on two widely studied datasets (Defects4J and QuixBugs) by comparing ThinkRepair with 12 SOTA APRs indicate the priority of ThinkRepair in fixing bugs. Notably, ThinkRepair fixes 98 bugs and improves baselines by 27\%∼344.4\% on Defects4J V1.2. On Defects4J V2.0, ThinkRepair fixes 12∼65 more bugs than the SOTA APRs. Additionally, ThinkRepair also makes a considerable improvement on QuixBugs (31 for Java and 21 for Python at most).

**Link**: [Read Paper](https://doi.org/10.1145/3650212.3680359)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)
