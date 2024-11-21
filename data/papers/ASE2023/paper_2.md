# An Empirical Study on Fine-Tuning Large Language Models of Code for Automated Program Repair

**Authors**: Huang, Kai and Meng, Xiangxin and Zhang, Jian and Liu, Yang and Wang, Wenjie and Li, Shuhao and Zhang, Yuqing

**Abstract**:

The advent of large language models (LLMs) has opened up new opportunities for automated program repair (APR). In particular, some recent studies have explored how to leverage large language models of code (LLMCs) for program repair tasks and show promising results. However, most of them adopt the zero/few-shot learning paradigm for APR, which directly use LLMCs to generate the possibly correct code given its surrounding context. Though effective, the repair capabilities of LLMCs based on the fine-tuning paradigm have yet to be extensively explored. Also, it remains unknown whether LLMCs have the potential to repair more complicated bugs (e.g., multi-hunk bugs). To fill the gap, in this work, we conduct a comprehensive study on the program repair capability of LLMCs in the fine-tuning paradigm. We select 5 popular LLMCs with representative pre-training architectures, including CodeBERT, GraphCode-BERT, PLBART, CodeT5, and UniX coder. We consider 3 typical program repair scenarios (i.e., bugs, vulnerabilities, and errors) involving 3 programming languages (i.e., Java, $\mathrm{C}/\mathrm{C}++$, and JavaScript). Notably, we take both single-hunk and multi-hunk bugs/vulnerabilities into account. We then fine-tune them on widely-used datasets and compare them with existing state-of-the-art APR tools. We also investigate the impact of different design choices, which include code abstractions, code representations, and model evaluation metrics. Our experimental results show that LLMCs in the fine-tuning paradigm can significantly outperform previous state-of-the-art APR tools. Through in-depth analysis, we provide insights into choosing appropriate strategies to guide LLMCs for better performance. Lastly, we reveal several limitations of LLMCs for APR and make suggestions for future research on LLMC-based APR.

**Link**: [Read Paper](No Link Available)

**Labels**: code generation, program repair, empirical study
