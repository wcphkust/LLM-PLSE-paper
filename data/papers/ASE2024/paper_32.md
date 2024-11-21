# Attacks and Defenses for Large Language Models on Coding Tasks

**Authors**: Zhang, Chi and Wang, Zifan and Zhao, Ruoshi and Mangal, Ravi and Fredrikson, Matt and Jia, Limin and Pasareanu, Corina

**Abstract**:

Modern large language models (LLMs), such as ChatGPT, have demonstrated impressive capabilities for coding tasks, including writing and reasoning about code. They improve upon previous neural network models of code, such as code2seq or seq2seq, that already demonstrated competitive results when performing tasks such as code summarization and identifying code vulnerabilities. However, these previous code models were shown vulnerable to adversarial examples, i.e., small syntactic perturbations designed to "fool" the models. In this paper, we first aim to study the transferability of adversarial examples, generated through white-box attacks on smaller code models, to LLMs. We also propose a new attack using an LLM to generate the perturbations. Further, we propose novel cost-effective techniques to defend LLMs against such adversaries via prompting, without incurring the cost of retraining. These prompt-based defenses involve modifying the prompt to include additional information, such as examples of adversarially perturbed code and explicit instructions for reversing adversarial perturbations. Our preliminary experiments show the effectiveness of the attacks and the proposed defenses on popular LLMs such as GPT-3.5 and GPT-4.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695297)

**Labels**: code model, security, attack, defense
