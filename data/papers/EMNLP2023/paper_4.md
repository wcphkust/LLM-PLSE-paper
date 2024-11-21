# Symbolic Planning and Code Generation for Grounded Dialogue

**Authors**: Chiu, Justin and Zhao, Wenting and Chen, Derek and Vaduguru, Saujas and Rush, Alexander and Fried, Daniel

**Abstract**:

Large language models (LLMs) excel at processing and generating text and code. However, LLMs have had limited applicability in grounded task-oriented dialogue as they are difficult to steer toward task objectives and fail to handle novel grounding. We present a modular and interpretable grounded dialogue system that addresses these shortcomings by composing LLMs with a symbolic planner and grounded code execution. Our system, consists of a reader and planner: the reader leverages an LLM to convert partner utterances into executable code, calling functions that perform grounding. The translated code’s output is stored to track dialogue state, while a symbolic planner determines the next appropriate response. We evaluate our system’s performance on the demanding OneCommon dialogue task, involving collaborative reference resolution on abstract images of scattered dots. Our system substantially outperforms the previous state-of-the-art, including improving task success in human evaluations from 56% to 69% in the most challenging setting.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.460)

**Labels**: code generation, program synthesis, agent design, planning
