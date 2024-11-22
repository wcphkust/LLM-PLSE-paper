# Risky Dynamic Typing-related Practices in Python: An Empirical Study

**Authors**: Chen, Zhifei and Chen, Lin and Yang, Yibiao and Feng, Qiong and Li, Xuansong and Song, Wei

**Abstract**:

Python’s dynamic typing nature provides developers with powerful programming abstractions. However, many type-related bugs are accumulated in code bases of Python due to the misuse of dynamic typing. The goal of this article is to aid in the understanding of developers’ high-risk practices toward dynamic typing and the early detection of type-related bugs. We first formulate the rules of six types of risky dynamic typing-related practices (type smells for short) in Python. We then develop a rule-based tool named RUPOR, which builds an accurate type base to detect type smells. Our evaluation shows that RUPOR outperforms the existing type smell detection techniques (including the Large Language Models–based approaches, Mypy, and PYDYPE) on a benchmark of 900 Python methods. Based on RUPOR, we conduct an empirical study on 25 real-world projects. We find that type smells are significantly related to the occurrence of post-release faults. The fault-proneness prediction model built with type smell features slightly outperforms the model built without them. We also summarize the common patterns, including inserting type check to fix type smell bugs. These findings provide valuable insights for preventing and fixing type-related bugs in the programs written in dynamic-typed languages.

**Link**: [Read Paper](https://doi.org/10.1145/3649593)

**Labels**: [static analysis](../../labels/static_analysis.md), [type inference](../../labels/type_inference.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)
