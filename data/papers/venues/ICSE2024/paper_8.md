# Traces of Memorisation in Large Language Models for Code

**Authors**: Al-Kaswan, Ali and Izadi, Maliheh and van Deursen, Arie

**Abstract**:

Large language models have gained significant popularity because of their ability to generate human-like text and potential applications in various fields, such as Software Engineering. Large language models for code are commonly trained on large unsanitised corpora of source code scraped from the internet. The content of these datasets is memorised and can be extracted by attackers with data extraction attacks. In this work, we explore memorisation in large language models for code and compare the rate of memorisation with large language models trained on natural language. We adopt an existing benchmark for natural language and construct a benchmark for code by identifying samples that are vulnerable to attack. We run both benchmarks against a variety of models, and perform a data extraction attack. We find that large language models for code are vulnerable to data extraction attacks, like their natural language counterparts. From the training data that was identified to be potentially extractable we were able to extract 47\% from a CodeGen-Mono-16B code completion model. We also observe that models memorise more, as their parameter count grows, and that their pre-training data are also vulnerable to attack. We also find that data carriers are memorised at a higher rate than regular code or documentation and that different model architectures memorise different samples. Data leakage has severe outcomes, so we urge the research community to further investigate the extent of this phenomenon using a wider range of models and extraction techniques in order to build safeguards to mitigate this issue.

**Link**: [Read Paper](https://doi.org/10.1145/3597503.3639133)

**Labels**: [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md), [attack](../../labels/attack.md), [benchmark](../../labels/benchmark.md)
