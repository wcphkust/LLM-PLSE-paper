# Code LLM Paper Repository

This repository provides a curated list of research papers focused on Large Language Models (LLMs) for code. It aims to facilitate researchers and practitioners in exploring the rapidly growing body of literature on this topic. The papers are systematically collected from various top-tier venues, categorized, and labeled for easier navigation.

## Venues

We have systematically selected papers from the following venues, which are top-tier conferences and journals in SE/PL/Sec/NLP communities.

- Software Engineering (SE): [ICSE2023](data/papers/venues/ICSE2023/README.md), [ICSE2024](data/papers/venues/ICSE2024/README.md), [FSE2023](data/papers/venues/FSE2023/README.md), [FSE2024](data/papers/venues/FSE2024/README.md), [ASE2023](data/papers/venues/ASE2023/README.md), [ASE2024](data/papers/venues/ASE2024/README.md), [ISSTA2023](data/papers/venues/ISSTA2023/README.md), [ISSTA2024](data/papers/venues/ISSTA2024/README.md), [TSE2023](data/papers/venues/TSE2023/README.md), [TSE2024](data/papers/venues/TSE2024/README.md), [TOSEM2023](data/papers/venues/TOSEM2023/README.md), [TOSEM2024](data/papers/venues/TOSEM2024/README.md)

- Programming Languages (PL): [PLDI2023](data/papers/venues/PLDI2023/README.md), [POPL2025](data/papers/venues/POPL2025/README.md), [OOPSLA2023](data/papers/venues/OOPSLA2023/README.md), [OOPSLA2024](data/papers/venues/OOPSLA2024/README.md)

- Security (Sec): [S&P2023](data/papers/venues/S&P2023/README.md), [S&P2024](data/papers/venues/S&P2024/README.md), [USENIXSec2023](data/papers/venues/USENIXSec2023/README.md), [USENIXSec2023](data/papers/venues/USENIXSec2023/README.md), [NDSS2023](data/papers/venues/NDSS2023/README.md), [NDSS2024](data/papers/venues/NDSS2024/README.md)

- Natural Language Processing (NLP): [ACL2023](data/papers/venues/ACL2023/README.md), [ACL2024](data/papers/venues/ACL2024/README.md), [EMNLP2023](data/papers/venues/EMNLP2023/README.md), [EMNLP2024](data/papers/venues/EMNLP2024/README.md), [NAACL2023](data/papers/venues/NAACL2023/README.md), [NAACL2024](data/papers/venues/NAACL2024/README.md)

