# NAACL2024

Number of papers: 6

## [Deceptive Semantic Shortcuts on Reasoning Chains: How Far Can Models Go without Hallucination?](paper_6.md)
- **Authors**: Li, Bangzheng and Zhou, Ben and Wang, Fei and Fu, Xingyu and Roth, Dan and Chen, Muhao
- **Abstract**: Despite the high performances of large language models (LLMs) across numerous benchmarks, recent research has unveiled their suffering from hallucinations and unfaithful reasoning. This work studies a type of hallucination induced by semantic associations. We investigate to what extent LLMs take shortcuts from certain keyword/entity biases in the prompt instead of following correct reasoning paths. To quantify this phenomenon, we propose a novel probing method and benchmark called EUREQA. EUREQA...
- **Link**: [Read Paper](https://aclanthology.org/2024.naacl-long.424/)
[hallucination in reasoning](../../labels/hallucination_in_reasoning.md), [empirical study](../../labels/empirical_study.md)

## [Evaluating In-Context Learning of Libraries for Code Generation](paper_4.md)
- **Authors**: Patel, Arkil and Reddy, Siva and Bahdanau, Dzmitry and Dasigi, Pradeep
- **Abstract**: Contemporary Large Language Models (LLMs) exhibit a high degree of code generation and comprehension capability. A particularly promising area is their ability to interpret code modules from unfamiliar libraries for solving user-instructed tasks. Recent work has shown that large proprietary LLMs can learn novel library usage in-context from demonstrations. These results raise several open questions: whether demonstrations of library usage is required, whether smaller (and more open) models also ...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.naacl-long.161)
[code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [empirical study](../../labels/empirical_study.md)

## [PaD: Program-aided Distillation Can Teach Small Models Reasoning Better than Chain-of-thought Fine-tuning](paper_3.md)
- **Authors**: Zhu, Xuekai and Qi, Biqing and Zhang, Kaiyan and Long, Xinwei and Lin, Zhouhan and Zhou, Bowen
- **Abstract**: While large language models (LLMs) excel in various natural language processing tasks, their huge size and the inaccessibility of parameters present challenges for practical deployment. Previous studies try to distill task-specific ability from LLMs to smaller models, using data synthesis and chain-of-thought (CoT) fine-tuning. However, synthetic CoT data often contains faulty reasoning, which deteriorates the quality of distillation, especially in reasoning capabilities. In this work, we propos...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.naacl-long.142)
[prompt strategy](../../labels/prompt_strategy.md), [reason with code](../../labels/reason_with_code.md)

## [Program-Aided Reasoners (Better) Know What They Know](paper_2.md)
- **Authors**: Kabra, Anubha and Rangreji, Sanketh and Mathur, Yash and Madaan, Aman and Liu, Emmy and Neubig, Graham
- **Abstract**: Prior work shows that program-aided reasoning, in which large language models (LLMs) are combined with programs written in programming languages such as Python, can significantly improve accuracy on various reasoning tasks. However, while accuracy is essential, it is also important for such reasoners to “know what they know”, which can be quantified through the calibration of the model. In this paper, we compare the calibration of Program Aided Language Models (PAL) and text-based Chain-of-thoug...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.naacl-long.125)
[prompt strategy](../../labels/prompt_strategy.md), [reason with code](../../labels/reason_with_code.md)

## [UICoder: Finetuning Large Language Models to Generate User Interface Code through Automated Feedback](paper_5.md)
- **Authors**: Wu, Jason and Schoop, Eldon and Leung, Alan and Barik, Titus and Bigham, Jeffrey and Nichols, Jeffrey
- **Abstract**: Many large language models (LLMs) struggle to consistently generate UI code that compiles and produces visually relevant designs. Existing approaches to improve generation rely either on expensive human feedback or distilling a proprietary model. In this paper, we explore the use of automated feedback (compilers and multi-modal models) to guide LLMs to generate high-quality UI code. Our method starts with an existing LLM and iteratively produces improved models by self-generating a large synthet...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.naacl-long.417)
[code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)

## [Unleashing the Emergent Cognitive Synergy in Large Language Models: A Task-Solving Agent through Multi-Persona Self-Collaboration](paper_1.md)
- **Authors**: Wang, Zhenhailong and Mao, Shaoguang and Wu, Wenshan and Ge, Tao and Wei, Furu and Ji, Heng
- **Abstract**: Human intelligence thrives on cognitive synergy, where collaboration among different minds yield superior outcomes compared to isolated individuals. In this work, we propose Solo Performance Prompting (SPP), which transforms a single LLM into a cognitive synergist by engaging in multi-turn self-collaboration with multiple personas. A cognitive synergist is an intelligent agent that collaboratively combines multiple minds’ strengths and knowledge to enhance problem-solving in complex tasks. By dy...
- **Link**: [Read Paper](https://doi.org/10.18653/v1/2024.naacl-long.15)
[agent design](../../labels/agent_design.md), [planning](../../labels/planning.md)