# Do Language Models Learn Semantics of Code? {A} Case Study in Vulnerability Detection

**Authors**: Benjamin Steenhoek and Md Mahbubur Rahman and Shaila Sharmin and Wei Le

**Abstract**:

Recently, pretrained language models have shown state-of-the-art performance on the vulnerability detection task. These models are pretrained on a large corpus of source code, then fine-tuned on a smaller supervised vulnerability dataset. Due to the different training objectives and the performance of the models, it is interesting to consider whether the models have learned the semantics of code relevant to vulnerability detection, namely bug semantics, and if so, how the alignment to bug semantics relates to model performance. In this paper, we analyze the models using three distinct methods: interpretability tools, attention analysis, and interaction matrix analysis. We compare the models' influential feature sets with the bug semantic features which define the causes of bugs, including buggy paths and Potentially Vulnerable Statements (PVS). We find that (1) better-performing models also aligned better with PVS, (2) the models failed to align strongly to PVS, and (3) the models failed to align at all to buggy paths. Based on our analysis, we developed two annotation methods which highlight the bug semantics inside the model's inputs. We evaluated our approach on four distinct transformer models and four vulnerability datasets and found that our annotations improved the models' performance in the majority of settings - 11 out of 16, with up to 9.57 points improvement in F1 score compared to conventional fine-tuning. We further found that with our annotations, the models aligned up to 232% better to potentially vulnerable statements. Our findings indicate that it is helpful to provide the model with information of the bug semantics, that the model can attend to it, and motivate future work in learning more complex path-based bug semantics.

**Link**: [Read Paper](https://doi.org/10.48550/arXiv.2311.04109)

**Labels**: static analysis, bug detection, empirical study
