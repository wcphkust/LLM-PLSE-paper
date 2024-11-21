# Defending Large Language Models Against Jailbreak Attacks via Layer-specific Editing

**Authors**: Zhao, Wei and Li, Zhe and Li, Yige and Zhang, Ye and Sun, Jun

**Abstract**:

Large language models (LLMs) are increasingly being adopted in a wide range of real-world applications. Despite their impressive performance, recent studies have shown that LLMs are vulnerable to deliberately crafted adversarial prompts even when aligned via Reinforcement Learning from Human Feedback or supervised fine-tuning. While existing defense methods focus on either detecting harmful prompts or reducing the likelihood of harmful responses through various means, defending LLMs against jailbreak attacks based on the inner mechanisms of LLMs remains largely unexplored. In this work, we investigate how LLMs respond to harmful prompts and propose a novel defense method termed Layer-specific Editing (LED) to enhance the resilience of LLMs against jailbreak attacks. Through LED, we reveal that several critical safety layers exist among the early layers of LLMs. We then show that realigning these safety layers (and some selected additional layers) with the decoded safe response from identified toxic layers can significantly improve the alignment of LLMs against jailbreak attacks. Extensive experiments across various LLMs (e.g., Llama2, Mistral) show the effectiveness of LED, which effectively defends against jailbreak attacks while maintaining performance on benign prompts. Our code is available at https://github.com/ledllm/ledllm.

**Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.293)

**Labels**: code model, security, defense
