# Coffee-Gym: An Environment for Evaluating and Improving Natural Language Feedback on Erroneous Code

**Authors**: Chae, Hyungjoo and Kwon, Taeyoon and Moon, Seungjun and Song, Yongho and Kang, Dongjin and Ong, Kai Tzu-iunn and Kwak, Beong-woo and Bae, Seonghyeon and Hwang, Seung-won and Yeo, Jinyoung

**Abstract**:

This paper presents Coffee-Gym, a comprehensive RL environment for training models that provide feedback on code editing. Coffee-Gym includes two major components: (1) Coffee, a dataset containing humans’ code edit traces for coding questions and human-written feedback for editing erroneous code; (2) CoffeeEval, a reward function that faithfully reflects the helpfulness of feedback by assessing the performance of the revised code in unit tests. With them, Coffee-Gym addresses the unavailability of high-quality datasets for training feedback models with RL, and provides more accurate rewards than the SOTA reward model (i.e., GPT-4). By applying Coffee-Gym, we elicit feedback models that outperform baselines in enhancing open-source code LLMs’ code editing, making them comparable with closed-source LLMs. We make the dataset and the model checkpoint publicly available in https://huggingface.co/spaces/Coffee-Gym/Project-Coffee-Gym.

**Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.1254)

**Labels**: code generation, program repair, benchmark
