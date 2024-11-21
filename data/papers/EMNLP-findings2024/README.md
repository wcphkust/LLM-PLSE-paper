# EMNLP-findings2024

Number of papers: 18

## [TransLLaMa: LLM-based Simultaneous Translation System](paper_1.md)
- **Authors**: Koshkin, Roman and Sudoh, Katsuhito and Nakamura, Satoshi
- **Abstract**: Decoder-only large language models (LLMs) have recently demonstrated impressive capabilities in text generation and reasoning. Nonetheless, they have limited applications in simultaneous machine translation (SiMT), currently dominated by encoder-decoder transformers. This study demonstrates that, af...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.27)
- **Labels**: code generation, program transformation, empirical study

## [Introducing Compiler Semantics into Large Language Models as Programming Language Translators: A Case Study of C to x86 Assembly](paper_2.md)
- **Authors**: Zhang, Shuoming and Zhao, Jiacheng and Xia, Chunwei and Wang, Zheng and Chen, Yunji and Cui, Huimin
- **Abstract**: Compilers are complex software containing millions of lines of code, taking years to develop. This paper investigates to what extent Large Language Models (LLMs) can replace hand-crafted compilers in translating high-level programming languages to machine instructions, using C to x86 assembly as a c...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.55)
- **Labels**: code generation, program transformation

## [EvoR: Evolving Retrieval for Code Generation](paper_3.md)
- **Authors**: Su, Hongjin and Jiang, Shuyang and Lai, Yuhang and Wu, Haoyuan and Shi, Boao and Liu, Che and Liu, Qian and Yu, Tao
- **Abstract**: Recently the retrieval-augmented generation (RAG) has been successfully applied in code generation. However, existing pipelines for retrieval-augmented code generation (RACG) employ static knowledge bases with a single source, limiting the adaptation capabilities of Large Language Models (LLMs) to d...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.143)
- **Labels**: code generation, code completion, source code model, prompt strategy, RAG

## [NormTab: Improving Symbolic Reasoning in LLMs Through Tabular Data Normalization](paper_4.md)
- **Authors**: Nahid, Md and Rafiei, Davood
- **Abstract**: In recent years, Large Language Models (LLMs) have demonstrated remarkable capabilities in parsing textual data and generating code. However, their performance in tasks involving tabular data, especially those requiring symbolic reasoning, faces challenges due to the structural variance and inconsis...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.203)
- **Labels**: static analysis, fundamental analysis

## [Sanitizing Large Language Models in Bug Detection with Data-Flow](paper_5.md)
- **Authors**: Wang, Chengpeng and Zhang, Wuqi and Su, Zian and Xu, Xiangzhe and Zhang, Xiangyu
- **Abstract**: Large language models (LLMs) show potential in code reasoning tasks, facilitating the customization of detecting bugs in software development. However, the hallucination effect can significantly compromise the reliability of bug reports. This work formulates a new schema of bug detection and present...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.217)
- **Labels**: static analysis, bug detection, fundamental analysis

## [Stanceformer: Target-Aware Transformer for Stance Detection](paper_6.md)
- **Authors**: Garg, Krishna and Caragea, Cornelia
- **Abstract**: The task of Stance Detection involves discerning the stance expressed in a text towards a specific subject or target. Prior works have relied on existing transformer models that lack the capability to prioritize targets effectively. Consequently, these models yield similar performance regardless of ...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.286)
- **Labels**: static analysis, bug detection, empirical study

## [Defending Large Language Models Against Jailbreak Attacks via Layer-specific Editing](paper_7.md)
- **Authors**: Zhao, Wei and Li, Zhe and Li, Yige and Zhang, Ye and Sun, Jun
- **Abstract**: Large language models (LLMs) are increasingly being adopted in a wide range of real-world applications. Despite their impressive performance, recent studies have shown that LLMs are vulnerable to deliberately crafted adversarial prompts even when aligned via Reinforcement Learning from Human Feedbac...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.293)
- **Labels**: code model, security, defense

## [Self-Constructed Context Decompilation with Fined-grained Alignment Enhancement](paper_8.md)
- **Authors**: Feng, Yunlong and Teng, Dechuan and Xu, Yang and Mu, Honglin and Xu, Xiao and Qin, Libo and Zhu, Qingfu and Che, Wanxiang
- **Abstract**: Decompilation transforms compiled code back into a high-level programming language for analysis when source code is unavailable. Previous work has primarily focused on enhancing decompilation performance by increasing the scale of model parameters or training data for pre-training. Based on the char...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.385)
- **Labels**: code generation, program decompilation, code model, training, binary code model, benchmark

## [AutoDetect: Towards a Unified Framework for Automated Weakness Detection in Large Language Models](paper_9.md)
- **Authors**: Cheng, Jiale and Lu, Yida and Gu, Xiaotao and Ke, Pei and Liu, Xiao and Dong, Yuxiao and Wang, Hongning and Tang, Jie and Huang, Minlie
- **Abstract**: Although Large Language Models (LLMs) are becoming increasingly powerful, they still exhibit significant but subtle weaknesses, such as mistakes in instruction-following or coding tasks.As these unexpected errors could lead to severe consequences in practical deployments, it is crucial to investigat...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.397)
- **Labels**: code model, security, attack, empirical study

