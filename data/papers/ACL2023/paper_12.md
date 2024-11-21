# A Static Evaluation of Code Completion by Large Language Models

**Authors**: Ding, Hantian and Kumar, Varun and Tian, Yuchen and Wang, Zijian and Kwiatkowski, Rob and Li, Xiaopeng and Ramanathan, Murali Krishna and Ray, Baishakhi and Bhatia, Parminder and Sengupta, Sudipta

**Abstract**:

Large language models trained on code have shown great potential to increase productivity of software developers. Several execution-based benchmarks have been proposed to evaluate functional correctness of model-generated code on simple programming problems. Nevertheless, it is expensive to perform the same evaluation on complex real-world projects considering the execution cost. On the other hand, static analysis tools such as linters, which can detect errors without running the program, haven’t been well explored for evaluating code generation models. In this work, we propose a static evaluation framework to quantify static errors in Python code completions, by leveraging Abstract Syntax Trees. Compared with execution-based evaluation, our method is not only more efficient, but also applicable to code in the wild. For experiments, we collect code context from open source repos to generate one million function bodies using public models. Our static analysis reveals that Undefined Name and Unused Variable are the most common errors among others made by language models. Through extensive studies, we also show the impact of sampling temperature, model size, and context on static errors in code completions.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2023.acl-industry.34)

**Labels**: code generation, code completion, empirical study
