# XSemPLR: Cross-Lingual Semantic Parsing in Multiple Natural Languages and Meaning Representations

**Authors**: Zhang, Yusen and Wang, Jun and Wang, Zhiguo and Zhang, Rui

**Abstract**:

Cross-Lingual Semantic Parsing (CLSP) aims to translate queries in multiple natural languages (NLs) into meaning representations (MRs) such as SQL, lambda calculus, and logic forms. However, existing CLSP models are separately proposed and evaluated on datasets of limited tasks and applications, impeding a comprehensive and unified evaluation of CLSP on a diverse range of NLs and MRs. To this end, we present XSemPLR, a unified benchmark for cross-lingual semantic parsing featured with 22 natural languages and 8 meaning representations by examining and selecting 9 existing datasets to cover 5 tasks and 164 domains. We use XSemPLR to conduct a comprehensive benchmark study on a wide range of multilingual language models including encoder-based models (mBERT, XLM-R), encoder-decoder models (mBART, mT5), and decoder-based models (Codex, BLOOM). We design 6 experiment settings covering various lingual combinations (monolingual, multilingual, cross-lingual) and numbers of learning samples (full dataset, few-shot, and zero-shot). Our experiments show that encoder-decoder models (mT5) achieve the highest performance compared with other popular models, and multilingual training can further improve the average performance. Notably, multilingual large language models (e.g., BLOOM) are still inadequate to perform CLSP tasks. We also find that the performance gap between monolingual training and cross-lingual transfer learning is still significant for multilingual models, though it can be mitigated by cross-lingual few-shot training. Our dataset and code are available at https://github.com/psunlpgroup/XSemPLR.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2023.acl-long.887)

**Labels**: code model, training, source code model
