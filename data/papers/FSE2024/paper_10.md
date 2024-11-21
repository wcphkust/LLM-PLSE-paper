# An Empirical Study on Code Review Activity Prediction and Its Impact in Practice

**Authors**: Olewicki, Doriane and Habchi, Sarra and Adams, Bram

**Abstract**:

During code reviews, an essential step in software quality assurance, reviewers have the difficult task of understanding and evaluating code changes to validate their quality and prevent introducing faults to the codebase. This is a tedious process where the effort needed is highly dependent on the code submitted, as well as the author’s and the reviewer’s experience, leading to median wait times for review feedback of 15-64 hours. Through an initial user study carried with 29 experts, we found that re-ordering the files changed by a patch within the review environment has potential to improve review quality, as more comments are written (+23\%), and participants’ file-level hot-spot precision and recall increases to 53\% (+13\%) and 28\% (+8\%), respectively, compared to the alphanumeric ordering. Hence, this paper aims to help code reviewers by predicting which files in a submitted patch need to be (1) commented, (2) revised, or (3) are hot-spots (commented or revised). To predict these tasks, we evaluate two different types of text embeddings (i.e., Bag-of-Words and Large Language Models encoding) and review process features (i.e., code size-based and history-based features). Our empirical study on three open-source and two industrial datasets shows that combining the code embedding and review process features leads to better results than the state-of-the-art approach. For all tasks, F1-scores (median of 40-62\%) are significantly better than the state-of-the-art (from +1 to +9\%).

**Link**: [Read Paper](https://doi.org/10.1145/3660806)

**Labels**: software maintenance and deployment, code review, empirical study
