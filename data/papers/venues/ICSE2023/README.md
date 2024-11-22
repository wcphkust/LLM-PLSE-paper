# ICSE2023

Number of papers: 11

## [CodaMosa: Escaping Coverage Plateaus in Test Generation with Pre-Trained Large Language Models](paper_1.md)
- **Authors**: Lemieux, Caroline and Inala, Jeevana Priya and Lahiri, Shuvendu K. and Sen, Siddhartha
- **Abstract**: Search-based software testing (SBST) generates high-coverage test cases for programs under test with a combination of test case generation and mutation. SBST's performance relies on there being a reasonable probability of generating test cases that exercise the core logic of the program under test. Given such test cases, SBST can then explore the space around them to exercise various parts of the ...
- **Link**: [Read Paper](https://doi.org/10.1109/ICSE48619.2023.00085)
- **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)

## [CCTest: Testing and Repairing Code Completion Systems](paper_2.md)
- **Authors**: Li, Zongjie and Wang, Chaozheng and Liu, Zhibo and Wang, Haoxuan and Chen, Dong and Wang, Shuai and Gao, Cuiyun
- **Abstract**: Code completion, a highly valuable topic in the software development domain, has been increasingly promoted for use by recent advances in large language models (LLMs). To date, visible LLM-based code completion frameworks such as GitHub Copilot and GPT are trained using deep learning over vast quantities of unstructured text and open source code. As the paramount component and the cornerstone in d...
- **Link**: [Read Paper](https://doi.org/10.1109/ICSE48619.2023.00110)
- **Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md)

