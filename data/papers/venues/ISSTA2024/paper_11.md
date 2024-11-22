# CREF: An LLM-Based Conversational Software Repair Framework for Programming Tutors

**Authors**: Yang, Boyang and Tian, Haoye and Pian, Weiguo and Yu, Haoran and Wang, Haitao and Klein, Jacques and Bissyand\'{e}, Tegawend\'{e} F. and Jin, Shunfu

**Abstract**:

With the proven effectiveness of Large Language Models (LLMs) in code-related tasks, researchers have explored their potential for program repair. However, existing repair benchmarks might have influenced LLM training data, potentially causing data leakage. To evaluate LLMs’ realistic repair capabilities, (i) we introduce an extensive, non-crawled benchmark TutorCode, comprising 1,239 C++ defect codes and associated information such as tutor guidance, solution description, failing test cases, and the corrected code. Our work assesses LLM’s repair performance on TutorCode, measuring repair correctness (TOP-5 and AVG-5) and patch precision (RPSR). (ii) We then provide a comprehensive investigation into which types of extra information can help LLMs improve their repair performance. Among these types, tutor guidance was the most effective information. To fully harness LLMs’ conversational capabilities and the benefits of augmented information, (iii) we introduce a novel conversational semi-automatic repair framework CREF assisting human programming tutors. It demonstrates a remarkable AVG-5 improvement of 17.2\%-24.6\% compared to the baseline, achieving an impressive AVG-5 of 76.6\% when utilizing GPT-4. These results highlight the potential for enhancing LLMs’ repair capabilities through tutor interactions and historical conversations. The successful application of CREF in a real-world educational setting demonstrates its effectiveness in reducing tutors’ workload and improving students’ learning experience, showing promise for code review and other software engineering tasks.

**Link**: [Read Paper](https://doi.org/10.1145/3650212.3680328)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)
