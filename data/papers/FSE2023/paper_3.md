# Baldur: Whole-Proof Generation and Repair with Large Language Models

**Authors**: First, Emily and Rabe, Markus N. and Ringer, Talia and Brun, Yuriy

**Abstract**:

Formally verifying software is a highly desirable but labor-intensive task.  Recent work has developed methods to automate formal verification using proof assistants, such as Coq and Isabelle/HOL, e.g., by training a model to predict one proof step at a time and using that model to search through the space of possible proofs.  This paper introduces a new method to automate formal verification: We use large language models, trained on natural language and code and fine-tuned on proofs, to generate whole proofs at once.  We then demonstrate that a model fine-tuned to repair generated proofs further increasing proving power.  This paper:  (1) Demonstrates that whole-proof generation using transformers is possible and is as effective but more efficient than search-based techniques.  (2) Demonstrates that giving the learned model additional context, such as a prior failed proof attempt and the ensuing error message, results in proof repair that further improves automated proof generation.  (3) Establishes, together with prior work, a new state of the art for fully automated proof synthesis.  We reify our method in a prototype, Baldur, and evaluate it on a benchmark of 6,336 Isabelle/HOL theorems and their proofs,  empirically showing the effectiveness of whole-proof generation, repair, and added context. We also show that Baldur complements the state-of-the-art tool, Thor, by automatically generating proofs for an additional 8.7\% of the theorems. Together, Baldur and Thor can prove 65.7\% of the theorems fully automatically. This paper paves the way for new research into using large language models for automating formal verification.

**Link**: [Read Paper](https://doi.org/10.1145/3611643.3616243)

**Labels**: static analysis, program verification
