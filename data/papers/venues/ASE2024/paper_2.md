# Instructive Code Retriever: Learn from Large Language Model's Feedback for Code Intelligence Tasks

**Authors**: Lu, Jiawei and Wang, Haoye and Liu, Zhongxin and Liang, Keyu and Bao, Lingfeng and Yang, Xiaohu

**Abstract**:

Recent studies proposed to leverage large language models (LLMs) with In-Context Learning (ICL) to handle code intelligence tasks without fine-tuning. ICL employs task instructions and a set of examples as demonstrations to guide the model in generating accurate answers without updating its parameters. While ICL has proven effective for code intelligence tasks, its performance heavily relies on the selected examples. Previous work has achieved some success in using BM25 to retrieve examples for code intelligence tasks. However, existing approaches lack the ability to understand the semantic and structural information of queries, resulting in less helpful demonstrations. Moreover, they do not adapt well to the complex and dynamic nature of user queries in diverse domains. In this paper, we introduce a novel approach named Instructive Code Retriever (ICR), which is designed to retrieve examples that enhance model inference across various code intelligence tasks and datasets. We enable ICR to learn the semantic and structural information of the corpus by a tree-based loss function. To better understand the correlation between queries and examples, we incorporate the feedback from LLMs to guide the training of the retriever. Experimental results demonstrate that our retriever significantly outperforms state-of-the-art approaches. We evaluate our model's effectiveness on various tasks, i.e., code summarization, program synthesis, and bug fixing. Compared to previous state-of-the-art algorithms, our method achieved improvements of 50.0\% and 90.0\% in terms of BLEU-4 for two code summarization datasets, 74.6\% CodeBLEU on program synthesis dataset, and increases of 3.6 and 3.2 BLEU-4 on two bug fixing datasets.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3694997)

**Labels**: [prompt strategy](../../labels/prompt_strategy.md), [retrieval-augmented generation](../../labels/retrieval-augmented_generation.md)
