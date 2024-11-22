# LLM-Based Java Concurrent Program to ArkTS Converter

**Authors**: Liu, Runlin and Lin, Yuhang and Hu, Yunge and Zhang, Zhe and Gao, Xiang

**Abstract**:

HarmonyOS NEXT is a distributed operating system developed to support HarmonyOS native apps. To support the new and independent Harmony ecosystem, developers are required to migrate their applications from Android to HarmonyOS. However, HarmonyOS utilizes ArkTS, a superset of TypeScript, as the programming language for application development. Hence, migrating applications to HarmonyOS requires translating programs across different program languages, e.g., Java, which is known to be very challenging, especially for concurrency programs. Java utilizes shared memory to implement concurrency programs, while ArkTS relies on message passing (i.e., Actor model). This paper presents an LLM-based concurrent Java program to ArkTS converter.Our converter utilizes large language models (LLMs) for efficient code translation, integrating ArkTS's SharedArrayBuffer API to create ThreadBridge, a library that replicates Java's shared memory model. Using LLM's Chain-of-Thought mechanism, the translation process is divided into specialized chains: the TS chain, concurrency chain, and synchronization chain, each handling TypeScript syntax, concurrency patterns, and synchronization logic with precision.This study offers solutions to bridge concurrency model differences between Java and ArkTS, reducing manual code rewriting and speeding up adaptation for HarmonyOS NEXT. Experiments show the converter successfully compiles 66\% of 53 test samples, with 69\% accuracy for compiled results. Overall, the approach shows promise in converting concurrent Java programs to ArkTS, laying the foundation for future improvements.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695362)

**Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)
