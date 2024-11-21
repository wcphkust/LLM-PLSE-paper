# MapCoder: Multi-Agent Code Generation for Competitive Problem Solving

**Authors**: Islam, Md. Ashraful and Ali, Mohammed Eunus and Parvez, Md Rizwan

**Abstract**:

Code synthesis, which requires a deep understanding of complex natural language (NL) problem descriptions, generation of code instructions for complex algorithms and data structures, and the successful execution of comprehensive unit tests, presents a significant challenge. Thus, while large language models (LLMs) demonstrate impressive proficiency in natural language processing (NLP), their performance in code generation tasks remains limited. In this paper, we introduce a new approach to code generation tasks leveraging the multi-agent prompting that uniquely replicates the full cycle of program synthesis as observed in human developers. Our framework, MapCoder, consists of four LLM agents specifically designed to emulate the stages of this cycle: recalling relevant examples, planning, code generation, and debugging. After conducting thorough experiments, with multiple LLMs ablations and analyses across eight challenging competitive problem-solving and program synthesis benchmarks—MapCoder showcases remarkable code generation capabilities, achieving their new state-of-the-art (pass@1) results—(HumanEval 93.9%, MBPP 83.1%, APPS 22.0%, CodeContests 28.5%, and xCodeEval 45.3%). Moreover, our method consistently delivers superior performance across various programming languages and varying problem difficulties. We open-source our framework at https://github.com/Md-Ashraful-Pramanik/MapCoder.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.269)

**Labels**: code generation, program synthesis, agent design
