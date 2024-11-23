# TSE2023

Number of papers: 6

- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)

- **Labels**: [general coding task](../../labels/general_coding_task.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [benchmark](../../labels/benchmark.md)

- **Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

- **Labels**: [general coding task](../../labels/general_coding_task.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

- **Labels**: [static analysis](../../labels/static_analysis.md), [code search](../../labels/code_search.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

## [CoSS: Leveraging Statement Semantics for Code Summarization](paper_4.md)
- **Authors**: Shi, Chaochen and Cai, Borui and Zhao, Yao and Gao, Longxiang and Sood, Keshav and Xiang, Yong
- **Abstract**: Automated code summarization tools allow generating descriptions for code snippets in natural language, which benefits software development and maintenance. Recent studies demonstrate that the quality of generated summaries can be improved by using additional code representations beyond token sequences. The majority of contemporary approaches mainly focus on extracting code syntactic and structural information from abstract syntax trees (ASTs). However, from the view of macro-structures, it is c...
- **Link**: [Read Paper](https://doi.org/10.1109/TSE.2023.3256362)


## [CombTransformers: Statement-Wise Transformers for Statement-Wise Representations](paper_2.md)
- **Authors**: Bertolotti, Francesco and Cazzola, Walter
- **Abstract**: This study presents a novel category of Transformer architectures known as comb transformers, which effectively reduce the space complexity of the self-attention layer from a quadratic to a subquadratic level. This is achieved by processing sequence segments independently and incorporating &lt;inline-formula&gt;&lt;tex-math notation="LaTeX"&gt;$mathcal{X}$&lt;/tex-math&gt;&lt;alternatives&gt;&lt;mml:math&gt;&lt;mml:mrow&gt;&lt;mml:mi mathvariant="script"&gt;X&lt;/mml:mi&gt;&lt;/mml:mrow&gt;&lt;/...
- **Link**: [Read Paper](https://doi.org/10.1109/TSE.2023.3310793)


## [MultiPL-E: A Scalable and Polyglot Approach to Benchmarking Neural Code Generation](paper_3.md)
- **Authors**: Cassano, Federico and Gouwar, John and Nguyen, Daniel and Nguyen, Sydney and Phipps-Costin, Luna and Pinckney, Donald and Yee, Ming-Ho and Zi, Yangtian and Anderson, Carolyn Jane and Feldman, Molly Q and Guha, Arjun and Greenberg, Michael and Jangda, Abhinav
- **Abstract**: Large language models have demonstrated the ability to generate both natural language and programming language text. Although contemporary code generation models are trained on corpora with several programming languages, they are tested using benchmarks that are typically monolingual. The most widely used code generation benchmarks only target Python, so there is little quantitative evidence of how code generation models perform on other programming languages. We propose MultiPL-E, a system for ...
- **Link**: [Read Paper](https://doi.org/10.1109/TSE.2023.3267446)


## [On the Effectiveness of Transfer Learning for Code Search](paper_6.md)
- **Authors**: Salza, Pasquale and Schwizer, Christoph and Gu, Jian and Gall, Harald C.
- **Abstract**: The Transformer architecture and transfer learning have marked a quantum leap in natural language processing, improving the state of the art across a range of text-based tasks. This paper examines how these advancements can be applied to and improve code search. To this end, we pre-train a BERT-based model on combinations of natural language and source code data and fine-tune it on pairs of StackOverflow question titles and code answers. Our results show that the pre-trained models consistently ...
- **Link**: [Read Paper](https://doi.org/10.1109/TSE.2022.3192755)


## [Using Transfer Learning for Code-Related Tasks](paper_5.md)
- **Authors**: Mastropaolo, Antonio and Cooper, Nathan and Palacio, David Nader and Scalabrino, Simone and Poshyvanyk, Denys and Oliveto, Rocco and Bavota, Gabriele
- **Abstract**: Deep learning (DL) techniques have been used to support several code-related tasks such as code summarization and bug-fixing. In particular, pre-trained transformer models are on the rise, also thanks to the excellent results they achieved in Natural Language Processing (NLP) tasks. The basic idea behind these models is to first pre-train them on a generic dataset using a self-supervised task (e.g., filling masked words in sentences). Then, these models are fine-tuned to support specific tasks o...
- **Link**: [Read Paper](https://doi.org/10.1109/TSE.2022.3183297)


## [VulExplainer: A Transformer-Based Hierarchical Distillation for Explaining Vulnerability Types](paper_1.md)
- **Authors**: Fu, Michael and Nguyen, Van and Tantithamthavorn, Chakkrit Kla and Le, Trung and Phung, Dinh
- **Abstract**: Deep learning-based vulnerability prediction approaches are proposed to help under-resourced security practitioners to detect vulnerable functions. However, security practitioners still do not know what type of vulnerabilities correspond to a given prediction (aka CWE-ID). Thus, a novel approach to explain the type of vulnerabilities for a given prediction is imperative. In this paper, we propose &lt;italic&gt;VulExplainer&lt;/italic&gt;, an approach to explain the type of vulnerabilities. We re...
- **Link**: [Read Paper](https://doi.org/10.1109/TSE.2023.3305244)
