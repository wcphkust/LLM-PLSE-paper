# Go Static: Contextualized Logging Statement Generation

**Authors**: Li, Yichen and Huo, Yintong and Zhong, Renyi and Jiang, Zhihan and Liu, Jinyang and Huang, Junjie and Gu, Jiazhen and He, Pinjia and Lyu, Michael R.

**Abstract**:

Logging practices have been extensively investigated to assist developers in writing appropriate logging statements for documenting software behaviors. Although numerous automatic logging approaches have been proposed, their performance remains unsatisfactory due to the constraint of the single-method input, without informative programming context outside the method. Specifically, we identify three inherent limitations with single-method context: limited static scope of logging statements, inconsistent logging styles, and missing type information of logging variables.                                To tackle these limitations, we propose SCLogger, the first contextualized logging statement generation approach with inter-method static contexts.First, SCLogger extracts inter-method contexts with static analysis to construct the contextualized prompt for language models to generate a tentative logging statement. The contextualized prompt consists of an extended static scope and sampled similar methods, ordered by the chain-of-thought (COT) strategy. Second, SCLogger refines the access of logging variables by formulating a new refinement prompt for language models, which incorporates detailed type information of variables in the tentative logging statement.                                The evaluation results show that SCLogger surpasses the state-of-the-art approach by 8.7\% in logging position accuracy, 32.1\% in level accuracy, 19.6\% in variable precision, and 138.4\% in text BLEU-4 score. Furthermore, SCLogger consistently boosts the performance of logging statement generation across a range of large language models, thereby showcasing the generalizability of this approach.

**Link**: [Read Paper](https://doi.org/10.1145/3643754)

**Labels**: software maintenance and deployment, system log analysis
