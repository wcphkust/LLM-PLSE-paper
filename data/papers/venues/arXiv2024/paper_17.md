# LLM4Vuln: {A} Unified Evaluation Framework for Decoupling and Enhancing LLMs' Vulnerability Reasoning

**Authors**: Yuqiang Sun and Daoyuan Wu and Yue Xue and Han Liu and Wei Ma and Lyuye Zhang and Miaolei Shi and Yang Liu

**Abstract**:

Large language models (LLMs) have demonstrated significant potential in various tasks, including vulnerability detection. However, current efforts in this area are preliminary, lacking clarity on whether LLMs' vulnerability reasoning capabilities stem from the models themselves or external aids such as knowledge retrieval and tooling support.This paper aims to isolate LLMs' vulnerability reasoning from other capabilities, such as vulnerability knowledge adoption, context information retrieval, and structured output generation. We introduce LLM4Vuln, a unified evaluation framework that separates and assesses LLMs' vulnerability reasoning capabilities and examines improvements when combined with other enhancements.We conducted controlled experiments with 97 ground-truth vulnerabilities and 97 non-vulnerable cases in Solidity and Java, testing them in a total of 9,312 scenarios across four LLMs (GPT-4, GPT-3.5, Mixtral, and Llama 3). Our findings reveal the varying impacts of knowledge enhancement, context supplementation, prompt schemes, and models. Additionally, we identified 14 zero-day vulnerabilities in four pilot bug bounty programs, resulting in $3,576 in bounties.

**Link**: [Read Paper](https://doi.org/10.48550/arXiv.2401.16185)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [benchmark](../../labels/benchmark.md)
