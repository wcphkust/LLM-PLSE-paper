# IR Code Model

- [Fair: Flow type-aware pre-training of compiler intermediate representations](../venues/ICSE2024/paper_21.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: While the majority of existing pre-trained models from code learn source code features such as code tokens and abstract syntax trees, there are some other works that focus on learning from compiler intermediate representations (IRs). Existing IR-based models typically utilize IR features such as instructions, control and data flow graphs (CDFGs), call graphs, etc. However, these methods confuse variable nodes and instruction nodes in a CDFG and fail to distinguish different types of flows, and t...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [IR code model](IR_code_model.md)


- [How could neural networks understand programs?](../venues/ICML2021/paper_1.md), ([ICML2021](../venues/ICML2021/README.md))

  - **Abstract**: Semantic understanding of programs is a fundamental problem for programming language processing (PLP). Recent works that learn representations of code based on pre-training techniques in NLP have pushed the frontiers in this direction. However, the semantics of PL and NL have essential differences. These being ignored, we believe it is difficult to build a model to better understand programs, by either directly applying off-the-shelf NLP pre-training techniques to the source code, or adding feat...
  - **Labels**: [general coding task](general_coding_task.md), [code model](code_model.md), [code model training](code_model_training.md), [IR code model](IR_code_model.md)


- [Meta large language model compiler: Foundation models of compiler optimization](../venues/Meta2024/paper_1.md), ([Meta2024](../venues/Meta2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated remarkable capabilities across a variety of software engineering and coding tasks. However, their application in the domain of code and compiler optimization remains underexplored. Training LLMs is resource-intensive, requiring substantial GPU hours and extensive data collection, which can be prohibitive. To address this gap, we introduce Meta Large Language Model Compiler (LLM Compiler), a suite of robust, openly available, pre-trained models speci...
  - **Labels**: [static analysis](static_analysis.md), [program optimization](program_optimization.md), [code model](code_model.md), [code model training](code_model_training.md), [IR code model](IR_code_model.md)


- [Programl: A graph-based program representation for data flow analysis and compiler optimizations](../venues/ICML2021/paper_2.md), ([ICML2021](../venues/ICML2021/README.md))

  - **Abstract**: Machine learning (ML) is increasingly seen as a viable approach for building compiler optimization heuristics, but many ML methods cannot replicate even the simplest of the data flow analyses that are critical to making good optimization decisions. We posit that if ML cannot do that, then it is insufficiently able to reason about programs. We formulate data flow analyses as supervised learning tasks and introduce a large open dataset of programs and their corresponding labels from several analys...
  - **Labels**: [static analysis](static_analysis.md), [data-flow analysis](data-flow_analysis.md), [program optimization](program_optimization.md), [code model](code_model.md), [code model training](code_model_training.md), [IR code model](IR_code_model.md)


- [UniCoder: Scaling Code Large Language Model via Universal Code](../venues/ACL2024/paper_10.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Intermediate reasoning or acting steps have successfully improved large language models (LLMs) for handling various downstream natural language processing (NLP) tasks.When applying LLMs for code generation, recent works mainly focus on directing the models to articulate intermediate natural-language reasoning steps, as in chain-of-thought (CoT) prompting, and then output code with the natural language or other structured intermediate steps. However, such output is not suitable for code translati...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model training](code_model_training.md), [IR code model](IR_code_model.md)
