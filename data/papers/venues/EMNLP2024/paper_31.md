# How Do Your Code LLMs perform? Empowering Code Instruction Tuning with Really Good Data

**Authors**: Wang, Yejie and He, Keqing and Fu, Dayuan and GongQue, Zhuoma and Xu, Heyang and Chen, Yanxu and Wang, Zhexu and Fu, Yujia and Dong, Guanting and Diao, Muxi and Wang, Jingang and Zhang, Mengdi and Cai, Xunliang and Xu, Weiran

**Abstract**:

Recently, there has been a growing interest in studying how to construct better code instruction tuning data. However, we observe Code models trained with these datasets exhibit high performance on HumanEval but perform worse on other benchmarks such as LiveCodeBench. Upon further investigation, we find that many datasets suffer from severe data leakage. After cleaning up most of the leaked data, some well-known high-quality datasets perform poorly. This discovery reveals a new challenge: identifying which dataset genuinely qualify as high-quality code instruction data. To address this, we propose an efficient code data pruning strategy for selecting good samples. Our approach is based on three dimensions: instruction complexity, response quality, and instruction diversity. Based on our selected data, we present XCoder, a family of models finetuned from LLaMA3. Our experiments show Xcoder achieves new state-of-the-art performance using fewer training data, which verify the effectiveness of our data strategy. Moreover, we perform a comprehensive analysis on the data composition and find existing code datasets have different characteristics according to their construction methods, which provide new insights for future code LLMs.

**Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.777)

**Labels**: [code generation](../../labels/code_generation.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)
