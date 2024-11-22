# Rethinking Code Refinement: Learning to Judge Code Efficiency

**Authors**: Seo, Minju and Baek, Jinheon and Hwang, Sung Ju

**Abstract**:

Large Language Models (LLMs) have demonstrated impressive capabilities in understanding and generating codes. Due to these capabilities, many recent methods are proposed to automatically refine the codes with LLMs. However, we should rethink that the refined codes (from LLMs and even humans) are not always more efficient than their original versions. On the other hand, running two different versions of codes and comparing them every time is not ideal and time-consuming. Therefore, in this work, we propose a novel method based on the code language model that is trained to judge the efficiency between two different codes (generated across humans and machines) by either classifying the superior one or predicting the relative improvement. We validate our method on multiple programming languages with multiple refinement steps, demonstrating that the proposed method can effectively distinguish between more and less efficient versions of code.

**Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.645)

**Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)
