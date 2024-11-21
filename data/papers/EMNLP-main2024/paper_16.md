# DocCGen: Document-based Controlled Code Generation

**Authors**: Pimparkhede, Sameer and Kammakomati, Mehant and Tamilselvam, Srikanth G. and Kumar, Prince and Kumar, Ashok Pon and Bhattacharyya, Pushpak

**Abstract**:

Recent developments show that Large Language Models (LLMs) produce state-of-the-art performance on natural language (NL) to code generation for resource-rich general-purpose languages like C++, Java, and Python. However, their practical usage for structured domain-specific languages (DSLs) such as YAML, JSON is limited due to domain-specific schema, grammar, and customizations generally unseen by LLMs during pre-training. Efforts have been made to mitigate this challenge via in-context learning through relevant examples or by fine-tuning. However, it suffers from problems, such as limited DSL samples and prompt sensitivity but enterprises maintain good documentation of the DSLs. Therefore, we propose DocCGen, a framework that can leverage such rich knowledge by breaking the NL-to-Code generation task for structured code languages into a two-step process. First, it detects the correct libraries using the library documentation that best matches the NL query. Then, it utilizes schema rules extracted from the documentation of these libraries to constrain the decoding. We evaluate our framework for two complex structured languages, Ansible YAML and Bash command, consisting of two settings: Out-of-domain (OOD) and In domain (ID). Our extensive experiments show that DocCGen consistently improves different sized language models across all six evaluation metrics, reducing syntactic and semantic errors in structured code.

**Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.1040)

**Labels**: code generation, program synthesis
