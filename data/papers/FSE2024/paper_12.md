# Mining Action Rules for Defect Reduction Planning

**Authors**: Oueslati, Khouloud and Laberge, Gabriel and Lamothe, Maxime and Khomh, Foutse

**Abstract**:

Defect reduction planning plays a vital role in enhancing software quality and minimizing software maintenance costs. By training a black box machine learning model and “explaining” its predictions, explainable AI for software engineering aims to identify the code characteristics that impact maintenance risks. However, post-hoc explanations do not always faithfully reflect what the original model computes. In this paper, we introduce CounterACT, a Counterfactual ACTion rule mining approach that can generate defect reduction plans without black-box models. By leveraging action rules, CounterACT provides a course of action that can be considered as a counterfactual explanation for the class (e.g., buggy or not buggy) assigned to a piece of code. We compare the effectiveness of CounterACT with the original action rule mining algorithm and six established defect reduction approaches on 9 software projects. Our evaluation is based on (a) overlap scores between proposed code changes and actual developer modifications; (b) improvement scores in future releases; and (c) the precision, recall, and F1-score of the plans. Our results show that, compared to competing approaches, CounterACT’s explainable plans achieve higher overlap scores at the release level (median 95\%) and commit level (median 85.97\%), and they offer better trade-off between precision and recall (median F1-score 88.12\%). Finally, we venture beyond planning and explore leveraging Large Language models (LLM) for generating code edits from our generated plans. Our results show that suggested LLM code edits supported by our plans are actionable and are more likely to pass relevant test cases than vanilla LLM code recommendations.

**Link**: [Read Paper](https://doi.org/10.1145/3660809)

**Labels**: code generation, program repair, empirical study
