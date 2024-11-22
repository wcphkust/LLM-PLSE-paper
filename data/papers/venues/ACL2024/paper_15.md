# Who Wrote this Code? Watermarking for Code Generation

**Authors**: Lee, Taehyun and Hong, Seokhee and Ahn, Jaewoo and Hong, Ilgee and Lee, Hwaran and Yun, Sangdoo and Shin, Jamin and Kim, Gunhee

**Abstract**:

Since the remarkable generation performance of large language models raised ethical and legal concerns, approaches to detect machine-generated text by embedding watermarks are being developed.However, we discover that the existing works fail to function appropriately in code generation tasks due to the task’s nature of having low entropy.Extending a logit-modifying watermark method, we propose Selective WatErmarking via Entropy Thresholding (SWEET), which enhances detection ability and mitigates code quality degeneration by removing low-entropy segments at generating and detecting watermarks.Our experiments show that SWEET significantly improves code quality preservation while outperforming all baselines, including post-hoc detection methods, in detecting machine-generated code text.Our code is available inhttps://github.com/hongcheki/sweet-watermark.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.268)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md), [defense](../../labels/defense.md)
