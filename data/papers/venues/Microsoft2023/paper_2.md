# E{\&}V: Prompting Large Language Models to Perform Static Analysis by Pseudo-code Execution and Verification

**Authors**: Yu Hao and Weiteng Chen and Ziqiao Zhou and Weidong Cui

**Abstract**:

Static analysis, the process of examining code without executing it, is crucial for identifying software issues. Yet, static analysis is hampered by its complexity and the need for customization for different targets. Traditional static analysis tools require extensive human effort and are often limited to specific target programs and programming languages. Recent advancements in Large Language Models (LLMs), such as GPT-4 and Llama, offer new capabilities for software engineering tasks. However, their application in static analysis, especially in understanding complex code structures, remains under-explored. This paper introduces a novel approach named E&V , which leverages LLMs to perform static analysis. Specifically, E&V employs LLMs to simulate the execution of pseudo-code, effectively conducting static analysis encoded in the pseudo-code with minimal human effort, thereby improving the accuracy of results. E&V includes a verification process for pseudo-code execution without needing an external oracle. This process allows E&V to mitigate hallucinations of LLMs and enhance the accuracy of static analysis results. We have implemented E&V in a prototype tool designed for triaging crashes through backward taint analysis. This prototype, paired with GPT-4-32k, has been applied to triage 170 recently fixed Linux kernel bugs across seven bug categories. Our experiments demonstrate that the prototype correctly identifies the blamed function in 81.2% of the cases. Additionally, we observe that our novel verification process significantly improves the accuracy, increasing it from 28.2% to 81.2%.

**Link**: [Read Paper](https://doi.org/10.48550/arXiv.2312.08477)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
