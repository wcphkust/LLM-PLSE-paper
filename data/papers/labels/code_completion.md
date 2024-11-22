# Code Completion

- [A Static Evaluation of Code Completion by Large Language Models](../venues/ACL2023/paper_12.md), ([ACL2023](../venues/ACL2023/README.md))

  - **Abstract**: Large language models trained on code have shown great potential to increase productivity of software developers. Several execution-based benchmarks have been proposed to evaluate functional correctness of model-generated code on simple programming problems. Nevertheless, it is expensive to perform the same evaluation on complex real-world projects considering the execution cost. On the other hand, static analysis tools such as linters, which can detect errors without running the program, haven’...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [empirical study](empirical_study.md)


- [Attribution-guided Adversarial Code Prompt Generation for Code Completion Models](../venues/ASE2024/paper_45.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Large language models have made significant progress in code completion, which may further remodel future software development. However, these code completion models are found to be highly risky as they may introduce vulnerabilities unintentionally or be induced by a special input, i.e., adversarial code prompt. Prior studies mainly focus on the robustness of these models, but their security has not been fully analyzed.In this paper, we propose a novel approach AdvPro that can automatically gene...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model security](code_model_security.md), [attack](attack.md)


- [CCTest: Testing and Repairing Code Completion Systems](../venues/ICSE2023/paper_2.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Code completion, a highly valuable topic in the software development domain, has been increasingly promoted for use by recent advances in large language models (LLMs). To date, visible LLM-based code completion frameworks such as GitHub Copilot and GPT are trained using deep learning over vast quantities of unstructured text and open source code. As the paramount component and the cornerstone in daily programming tasks, code completion has largely boosted professionals' efficiency in building re...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md)


- [CoEdPilot: Recommending Code Edits with Learned Prior Edit Relevance, Project-wise Awareness, and Interactive Nature](../venues/ISSTA2024/paper_8.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Recent years have seen the development of LLM-based code generation. Compared to generating code in a software project, incremental code edits are empirically observed to be more frequent. The emerging code editing approaches usually formulate the problem as generating an edit based on known relevant prior edits and context. However, practical code edits can be more complicated. First, an editing session can include multiple (ir)relevant edits to the code under edit. Second, the inference of the...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [DiffCoder: Enhancing Large Language Model on API Invocation via Analogical Code Exercises](../venues/FSE2024/paper_16.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: The task of code generation aims to generate code solutions based on given programming problems. Recently, code large language models (code LLMs) have shed new light on this task, owing to their formidable code generation capabilities. While these models are powerful, they seldom focus on further improving the accuracy of library-oriented API invocation. Nonetheless, programmers frequently invoke APIs in routine coding tasks. In this paper, we aim to enhance the proficiency of existing code LLMs...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md)


- [Domain Adaptive Code Completion via Language Models and Decoupled Domain Databases](../venues/ASE2023/paper_18.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Large Language Models (LLMs) have demonstrated remarkable performance in code completion. However, due to the lack of domain-specific knowledge, they may not be optimal in completing code that requires intensive domain knowledge for example completing the library names. Although there are several works that have confirmed the effectiveness of fine-tuning techniques to adapt language models for code completion in specific domains. They are limited by the need for constant fine-tuning of the model...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [DroidCoder: Enhanced Android Code Completion with Context-Enriched Retrieval-Augmented Generation](../venues/ASE2024/paper_13.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Android is the most popular mobile operating system. However, Android development requires extensive coding, especially for unique features such as lifecycle callbacks and UI widgets. Existing code completion methods typically utilize Retrieval-Augmented Generation (RAG) to provide contextual information for pre-trained code large language models (Code LLMs) to perform completion. Despite considerable progress in these methods, their effectiveness in Android development remains limited. This is ...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [EvoR: Evolving Retrieval for Code Generation](../venues/EMNLP2024/paper_3.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Recently the retrieval-augmented generation (RAG) has been successfully applied in code generation. However, existing pipelines for retrieval-augmented code generation (RACG) employ static knowledge bases with a single source, limiting the adaptation capabilities of Large Language Models (LLMs) to domains they have insufficient knowledge of. In this work, we develop a novel pipeline, EVOR, that employs the synchronous evolution of both queries and diverse knowledge bases. On two realistic settin...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [source code model](source_code_model.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [Follow-Up Attention: An Empirical Study of Developer and Neural Model Code Exploration](../venues/TSE2024/paper_12.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: Recent neural models of code, such as OpenAI Codex and AlphaCode, have demonstrated remarkable proficiency at code generation due to the underlying attention mechanism. However, it often remains unclear how the models actually process code, and to what extent their reasoning and the way their attention mechanism scans the code matches the patterns of developers. A poor understanding of the model reasoning process limits the way in which current neural models are leveraged today, so far mostly fo...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md), [benchmark](benchmark.md)


- [Grace: Language Models Meet Code Edits](../venues/FSE2023/paper_4.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Developers spend a significant amount of time in editing code for a variety of reasons such as bug fixing or adding new features. Designing effective methods to predict code edits has been an active yet challenging area of research due to the diversity of code edits and the difficulty of capturing the developer intent. In this work, we address these challenges by endowing pre-trained large language models (LLMs) with the knowledge of relevant prior associated edits, which we call the Grace (Gene...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph](../venues/ASE2024/paper_10.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: The performance of repository-level code completion depends upon the effective leverage of both general and repository-specific knowledge. Despite the impressive capability of code LLMs in general code completion tasks, they often exhibit less satisfactory performance on repository-level completion due to the lack of repository-specific knowledge in these LLMs. To address this problem, we propose GraphCoder, a retrieval-augmented code completion framework that leverages LLMs' general code knowle...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md)


- [Grounded Copilot: How Programmers Interact with Code-Generating Models](../venues/OOPLSA2023/paper_1.md), ([OOPLSA2023](../venues/OOPLSA2023/README.md))

  - **Abstract**: Powered by recent advances in code-generating models, AI assistants like Github Copilot promise to change the face of programming forever. But what is this new face of programming? We present the first grounded theory analysis of how programmers interact with Copilot, based on observing 20 participants—with a range of prior experience using the assistant—as they solve diverse programming tasks across four languages. Our main finding is that interactions with programming assistants are bimodal: i...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [empirical study](empirical_study.md)


- [HiRoPE: Length Extrapolation for Code Models Using Hierarchical Position](../venues/ACL2024/paper_2.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Addressing the limitation of context length in large language models for code-related tasks is the primary focus of this paper. Existing LLMs are constrained by their pre-trained context lengths, leading to performance issues in handling long complex code sequences. Inspired by how human programmers navigate code, we introduce Hierarchical Rotary Position Embedding (HiRoPE), a novel approach that enhances the traditional rotary position embedding into a hierarchical format based on the hierarchi...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [Language Models for Code Completion: A Practical Evaluation](../venues/ICSE2024/paper_26.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Transformer-based language models for automatic code completion have shown great promise so far, yet the evaluation of these models rarely uses real data. This study provides both quantitative and qualitative assessments of three public code language models when completing real-world code. We first developed an open-source IDE extension, Code4Me, for the online evaluation of the models. We collected real auto-completion usage data for over a year from more than 1200 users, resulting in over 600K...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md)


- [LongCoder: {A} Long-Range Pre-trained Language Model for Code Completion](../venues/ICML2023/paper_1.md), ([ICML2023](../venues/ICML2023/README.md))

  - **Abstract**: In this paper, we introduce a new task for code completion that focuses on handling long code input and propose a sparse Transformer model, called LongCoder, to address this task. LongCoder employs a sliding window mechanism for self-attention and introduces two types of globally accessible tokens-bridge tokens and memory tokens-to improve performance and efficiency. Bridge tokens are inserted throughout the input sequence to aggregate local information and facilitate global interaction, while m...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model training](code_model_training.md), [source code model](source_code_model.md)


- [On the Applicability of Language Models to Block-Based Programs](../venues/ICSE2023/paper_8.md), ([ICSE2023](../venues/ICSE2023/README.md))

  - **Abstract**: Block-based programming languages like SCRATCH are increasingly popular for programming education and end-user programming. Recent program analyses build on the insight that source code can be modelled using techniques from natural language processing. Many of the regularities of source code that support this approach are due to the syntactic overhead imposed by textual programming languages. This syntactic overhead, however, is precisely what block-based languages remove in order to simplify pr...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md)


- [On the Evaluation of Neural Code Translation: Taxonomy and Benchmark](../venues/ASE2023/paper_14.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: In recent years, neural code translation has gained increasing attention. While most of the research focuses on improving model architectures and training processes, we notice that the evaluation process and benchmark for code translation models are severely limited: they primarily treat source code as natural languages and provide a holistic accuracy score while disregarding the full spectrum of model capabilities across different translation types and complexity. In this paper, we present a co...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [empirical study](empirical_study.md)


- [RepoSim: Evaluating Prompt Strategies for Code Completion via User Behavior Simulation](../venues/ASE2024/paper_33.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Large language models (LLMs) have revolutionized code completion tasks. IDE plugins such as MarsCode can generate code recommendations, saving developers significant time and effort. However, current evaluation methods for code completion are limited by their reliance on static code benchmarks, which do not consider human interactions and evolving repositories. This paper proposes RepoSim, a novel benchmark designed to evaluate code completion tasks by simulating the evolving process of reposito...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md)


- [Repository-Level Prompt Generation for Large Language Models of Code](../venues/ICML2023/paper_2.md), ([ICML2023](../venues/ICML2023/README.md))

  - **Abstract**: With the success of large language models (LLMs) of code and their use as code assistants (e.g. Codex used in GitHub Copilot), techniques for introducing domain-specific knowledge in the prompt design process become important. In this work, we propose a framework called Repo-Level Prompt Generator that learns to generate example-specific prompts using prompt proposals. The prompt proposals take context from the entire repository, thereby incorporating both the structure of the repository and the...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md)


- [Rewriting the Code: A Simple Method for Large Language Model Augmented Code Search](../venues/ACL2024/paper_8.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: In code search, the Generation-Augmented Retrieval (GAR) framework, which generates exemplar code snippets to augment queries, has emerged as a promising strategy to address the principal challenge of modality misalignment between code snippets and natural language queries, particularly with the demonstrated code generation capabilities of Large Language Models (LLMs). Nevertheless, our preliminary investigations indicate that the improvements conferred by such an LLM-augmented framework are som...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [empirical study](empirical_study.md)


- [TrojanPuzzle: Covertly Poisoning Code-Suggestion Models](../venues/S&P2024/paper_3.md), ([S&P2024](../venues/S&P2024/README.md))

  - **Abstract**: With tools like GitHub Copilot, automatic code suggestion is no longer a dream in software engineering. These tools, based on large language models, are typically trained on massive corpora of code mined from unvetted public sources. As a result, these models are susceptible to data poisoning attacks where an adversary manipulates the model’s training by injecting malicious data. Poisoning attacks could be designed to influence the model’s suggestions at run time for chosen contexts, such as ind...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md), [attack](attack.md), [code generation](code_generation.md), [code completion](code_completion.md)


- [When Neural Code Completion Models Size up the Situation: Attaining Cheaper and Faster Completion through Dynamic Model Inference](../venues/ICSE2024/paper_7.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Leveraging recent advancements in large language models, modern neural code completion models have demonstrated the capability to generate highly accurate code suggestions. However, their massive size poses challenges in terms of computational costs and environmental impact, hindering their widespread adoption in practical scenarios. Dynamic inference emerges as a promising solution, as it allocates minimal computation during inference while maintaining the model's performance. In this research,...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [empirical study](empirical_study.md)