## [Automated Repair of Programs from Large Language Models](paper_3.md)
- **Authors**: Fan, Zhiyu and Gao, Xiang and Mirchev, Martin and Roychoudhury, Abhik and Tan, Shin Hwei
- **Abstract**: Large language models such as Codex, have shown the capability to produce code for many programming tasks. However, the success rate of existing models is low, especially for complex programming tasks. One of the reasons is that language models lack awareness of program semantics, resulting in incorrect programs, or even programs which do not compile. In this paper, we systematically study whether...
- **Link**: [Read Paper](https://doi.org/10.1109/ICSE48619.2023.00128)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)

## [Automated Program Repair in the Era of Large Pre-Trained Language Models](paper_4.md)
- **Authors**: Xia, Chunqiu Steven and Wei, Yuxiang and Zhang, Lingming
- **Abstract**: Automated Program Repair (APR) aims to help developers automatically patch software bugs. However, current state-of-the-art traditional and learning-based APR techniques face the problem of limited patch variety, failing to fix complicated bugs. This is mainly due to the reliance on bug-fixing datasets to craft fix templates (traditional) or directly predict potential patches (learning-based). Lar...
- **Link**: [Read Paper](https://doi.org/10.1109/ICSE48619.2023.00129)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)

## [Large Language Models are Few-Shot Testers: Exploring LLM-Based General Bug Reproduction](paper_5.md)
- **Authors**: Kang, Sungmin and Yoon, Juyeon and Yoo, Shin
- **Abstract**: Many automated test generation techniques have been developed to aid developers with writing tests. To facilitate full automation, most existing techniques aim to either increase coverage, or generate exploratory inputs. However, existing test generation techniques largely fall short of achieving more semantic objectives, such as generating tests to reproduce a given bug report. Reproducing bugs i...
- **Link**: [Read Paper](https://doi.org/10.1109/ICSE48619.2023.00194)
- **Labels**: [program testing](../../labels/program_testing.md), [bug reproduction](../../labels/bug_reproduction.md)

## [Explaining Software Bugs Leveraging Code Structures in Neural Machine Translation](paper_6.md)
- **Authors**: Mahbub, Parvez and Shuvo, Ohiduzzaman and Rahman, Mohammad Masudur
- **Abstract**: Software bugs claim ≈ 50\% of development time and cost the global economy billions of dollars. Once a bug is reported, the assigned developer attempts to identify and understand the source code responsible for the bug and then corrects the code. Over the last five decades, there has been significant research on automatically finding or correcting software bugs. However, there has been little rese...
- **Link**: [Read Paper](https://doi.org/10.1109/ICSE48619.2023.00063)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)

## [Concrat: An Automatic C-to-Rust Lock API Translator for Concurrent Programs](paper_7.md)
- **Authors**: Hong, Jaemin and Ryu, Sukyoung
- **Abstract**: Concurrent programs suffer from data races. To prevent data races, programmers use locks. However, programs can eliminate data races only when they acquire and release correct locks at correct timing. The lock API of C, in which people have developed a large portion of legacy system programs, does not validate the correct use of locks. On the other hand, Rust, a recently developed system programmi...
- **Link**: [Read Paper](https://doi.org/10.1109/ICSE48619.2023.00069)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)

## [On the Applicability of Language Models to Block-Based Programs](paper_8.md)
- **Authors**: Griebl, Elisabeth and Fein, Benedikt and Oberm\"{u}ller, Florian and Fraser, Gordon and Just, Ren\'{e
- **Abstract**: Block-based programming languages like SCRATCH are increasingly popular for programming education and end-user programming. Recent program analyses build on the insight that source code can be modelled using techniques from natural language processing. Many of the regularities of source code that support this approach are due to the syntactic overhead imposed by textual programming languages. This...
- **Link**: [Read Paper](https://doi.org/10.1109/ICSE48619.2023.00199)
- **Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md)

## [Automating Code-Related Tasks Through Transformers: The Impact of Pre-Training](paper_9.md)
- **Authors**: Tufano, Rosalia and Pascarella, Luca and Bavota, Gabriele
- **Abstract**: Transformers have gained popularity in the software engineering (SE) literature. These deep learning models are usually pre-trained through a self-supervised objective, meant to provide the model with basic knowledge about a language of interest (e.g., Java). A classic pre-training objective is the masked language model (MLM), in which a percentage of tokens from the input (e.g., a Java method) is...
- **Link**: [Read Paper](https://doi.org/10.1109/ICSE48619.2023.00203)
- **Labels**: [general coding task](../../labels/general_coding_task.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md), [empirical study](../../labels/empirical_study.md)

## [Retrieval-Based Prompt Selection for Code-Related Few-Shot Learning](paper_10.md)
- **Authors**: Nashid, Noor and Sintaha, Mifta and Mesbah, Ali
- **Abstract**: Large language models trained on massive code corpora can generalize to new tasks without the need for task-specific fine-tuning. In few-shot learning, these models take as input a prompt, composed of natural language instructions, a few instances of task demonstration, and a query and generate an output. However, the creation of an effective prompt for code-related tasks in few-shot learning has ...
- **Link**: [Read Paper](https://doi.org/10.1109/ICSE48619.2023.00205)
- **Labels**: [general coding task](../../labels/general_coding_task.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [prompt strategy](../../labels/prompt_strategy.md), [retrieval-augmented generation](../../labels/retrieval-augmented_generation.md)

## [VULGEN: Realistic Vulnerability Generation Via Pattern Mining and Deep Learning](paper_11.md)
- **Authors**: Nong, Yu and Ou, Yuzhe and Pradel, Michael and Chen, Feng and Cai, Haipeng
- **Abstract**: Building new, powerful data-driven defenses against prevalent software vulnerabilities needs sizable, quality vulnerability datasets, so does large-scale benchmarking of existing defense solutions. Automatic data generation would promisingly meet the need, yet there is little work aimed to generate much-needed quality vulnerable samples. Meanwhile, existing similar and adaptable techniques suffer ...
- **Link**: [Read Paper](https://doi.org/10.1109/ICSE48619.2023.00211)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [benchmark](../../labels/benchmark.md)

