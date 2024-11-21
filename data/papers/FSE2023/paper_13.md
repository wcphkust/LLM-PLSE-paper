# Evaluating Transfer Learning for Simplifying GitHub READMEs

**Authors**: Gao, Haoyu and Treude, Christoph and Zahedi, Mansooreh

**Abstract**:

Software documentation captures detailed knowledge about a software product, e.g., code, technologies, and design. It plays an important role in the coordination of development teams and in conveying ideas to various stakeholders. However, software documentation can be hard to comprehend if it is written with jargon and complicated sentence structure. In this study, we explored the potential of text simplification techniques in the domain of software engineering to automatically simplify GitHub README files. We collected software-related pairs of GitHub README files consisting of 14,588 entries, aligned difficult sentences with their simplified counterparts, and trained a Transformer-based model to automatically simplify difficult versions. To mitigate the sparse and noisy nature of the software-related simplification dataset, we applied general text simplification knowledge to this field. Since many general-domain difficult-to-simple Wikipedia document pairs are already publicly available, we explored the potential of transfer learning by first training the model on the Wikipedia data and then fine-tuning it on the README data. Using automated BLEU scores and human evaluation, we compared the performance of different transfer learning schemes and the baseline models without transfer learning. The transfer learning model using the best checkpoint trained on a general topic corpus achieved the best performance of 34.68 BLEU score and statistically significantly higher human annotation scores compared to the rest of the schemes and baselines. We conclude that using transfer learning is a promising direction to circumvent the lack of data and drift style problem in software README files simplification and achieved a better trade-off between simplification and preservation of meaning.

**Link**: [Read Paper](https://doi.org/10.1145/3611643.3616291)

**Labels**: software maintenance and deployment, documentation generation
