# Bridging Gaps in LLM Code Translation: Reducing Errors with Call Graphs and Bridged Debuggers

**Authors**: Luo, Yang and Yu, Richard and Zhang, Fajun and Liang, Ling and Xiong, Yongqiang

**Abstract**:

When using large language models (LLMs) for code translation of complex software, numerous compilation and runtime errors can occur due to insufficient context awareness. To address this issue, this paper presents a code translation method based on call graphs and bridged debuggers: TransGraph. TransGraph first obtains the call graph of the entire code project using the Language Server Protocol, which provides a detailed description of the function call relationships in the program. Through this structured view of the code, LLMs can more effectively handle large-scale and complex codebases, significantly reducing compilation errors. Furthermore, TransGraph, combined with bridged debuggers and dynamic test case generation, significantly reduces runtime errors, overcoming the limitations of insufficient test case coverage in traditional methods. In experiments on six datasets including CodeNet and Avatar, TransGraph outperformed existing code translation methods and LLMs in terms of translation accuracy, with improvements of up to 10.2\%.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695322)

**Labels**: code generation, program transformation
