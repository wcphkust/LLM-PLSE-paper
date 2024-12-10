# Code Model Security

- [An Extensive Study on Adversarial Attack against Pre-trained Models of Code](../venues/FSE2023/paper_11.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Transformer-based pre-trained models of code (PTMC) have been widely utilized and have achieved state-of-the-art performance in many mission-critical applications. However, they can be vulnerable to adversarial attacks through identifier substitution or coding style transformation, which can significantly degrade accuracy and may further incur security concerns. Although several approaches have been proposed to generate adversarial examples for PTMC, the effectiveness and efficiency of such appr...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md), [empirical study](empirical_study.md)


- [An investigation into misuse of java security apis by large language models](../venues/ASIACCS2024/paper_1.md), ([ASIACCS2024](../venues/ASIACCS2024/README.md))

  - **Abstract**: The increasing trend of using Large Language Models (LLMs) for code generation raises the question of their capability to generate trustworthy code. While many researchers are exploring the utility of code generation for uncovering software vulnerabilities, one crucial but often overlooked aspect is the security Application Programming Interfaces (APIs). APIs play an integral role in upholding software security, yet effectively integrating security APIs presents substantial challenges. This lead...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md), [empirical study](empirical_study.md)


- [Attacks and Defenses for Large Language Models on Coding Tasks](../venues/ASE2024/paper_32.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Modern large language models (LLMs), such as ChatGPT, have demonstrated impressive capabilities for coding tasks, including writing and reasoning about code. They improve upon previous neural network models of code, such as code2seq or seq2seq, that already demonstrated competitive results when performing tasks such as code summarization and identifying code vulnerabilities. However, these previous code models were shown vulnerable to adversarial examples, i.e., small syntactic perturbations des...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md)


- [Attribution-guided Adversarial Code Prompt Generation for Code Completion Models](../venues/ASE2024/paper_45.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Large language models have made significant progress in code completion, which may further remodel future software development. However, these code completion models are found to be highly risky as they may introduce vulnerabilities unintentionally or be induced by a special input, i.e., adversarial code prompt. Prior studies mainly focus on the robustness of these models, but their security has not been fully analyzed.In this paper, we propose a novel approach AdvPro that can automatically gene...
  - **Labels**: [code generation](code_generation.md), [code completion](code_completion.md), [code model](code_model.md), [code model security](code_model_security.md)


- [AutoDetect: Towards a Unified Framework for Automated Weakness Detection in Large Language Models](../venues/EMNLP2024/paper_8.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Although Large Language Models (LLMs) are becoming increasingly powerful, they still exhibit significant but subtle weaknesses, such as mistakes in instruction-following or coding tasks.As these unexpected errors could lead to severe consequences in practical deployments, it is crucial to investigate the limitations within LLMs systematically.Traditional benchmarking approaches cannot thoroughly pinpoint specific model deficiencies, while manual inspections are costly and not scalable. In this p...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md), [empirical study](empirical_study.md)


- [CoSec: On-the-Fly Security Hardening of Code LLMs via Supervised Co-decoding](../venues/ISSTA2024/paper_18.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: Large Language Models (LLMs) specialized in code have shown exceptional proficiency across various programming-related tasks, particularly code generation. Nonetheless, due to its nature of pretraining on massive uncritically filtered data, prior studies have shown that code LLMs are prone to generate code with potential vulnerabilities. Existing approaches to mitigate this risk involve crafting data without vulnerability and subsequently retraining or fine-tuning the model. As the number of par...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md)


- [CodeIP: A Grammar-Guided Multi-Bit Watermark for Large Language Models of Code](../venues/EMNLP2024/paper_9.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large Language Models (LLMs) have achieved remarkable progress in code generation. It now becomes crucial to identify whether the code is AI-generated and to determine the specific model used, particularly for purposes such as protecting Intellectual Property (IP) in industry and preventing cheating in programming exercises. To this end, several attempts have been made to insert watermarks into machine-generated code. However, existing approaches are limited to inserting only a single bit of inf...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model security](code_model_security.md)


- [Constrained Decoding for Secure Code Generation](../venues/arXiv2024/paper_3.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Code Large Language Models (Code LLMs) have been increasingly used by developers to boost productivity, but they often generate vulnerable code. Thus, there is an urgent need to ensure that code generated by Code LLMs is correct and secure. Previous research has primarily focused on generating secure code, overlooking the fact that secure code also needs to be correct. This oversight can lead to a false sense of security. Currently, the community lacks a method to measure actual progress in this...
  - **Labels**: [code generation](code_generation.md), [code model](code_model.md), [code model security](code_model_security.md)


- [Defending Large Language Models Against Jailbreak Attacks via Layer-specific Editing](../venues/EMNLP2024/paper_6.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Large language models (LLMs) are increasingly being adopted in a wide range of real-world applications. Despite their impressive performance, recent studies have shown that LLMs are vulnerable to deliberately crafted adversarial prompts even when aligned via Reinforcement Learning from Human Feedback or supervised fine-tuning. While existing defense methods focus on either detecting harmful prompts or reducing the likelihood of harmful responses through various means, defending LLMs against jail...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md)


- [Instruction tuning for secure code generation](../venues/ICML2024/paper_1.md), ([ICML2024](../venues/ICML2024/README.md))

  - **Abstract**: Modern language models (LMs) have gained widespread acceptance in everyday and professional contexts, particularly in programming. An essential procedure enabling this adoption is instruction tuning, which substantially enhances LMs' practical utility by training them to follow user instructions and human preferences. However, existing instruction tuning schemes overlook a crucial aspect: the security of generated code. As a result, even the state-of-the-art instruction-tuned LMs frequently prod...
  - **Labels**: [code generation](code_generation.md), [code model](code_model.md), [code model security](code_model_security.md)


- [Large language models for code: Security hardening and adversarial testing](../venues/CCS2023/paper_1.md), ([CCS2023](../venues/CCS2023/README.md))

  - **Abstract**: Large language models (large LMs) are increasingly trained on massive codebases and used to generate code. However, LMs lack awareness of security and are found to frequently produce unsafe code. This work studies the security of LMs along two important axes: (i) security hardening, which aims to enhance LMs' reliability in generating secure code, and (ii) adversarial testing, which seeks to evaluate LMs' security at an adversarial standpoint. We address both of these by formulating a new securi...
  - **Labels**: [code generation](code_generation.md), [code model](code_model.md), [code model security](code_model_security.md)


- [PELICAN: exploiting backdoors of naturally trained deep learning models in binary code analysis](../venues/USENIXSec2023/paper_3.md), ([USENIXSec2023](../venues/USENIXSec2023/README.md))

  - **Abstract**: Deep Learning (DL) models are increasingly used in many cyber-security applications and achieve superior performance compared to traditional solutions. In this paper, we study backdoor vulnerabilities in naturally trained models used in binary analysis. These backdoors are not injected by attackers but rather products of defects in datasets and/or training processes. The attacker can exploit these vulnerabilities by injecting some small fixed input pattern (e.g., an instruction) called backdoor ...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md), [code model](code_model.md), [code model training](code_model_training.md), [binary code model](binary_code_model.md)


- [Poster: Boosting Adversarial Robustness by Adversarial Pre-training](../venues/CCS2023/paper_3.md), ([CCS2023](../venues/CCS2023/README.md))

  - **Abstract**: Vision Transformer (ViT) shows superior performance on various tasks, but, similar to other deep learning techniques, it is vulnerable to adversarial attacks. Due to the differences between ViT and traditional CNNs, previous works designed new adversarial training methods as defenses according to the design of ViT, such as blocking attention to individual patches or dropping embeddings with low attention. However, these methods usually focus on fine-tuning stage or the training of the model itse...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md)


