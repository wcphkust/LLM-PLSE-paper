# Leveraging Context-Aware Prompting for Commit Message Generation

**Authors**: Jiang, Zhihua and Chen, Jianwei and Rao, Dongning and Ye, Guanghui

**Abstract**:

Writing comprehensive commit messages is tedious yet important, because these messages describe changes of code, such as fixing bugs or adding new features. However, most existing methods focus on either only the changed lines or nearest context lines, without considering the effectiveness of selecting useful contexts. On the other hand, it is possible that introducing excessive contexts can lead to noise. To this end, we propose a code model COMMIT (Context-aware prOMpting based comMIt-message generaTion) in conjunction with a code dataset CODEC (COntext and metaData Enhanced Code dataset). Leveraging program slicing, CODEC consolidates code changes along with related contexts via property graph analysis. Further, utilizing CodeT5+ as the backbone model, we train COMMIT via context-aware prompt on CODEC. Experiments show that COMMIT can surpass all compared models including pre-trained language models for code (code-PLMs) such as CommitBART and large language models for code (code-LLMs) such as Code-LlaMa. Besides, we investigate several research questions (RQs), further verifying the effectiveness of our approach. We release the data and code at: https://github.com/Jnunlplab/COMMIT.git.

**Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.749)

**Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [commit message generation](../../labels/commit_message_generation.md)
