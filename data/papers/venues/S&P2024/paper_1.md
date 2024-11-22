# LLMs Cannot Reliably Identify and Reason About Security Vulnerabilities (Yet?): A Comprehensive Evaluation, Framework, and Benchmarks

**Authors**: Ullah, Saad and Han, Mingji and Pujar, Saurabh and Pearce, Hammond and Coskun, Ayse and Stringhini, Gianluca

**Abstract**:

Large Language Models (LLMs) have been suggested for use in automated vulnerability repair, but benchmarks showing they can consistently identify security-related bugs are lacking. We thus develop SecLLMHolmes, a fully automated evaluation framework that performs the most detailed investigation to date on whether LLMs can reliably identify and reason about security-related bugs. We construct a set of 228 code scenarios and analyze eight of the most capable LLMs across eight different investigative dimensions using our framework. Our evaluation shows LLMs provide non-deterministic responses, incorrect and unfaithful reasoning, and perform poorly in real-world scenarios. Most importantly, our findings reveal significant non-robustness in even the most advanced models like ‘PaLM2’ and ‘GPT-4’: by merely changing function or variable names, or by the addition of library functions in the source code, these models can yield incorrect answers in 26% and 17% of cases, respectively. These findings demonstrate that further LLM advances are needed before LLMs can be used as general purpose security assistants.

**Link**: [Read Paper](https://arxiv.org/pdf/2312.12575)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [empirical study](../../labels/empirical_study.md)
