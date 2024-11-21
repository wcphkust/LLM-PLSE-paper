# Multilingual Code Co-evolution using Large Language Models

**Authors**: Zhang, Jiyang and Nie, Pengyu and Li, Junyi Jessy and Gligoric, Milos

**Abstract**:

Many software projects implement APIs and algorithms in multiple programming languages. Maintaining such projects is tiresome, as developers have to ensure that any change (e.g., a bug fix or a new feature) is being propagated, timely and without errors, to implementations in other programming languages. In the world of ever-changing software, using rule-based translation tools (i.e., transpilers) or machine learning models for translating code from one language to another provides limited value. Translating each time the entire codebase from one language to another is not the way developers work. In this paper, we target a novel task: translating code changes from one programming language to another using large language models (LLMs). We design and implement the first LLM, dubbed Codeditor, to tackle this task. Codeditor explicitly models code changes as edit sequences and learns to correlate changes across programming languages. To evaluate Codeditor, we collect a corpus of 6,613 aligned code changes from 8 pairs of open-source software projects implementing similar functionalities in two programming languages (Java and C#). Results show that Codeditor outperforms the state-of-the-art approaches by a large margin on all commonly used automatic metrics. Our work also reveals that Codeditor is complementary to the existing generation-based models, and their combination ensures even greater performance.

**Link**: [Read Paper](https://doi.org/10.1145/3611643.3616350)

**Labels**: code generation, program transformation, code model, training, source code model
