# Chain of code: Reasoning with a language model-augmented code emulator

**Authors**: Li, Chengshu and Liang, Jacky and Zeng, Andy and Chen, Xinyun and Hausman, Karol and Sadigh, Dorsa and Levine, Sergey and Fei-Fei, Li and Xia, Fei and Ichter, Brian

**Abstract**:

Code provides a general syntactic structure to build complex programs and perform precise computations when paired with a code interpreter -- we hypothesize that language models (LMs) can leverage code-writing to improve Chain of Thought reasoning not only for logic and arithmetic tasks, but also for linguistic ones (and in particular, those that are a mix of both). For example, consider prompting an LM to write code that counts the number of times it detects sarcasm in an essay: the LM may struggle to write an implementation for "detect_sarcasm(string)" that can be executed by the interpreter (handling the edge cases would be insurmountable). However, LMs may still produce a valid solution if they are used not only to write the code, but also to selectively "emulate" the interpreter by generating the expected output of "detect_sarcasm(string)" and other lines of code (e.g., that the interpreter could not compile). In this work, we propose Chain of Code (CoT), a simple yet surprisingly effective extension that improves LM code-driven reasoning. The key idea is to encourage LMs to format linguistic sub-tasks in a program as flexible pseudocode that the compiler can explicitly catch undefined behaviors and hand off to simulate with an LM (as an "LMulator"). Experiments demonstrate that Chain of Code outperforms Chain of Thought and other baselines across a variety of benchmarks; on BIG-Bench Hard, Chain of Code achieves 84%, a gain of 12% over Chain of Thought. CoT scales well with large and small models alike, and broadens the scope of reasoning questions that LMs can correctly answer by "thinking in code". Project webpage: https://chain-of-code.github.io/.

**Link**: [Read Paper](https://arxiv.org/pdf/2312.04474.pdf)

**Labels**: [prompt strategy](../../labels/prompt_strategy.md), [reason with code](../../labels/reason_with_code.md)
