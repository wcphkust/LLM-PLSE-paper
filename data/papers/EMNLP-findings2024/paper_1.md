# TransLLaMa: LLM-based Simultaneous Translation System

**Authors**: Koshkin, Roman and Sudoh, Katsuhito and Nakamura, Satoshi

**Abstract**:

Decoder-only large language models (LLMs) have recently demonstrated impressive capabilities in text generation and reasoning. Nonetheless, they have limited applications in simultaneous machine translation (SiMT), currently dominated by encoder-decoder transformers. This study demonstrates that, after fine-tuning on a small dataset comprising causally aligned source and target sentence pairs, a pre-trained open-source LLM can control input segmentation directly by generating a special “wait” token. This obviates the need for a separate policy and enables the LLM to perform English-German and English-Russian SiMT tasks with BLEU scores that are comparable to those of specific state-of-the-art baselines. We also evaluated closed-source models such as GPT-4, which displayed encouraging results in performing the SiMT task without prior training (zero-shot), indicating a promising avenue for enhancing future SiMT systems.

**Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.27)

**Labels**: code generation, program transformation, empirical study
