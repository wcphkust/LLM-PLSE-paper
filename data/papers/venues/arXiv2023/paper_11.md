# Impact of large language models on generating software specifications

**Authors**: Xie, Danning and Yoo, Byungwoo and Jiang, Nan and Kim, Mijung and Tan, Lin and Zhang, Xiangyu and Lee, Judy S

**Abstract**:

Software specifications are essential for ensuring the reliability of software systems. Existing specification extraction approaches, however, suffer from limited generalizability and require manual efforts. The recent emergence of Large Language Models (LLMs), which have been successfully applied to numerous software engineering tasks, offers a promising avenue for automating this process. In this paper, we conduct the first empirical study to evaluate the capabilities of LLMs for generating software specifications from software comments or documentation. We evaluate LLMs' performance with Few Shot Learning (FSL), enabling LLMs to generalize from a small number of examples, as well as different prompt construction strategies, and compare the performance of LLMs with traditional approaches. Additionally, we conduct a comparative diagnosis of the failure cases from both LLMs and traditional methods, identifying their unique strengths and weaknesses. Lastly, we conduct extensive experiments on 15 state of the art LLMs, evaluating their performance and cost effectiveness for generating software specifications. Our results show that with FSL, LLMs outperform traditional methods (by 5.6%), and more sophisticated prompt construction strategies can further enlarge this performance gap (up to 5.1 to 10.0%). Yet, LLMs suffer from their unique challenges, such as ineffective prompts and the lack of domain knowledge, which together account for 53 to 60% of LLM unique failures. The strong performance of open source models (e.g., StarCoder) makes closed source models (e.g., GPT 3 Davinci) less desirable due to size and cost. Our study offers valuable insights for future research to improve specification generation.

**Link**: [Read Paper](https://arxiv.org/pdf/2306.03324.pdf)

**Labels**: [static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md)
