# Improving Automated Program Repair with Domain Adaptation

**Authors**: Zirak, Armin and Hemmati, Hadi

**Abstract**:

Automated Program Repair (APR) is defined as the process of fixing a bug/defect in the source code, by an automated tool. APR tools have recently experienced promising results by leveraging state-of-the-art Neural Language Processing (NLP) techniques. APR tools such as TFix and CodeXGLUE that combine text-to-text transformers with software-specific techniques are outperforming alternatives, these days. However, in most APR studies, the train and test sets are chosen from the same set of projects (i.e., when APR fixes a bug in the test set from project A, the model has already seen example fixed bugs from project A in the training set). In the real world, however, APR models are meant to be generalizable to new and different projects. Therefore, there is a potential threat that reported APR models with high effectiveness perform poorly when the characteristics of the new project or its bugs are different than the training set’s (“Domain Shift”).In this study, we first define the problem of domain shift in automated program repair. Next, we measure the potential damage of domain shift on two recent APR models (TFix and CodeXGLUE). Based on this observation, we then propose a domain adaptation framework that can adapt an APR model for a given target project. We conduct an empirical study with three domain adaptation methods FullFineTuning, TuningWithLightWeightAdapterLayers, and CurriculumLearning and two APR models on 2,672 bugs from 12 projects.The results show that our proposed framework on average can improve the effectiveness of TFix by 13.05\% and CodeXGLUE by 48.78\%, in terms of “Exact Match”. Through experiments, we also show that the framework provides high efficiency and reliability (in terms of “Exposure Bias”). Using synthetic data to domain adapt TFix and CodeXGLUE on the projects with no data (Zero-shot learning), also results in an average improvement of 5.76\% and 17.62\% for TFix and CodeXGLUE, respectively.

**Link**: [Read Paper](https://doi.org/10.1145/3631972)

**Labels**: code generation, program repair