## [CodeIP: A Grammar-Guided Multi-Bit Watermark for Large Language Models of Code](paper_10.md)
- **Authors**: Guan, Batu and Wan, Yao and Bi, Zhangqian and Wang, Zheng and Zhang, Hongyu and Zhou, Pan and Sun, Lichao
- **Abstract**: Large Language Models (LLMs) have achieved remarkable progress in code generation. It now becomes crucial to identify whether the code is AI-generated and to determine the specific model used, particularly for purposes such as protecting Intellectual Property (IP) in industry and preventing cheating...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.541)
- **Labels**: code generation, program synthesis, code model, security, defense

## [Instruct, Not Assist: LLM-based Multi-Turn Planning and Hierarchical Questioning for Socratic Code Debugging](paper_11.md)
- **Authors**: Kargupta, Priyanka and Agarwal, Ishika and Tur, Dilek Hakkani and Han, Jiawei
- **Abstract**: Socratic questioning is an effective teaching strategy, encouraging critical thinking and problem-solving. The conversational capabilities of large language models (LLMs) show great potential for providing scalable, real-time student guidance. However, current LLMs often give away solutions directly...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.553)
- **Labels**: program testing, debugging, agent design, planning

## [Can LLMs Reason in the Wild with Programs?](paper_12.md)
- **Authors**: Yang, Yuan and Xiong, Siheng and Payani, Ali and Shareghi, Ehsan and Fekri, Faramarz
- **Abstract**: Large Language Models (LLMs) have shown superior capability to solve reasoning problems with programs. While being a promising direction, most of such frameworks are trained and evaluated in settings with a prior knowledge of task requirements. However, as LLMs become more capable, it is necessary t...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.573)
- **Labels**: prompt strategy, reason with code

## [Rethinking Code Refinement: Learning to Judge Code Efficiency](paper_13.md)
- **Authors**: Seo, Minju and Baek, Jinheon and Hwang, Sung Ju
- **Abstract**: Large Language Models (LLMs) have demonstrated impressive capabilities in understanding and generating codes. Due to these capabilities, many recent methods are proposed to automatically refine the codes with LLMs. However, we should rethink that the refined codes (from LLMs and even humans) are not...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.645)
- **Labels**: code generation, program transformation, code model, training, source code model

## [Revisiting the Impact of Pursuing Modularity for Code Generation](paper_14.md)
- **Authors**: Kang, Deokyeong and Seo, KiJung and Kim, Taeuk
- **Abstract**: Modular programming, which aims to construct the final program by integrating smaller, independent building blocks, has been regarded as a desirable practice in software development. However, with the rise of recent code generation agents built upon large language models (LLMs), a question emerges: ...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.676)
- **Labels**: code generation, program synthesis, empirical study

## [Enhancing Discourse Dependency Parsing with Sentence Dependency Parsing: A Unified Generative Method Based on Code Representation](paper_15.md)
- **Authors**: Shen, Zizhuo and Shao, Yanqiu and Li, Wei
- **Abstract**: Due to the high complexity of Discourse Dependency Parsing (DDP) tasks, their existing annotation resources are relatively scarce compared to other NLP tasks, and different DDP tasks also have significant differences in annotation schema. These issues have led to the dilemma of low resources for DDP...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.729)
- **Labels**: code generation, program synthesis, code model, training, source code model

## [On Leakage of Code Generation Evaluation Datasets](paper_16.md)
- **Authors**: Matton, Alexandre and Sherborne, Tom and Aumiller, Dennis and Tommasone, Elena and Alizadeh, Milad and He, Jingyi and Ma, Raymond and Voisin, Maxime and Gilsenan-McMahon, Ellen and Gallé, Matthias
- **Abstract**: In this paper, we consider contamination by code generation test sets, in particular in their use in modern large language models.We discuss three possible sources of such contamination and show findings supporting each of them: (i) direct data leakage, (ii) indirect data leakage through the use of ...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.772)
- **Labels**: code generation, program synthesis, benchmark

## [Socratic Human Feedback (SoHF): Expert Steering Strategies for LLM Code Generation](paper_17.md)
- **Authors**: Chidambaram, Subramanian and Li, Li Erran and Bai, Min and Li, Xiaopeng and Lin, Kaixiang and Zhou, Xiong and Williams, Alex C.
- **Abstract**: Large Language Models (LLMs) are increasingly used for generating code solutions, empowered by features like self-debugging and self-reflection. However, LLMs often struggle with complex programming problems without human guidance. This paper investigates the strategies employed by expert programmer...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.908)
- **Labels**: code generation, program synthesis, empirical study

## [PythonSaga: Redefining the Benchmark to Evaluate Code Generating LLMs](paper_18.md)
- **Authors**: Yadav, Ankit and Beniwal, Himanshu and Singh, Mayank
- **Abstract**: Driven by the surge in code generation using large language models (LLMs), numerous benchmarks have emerged to evaluate these LLMs capabilities. We conducted a large-scale human evaluation of *HumanEval* and *MBPP*, two popular benchmarks for Python code generation, analyzing their diversity and dif...
- **Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.996)
- **Labels**: code generation, program synthesis, benchmark