The papers accepted by USENIXSec2024 and CCS2024 have not been published in the proceedings. Due to the large volume, we do not systematically collect the papers published in top-tier ML conferences (ICML, NeurIPS, and ICLR) and arXiv. However, we are keeping manually adding important works published in these venues. We plan to expand the collection over time, and contributions are welcome. For details, see the section [How to Contribute](#3-contribution).


## Paper Selection Strategy
1. **Abstract Extraction**: Extract the abstracts from bib files or HTML files. The bib and HTML files of the above listed venues are stored in the directory `data/rawdata`.
2. **Keyword Matching**: Filter abstracts that meet both of the following conditions:
   - Contains at least one keyword from: `{"pretrain", "LLM", "large language model", "transformer", "code model"}`.
   - Contains the keyword `"code"` or `"program"`.
3. **Relevance Check Using LLMs**: Use LLMs to verify if the papers obtained in Step 2 are related to LLMs for code.
4. **Manual Labeling**: Manually assign labels to the papers based on domain knowledge.

All the selected papers along with the labels are maintained in the json file `data/labeldata/labeldata.json`.

## Taxonomy

The papers in this repository are categorized along three dimensions: **Application**, **Principle**, and **Research Paradigm**. Each paper is assigned multiple labels based on these categories. Note that categories are not necessarily disjoint.

### Application

This category focuses on typical tasks in Software Engineering (SE) and Programming Languages (PL).

- [General Coding Task](data/papers/labels/general_coding_task.md)   (31)
- [Program Testing](data/papers/labels/program_testing.md)   (47)
  - [Fuzzing](data/papers/labels/fuzzing.md)   (18)
  - [Library Testing](data/papers/labels/library_testing.md)   (1)
  - [Dbms Testing](data/papers/labels/DBMS_testing.md)   (1)
  - [Compiler Testing](data/papers/labels/compiler_testing.md)   (4)
  - [Protocol Fuzzing](data/papers/labels/protocol_fuzzing.md)   (1)
  - [Mutation Testing](data/papers/labels/mutation_testing.md)   (2)
  - [Unit Testing](data/papers/labels/unit_testing.md)   (7)
  - [Differential Testing](data/papers/labels/differential_testing.md)   (1)
  - [Debugging](data/papers/labels/debugging.md)   (9)
  - [Bug Reproduction](data/papers/labels/bug_reproduction.md)   (2)
  - [Vulnerability Exploitation](data/papers/labels/vulnerability_exploitation.md)   (6)
- [Code Generation](data/papers/labels/code_generation.md)   (190)
  - [Program Synthesis](data/papers/labels/program_synthesis.md)   (80)
  - [Code Completion](data/papers/labels/code_completion.md)   (22)
  - [Program Repair](data/papers/labels/program_repair.md)   (38)
  - [Program Transformation](data/papers/labels/program_transformation.md)   (26)
  - [Program Decompilation](data/papers/labels/program_decompilation.md)   (5)
- [Software Maintenance And Deployment](data/papers/labels/software_maintenance_and_deployment.md)   (18)
  - [Code Review](data/papers/labels/code_review.md)   (6)
  - [Documentation Generation](data/papers/labels/documentation_generation.md)   (2)
  - [Commit Message Generation](data/papers/labels/commit_message_generation.md)   (4)
  - [Software Configuration](data/papers/labels/software_configuration.md)   (1)
  - [System Log Analysis](data/papers/labels/system_log_analysis.md)   (4)
- [Static Analysis](data/papers/labels/static_analysis.md)   (109)
  - [Fundamental Analysis](data/papers/labels/fundamental_analysis.md)   (12)
  - [Specification Inference](data/papers/labels/specification_inference.md)   (7)
  - [Bug Detection](data/papers/labels/bug_detection.md)   (58)
  - [Program Verification](data/papers/labels/program_verification.md)   (15)
  - [Code Search](data/papers/labels/code_search.md)   (5)
  - [Code Similarity Analysis](data/papers/labels/code_similarity_analysis.md)   (4)
  - [Software Composition Analysis](data/papers/labels/software_composition_analysis.md)   (3)
  - [Code Summarization](data/papers/labels/code_summarization.md)   (8)
  - [Compiler Optimization](data/papers/labels/compiler_optimization.md)   (2)
  - [Type Inference](data/papers/labels/type_inference.md)   (3)

### Principle

This category focuses on model functionality and non-functional properties.

- [Code Model](data/papers/labels/code_model.md)   (103)
  - [Code Model Training](data/papers/labels/code_model_training.md)   (82)
    - [Source Code Model](data/papers/labels/source_code_model.md)   (64)
    - [Ir Code Model](data/papers/labels/IR_code_model.md)   (5)
    - [Binary Code Model](data/papers/labels/binary_code_model.md)   (13)
  - [Code Model Security](data/papers/labels/code_model_security.md)   (17)
  - [Code Model Robustness](data/papers/labels/code_model_robustness.md)   (4)
- [Hallucination In Reasoning](data/papers/labels/hallucination_in_reasoning.md)   (11)
- [Pl Design For Llms](data/papers/labels/PL_design_for_LLMs.md)   (3)
- [Agent Design](data/papers/labels/agent_design.md)   (18)
  - [Prompt Strategy](data/papers/labels/prompt_strategy.md)   (36)
    - [Retrieval-augmented Generation](data/papers/labels/retrieval-augmented_generation.md)   (7)
    - [Reason With Code](data/papers/labels/reason_with_code.md)   (17)
    - [Sampling And Ranking](data/papers/labels/sampling_and_ranking.md)   (3)
  - [Planning](data/papers/labels/planning.md)   (8)

### Research Paradigm

This category includes studies on benchmarks, empirical evaluations, and surveys.

- [Benchmark](data/papers/labels/benchmark.md)   (41)
- [Empirical Study](data/papers/labels/empirical_study.md)   (76)
- [Survey](data/papers/labels/survey.md)   (14)

## Contribution

We welcome contributions to expand this repository. Please follow these steps:

### Steps to Add New Papers
1. **Prepare a JSON File**: Format the file like `data/example.json`. Each paper should include:
   - `title`, `authors`, `abstract`, `link`, `venue`, and `labels` (aligned with the taxonomy in `data/category.json`).
2. **Upload the File**: Place the JSON file in the `data/patch` directory with a unique name.
3. **Update Markdown Files**: Run the following command to update the repository:
   ```bash
   python update_repo.py
