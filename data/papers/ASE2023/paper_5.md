# Better Patching Using LLM Prompting, via Self-Consistency

**Authors**: Ahmed, Toufique and Devanbu, Premkumar

**Abstract**:

Large Language models (LLMs) can be induced to solve non-trivial problems with “few-shot” prompts including illustrative problem-solution examples. Now if the few-shots also include “chain of thought” ($\mathcal{C}oT$) explanations, which are of the form problem-explanation-solution, LLMs will generate a “explained” solution, and perform even better. Recently an exciting, substantially better technique, self-consistency [1] ($\mathcal{S}-C$) has emerged, based on the intuition that there are many plausible explanations for the right solution; when the LLM is sampled repeatedly to generate a pool of explanation-solution pairs, for a given problem, the most frequently occurring solutions in the pool (ignoring the explanations) tend to be even more likely to be correct! Unfortunately, the use of this highly-performant $\mathcal{S}-C$ (or even $\mathcal{C}oT$) approach in software engineering settings is hampered by the lack of explanations; most software datasets lack explanations. In this paper, we describe an application of the $\mathcal{S}-C$ approach to program repair, using the commit log on the fix as the explanation, only in the illustrative few-shots. We achieve state-of-the art results, beating previous approaches to prompting-based program repair, on the MODIT dataset; we also find evidence suggesting that the correct commit messages are helping the LLM learn to produce better patches.

**Link**: [Read Paper](No Link Available)

**Labels**: code generation, program repair, prompt strategy
