# ICLR2024

Number of papers: 8

- **Labels**: [benchmark](../../labels/benchmark.md), [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)

- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)

- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)

- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)

- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)

- **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)

- **Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md)

- **Labels**: [hallucination in reasoning](../../labels/hallucination_in_reasoning.md), [empirical study](../../labels/empirical_study.md)

## [CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules](paper_5.md)
- **Authors**: Hung Le and Hailin Chen and Amrita Saha and Akash Gokul and Doyen Sahoo and Shafiq Joty
- **Abstract**: Large Language Models (LLMs) have already become quite proficient at solving simpler programming tasks like those in HumanEval or MBPP benchmarks. However, solving more complex and competitive programming tasks is still quite challenging for these models - possibly due to their tendency to generate solutions as monolithic code blocks instead of decomposing them into logical sub-tasks and sub-modules. On the other hand, experienced programmers instinctively write modularized code with abstraction...
- **Link**: [Read Paper](https://openreview.net/forum?id=vYhglxSj8j)


## [Guess \& Sketch: Language Model Guided Transpilation](paper_3.md)
- **Authors**: Lee, Celine and Mahmoud, Abdulrahman and Kurek, Michal and Campanoni, Simone and Brooks, David and Chong, Stephen and Wei, Gu-Yeon and Rush, Alexander M
- **Abstract**: Maintaining legacy software requires many software and systems engineering hours. Assembly code programs, which demand low-level control over the computer machine state and have no variable names, are particularly difficult for humans to analyze. Existing conventional program translators guarantee correctness, but are hand-engineered for the source and target programming languages in question. Learned transpilation, i.e. automatic translation of code, offers an alternative to manual re-writing a...
- **Link**: [Read Paper](https://openreview.net/forum?id=qPFsIbF3V6)


## [Hypothesis search: Inductive reasoning with language models](paper_2.md)
- **Authors**: Wang, Ruocheng and Zelikman, Eric and Poesia, Gabriel and Pu, Yewen and Haber, Nick and Goodman, Noah D
- **Abstract**: Inductive reasoning is a core problem-solving capacity: humans can identify underlying principles from a few examples, which can then be robustly generalized to novel scenarios. Recent work has evaluated large language models (LLMs) on inductive reasoning tasks by directly prompting them yielding "in context learning." This can work well for straightforward inductive tasks, but performs very poorly on more complex tasks such as the Abstraction and Reasoning Corpus (ARC). In this work, we propose...
- **Link**: [Read Paper](https://openreview.net/forum?id=G7UtIGQmjm)


## [Learning performance-improving code edits](paper_4.md)
- **Authors**: Shypula, Alexander and Madaan, Aman and Zeng, Yimeng and Alon, Uri and Gardner, Jacob and Hashemi, Milad and Neubig, Graham and Ranganathan, Parthasarathy and Bastani, Osbert and Yazdanbakhsh, Amir
- **Abstract**: With the waning of Moore's law, optimizing program performance has become a major focus of software research. However, high-level optimizations such as API and algorithm changes remain elusive due to the difficulty of understanding the semantics of code. Simultaneously, pretrained large language models (LLMs) have demonstrated strong capabilities at solving a wide range of programming tasks. To that end, we introduce a framework for adapting LLMs to high-level program optimization. First, we cur...
- **Link**: [Read Paper](https://arxiv.org/pdf/2302.07867)


## [Lemur: Integrating large language models in automated program verification](paper_6.md)
- **Authors**: Wu, Haoze and Barrett, Clark and Narodytska, Nina
- **Abstract**: The demonstrated code-understanding capability of LLMs raises the question of whether they can be used for automated program verification, a task that typically demands high-level abstract reasoning about program properties that is challenging for verification tools. We propose a general methodology to combine the power of LLMs and automated reasoners for automated program verification. We formally describe this methodology as a set of derivation rules and prove its soundness. We instantiate the...
- **Link**: [Read Paper](https://openreview.net/forum?id=Q3YaCghZNt)


## [Self-contradictory hallucinations of large language models: Evaluation, detection and mitigation](paper_8.md)
- **Authors**: M{\"u}ndler, Niels and He, Jingxuan and Jenko, Slobodan and Vechev, Martin
- **Abstract**: Large language models (large LMs) are susceptible to producing text that contains hallucinated content. An important instance of this problem is self-contradiction, where the LM generates two contradictory sentences within the same context. In this work, we present a comprehensive investigation into self-contradiction for various instruction-tuned LMs, covering evaluation, detection, and mitigation. Our primary evaluation task is open-domain text generation, but we also demonstrate the applicabi...
- **Link**: [Read Paper](https://arxiv.org/abs/2305.15852)


## [Swe-bench: Can language models resolve real-world github issues?](paper_1.md)
- **Authors**: Jimenez, Carlos E and Yang, John and Wettig, Alexander and Yao, Shunyu and Pei, Kexin and Press, Ofir and Narasimhan, Karthik
- **Abstract**: Language models have outpaced our ability to evaluate them effectively, but for their future development it is essential to study the frontier of their capabilities. We find real-world software engineering to be a rich, sustainable, and challenging testbed for evaluating the next generation of language models. To this end, we introduce SWE-bench, an evaluation framework consisting of 2,294 software engineering problems drawn from real GitHub issues and corresponding pull requests across 12 popul...
- **Link**: [Read Paper](https://arxiv.org/pdf/2310.06770)


## [Teaching large language models to self-debug](paper_7.md)
- **Authors**: Chen, Xinyun and Lin, Maxwell and Sch{\"a}rli, Nathanael and Zhou, Denny
- **Abstract**: Large language models (LLMs) have achieved impressive performance on code generation. However, for complex programming tasks, generating the correct solution in one go becomes challenging, thus some prior works have designed program repair approaches to improve code generation performance. In this work, we propose Self-Debugging, which teaches a large language model to debug its predicted program via few-shot demonstrations. In particular, we demonstrate that Self-Debugging can teach the large l...
- **Link**: [Read Paper](https://openreview.net/forum?id=KuPixIqPiq)
