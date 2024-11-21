# Face It Yourselves: An LLM-Based Two-Stage Strategy to Localize Configuration Errors via Logs

**Authors**: Shan, Shiwen and Huo, Yintong and Su, Yuxin and Li, Yichen and Li, Dan and Zheng, Zibin

**Abstract**:

Configurable software systems are prone to configuration errors, resulting in significant losses to companies. However, diagnosing these errors is challenging due to the vast and complex configuration space. These errors pose significant challenges for both experienced maintainers and new end-users, particularly those without access to the source code of the software systems. Given that logs are easily accessible to most end-users, we conduct a preliminary study to outline the challenges and opportunities of utilizing logs in localizing configuration errors. Based on the insights gained from the preliminary study, we propose an LLM-based two-stage strategy for end-users to localize the root-cause configuration properties based on logs. We further implement a tool, LogConfigLocalizer, aligned with the design of the aforementioned strategy, hoping to assist end-users in coping with configuration errors through log analysis. To the best of our knowledge, this is the first work to localize the root-cause configuration properties for end-users based on Large Language Models (LLMs) and logs. We evaluate the proposed strategy on Hadoop by LogConfigLocalizer and prove its efficiency with an average accuracy as high as 99.91\%. Additionally, we also demonstrate the effectiveness and necessity of different phases of the methodology by comparing it with two other variants and a baseline tool. Moreover, we validate the proposed methodology through a practical case study to demonstrate its effectiveness and feasibility.

**Link**: [Read Paper](https://doi.org/10.1145/3650212.3652106)

**Labels**: software maintenance and deployment, software configuration
