# LongCoder: {A} Long-Range Pre-trained Language Model for Code Completion

**Authors**: Daya Guo and Canwen Xu and Nan Duan and Jian Yin and Julian J. McAuley

**Abstract**:

In this paper, we introduce a new task for code completion that focuses on handling long code input and propose a sparse Transformer model, called LongCoder, to address this task. LongCoder employs a sliding window mechanism for self-attention and introduces two types of globally accessible tokens-bridge tokens and memory tokens-to improve performance and efficiency. Bridge tokens are inserted throughout the input sequence to aggregate local information and facilitate global interaction, while memory tokens are included to highlight important statements that may be invoked later and need to be memorized, such as package imports and definitions of classes, functions, or structures. We conduct experiments on a newly constructed dataset that contains longer code context and the publicly available CodeXGLUE benchmark. Experimental results demonstrate that LongCoder achieves superior performance on code completion tasks compared to previous models while maintaining comparable efficiency in terms of computational resources during inference.

**Link**: [Read Paper](https://proceedings.mlr.press/v202/guo23j.html)

**Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)
