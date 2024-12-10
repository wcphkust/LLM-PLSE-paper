# PTD-SQL: Partitioning and Targeted Drilling with LLMs in Text-to-SQL

**Authors**: Luo, Ruilin and Wang, Liyuan and Lin, Binghuai and Lin, Zicheng and Yang, Yujiu

**Abstract**:

Large Language Models (LLMs) have emerged as powerful tools for Text-to-SQL tasks, exhibiting remarkable reasoning capabilities. Different from tasks such as math word problem and commonsense reasoning, SQL solutions have a relatively fixed pattern. This facilitates the investigation of whether LLMs can benefit from categorical thinking, mirroring how humans acquire knowledge through inductive reasoning based on comparable examples. In this study, we propose that employing query group partitioning allows LLMs to focus on learning the thought processes specific to a single problem type, consequently enhancing their reasoning abilities across diverse difficulty levels and problem categories. Our experiments reveal that multiple advanced LLMs, when equipped with PTD-SQL, can either surpass or match previous state-of-the-art (SOTA) methods on the Spider and BIRD datasets. Intriguingly, models with varying initial performances have exhibited significant improvements mainly at the boundary of their capabilities after targeted drilling, suggesting a parallel with human progress. Code is available at https://github.com/lrlbbzl/PTD-SQL.

**Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.221)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [empirical study](../../labels/empirical_study.md)
