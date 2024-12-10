# CodeFort: Robust Training for Code Generation Models

**Authors**: Zhang, Yuhao and Wang, Shiqi and Qian, Haifeng and Wang, Zijian and Shang, Mingyue and Liu, Linbo and Gouda, Sanjay Krishna and Ray, Baishakhi and Ramanathan, Murali Krishna and Ma, Xiaofei and others

**Abstract**:

Code generation models are not robust to small perturbations, which often lead to inconsistent and incorrect generations and significantly degrade the performance of these models. Improving the robustness of code generation models is crucial to better user experience when these models are deployed in real-world applications. However, existing efforts have not addressed this issue for code generation models. To fill this gap, we propose CodeFort, a framework to improve the robustness of code generation models, generalizing a large variety of code perturbations to enrich the training data and enabling various robust training strategies, mixing data augmentation, batch augmentation, adversarial logits pairing, and contrastive learning, all carefully designed to support high-throughput training. Extensive evaluations show that we improve the average robust pass rates of baseline CodeGen models from 14.79 to 21.74. Notably, the improvement in robustness against code-syntax perturbations is evidenced by a significant decrease in pass rate drop from 95.04% to 53.35%

**Link**: [Read Paper](https://arxiv.org/pdf/2405.01567)

**Labels**: [code generation](../../labels/code_generation.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [code model](../../labels/code_model.md), [code model robustness](../../labels/code_model_robustness.md)
