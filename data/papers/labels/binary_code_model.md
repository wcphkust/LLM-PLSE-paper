# Binary Code Model

- [BinCola: Diversity-Sensitive Contrastive Learning for Binary Code Similarity Detection](../venues/TSE2024/paper_14.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Binary Code Similarity Detection (BCSD) is a fundamental binary analysis technique in the area of software security. Recently, advanced deep learning algorithms are integrated into BCSD platforms to achieve superior performance on well-known benchmarks. However, real-world large programs embed more complex diversities due to different compilers, various optimization levels, multiple architectures and even obfuscations. Existing BCSD solutions suffer from low accuracy issues in such complicated r...
  - **Labels**: [static analysis](static_analysis.md), [code similarity analysis](code_similarity_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [BinaryAI: Binary Software Composition Analysis via Intelligent Binary Source Code Matching](../venues/ICSE2024/paper_31.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: While third-party libraries (TPLs) are extensively reused to enhance productivity during software development, they can also introduce potential security risks such as vulnerability propagation. Software composition analysis (SCA), proposed to identify reused TPLs for reducing such risks, has become an essential procedure within modern DevSecOps. As one of the mainstream SCA techniques, binary-to-source SCA identifies the third-party source projects contained in binary files via binary source co...
  - **Labels**: [static analysis](static_analysis.md), [software composition analysis](software_composition_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [Codeart: Better code models by attention regularization when symbols are lacking](../venues/FSE2024/paper_26.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Transformer based code models have impressive performance in many software engineering tasks. However, their effectiveness degrades when symbols are missing or not informative. The reason is that the model may not learn to pay attention to the right correlations/contexts without the help of symbols. We propose a new method to pre-train general code models when symbols are lacking. We observe that in such cases, programs degenerate to something written in a very primitive language. We hence propo...
  - **Labels**: [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [Improving Binary Code Similarity Transformer Models by Semantics-Driven Instruction Deemphasis](../venues/ISSTA2023/paper_5.md), ([ISSTA2023](../venues/ISSTA2023/README.md))

  - **Abstract**: Given a function in the binary executable form, binary code similarity analysis determines a set of similar functions from a large pool of candidate functions. These similar functions are usually compiled from the same source code with different compilation setups. Such analysis has a large number of applications, such as malware detection, code clone detection, and automatic software patching. The state-of-the art methods utilize complex Deep Learning models such as Transformer models. We obser...
  - **Labels**: [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md), [static analysis](static_analysis.md), [code similarity analysis](code_similarity_analysis.md)


- [Jtrans: Jump-aware transformer for binary code similarity detection](../venues/ISSTA2022/paper_1.md), ([ISSTA2022](../venues/ISSTA2022/README.md))

  - **Abstract**: Binary code similarity detection (BCSD) has important applications in various fields such as vulnerabilities detection, software component analysis, and reverse engineering. Recent studies have shown that deep neural networks (DNNs) can comprehend instructions or control-flow graphs (CFG) of binary code and support BCSD. In this study, we propose a novel Transformer-based approach, namely jTrans, to learn representations of binary code. It is the first solution that embeds control flow informati...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [LLM4Decompile: Decompiling Binary Code with Large Language Models](../venues/EMNLP2024/paper_19.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Decompilation aims to convert binary code to high-level source code, but traditional tools like Ghidra often produce results that are difficult to read and execute. Motivated by the advancements in Large Language Models (LLMs), we propose LLM4Decompile, the first and largest open-source LLM series (1.3B to 33B) trained to decompile binary code. We optimize the LLM training process and introduce the LLM4Decompile-End models to decompile binary directly. The resulting models significantly outperfo...
  - **Labels**: [code generation](code_generation.md), [program decompilation](program_decompilation.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [Lmpa: Improving decompilation by synergy of large language model and program analysis](../venues/arXiv2023/paper_2.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: Decompilation aims to recover the source code form of a binary executable. It has many applications in security and software engineering such as malware analysis, vulnerability detection and code reuse. A prominent challenge in decompilation is to recover variable names. We propose a novel method that leverages the synergy of large language model (LLM) and program analysis. Language models encode rich multi-modal knowledge, but its limited input size prevents providing sufficient global context ...
  - **Labels**: [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [PELICAN: exploiting backdoors of naturally trained deep learning models in binary code analysis](../venues/USENIXSec2023/paper_3.md), ([USENIXSec2023](../venues/USENIXSec2023/README.md))

  - **Abstract**: Deep Learning (DL) models are increasingly used in many cyber-security applications and achieve superior performance compared to traditional solutions. In this paper, we study backdoor vulnerabilities in naturally trained models used in binary analysis. These backdoors are not injected by attackers but rather products of defects in datasets and/or training processes. The attacker can exploit these vulnerabilities by injecting some small fixed input pattern (e.g., an instruction) called backdoor ...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [RCFG2Vec: Considering Long-Distance Dependency for Binary Code Similarity Detection](../venues/ASE2024/paper_43.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Binary code similarity detection(BCSD), as a fundamental technique in software security, has various applications, including malware family detection, known vulnerability detection and code plagiarism detection. Recent deep learning-based BCSD approaches have demonstrated promising performance. However, they face two significant challenges that limit detection performance. First, most approaches that use sequence networks (like RNN and Transformer) utilize coarse-grained tokenization methods, wh...
  - **Labels**: [static analysis](static_analysis.md), [code similarity analysis](code_similarity_analysis.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [ReSym: Harnessing LLMs to Recover Variable and Data Structure Symbols from Stripped Binaries](../venues/CCS2024/paper_1.md), ([CCS2024](../venues/CCS2024/README.md))

  - **Abstract**: Decompilation aims to recover a binary executable to the source code form and hence has a wide range of applications in cyber security, such as malware analysis and legacy code hardening. A prominent challenge is to recover variable symbols, including both primitive and complex types such as user-defined data structures, along with their symbol information such as names and types. Existing efforts focus on solving parts of the problem, eg, recovering only types (without names) or only local vari...
  - **Labels**: [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md), [code generation](code_generation.md), [program decompilation](program_decompilation.md)


- [Self-Constructed Context Decompilation with Fined-grained Alignment Enhancement](../venues/EMNLP2024/paper_8.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Decompilation transforms compiled code back into a high-level programming language for analysis when source code is unavailable. Previous work has primarily focused on enhancing decompilation performance by increasing the scale of model parameters or training data for pre-training. Based on the characteristics of the decompilation task, we propose two methods: (1) Without fine-tuning, the Self-Constructed Context Decompilation (sc²dec) method recompiles the LLM’s decompilation results to constru...
  - **Labels**: [code generation](code_generation.md), [program decompilation](program_decompilation.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md), [benchmark](benchmark.md)


- [Source Code Foundation Models are Transferable Binary Analysis Knowledge Bases](../venues/NeurIPS2024/paper_2.md), ([NeurIPS2024](../venues/NeurIPS2024/README.md))

  - **Abstract**: Human-Oriented Binary Reverse Engineering (HOBRE) lies at the intersection of binary and source code, aiming to lift binary code to human-readable content relevant to source code, thereby bridging the binary-source semantic gap. Recent advancements in uni-modal code model pre-training, particularly in generative Source Code Foundation Models (SCFMs) and binary understanding models, have laid the groundwork for transfer learning applicable to HOBRE. However, existing approaches for HOBRE rely hea...
  - **Labels**: [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [WaDec: Decompiling WebAssembly Using Large Language Model](../venues/ASE2024/paper_9.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: WebAssembly (abbreviated Wasm) has emerged as a cornerstone of web development, offering a compact binary format that allows high-performance applications to run at near-native speeds in web browsers. Despite its advantages, Wasm's binary nature presents significant challenges for developers and researchers, particularly regarding readability when debugging or analyzing web applications. Therefore, effective decompilation becomes crucial. Unfortunately, traditional decompilers often struggle wit...
  - **Labels**: [code generation](code_generation.md), [program decompilation](program_decompilation.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)
