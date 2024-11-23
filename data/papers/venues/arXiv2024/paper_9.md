# Rectifier: Code translation with corrector via llms

**Authors**: Yin, Xin and Ni, Chao and Nguyen, Tien N and Wang, Shaohua and Yang, Xiaohu

**Abstract**:

Software migration is garnering increasing attention with the evolution of software and society. Early studies mainly relied on handcrafted translation rules to translate between two languages, the translation process is error-prone and time-consuming. In recent years, researchers have begun to explore the use of pre-trained large language models (LLMs) in code translation. However, code translation is a complex task that LLMs would generate mistakes during code translation, they all produce certain types of errors when performing code translation tasks, which include (1) compilation error, (2) runtime error, (3) functional error, and (4) non-terminating execution. We found that the root causes of these errors are very similar (e.g. failure to import packages, errors in loop boundaries, operator errors, and more). In this paper, we propose a general corrector, namely Rectifier, which is a micro and universal model for repairing translation errors. It learns from errors generated by existing LLMs and can be widely applied to correct errors generated by any LLM. The experimental results on translation tasks between C++, Java, and Python show that our model has effective repair ability, and cross experiments also demonstrate the robustness of our method.

**Link**: [Read Paper](https://arxiv.org/pdf/2407.07472)

**Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)