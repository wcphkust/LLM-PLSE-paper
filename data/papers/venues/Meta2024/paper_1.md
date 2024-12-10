# Meta large language model compiler: Foundation models of compiler optimization

**Authors**: Cummins, Chris and Seeker, Volker and Grubisic, Dejan and Roziere, Baptiste and Gehring, Jonas and Synnaeve, Gabriel and Leather, Hugh

**Abstract**:

Large Language Models (LLMs) have demonstrated remarkable capabilities across a variety of software engineering and coding tasks. However, their application in the domain of code and compiler optimization remains underexplored. Training LLMs is resource-intensive, requiring substantial GPU hours and extensive data collection, which can be prohibitive. To address this gap, we introduce Meta Large Language Model Compiler (LLM Compiler), a suite of robust, openly available, pre-trained models specifically designed for code optimization tasks. Built on the foundation of Code Llama, LLM Compiler enhances the understanding of compiler intermediate representations (IRs), assembly language, and optimization techniques. The model has been trained on a vast corpus of 546 billion tokens of LLVM-IR and assembly code and has undergone instruction fine-tuning to interpret compiler behavior. LLM Compiler is released under a bespoke commercial license to allow wide reuse and is available in two sizes: 7 billion and 13 billion parameters. We also present fine-tuned versions of the model, demonstrating its enhanced capabilities in optimizing code size and disassembling from x86_64 and ARM assembly back into LLVM-IR. These achieve 77% of the optimising potential of an autotuning search, and 45% disassembly round trip (14% exact match). This release aims to provide a scalable, cost-effective foundation for further research and development in compiler optimization by both academic researchers and industry practitioners.

**Link**: [Read Paper](https://arxiv.org/pdf/2302.05319)

**Labels**: [static analysis](../../labels/static_analysis.md), [program optimization](../../labels/program_optimization.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [IR code model](../../labels/IR_code_model.md)
