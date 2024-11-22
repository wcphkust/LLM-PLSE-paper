# AI-Assisted Code Authoring at Scale: Fine-Tuning, Deploying, and Mixed Methods Evaluation

**Authors**: Murali, Vijayaraghavan and Maddila, Chandra and Ahmad, Imad and Bolin, Michael and Cheng, Daniel and Ghorbani, Negar and Fernandez, Renuka and Nagappan, Nachiappan and Rigby, Peter C.

**Abstract**:

Generative LLMs have been shown to effectively power AI-based code authoring tools that can suggest entire statements or blocks of code during code authoring. In this paper we present CodeCompose, an AI-assisted code authoring tool developed and deployed at Meta internally. CodeCompose is based on the InCoder LLM that merges generative capabilities with bi-directionality. We have scaled up CodeCompose to serve tens of thousands of developers at Meta, across 9 programming languages and several coding surfaces. We present our experience in making design decisions about the model and system architecture for CodeCompose that addresses these challenges.        To release a LLM model at this scale, we needed to first ensure that it is sufficiently accurate. In a random sample of 20K source code files, depending on the language, we are able to reproduce hidden lines between 40\% and 58\% of the time, an improvement of 1.4\texttimes{} and 4.1\texttimes{} over a model trained only on public data.        We gradually rolled CodeCompose out to developers. At the time of this writing, 16K developers have used it with 8\% of their code coming directly from CodeCompose.        To triangulate our numerical findings, we conduct a thematic analysis on the feedback from 70 developers. We find that 91.5\% of the feedback is positive, with the most common themes being discovering APIs, dealing with boilerplate code, and accelerating coding. Meta continues to integrate this feedback into CodeCompose.

**Link**: [Read Paper](https://doi.org/10.1145/3643774)

**Labels**: [code generation](../../labels/code_generation.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)
