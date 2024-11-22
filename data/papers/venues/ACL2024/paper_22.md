# Integrate the Essence and Eliminate the Dross: Fine-Grained Self-Consistency for Free-Form Language Generation

**Authors**: Wang, Xinglin and Li, Yiwei and Feng, Shaoxiong and Yuan, Peiwen and Pan, Boyuan and Wang, Heda and Hu, Yao and Li, Kan

**Abstract**:

Self-consistency (SC), leveraging multiple samples from LLMs, shows significant gains on various reasoning tasks but struggles with free-form generation due to the difficulty of aggregating answers. Its variants, UCS and USC, rely on sample selection or voting mechanisms to improve output quality. These methods, however, face limitations due to their inability to fully utilize the nuanced consensus knowledge present within multiple candidate samples, often resulting in suboptimal outputs. We propose Fine-Grained Self-Consistency (FSC) to addresses these limitations by extracting and integrating segment-level commonalities from candidate samples, enhancing the performance of LLMs both in open-ended and reasoning tasks. Based on this, we present two additional strategies: candidate filtering, which enhances overall quality by identifying highly similar candidate sets, and merging, which reduces input token requirements by combining similar samples. The effectiveness of FSC is demonstrated through extensive experiments on various tasks, including summarization, code generation, and mathematical reasoning, using GPT-3.5-turbo and GPT-4. The results indicate significant improvements over baseline methods, showcasing the potential of FSC to optimize output quality by effectively synthesizing fine-grained consensus knowledge from multiple samples.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.634)

**Labels**: [general coding task](../../labels/general_coding_task.md), [empirical study](../../labels/empirical_study.md)
