# QEDCartographer: Automating Formal Verification Using Reward-Free Reinforcement Learning

**Authors**: Alex Sanchez-Stern, Abhishek Varghese, Zhanna Kaufman, Dylan Zhang, Talia Ringer, Yuriy Brun

**Abstract**:

Formal verification is a promising method for producing reliable software, but the difficulty of manually writing verification proofs severely limits its utility in practice. Recent methods have automated some proof synthesis by guiding a search through the proof space using a theorem prover. Unfortunately, the theorem prover provides only the crudest estimate of progress, resulting in effectively undirected search. To address this problem, we create QEDCartographer, an automated proof-synthesis tool that combines supervised and reinforcement learning to more effectively explore the proof space. QEDCartographer incorporates the proofs' branching structure, enabling reward-free search and overcoming the sparse reward problem inherent to formal verification. We evaluate QEDCartographer using the CoqGym benchmark of 68.5K theorems from 124 open-source Coq projects. QEDCartographer fully automatically proves 21.4% of the test-set theorems. Previous search-based proof-synthesis tools Tok, Tac, ASTactic, Passport, and Proverbot9001, which rely only on supervised learning, prove 9.6%, 9.8%, 10.9%, 12.5%, and 19.8%, respectively. Diva, which combines 62 tools, proves 19.2%. Comparing to the most effective prior tool, Proverbot9001, QEDCartographer produces 34% shorter proofs 29% faster, on average over the theorems both tools prove. Together, QEDCartographer and non-learning-based CoqHammer prove 30.3% of the theorems, while CoqHammer alone proves 26.6%. Our work demonstrates that reinforcement learning is a fruitful research direction for improving proof-synthesis tools' search mechanisms.

**Link**: [Read Paper](https://arxiv.org/abs/2408.09237)

**Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)
