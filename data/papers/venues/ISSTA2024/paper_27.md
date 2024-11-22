# UniTSyn: A Large-Scale Dataset Capable of Enhancing the Prowess of Large Language Models for Program Testing

**Authors**: He, Yifeng and Huang, Jiabo and Rong, Yuyang and Guo, Yiwen and Wang, Ethan and Chen, Hao

**Abstract**:

The remarkable capability of large language models (LLMs) in generating high-quality code has drawn increasing attention in the software testing community. However, existing code LLMs often demonstrate unsatisfactory capabilities in generating accurate, complete tests since they were trained on code snippets collected without differentiating between code for testing and for other purposes. In this paper, we present a large-scale dataset, UniTSyn, which can enhance LLMs for Unit Test Synthesis. Associating tests with the tested functions is crucial for LLMs to infer the expected behavior and the logic paths to be verified. By leveraging Language Server Protocol, UniTSyn achieves the challenging goal of collecting focal-test pairs without per-project execution setups or per-language heuristics, which tend to be fragile and difficult to scale. Containing 2.7 million focal-test pairs across five mainstream programming languages, it can enhance the test generation ability of LLMs. Our experiments demonstrate that, by building an autoregressive LLM based on UniTSyn, we can achieve significant benefits in learning and understanding unit test representations, resulting in improved generation accuracy and code coverage across all the evaluated programming languages.

**Link**: [Read Paper](https://haochen.org/publications/he2024unitsyn.pdf)

**Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md), [benchmark](../../labels/benchmark.md)
