# Towards Greener Yet Powerful Code Generation via Quantization: An Empirical Study

**Authors**: Wei, Xiaokai and Gonugondla, Sujan Kumar and Wang, Shiqi and Ahmad, Wasi and Ray, Baishakhi and Qian, Haifeng and Li, Xiaopeng and Kumar, Varun and Wang, Zijian and Tian, Yuchen and Sun, Qing and Athiwaratkun, Ben and Shang, Mingyue and Ramanathan, Murali Krishna and Bhatia, Parminder and Xiang, Bing

**Abstract**:

ML-powered code generation aims to assist developers to write code in a more productive manner by intelligently generating code blocks based on natural language prompts. Recently, large pretrained deep learning models have pushed the boundary of code generation and achieved impressive performance. However, the huge number of model parameters poses a significant challenge to their adoption in a typical software development environment, where a developer might use a standard laptop or mid-size server to develop code. Such large models cost significant resources in terms of memory, latency, dollars, as well as carbon footprint. Model compression is a promising approach to address these challenges. We have identified quantization as one of the most promising compression techniques for code-generation as it avoids expensive retraining costs. As quantization represents model parameters with lower-bit integer (e.g., int8), the model size and runtime latency would both benefit. We empirically evaluate quantized models on code generation tasks across different dimensions: (i) resource usage and carbon footprint, (ii) accuracy, and (iii) robustness. Through systematic experiments we find a code-aware quantization recipe that could run even a 6-billion-parameter model in a regular laptop without significant accuracy or robustness degradation. We find that the recipe is readily applicable to code summarization task as well.

**Link**: [Read Paper](https://doi.org/10.1145/3611643.3616302)

**Labels**: code generation, program synthesis, empirical study
