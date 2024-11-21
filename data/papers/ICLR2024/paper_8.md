# Self-contradictory hallucinations of large language models: Evaluation, detection and mitigation

**Authors**: M{\"u}ndler, Niels and He, Jingxuan and Jenko, Slobodan and Vechev, Martin

**Abstract**:

Large language models (large LMs) are susceptible to producing text that contains hallucinated content. An important instance of this problem is self-contradiction, where the LM generates two contradictory sentences within the same context. In this work, we present a comprehensive investigation into self-contradiction for various instruction-tuned LMs, covering evaluation, detection, and mitigation. Our primary evaluation task is open-domain text generation, but we also demonstrate the applicability of our approach to shorter question answering. Our analysis reveals the prevalence of self-contradictions, e.g., in 17.7% of all sentences produced by ChatGPT. We then propose a novel prompting-based framework designed to effectively detect and mitigate self-contradictions. Our detector achieves high accuracy, e.g., around 80% F1 score when prompting ChatGPT. The mitigation algorithm iteratively refines the generated text to remove contradictory information while preserving text fluency and informativeness. Importantly, our entire framework is applicable to black-box LMs and does not require retrieval of external knowledge. Rather, our method complements retrieval-based methods, as a large portion of self-contradictions (e.g., 35.2% for ChatGPT) cannot be verified using online text.

**Link**: [Read Paper](No Link Available)

**Labels**: hallucination in reasoning, empirical study
