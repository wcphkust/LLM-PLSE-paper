# Ranking llm-generated loop invariants for program verification

**Authors**: Chakraborty, Saikat and Lahiri, Shuvendu K and Fakhoury, Sarah and Musuvathi, Madanlal and Lal, Akash and Rastogi, Aseem and Senthilnathan, Aditya and Sharma, Rahul and Swamy, Nikhil

**Abstract**:

Synthesizing inductive loop invariants is fundamental to automating program verification. In this work, we observe that Large Language Models (such as gpt-3.5 or gpt-4) are capable of synthesizing loop invariants for a class of programs in a 0-shot setting, yet require several samples to generate the correct invariants. This can lead to a large number of calls to a program verifier to establish an invariant. To address this issue, we propose a {\it re-ranking} approach for the generated results of LLMs. We have designed a ranker that can distinguish between correct inductive invariants and incorrect attempts based on the problem definition. The ranker is optimized as a contrastive ranker. Experimental results demonstrate that this re-ranking mechanism significantly improves the ranking of correct invariants among the generated candidates, leading to a notable reduction in the number of calls to a verifier.

**Link**: [Read Paper](No Link Available)

**Labels**: static analysis, program verification, invariant generation, prompt strategy, sampling and ranking
