# SMT Solver Validation Empowered by Large Pre-Trained Language Models

**Authors**: Sun, Maolin and Yang, Yibiao and Wang, Yang and Wen, Ming and Jia, Haoxiang and Zhou, Yuming

**Abstract**:

SMT solvers are utilized to check the satisfiability of logic formulas and have been applied in various crucial domains, including software verification, test case generation, and program synthesis. However, bugs hidden in SMT solvers can lead to severe consequences, causing erroneous results in these domains. Therefore, ensuring the reliability and robustness of SMT solvers is of critical importance. Despite several testing approaches proposed for SMT solvers, generating effective test formulas to comprehensively test SMT solvers remains a challenge. To address this challenge, in this study, we propose to port large language models (LLMs) to generate SMT formulas for fuzzing solvers. Specifically, the study presents a novel retrain-finetune pipeline to unleash the potential of language models to generate effective SMT formulas and improve their generation performance through data augmentation. We implemented our approach as a practical fuzzing tool, named LasT,and then extensively tested the state-of-the-art SMT solvers, namely Z3, cvc5, and Bitwuzla. To date, Last has successfully uncovered 65 genuine bugs for the solvers, of which 45 have been fixed by the developers.

**Link**: [Read Paper](No Link Available)

**Labels**: program testing, fuzzing
