# Beware of the unexpected: Bimodal taint analysis

**Authors**: Chow, Yiu Wai and Sch{\"a}fer, Max and Pradel, Michael

**Abstract**:

Static analysis is a powerful tool for detecting security vulnerabilities and other programming problems. Global taint tracking, in particular, can spot vulnerabilities arising from complicated data flow across multiple functions. However, precisely identifying which flows are problematic is challenging, and sometimes depends on factors beyond the reach of pure program analysis, such as conventions and informal knowledge. For example, learning that a parameter name of an API function locale ends up in a file path is surprising and potentially problematic. In contrast, it would be completely unsurprising to find that a parameter command passed to an API function execaCommand is eventually interpreted as part of an operating-system command. This paper presents Fluffy, a bimodal taint analysis that combines static analysis, which reasons about data flow, with machine learning, which probabilistically determines which flows are potentially problematic. The key idea is to let machine learning models predict from natural language information involved in a taint flow, such as API names, whether the flow is expected or unexpected, and to inform developers only about the latter. We present a general framework and instantiate it with four learned models, which offer different trade-offs between the need to annotate training data and the accuracy of predictions. We implement Fluffy on top of the CodeQL analysis framework and apply it to 250K JavaScript projects. Evaluating on five common vulnerability types, we find that Fluffy achieves an F1 score of 0.85 or more on four of them across a variety of datasets.

**Link**: [Read Paper](https://arxiv.org/pdf/2301.10545.pdf)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
