# Type Inference

- [Generative Type Inference for Python](../venues/ASE2023/paper_12.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Python is a popular dynamic programming language, evidenced by its ranking as the second most commonly used language on GitHub. However, its dynamic type system can lead to potential type errors, leading researchers to explore automatic type inference approaches for Python programs. Existing type inference approaches can be generally grouped into three categories, i.e., rule-based, supervised, and cloze- style approaches. The rule-based type inference approaches can ensure the accuracy of predic...
  - **Labels**: [static analysis](static_analysis.md), [type inference](type_inference.md)


- [PyTy: Repairing Static Type Errors in Python](../venues/ICSE2024/paper_12.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Gradual typing enables developers to annotate types of their own choosing, offering a flexible middle ground between no type annotations and a fully statically typed language. As more and more code bases get type-annotated, static type checkers detect an increasingly large number of type errors. Unfortunately, fixing these errors requires manual effort, hampering the adoption of gradual typing in practice. This paper presents PyTy, an automated program repair approach targeted at statically dete...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [static analysis](static_analysis.md), [type inference](type_inference.md)


- [Risky Dynamic Typing-related Practices in Python: An Empirical Study](../venues/TOSEM2024/paper_6.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Python’s dynamic typing nature provides developers with powerful programming abstractions. However, many type-related bugs are accumulated in code bases of Python due to the misuse of dynamic typing. The goal of this article is to aid in the understanding of developers’ high-risk practices toward dynamic typing and the early detection of type-related bugs. We first formulate the rules of six types of risky dynamic typing-related practices (type smells for short) in Python. We then develop a rule...
  - **Labels**: [static analysis](static_analysis.md), [type inference](type_inference.md), [bug detection](bug_detection.md), [empirical study](empirical_study.md)
