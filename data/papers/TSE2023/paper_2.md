# CombTransformers: Statement-Wise Transformers for Statement-Wise Representations

**Authors**: Bertolotti, Francesco and Cazzola, Walter

**Abstract**:

This study presents a novel category of Transformer architectures known as comb transformers, which effectively reduce the space complexity of the self-attention layer from a quadratic to a subquadratic level. This is achieved by processing sequence segments independently and incorporating &lt;inline-formula&gt;&lt;tex-math notation="LaTeX"&gt;$mathcal{X}$&lt;/tex-math&gt;&lt;alternatives&gt;&lt;mml:math&gt;&lt;mml:mrow&gt;&lt;mml:mi mathvariant="script"&gt;X&lt;/mml:mi&gt;&lt;/mml:mrow&gt;&lt;/mml:math&gt;&lt;inline-graphic xlink:href="cazzola-ieq1-3310793.gif"/&gt;&lt;/alternatives&gt;&lt;/inline-formula&gt;-word embeddings to merge cross-segment information. The reduction in attention memory requirements enables the deployment of deeper architectures, potentially leading to more competitive outcomes. Furthermore, we design an abstract syntax tree (AST)-based code representation to effectively exploit comb transformer properties. To explore the potential of our approach, we develop nine specific instances based on three popular architectural concepts: funnel, hourglass, and encoder-decoder. These architectures are subsequently trained on three code-related tasks: method name generation, code search, and code summarization. These tasks encompass a range of capabilities: short/long sequence generation and classification. In addition to the proposed comb transformers, we also evaluate several baseline architectures for comparative analysis. Our findings demonstrate that the comb transformers match the performance of the baselines and frequently perform better.

**Link**: [Read Paper](https://doi.org/10.1109/TSE.2023.3310793)

**Labels**: general coding task, code model, training, source code model
