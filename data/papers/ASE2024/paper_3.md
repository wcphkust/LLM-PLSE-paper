# Understanding Code Changes Practically with Small-Scale Language Models

**Authors**: Li, Cong and Xu, Zhaogui and Di, Peng and Wang, Dongxia and Li, Zheng and Zheng, Qian

**Abstract**:

Recent studies indicate that traditional techniques for understanding code changes are not as effective as techniques that directly prompt language models (LMs). However, current LM-based techniques heavily rely on expensive, large LMs (LLMs) such as GPT-4 and Llama-13b, which are either commercial or prohibitively costly to deploy on a wide scale, thereby restricting their practical applicability. This paper explores the feasibility of deploying small LMs (SLMs) while maintaining comparable or superior performance to LLMs in code change understanding. To achieve this, we created a small yet high-quality dataset called HQCM which was meticulously reviewed, revised, and validated by five human experts. We fine-tuned state-of-the-art 7b and 220m SLMs using HQCM and compared them with traditional techniques and LLMs with ≥70b parameters. Our evaluation confirmed HQCM's benefits and demonstrated that SLMs, after finetuning by HQCM, can achieve superior performance in three change understanding tasks: change summarization, change classification, and code refinement. This study supports the use of SLMs in environments with security, computational, and financial constraints, such as in industry scenarios and on edge devices, distinguishing our work from the others.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3694999)

**Labels**: static analysis, code summarization, code model, training, source code model
