# Attribution-guided Adversarial Code Prompt Generation for Code Completion Models

**Authors**: Li, Xueyang and Meng, Guozhu and Liu, Shangqing and Xiang, Lu and Sun, Kun and Chen, Kai and Luo, Xiapu and Liu, Yang

**Abstract**:

Large language models have made significant progress in code completion, which may further remodel future software development. However, these code completion models are found to be highly risky as they may introduce vulnerabilities unintentionally or be induced by a special input, i.e., adversarial code prompt. Prior studies mainly focus on the robustness of these models, but their security has not been fully analyzed.In this paper, we propose a novel approach AdvPro that can automatically generate adversarial code prompts for these code completion models. AdvPro incorporates 14 code mutation strategies at the granularity of five levels. The mutation strategies are ensured to make no modifications to code semantics, which should be insensitive to the models. Moreover, we leverage gradient attribution to localize the important code as mutation points and speed up adversarial prompt generation. Extensive experiments are conducted on 13 state-of-the-art models belonging to 7 families. The results show that our approach can effectively generate adversarial prompts, with an increased rate of 69.6\% beyond the baseline ALERT. By comparing the results of attribution-guided localization, we find that the recognition results of important tokens in input codes are almost identical among different models. This finding reduces the limitation of using open-source alternative models to guide adversarial attacks against closed-source models. The results of the ablation study on the components of AdvPro show that CCMs focus on variable names, but other structures are equally crucial.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695517)

**Labels**: code generation, code completion, code model, security, attack
