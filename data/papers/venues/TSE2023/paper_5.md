# Using Transfer Learning for Code-Related Tasks

**Authors**: Mastropaolo, Antonio and Cooper, Nathan and Palacio, David Nader and Scalabrino, Simone and Poshyvanyk, Denys and Oliveto, Rocco and Bavota, Gabriele

**Abstract**:

Deep learning (DL) techniques have been used to support several code-related tasks such as code summarization and bug-fixing. In particular, pre-trained transformer models are on the rise, also thanks to the excellent results they achieved in Natural Language Processing (NLP) tasks. The basic idea behind these models is to first pre-train them on a generic dataset using a self-supervised task (e.g., filling masked words in sentences). Then, these models are fine-tuned to support specific tasks of interest (e.g., language translation). A single model can be fine-tuned to support multiple tasks, possibly exploiting the benefits of &lt;italic&gt;transfer learning&lt;/italic&gt;. This means that knowledge acquired to solve a specific task (e.g., language translation) can be useful to boost performance on another task (e.g., sentiment classification). While the benefits of transfer learning have been widely studied in NLP, limited empirical evidence is available when it comes to code-related tasks. In this paper, we assess the performance of the Text-To-Text Transfer Transformer (T5) model in supporting four different code-related tasks: (i) automatic bug-fixing, (ii) injection of code mutants, (iii) generation of assert statements, and (iv) code summarization. We pay particular attention in studying the role played by pre-training and multi-task fine-tuning on the model's performance. We show that (i) the T5 can achieve better performance as compared to state-of-the-art baselines; and (ii) while pre-training helps the model, not all tasks benefit from a multi-task fine-tuning.

**Link**: [Read Paper](https://doi.org/10.1109/TSE.2022.3183297)

**Labels**: [general coding task](../../labels/general_coding_task.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)
