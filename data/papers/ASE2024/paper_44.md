# ART: A Unified Unsupervised Framework for Incident Management in Microservice Systems

**Authors**: Sun, Yongqian and Shi, Binpeng and Mao, Mingyu and Ma, Minghua and Xia, Sibo and Zhang, Shenglin and Pei, Dan

**Abstract**:

Automated incident management is critical for large-scale microservice systems, including tasks such as anomaly detection (AD), failure triage (FT), and root cause localization (RCL). Currently, most techniques focus only on a single task, overlooking shared knowledge across closely related tasks. However, employing isolated models for managing multiple tasks may result in inefficiencies, delayed responses, a lack of systemic perspective, and complexity in updates and operations. Therefore we propose ART, an unsupervised framework that integrates a full-process solution covering Anomaly detection, failure Triage, and Root cause localization. It reaches the unification of multiple tasks by extracting the shared knowledge. Specifically, we first conduct an empirical study to analyze how the shared knowledge embedded in anomalous deviations manifests in AD, FT, and RCL. To better calculate deviations and extract shared knowledge, we sequentially model channel, temporal, and call dependencies using Transformer Encoder, GRU, and GraphSAGE, respectively. Then unified failure representations enhance the interpretability of abstract features with explicit semantic information, serving as the basis for unsupervised multitask solutions. Our evaluations on the datasets generated from two benchmark microservice systems demonstrate that ART outperforms existing methods in terms of AD (improving by 5.65\% to 60.8\%), FT (improving by 13.2\% to 95.7\%), and RCL (improving by 13.3\% to 205\%).

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695495)

**Labels**: general coding task
