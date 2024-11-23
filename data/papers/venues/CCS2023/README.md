# CCS2023

Number of papers: 3

## [Large language models for code: Security hardening and adversarial testing](paper_1.md)
- **Authors**: He, Jingxuan and Vechev, Martin
- **Abstract**: Large language models (large LMs) are increasingly trained on massive codebases and used to generate code. However, LMs lack awareness of security and are found to frequently produce unsafe code. This work studies the security of LMs along two important axes: (i) security hardening, which aims to enhance LMs' reliability in generating secure code, and (ii) adversarial testing, which seeks to evaluate LMs' security at an adversarial standpoint. We address both of these by formulating a new securi...
- **Link**: [Read Paper](https://arxiv.org/abs/2302.05319)
[code generation](../../labels/code_generation.md), [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md), [defense](../../labels/defense.md), [attack](../../labels/attack.md)

## [Poster: Boosting Adversarial Robustness by Adversarial Pre-training](paper_3.md)
- **Authors**: Xu, Xiaoyun and Picek, Stjepan
- **Abstract**: Vision Transformer (ViT) shows superior performance on various tasks, but, similar to other deep learning techniques, it is vulnerable to adversarial attacks. Due to the differences between ViT and traditional CNNs, previous works designed new adversarial training methods as defenses according to the design of ViT, such as blocking attention to individual patches or dropping embeddings with low attention. However, these methods usually focus on fine-tuning stage or the training of the model itse...
- **Link**: [Read Paper](https://doi.org/10.1145/3576915.3624370)
[code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md), [defense](../../labels/defense.md)

## [Prompt Fuzzing for Fuzz Driver Generation](paper_2.md)
- **Authors**: Lyu, Yunlong and Xie, Yuxuan and Chen, Peng and Chen, Hao
- **Abstract**: Writing high-quality fuzz drivers is time-consuming and requires a deep understanding of the library. However, the performance of the state-of-the-art automatic fuzz driver generation techniques leaves a lot to be desired. Fuzz drivers, which are learned from consumer code, can reach deep states but are restricted to their external inputs. On the other hand, interpretative fuzzing can explore most APIs but requires numerous attempts in a vast search space. We propose PromptFuzz, a coverage-guide...
- **Link**: [Read Paper](https://arxiv.org/pdf/2312.17677.pdf)
[program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)