- [Security of Language Models for Code: A Systematic Literature Review](../venues/arXiv2024/paper_1.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Language models for code (CodeLMs) have emerged as powerful tools for code-related tasks, outperforming traditional methods and standard machine learning approaches. However, these models are susceptible to security vulnerabilities, drawing increasing research attention from domains such as software engineering, artificial intelligence, and cybersecurity. Despite the growing body of research focused on the security of CodeLMs, a comprehensive survey in this area remains absent. To address this g...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md), [survey](survey.md)


- [Traces of Memorisation in Large Language Models for Code](../venues/ICSE2024/paper_8.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Large language models have gained significant popularity because of their ability to generate human-like text and potential applications in various fields, such as Software Engineering. Large language models for code are commonly trained on large unsanitised corpora of source code scraped from the internet. The content of these datasets is memorised and can be extracted by attackers with data extraction attacks. In this work, we explore memorisation in large language models for code and compare ...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md), [benchmark](benchmark.md)


- [TrojanPuzzle: Covertly Poisoning Code-Suggestion Models](../venues/S&P2024/paper_3.md), ([S&P2024](../venues/S&P2024/README.md))

  - **Abstract**: With tools like GitHub Copilot, automatic code suggestion is no longer a dream in software engineering. These tools, based on large language models, are typically trained on massive corpora of code mined from unvetted public sources. As a result, these models are susceptible to data poisoning attacks where an adversary manipulates the model’s training by injecting malicious data. Poisoning attacks could be designed to influence the model’s suggestions at run time for chosen contexts, such as ind...
  - **Labels**: [code model](code_model.md), [code model security](code_model_security.md), [code generation](code_generation.md), [code completion](code_completion.md)


- [Who Wrote this Code? Watermarking for Code Generation](../venues/ACL2024/paper_15.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Since the remarkable generation performance of large language models raised ethical and legal concerns, approaches to detect machine-generated text by embedding watermarks are being developed.However, we discover that the existing works fail to function appropriately in code generation tasks due to the task’s nature of having low entropy.Extending a logit-modifying watermark method, we propose Selective WatErmarking via Entropy Thresholding (SWEET), which enhances detection ability and mitigates...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [code model](code_model.md), [code model security](code_model_security.md)
