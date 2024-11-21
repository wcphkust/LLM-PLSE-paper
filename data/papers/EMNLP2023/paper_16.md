# CodeBERTScore: Evaluating Code Generation with Pretrained Models of Code

**Authors**: Zhou, Shuyan and Alon, Uri and Agarwal, Sumit and Neubig, Graham

**Abstract**:

Since the rise of neural natural-language-to-code models (NL\rightarrowCode) that can generate long expressions and statements rather than a single next-token, one of the major problems has been reliably evaluating their generated output. In this paper, we propose CodeBERTScore: an evaluation metric for code generation, which builds on BERTScore (Zhang et al., 2020). Instead of encoding only the generated tokens as in BERTScore, CodeBERTScore also encodes the natural language input preceding the generated code, thus modeling the consistency between the generated code and its given natural language context as well. We perform an extensive evaluation of CodeBERTScore across four programming languages. We find that CodeBERTScore achieves a higher correlation with human preference and with functional correctness than all existing metrics. That is, generated code that receives a higher score by CodeBERTScore is more likely to be preferred by humans, as well as to function correctly when executed. We release five language-specific pretrained models to use with our publicly available code. Our language-specific models have been downloaded more than **1,000,000** times from the Huggingface Hub. Our code and data are available at https://github.com/neulab/code-bert-score

**Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.859)

**Labels**: code generation, code model, training, source code model
