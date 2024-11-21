# LLMDFA: Analyzing Dataflow in Code with Large Language Model

**Authors**: Chengpeng Wang and Wuqi Zhang and Zian Su and Xiangzhe Xu and Xiaoheng Xie and Xiangyu Zhang

**Abstract**:

Dataflow analysis is a fundamental code analysis technique that identifies dependencies between program values. Traditional approaches typically necessitate successful compilation and expert customization, hindering their applicability and usability for analyzing uncompilable programs with evolving analysis needs in realworld scenarios. This paper presents LLMDFA, an LLM-powered compilation-free and customizable dataflow analysis framework. To address hallucinations for reliable results, we decompose the problem into several subtasks and introduce a series of novel strategies. Specifically, we leverage LLMs to synthesize code that outsources delicate reasoning to external expert tools, such as using a parsing library to extract program values of interest and invoking an automated theorem prover to validate path feasibility. Additionally, we adopt a few-shot chain-of-thought prompting to summarize dataflow facts in individual functions, aligning the LLMs with the program semantics of small code snippets to mitigate hallucinations. We evaluate LLMDFA on synthetic programs to detect three representative types of bugs and on real-world Android applications for customized bug detection. On average, LLMDFA achieves 87.10% precision and 80.77% recall, surpassing existing techniques with F1 score improvements of up to 0.35. We have open-sourced LLMDFA at https://github.com/chengpeng-wang/LLMDFA.

**Link**: [Read Paper](No Link Available)

**Labels**: static analysis, bug detection
