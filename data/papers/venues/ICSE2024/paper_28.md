# Out of Sight, Out of Mind: Better Automatic Vulnerability Repair by Broadening Input Ranges and Sources

**Authors**: Zhou, Xin and Kim, Kisub and Xu, Bowen and Han, Donggyun and Lo, David

**Abstract**:

The advances of deep learning (DL) have paved the way for automatic software vulnerability repair approaches, which effectively learn the mapping from the vulnerable code to the fixed code. Nevertheless, existing DL-based vulnerability repair methods face notable limitations: 1) they struggle to handle lengthy vulnerable code, 2) they treat code as natural language texts, neglecting its inherent structure, and 3) they do not tap into the valuable expert knowledge present in the expert system. To address this, we propose VulMaster, a Transformer-based neural network model that excels at generating vulnerability repairs by comprehensively understanding the entire vulnerable code, irrespective of its length. This model also integrates diverse information, encompassing vulnerable code structures and expert knowledge from the CWE system. We evaluated VulMaster on a real-world C/C++ vulnerability repair dataset comprising 1,754 projects with 5,800 vulnerable functions. The experimental results demonstrated that VulMaster exhibits substantial improvements compared to the learning-based state-of-the-art vulnerability repair approach. Specifically, VulMaster improves the EM, BLEU, and CodeBLEU scores from 10.2\% to 20.0\%, 21.3\% to 29.3\%, and 32.5\% to 40.9\%, respectively.

**Link**: [Read Paper](https://doi.org/10.1145/3597503.3639222)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)
