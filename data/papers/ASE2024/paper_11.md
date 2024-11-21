# Semantic Sleuth: Identifying Ponzi Contracts via Large Language Models

**Authors**: Wu, Cong and Chen, Jing and Wang, Ziwei and Liang, Ruichao and Du, Ruiying

**Abstract**:

Smart contracts, self-executing agreements directly encoded in code, are fundamental to blockchain technology, especially in decentralized finance (DeFi) and Web3. However, the rise of Ponzi schemes in smart contracts poses significant risks, leading to substantial financial losses and eroding trust in blockchain systems. Existing detection methods, such as PonziGuard, depend on large amounts of labeled data and struggle to identify unseen Ponzi schemes, limiting their reliability and generalizability. In contrast, we introduce PonziSleuth, the first LLM-driven approach for detecting Ponzi smart contracts, which requires no labeled training data. PonziSleuth utilizes advanced language understanding capabilities of LLMs to analyze smart contract source code through a novel two-step zero-shot chain-of-thought prompting technique. Our extensive evaluation on benchmark datasets and real-world contracts demonstrates that PonziSleuth delivers comparable, and often superior, performance without the extensive data requirements, achieving a balanced detection accuracy of 96.06\% with GPT-3.5-turbo, 93.91\% with LLAMA3, and 94.27\% with Mistral. In real-world detection, PonziSleuth successfully identified 15 new Ponzi schemes from 4,597 contracts verified by Etherscan in March 2024, with a false negative rate of 0\% and a false positive rate of 0.29\%. These results highlight PonziSleuth's capability to detect diverse and novel Ponzi schemes, marking a significant advancement in leveraging LLMs for enhancing blockchain security and mitigating financial scams.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695055)

**Labels**: static analysis, bug detection
