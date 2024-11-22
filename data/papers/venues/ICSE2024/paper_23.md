# EGFE: End-to-end Grouping of Fragmented Elements in UI Designs with Multimodal Learning

**Authors**: Chen, Liuqing and Chen, Yunnong and Xiao, Shuhong and Song, Yaxuan and Sun, Lingyun and Zhen, Yankun and Zhou, Tingting and Chang, Yanfang

**Abstract**:

When translating UI design prototypes to code in industry, automatically generating code from design prototypes can expedite the development of applications and GUI iterations. However, in design prototypes without strict design specifications, UI components may be composed of fragmented elements. Grouping these fragmented elements can greatly improve the readability and maintainability of the generated code. Current methods employ a two-stage strategy that introduces hand-crafted rules to group fragmented elements. Unfortunately, the performance of these methods is not satisfying due to visually overlapped and tiny UI elements. In this study, we propose EGFE, a novel method for automatically End-to-end Grouping Fragmented Elements via UI sequence prediction. To facilitate the UI understanding, we innovatively construct a Transformer encoder to model the relationship between the UI elements with multi-modal representation learning. The evaluation on a dataset of 4606 UI prototypes collected from professional UI designers shows that our method outperforms the state-of-the-art baselines in the precision (by 29.75\%), recall (by 31.07\%), and F1-score (by 30.39\%) at edit distance threshold of 4. In addition, we conduct an empirical study to assess the improvement of the generated front-end code. The results demonstrate the effectiveness of our method on a real software engineering application. Our end-to-end fragmented elements grouping method creates opportunities for improving UI-related software engineering tasks.

**Link**: [Read Paper](https://doi.org/10.1145/3597503.3623313)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)
