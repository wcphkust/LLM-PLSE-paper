# Towards Efficient Fine-Tuning of Language Models With Organizational Data for Automated Software Review

**Authors**: Nashaat, Mona and Miller, James

**Abstract**:

Large language models like BERT and GPT possess significant capabilities and potential impacts across various applications. Software engineers often use these models for code-related tasks, including generating, debugging, and summarizing code. Nevertheless, large language models still have several flaws, including model hallucination. (e.g., generating erroneous code and producing outdated and inaccurate programs) and the substantial computational resources and energy required for training and fine-tuning. To tackle these challenges, we propose CodeMentor, a framework for few-shot learning to train large language models with the data available within the organization. We employ the framework to train a language model for code review activities, such as code refinement and review generation. The framework utilizes heuristic rules and weak supervision techniques to leverage available data, such as previous review comments, issue reports, and related code updates. Then, the framework employs the constructed dataset to fine-tune LLMs for code review tasks. Additionally, the framework integrates domain expertise by employing reinforcement learning with human feedback. This allows domain experts to assess the generated code and enhance the model performance. Also, to assess the performance of the proposed model, we evaluate it with four state-of-the-art techniques in various code review tasks. The experimental results attest that CodeMentor enhances the performance in all tasks compared to the state-of-the-art approaches, with an improvement of up to 22.3%, 43.4%, and 24.3% in code quality estimation, review generation, and bug report summarization tasks, respectively.

**Link**: [Read Paper](https://doi.org/10.1109/TSE.2024.3428324)

**Labels**: code generation, program repair, code model, training, source code model
