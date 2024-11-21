# RealVul: Can We Detect Vulnerabilities in Web Applications with LLM?

**Authors**: Cao, Di and Liao, Yong and Shang, Xiuwei

**Abstract**:

The latest advancements in large language models (LLMs) have sparked interest in their potential for software vulnerability detection. However, there is currently a lack of research specifically focused on vulnerabilities in the PHP language, and challenges in data sampling and processing persist, hindering the model’s ability to effectively capture the characteristics of specific vulnerabilities. In this paper, we present RealVul, the first LLM-based framework designed for PHP vulnerability detection, addressing these issues. By improving code sampling methods and employing normalization techniques, we can isolate potential vulnerability triggers while streamlining the code and eliminating unnecessary semantic information, enabling the model to better understand and learn from the generated vulnerability samples. We also address the issue of insufficient PHP vulnerability samples by improving data synthesis methods. To evaluate RealVul’s performance, we conduct an extensive analysis using five distinct code LLMs on vulnerability data from 180 PHP projects. The results demonstrate a significant improvement in both effectiveness and generalization compared to existing methods, effectively boosting the vulnerability detection capabilities of these models.

**Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.472)

**Labels**: static analysis, bug detection
