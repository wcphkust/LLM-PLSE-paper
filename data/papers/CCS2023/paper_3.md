# Poster: Boosting Adversarial Robustness by Adversarial Pre-training

**Authors**: Xu, Xiaoyun and Picek, Stjepan

**Abstract**:

Vision Transformer (ViT) shows superior performance on various tasks, but, similar to other deep learning techniques, it is vulnerable to adversarial attacks. Due to the differences between ViT and traditional CNNs, previous works designed new adversarial training methods as defenses according to the design of ViT, such as blocking attention to individual patches or dropping embeddings with low attention. However, these methods usually focus on fine-tuning stage or the training of the model itself. Improving robustness at the pre-training stage, especially with lower overhead, has yet to be thoroughly investigated. This paper proposes a novel method, Adv-MAE, which increases adversarial robustness by masked adversarial pre-training without a penalty to performance on clean data. We design a simple method to generate adversarial perturbation for the autoencoder, as the autoencoder does not provide classification results. Then, we use masked inputs with perturbation to conduct adversarial training for the autoencoder. The pre-trained autoencoder can be used to build a ViT with better robustness. Our experimental results show that, when using adversarial fine-tuning, Adv-MAE offers better accuracy under adversarial attack than the non-adversarial pre-training method (3.46\% higher on CIFAR-10, 1.12\% higher on Tiny ImageNet). It also shows better accuracy on clean data (4.94\% higher on CIFAR-10, 1.74\% higher on Tiny ImageNet), meaning Adv-MAE does not deteriorate performance on clean inputs. In addition, masked pre-training also shows much lower time consumption at each training epoch.

**Link**: [Read Paper](https://doi.org/10.1145/3576915.3624370)

**Labels**: code model, security, defense
