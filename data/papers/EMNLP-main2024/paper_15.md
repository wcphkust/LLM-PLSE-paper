# Re-Reading Improves Reasoning in Large Language Models

**Authors**: Xu, Xiaohan and Tao, Chongyang and Shen, Tao and Xu, Can and Xu, Hongbo and Long, Guodong and Lou, Jian-Guang and Ma, Shuai

**Abstract**:

To enhance the reasoning capabilities of off-the-shelf Large Language Models (LLMs), we introduce a simple, yet general and effective prompting method, RE2, i.e., Re-Reading the question as input. Unlike most thought-eliciting prompting methods, such as Chain-of-Thought (CoT), which aim to elicit the reasoning process in the output, RE2 shifts the focus to the input by processing questions twice, thereby enhancing the understanding process. Consequently, RE2 demonstrates strong generality and compatibility with most thought-eliciting prompting methods, including CoT. Crucially, RE2 facilitates a “bidirectional” encoding in unidirectional decoder-only LLMs because the first pass could provide global information for the second pass. We begin with a preliminary empirical study as the foundation of RE2, illustrating its potential to enable “bidirectional” attention mechanisms. We then evaluate RE2 on extensive reasoning benchmarks across 14 datasets, spanning 112 experiments, to validate its effectiveness and generality. Our findings indicate that, with the exception of a few scenarios on vanilla ChatGPT, RE2 consistently enhances the reasoning performance of LLMs through a simple re-reading strategy. Further analyses reveal RE2’s adaptability, showing how it can be effectively integrated with different LLMs, thought-eliciting prompting, and ensemble strategies.

**Link**: [Read Paper](https://aclanthology.org/2024.emnlp-main.871)

**Labels**: prompt strategy
