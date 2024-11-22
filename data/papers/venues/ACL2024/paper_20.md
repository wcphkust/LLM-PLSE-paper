# XCodeEval: An Execution-based Large Scale Multilingual Multitask Benchmark for Code Understanding, Generation, Translation and Retrieval

**Authors**: Khan, Mohammad Abdullah Matin and Bari, M. Saiful and Long, Do and Wang, Weishi and Parvez, Md Rizwan and Joty, Shafiq

**Abstract**:

Recently, pre-trained large language models (LLMs) have shown impressive abilities in generating codes from natural language descriptions, repairing buggy codes, translating codes between languages, and retrieving relevant code segments. However, the evaluation of these models has often been performed in a scattered way on only one or two specific tasks, in a few languages, at a partial granularity (e.g., function) level, and in many cases without proper training data. Even more concerning is that in most cases the evaluation of generated codes has been done in terms of mere lexical overlap with a reference code rather than actual execution. We introduce *xCodeEval*, the largest executable multilingual multitask benchmark to date consisting of 25 M document-level coding examples (16.5 B tokens) from about 7.5 K unique problems covering up to 11 programming languages with execution-level parallelism. It features a total of 7 tasks involving code understanding, generation, translation and retrieval. *xCodeEval* adopts an execution-based evaluation and offers a multilingual code execution engine, *ExecEval* that supports unit test based execution in all the 11 languages. To address the challenge of balancing the distributions of text-code samples over multiple attributes in validation/test sets, we propose a novel data splitting and a data selection schema based on the geometric mean and graph-theoretic principle. Our experiments with OpenAI’s LLMs (zero-shot) and open-LLMs (zero-shot and fine-tuned) on the tasks and languages demonstrate to be quite challenging as per the current advancements in language models.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.367)

**Labels**: [general coding task](../../labels/general_coding_task.md), [benchmark](../../labels/benchmark.md)
