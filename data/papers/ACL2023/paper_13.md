# ReCode: Robustness Evaluation of Code Generation Models

**Authors**: Wang, Shiqi and Li, Zheng and Qian, Haifeng and Yang, Chenghao and Wang, Zijian and Shang, Mingyue and Kumar, Varun and Tan, Samson and Ray, Baishakhi and Bhatia, Parminder and Nallapati, Ramesh and Ramanathan, Murali Krishna and Roth, Dan and Xiang, Bing

**Abstract**:

Code generation models have achieved impressive performance. However, they tend to be brittle as slight edits to a prompt could lead to very different generations; these robustness properties, critical for user experience when deployed in real-life applications, are not well understood. Most existing works on robustness in text or code tasks have focused on classification, while robustness in generation tasks is an uncharted area and to date there is no comprehensive benchmark for robustness in code generation. In this paper, we propose ReCode, a comprehensive robustness evaluation benchmark for code generation models. We customize over 30 transformations specifically for code on docstrings, function and variable names, code syntax, and code format. They are carefully designed to be natural in real-life coding practice, preserve the original semantic meaning, and thus provide multifaceted assessments of a model’s robustness performance. With human annotators, we verified that over 90% of the perturbed prompts do not alter the semantic meaning of the original prompt. In addition, we define robustness metrics for code generation models considering the worst-case behavior under each type of perturbation, taking advantage of the fact that executing the generated code can serve as objective evaluation. We demonstrate ReCode on SOTA models using HumanEval, MBPP, as well as function completion tasks derived from them. Interesting observations include: better robustness for CodeGen over InCoder and GPT-J; models are most sensitive to syntax perturbations; more challenging robustness evaluation on MBPP over HumanEval.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2023.acl-long.773)

**Labels**: code model, training, source code model, code model, robustness
