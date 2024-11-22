# Examining Zero-Shot Vulnerability Repair with Large Language Models

**Authors**: Pearce, Hammond and Tan, Benjamin and Ahmad, Baleegh and Karri, Ramesh and Dolan-Gavitt, Brendan

**Abstract**:

Human developers can produce code with cybersecurity bugs. Can emerging ‘smart’ code completion tools help repair those bugs? In this work, we examine the use of large language models (LLMs) for code (such as OpenAI’s Codex and AI21’s Jurassic J-1) for zero-shot vulnerability repair. We investigate challenges in the design of prompts that coax LLMs into generating repaired versions of insecure code. This is difficult due to the numerous ways to phrase key information— both semantically and syntactically—with natural languages. We perform a large scale study of five commercially available, black-box, "off-the-shelf" LLMs, as well as an open-source model and our own locally-trained model, on a mix of synthetic, hand-crafted, and real-world security bug scenarios. Our experiments demonstrate that while the approach has promise (the LLMs could collectively repair 100% of our synthetically generated and hand-crafted scenarios), a qualitative evaluation of the model’s performance over a corpus of historical real-world examples highlights challenges in generating functionally correct code.

**Link**: [Read Paper](https://doi.ieeecomputersociety.org/10.1109/SP46215.2023.10179420)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)
