# Pre-train, prompt, and predict: A systematic survey of prompting methods in natural language processing

**Authors**: Liu, Pengfei and Yuan, Weizhe and Fu, Jinlan and Jiang, Zhengbao and Hayashi, Hiroaki and Neubig, Graham

**Abstract**:

This article surveys and organizes research works in a new paradigm in natural language processing, which we dub “prompt-based learning.” Unlike traditional supervised learning, which trains a model to take in an input x and predict an output y as P(y|x), prompt-based learning is based on language models that model the probability of text directly. To use these models to perform prediction tasks, the original input x is modified using a template into a textual string prompt x′ that has some unfilled slots, and then the language model is used to probabilistically fill the unfilled information to obtain a final string x̂, from which the final output y can be derived. This framework is powerful and attractive for a number of reasons: It allows the language model to be pre-trained on massive amounts of raw text, and by defining a new prompting function the model is able to perform few-shot or even zero-shot learning, adapting to new scenarios with few or no labeled data. In this article, we introduce the basics of this promising paradigm, describe a unified set of mathematical notations that can cover a wide variety of existing work, and organize existing work along several dimensions, e.g., the choice of pre-trained language models, prompts, and tuning strategies. To make the field more accessible to interested beginners, we not only make a systematic review of existing works and a highly structured typology of prompt-based concepts but also release other resources, e.g., a website NLPedia–Pretrain including constantly updated survey and paperlist.

**Link**: [Read Paper](https://arxiv.org/pdf/2107.13586)

**Labels**: [survey](../../labels/survey.md), [prompt strategy](../../labels/prompt_strategy.md)
