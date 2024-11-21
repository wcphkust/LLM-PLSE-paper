# FastFixer: An Efficient and Effective Approach for Repairing Programming Assignments

**Authors**: Liu, Fang and Liu, Zhenwei and Zhao, Qianhui and Jiang, Jing and Zhang, Li and Sun, Zian and Li, Ge and Li, Zhongqi and Ma, Yuchi

**Abstract**:

Providing personalized and timely feedback for student's programming assignments is useful for programming education. Automated program repair (APR) techniques have been used to fix the bugs in programming assignments, where the Large Language Models (LLMs) based approaches have shown promising results. Given the growing complexity of identifying and fixing bugs in advanced programming assignments, current fine-tuning strategies for APR are inadequate in guiding the LLM to identify bugs and make accurate edits during the generative repair process. Furthermore, the autoregressive decoding approach employed by the LLM could potentially impede the efficiency of the repair, thereby hindering the ability to provide timely feedback. To tackle these challenges, we propose FastFixer, an efficient and effective approach for programming assignment repair. To assist the LLM in accurately identifying and repairing bugs, we first propose a novel repair-oriented fine-tuning strategy, aiming to enhance the LLM's attention towards learning how to generate the necessary patch and its associated context. Furthermore, to speed up the patch generation, we propose an inference acceleration approach that is specifically tailored for the program repair task. The evaluation results demonstrate that FastFixer obtains an overall improvement of 20.46\% in assignment fixing when compared to the state-of-the-art baseline. Considering the repair efficiency, FastFixer achieves a remarkable inference speedup of 16.67\texttimes{} compared to the autoregressive decoding algorithm.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695062)

**Labels**: code generation, program repair
