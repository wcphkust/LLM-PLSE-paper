# Language-to-Code Translation with a Single Labeled Example

**Authors**: Bostrom, Kaj and Jhamtani, Harsh and Fang, Hao and Thomson, Sam and Shin, Richard and Xia, Patrick and Van Durme, Benjamin and Eisner, Jason and Andreas, Jacob

**Abstract**:

Tools for translating natural language into code promise natural, open-ended interaction with databases, web APIs, and other software systems. However, this promise is complicated by the diversity and continual development of these systems, each with its own interface and distinct set of features. Building a new language-to-code translator, even starting with a large language model (LM), typically requires annotating a large set of natural language commands with their associated programs. In this paper, we describe ICIP (In-Context Inverse Programming), a method for bootstrapping a language-to-code system using mostly (or entirely) unlabeled programs written using a potentially unfamiliar (but human-readable) library or API. ICIP uses a pre-trained LM to assign candidate natural language descriptions to these programs, then iteratively refines the descriptions to ensure global consistency. Across nine different application domains from the Overnight and Spider benchmarks and text-davinci-003 and CodeLlama-7b-Instruct models, ICIP outperforms a number of prompting baselines. Indeed, in a “nearly unsupervised” setting with only a single annotated program and 100 unlabeled examples, it achieves up to 85% of the performance of a fully supervised system.

**Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.462)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [benchmark](../../labels/benchmark.md)
