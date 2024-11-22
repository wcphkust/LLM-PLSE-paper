# SCPatcher: Mining Crowd Security Discussions to Enrich Secure Coding Practices

**Authors**: Jiang, Ziyou and Shi, Lin and Yang, Guowei and Wang, Qing

**Abstract**:

Secure coding practices (SCPs) have been proposed to guide software developers to write code securely to prevent potential security vulnerabilities. Yet, they are typically one-sentence principles without detailed specifications, e.g., “Properly free allocated memory upon the completion of functions and at all exit points.”, which makes them difficult to follow in practice, especially for software developers who are not yet experienced in secure programming. To address this problem, this paper proposes SCPatcher, an automated approach to enrich secure coding practices by mining crowd security discussions on online knowledge-sharing platforms, such as Stack Overflow. In particular, for each security post, SCPatcher first extracts the area of coding examples and coding explanations with a fix-prompt tuned Large Language Model (LLM) via Prompt Learning. Then, it hierarchically slices the lengthy code into coding examples and summarizes the coding explanations with the areas. Finally, SCPatcher matches the CWE and Public SCP, integrating them with extracted coding examples and explanations to form the SCP specifications, which are the wild SCPs with details, proposed by the developers. To evaluate the performance of SCPatcher, we conduct experiments on 3,907 security posts from Stack Overflow. The experimental results show that SCPatcher outperforms all baselines in extracting the coding examples with 2.73 % MLine on average, as well as coding explanations with 3.97 % F1 on average. Moreover, we apply SCPatcher on 447 new security posts to further evaluate its practicality, and the extracted SCP specifications enrich the public SCPs with 3,074 lines of code and 1,967 sentences.

**Link**: [Read Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10298463)

**Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [code review](../../labels/code_review.md)
