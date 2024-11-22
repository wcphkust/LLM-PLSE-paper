# Enhancing Large Language Models in Coding Through Multi-Perspective Self-Consistency

**Authors**: Huang, Baizhou and Lu, Shuai and Wan, Xiaojun and Duan, Nan

**Abstract**:

Large language models (LLMs) have exhibited remarkable ability in code generation. However, generating the correct solution in a single attempt still remains a challenge. Prior works utilize verification properties in software engineering to verify and re-rank solutions in a majority voting manner. But the assumption behind them that generated verification properties have better qualities than solutions may not always hold. In this paper, we treat them equally as different perspectives of LLMs’ reasoning processes. We propose the Multi-Perspective Self-Consistency (MPSC) framework incorporating both inter- and intra-consistency across outputs from multiple perspectives. Specifically, we prompt LLMs to generate diverse outputs from three perspectives, Solution, Specification and Test case, constructing a 3-partite graph. With two measure functions of consistency, we embed both inter- and intra-consistency information into the graph. The optimal choice of solutions is then determined based on analysis in the graph.MPSC significantly boosts performance of foundation models (ChatGPT in this paper) on various benchmarks, including HumanEval (+15.91%), MBPP (+6.43%) and CodeContests (+9.37%), even surpassing GPT-4.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.78)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)
