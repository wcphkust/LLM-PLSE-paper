# Cross-lingual Code Clone Detection: When LLMs Fail Short Against Embedding-based Classifier

**Authors**: Moumoula, Micheline Benedicte and Kabore, Abdoul Kader and Klein, Jacques and Bissyande, Tegawende F.

**Abstract**:

Cross-lingual code clone detection has gained attention in software development due to the use of multiple programming languages. Recent advances in machine learning, particularly Large Language Models (LLMs), have motivated a reexamination of this problem.This paper evaluates the performance of four LLMs and eight prompts for detecting cross-lingual code clones, as well as a pretrained embedding model for classifying clone pairs. Both approaches are tested on the XLCoST and CodeNet datasets.Our findings show that while LLMs achieve high F1 scores (up to 0.98) on straightforward programming examples, they struggle with complex cases and cross-lingual understanding. In contrast, embedding models, which map code fragments from different languages into a common representation space, allow for the training of a basic classifier that outperforms LLMs by approximately 2 and 24 percentage points on the XLCoST and CodeNet datasets, respectively. This suggests that embedding models provide more robust representations, enabling state-of-the-art performance in cross-lingual code clone detection.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695335)

**Labels**: [static analysis](../../labels/static_analysis.md), [code similarity analysis](../../labels/code_similarity_analysis.md)
