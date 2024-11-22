# LLMIF: Augmented Large Language Model for Fuzzing IoT Devices

**Authors**: Wang, Jincheng and Yu, Le and Luo, Xiapu

**Abstract**:

Despite the efficacy of fuzzing in verifying the implementation correctness of network protocols, existing IoT protocol fuzzing approaches grapple with several limitations, including obfuscated message formats, unresolved message dependencies, and a lack of evaluations on the testing cases. These limitations significantly curtail the capabilities of IoT fuzzers in vulnerability identification. In this work, we show that the protocol specification contains fruitful descriptions of protocol messages, which can be used to overcome the above limitations and guide IoT protocol fuzzing. To automate the specification analysis, we augment the large language model with the specification contents, and drive it to perform two tasks (i.e., protocol information extraction, and device response reasoning). We further design and implement a fuzzing algorithm, LLMIF, which incorporates the LLM into IoT fuzzing. Finally, we select Zigbee as the target protocol and initiate comprehensive evaluations. The evaluation result shows that LLMIF successfully addressed the above limitations. Compared with the existing Zigbee fuzzers, it increases the protocol message coverage and code coverage by 55.2% and 53.9%, respectively. Besides the enhanced coverage, LLMIF unearthed 11 vulnerabilities on real-world Zigbee devices, which include eight previously unknown vulnerabilities. Seven of them are not covered by the existing Zigbee fuzzers.

**Link**: [Read Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10646659)

**Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)
