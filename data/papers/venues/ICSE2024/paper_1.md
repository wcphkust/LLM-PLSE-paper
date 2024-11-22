# UniLog: Automatic Logging via LLM and In-Context Learning

**Authors**: Xu, Junjielong and Cui, Ziang and Zhao, Yuan and Zhang, Xu and He, Shilin and He, Pinjia and Li, Liqun and Kang, Yu and Lin, Qingwei and Dang, Yingnong and Rajmohan, Saravan and Zhang, Dongmei

**Abstract**:

Logging, which aims to determine the position of logging statements, the verbosity levels, and the log messages, is a crucial process for software reliability enhancement. In recent years, numerous automatic logging tools have been designed to assist developers in one of the logging tasks (e.g., providing suggestions on whether to log in try-catch blocks). These tools are useful in certain situations yet cannot provide a comprehensive logging solution in general. Moreover, although recent research has started to explore end-to-end logging, it is still largely constrained by the high cost of fine-tuning, hindering its practical usefulness in software development. To address these problems, this paper proposes UniLog, an automatic logging framework based on the in-context learning (ICL) paradigm of large language models (LLMs). Specifically, UniLog can generate an appropriate logging statement with only a prompt containing five demonstration examples without any model tuning. In addition, UniLog can further enhance its logging ability after warmup with only a few hundred random samples. We evaluated UniLog on a large dataset containing 12,012 code snippets extracted from 1,465 GitHub repositories. The results show that UniLog achieved the state-of-the-art performance in automatic logging: (1) 76.9\% accuracy in selecting logging positions, (2) 72.3\% accuracy in predicting verbosity levels, and (3) 27.1 BLEU-4 score in generating log messages. Meanwhile, UniLog requires less than 4\% of the parameter tuning time needed by fine-tuning the same LLM.

**Link**: [Read Paper](https://doi.org/10.1145/3597503.3623326)

**Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [system log analysis](../../labels/system_log_analysis.md)
