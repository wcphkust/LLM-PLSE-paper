# Don't Transform the Code, Code the Transforms: Towards Precise Code Rewriting using LLMs

**Authors**: Cummins, Chris and Seeker, Volker and Armengol-Estap{\'e}, Jordi and Markosyan, Aram H and Synnaeve, Gabriel and Leather, Hugh

**Abstract**:

Tools for rewriting, refactoring and optimizing code should be fast and correct. Large language models (LLMs), by their nature, possess neither of these qualities. Yet, there remains tremendous opportunity in using LLMs to improve code. We explore the use of LLMs not to transform code, but to code transforms. We propose a chain-of-thought approach to synthesizing code transformations from a small number of input/output code examples that incorporates execution and feedback. Unlike the direct rewrite approach, LLM-generated transformations are easy to inspect, debug, and validate. The logic of the rewrite is explicitly coded and easy to adapt. The compute required to run code transformations is minute compared to that of LLM rewriting. We test our approach on 16 Python code transformations and find that LLM- generated transforms are perfectly precise for 7 of them and less imprecise than direct LLM rewriting on the others. We hope to encourage further research to improving the precision of LLM code rewriting.

**Link**: [Read Paper](https://arxiv.org/pdf/2410.08806)

**Labels**: [prompt strategy](../../labels/prompt_strategy.md), [reason with code](../../labels/reason_with_code.md)
