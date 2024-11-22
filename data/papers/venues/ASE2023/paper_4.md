# Improving Code Extraction from Coding Screencasts Using a Code-Aware Encoder-Decoder Model

**Authors**: Malkadi, Abdulkarim and Tayeb, Ahmad and Haiduc, Sonia

**Abstract**:

Accurate automatic code extraction from tutorial videos is crucial for software developers seeking to reuse the code contained in these videos. Current methods using optical character recognition (OCR) often yield inaccurate results due to code complexity and variations in screencast formats. To address this issue, we introduce CodeT5-OCRfix, an approach that leverages the pre-trained code-aware large language model CodeT5 to enhance code extraction accuracy by post-processing OCRed code. We first collect a large and diverse dataset of source code screenshots captured from more than 10K Java projects from GitHub. We then apply the most widely used OCR engine for the task of code extraction from videos, Tesseract, on these screenshots and collect the OCRed code along with the ground truth code extracted from the Java files. We built a training dataset of more than 585K pairs of OCRed and ground truth code pairs, which we then used to fine-tune CodeT5, obtaining our model CodeT5-OCRfix. An empirical evaluation on both screenshots and screencast frames shows that CodeT5-OCRfix outperforms baseline code extraction models and is also more time-efficient. Our approach therefore improves the state-of-the-art in code extraction techniques from screencasts and images.

**Link**: [Read Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10298433)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)
