# CodeBenchGen: Creating Scalable Execution-based Code Generation Benchmarks

**Authors**: Xie, Yiqing and Xie, Alex and Sheth, Divyanshu and Liu, Pengfei and Fried, Daniel and Rose, Carolyn

**Abstract**:

To facilitate evaluation of code generation systems across diverse scenarios, we present CodeBenchGen, a framework to create scalable execution-based benchmarks that only requires light guidance from humans. Specifically, we leverage a large language model (LLM) to convert an arbitrary piece of code into an evaluation example, including test cases for execution-based evaluation. We illustrate the usefulness of our framework by creating a dataset, Exec-CSN, which includes 1,931 examples involving 293 libraries revised from code in 367 GitHub repositories taken from the CodeSearchNet dataset. To demonstrate the complexity and solvability of examples in Exec-CSN, we present a human study demonstrating that 81.3% of the examples can be solved by humans and 61% are rated as ``requires effort to solve''. We conduct code generation experiments on open-source and proprietary models and analyze the performance of both humans and models. We will release the code of both the framework and the dataset upon acceptance.

**Link**: [Read Paper](https://arxiv.org/pdf/2404.00566)

**Labels**: [code generation](../../labels/code_generation.md), [benchmark](../../labels/benchmark.md)
