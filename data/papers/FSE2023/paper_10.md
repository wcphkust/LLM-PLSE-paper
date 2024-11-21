# Log Parsing with Generalization Ability under New Log Types

**Authors**: Yu, Siyu and Wu, Yifan and Li, Zhijing and He, Pinjia and Chen, Ningjiang and Liu, Changjian

**Abstract**:

Log parsing, which converts semi-structured logs into structured logs, is the first step for automated log analysis.  Existing parsers are still unsatisfactory in real-world systems due to new log types in new-coming logs.  In practice, available logs collected during system runtime often do not contain all the possible log types of a system because log types related to infrequently activated system states are unlikely to be recorded and new log types are frequently introduced with system updates.  Meanwhile, most existing parsers require preprocessing to extract variables in advance, but preprocessing is based on the operator’s prior knowledge of available logs and therefore may not work well on new log types.  In addition, parser parameters set based on available logs are difficult to generalize to new log types.  To support new log types, we propose a variable generation imitation strategy to craft a novel log parsing approach with generalization ability, called Log3T. Log3T employs a pre-trained transformer encoder-based model to extract log templates and can update parameters at parsing time to adapt to new log types by a modified test-time training.  Experimental results on 16 benchmark datasets show that Log3T outperforms the state-of-the-art parsers in terms of parsing accuracy. In addition, Log3T can automatically adapt to new log types in new-coming logs.

**Link**: [Read Paper](https://doi.org/10.1145/3611643.3616355)

**Labels**: software maintenance and deployment, system log analysis
