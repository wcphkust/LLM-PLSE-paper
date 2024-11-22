# Self-Supervised Query Reformulation for Code Search

**Authors**: Mao, Yuetian and Wan, Chengcheng and Jiang, Yuze and Gu, Xiaodong

**Abstract**:

Automatic query reformulation is a widely utilized technology for enriching user requirements and enhancing the outcomes of code search. It can be conceptualized as a machine translation task, wherein the objective is to rephrase a given query into a more comprehensive alternative. While showing promising results, training such a model typically requires a large parallel corpus of query pairs (i.e., the original query and a reformulated query) that are confidential and unpublished by online code search engines. This restricts its practicality in software development processes. In this paper, we propose SSQR, a self-supervised query reformulation method that does not rely on any parallel query corpus. Inspired by pre-trained models, SSQR treats query reformulation as a masked language modeling task conducted on an extensive unannotated corpus of queries. SSQR extends T5 (a sequence-to-sequence model based on Transformer) with a new pre-training objective named corrupted query completion (CQC), which randomly masks words within a complete query and trains T5 to predict the masked content. Subsequently, for a given query to be reformulated, SSQR identifies potential locations for expansion and leverages the pre-trained T5 model to generate appropriate content to fill these gaps. The selection of expansions is then based on the information gain associated with each candidate. Evaluation results demonstrate that SSQR outperforms unsupervised baselines significantly and achieves competitive performance compared to supervised methods.

**Link**: [Read Paper](https://doi.org/10.1145/3611643.3616306)

**Labels**: [static analysis](../../labels/static_analysis.md), [code search](../../labels/code_search.md)
