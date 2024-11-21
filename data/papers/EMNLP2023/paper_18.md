# On Sample-Efficient Code Generation

**Authors**: Han, Hojae and Kim, Yu Jin and Kim, Byoungjip and Lee, Youngwon and Lee, Kyungjae and Lee, Kyungmin and Lee, Moontae and Bae, Kyunghoon and Hwang, Seung-won

**Abstract**:

Large language models often struggle to predict runtime behavior in code generation tasks, leading to a reliance on rejection sampling (best-of-n) to generate multiple code snippets then select the best. Our distinction is reducing sampling costs, without compromising generation quality. We introduce EFFICODE, a novel framework that prioritizes sampling on test problems that models can solve. We show how EFFICODE estimates solvability to optimize computational costs during multiple sampling. Based on empirical evidence, EFFICODE consistently demonstrates reduced sampling budgets while maintaining comparable code generation performance, especially when problems are challenging. In addition, utilizing EFFICODE to rank sampled code snippets also shows its effectiveness in answer code selection for reducing temporal costs, by not requiring any execution or test case generation.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-industry.73)

**Labels**: code generation, program synthesis
