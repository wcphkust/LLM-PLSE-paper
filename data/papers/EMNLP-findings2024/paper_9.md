# AutoDetect: Towards a Unified Framework for Automated Weakness Detection in Large Language Models

**Authors**: Cheng, Jiale and Lu, Yida and Gu, Xiaotao and Ke, Pei and Liu, Xiao and Dong, Yuxiao and Wang, Hongning and Tang, Jie and Huang, Minlie

**Abstract**:

Although Large Language Models (LLMs) are becoming increasingly powerful, they still exhibit significant but subtle weaknesses, such as mistakes in instruction-following or coding tasks.As these unexpected errors could lead to severe consequences in practical deployments, it is crucial to investigate the limitations within LLMs systematically.Traditional benchmarking approaches cannot thoroughly pinpoint specific model deficiencies, while manual inspections are costly and not scalable. In this paper, we introduce a unified framework, AutoDetect, to automatically expose weaknesses in LLMs across various tasks. Inspired by the educational assessment process that measures students’ learning outcomes, AutoDetect consists of three LLM-powered agents: Examiner, Questioner, and Assessor.The collaboration among these three agents is designed to realize comprehensive and in-depth weakness identification. Our framework demonstrates significant success in uncovering flaws, with an identification success rate exceeding 30% in prominent models such as ChatGPT and Claude.More importantly, these identified weaknesses can guide specific model improvements, proving more effective than untargeted data augmentation methods like Self-Instruct. Our approach has led to substantial enhancements in popular LLMs, including the Llama series and Mistral-7b, boosting their performance by over 10% across several benchmarks.Code and data are publicly available at https://github.com/thu-coai/AutoDetect.

**Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.397)

**Labels**: code model, security, attack, empirical study
