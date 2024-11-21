# Semi-Supervised Code Translation Overcoming the Scarcity of Parallel Code Data

**Authors**: Zhu, Ming and Karim, Mohimenul and Lourentzou, Ismini and Yao, Daphne

**Abstract**:

Neural code translation is the task of converting source code from one programming language to another. One of the main challenges is the scarcity of parallel code data, which hinders the ability of translation models to learn accurate cross-language alignments. In this paper, we introduce MIRACLE, a semi-supervised approach that improves code translation through synthesizing high-quality parallel code data and curriculum learning on code data with ascending alignment levels. MIRACLE leverages static analysis and compilation to generate synthetic parallel code datasets with enhanced quality and alignment to address the challenge of data scarcity. We evaluate the proposed method along with strong baselines including instruction-tuned Large Language Models (LLMs) for code. Our analysis reveals that LLMs pre-trained on open-source code data, regardless of their size, suffer from the "shallow translation" problem. This issue arises when translated code copies labels, statements, and even code blocks from the source language, leading to compilation and runtime errors. Extensive experiments demonstrate that our method significantly mitigates this issue, enhancing code translation performance across multiple models in C++, Java, Python, and C. Remarkably, MIRACLE outperforms code LLMs that are ten times larger in size. MIRACLE also achieves up to a 43\% improvement in C code translation with fewer than 150 annotated examples.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695524)

**Labels**: code generation, program transformation
