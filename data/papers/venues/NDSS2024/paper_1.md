# DeGPT: Optimizing Decompiler Output with LLM

**Authors**: Peiwei Hu and Chinese Academy of Sciences and Beijing and China) and Ruigang Liang and Chinese Academy of Sciences and Beijing and China) and Kai Chen and Chinese Academy of Sciences and China)

**Abstract**:

Reverse engineering is essential in malware analysis, vulnerability discovery, etc. Decompilers assist the reverse engineers by lifting the assembly to the high-level programming language, which highly boosts binary comprehension. However, decompilers suffer from problems such as meaningless variable names, redundant variables, and lacking comments describing the purpose of the code. Previous studies have shown promising performance in refining the decompiler output by training the models with huge datasets containing various decompiler outputs. However, even datasets that take much time to construct cover limited binaries in the real world. The performance degrades severely facing the binary migration.In this paper, we present DeGPT, an end-to-end framework aiming to optimize the decompiler output to improve its readability and simplicity and further assist the reverse engineers in understanding the binaries better. The Large Language Model (LLM) can mitigate performance degradation with its extraordinary ability endowed by large model size and training set containing rich multi-modal data. However, its potential is difficult to unlock through one-shot use. Thus, we propose the three-role mechanism, which includes referee (R_ref), advisor (R_adv), and operator (R_ope), to adapt the LLM to our optimization tasks. Specifically, R_ref provides the optimization scheme for the target decompiler output, while R_adv gives the rectification measures based on the scheme, and R_ope inspects whether the optimization changes the original function semantics and concludes the final verdict about whether to accept the optimizations. We evaluate DeGPT on the datasets containing decompiler outputs of various software, such as the practical command line tools, malware, a library for audio processing, and implementations of algorithms. The experimental results show that even on the output of the current top-level decompiler (Ghidra), DeGPT can achieve 24.4% reduction in the cognitive burden of understanding the decompiler outputs and provide comments of which 62.9% can provide practical semantics for the reverse engineers to help the understanding of binaries. Our user surveys also show that the optimizations can significantly simplify the code and add helpful semantic information (variable names and comments), facilitating a quick and accurate understanding of the binary.

**Link**: [Read Paper](https://www.ndss-symposium.org/ndss-paper/degpt-optimizing-decompiler-output-with-llm)

**Labels**: [code generation](../../labels/code_generation.md), [program decompilation](../../labels/program_decompilation.md)