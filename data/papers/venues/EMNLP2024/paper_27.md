# CodeAgent: Autonomous Communicative Agents for Code Review

**Authors**: Tang, Xunzhu and Kim, Kisub and Song, Yewei and Lothritz, Cedric and Li, Bei and Ezzini, Saad and Tian, Haoye and Klein, Jacques and Bissyandé, Tegawendé F.

**Abstract**:

Code review, which aims at ensuring the overall quality and reliability of software, is a cornerstone of software development. Unfortunately, while crucial, Code review is a labor-intensive process that the research community is looking to automate. Existing automated methods rely on single input-output generative models and thus generally struggle to emulate the collaborative nature of code review. This work introduces CodeAgent, a novel multi-agent Large Language Model (LLM) system for code review automation. CodeAgent incorporates a supervisory agent, QA-Checker, to ensure that all the agents’ contributions address the initial review question. We evaluated CodeAgent on critical code review tasks: (1) detect inconsistencies between code changes and commit messages, (2) identify vulnerability introductions, (3) validate code style adherence, and (4) suggest code revisions. The results demonstrate CodeAgent’s effectiveness, contributing to a new state-of-the-art in code review automation. Our data and code are publicly available (https://github.com/Daniel4SE/codeagent).

**Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.632)

**Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [code review](../../labels/code_review.md), [agent design](../../labels/agent_design.md)
