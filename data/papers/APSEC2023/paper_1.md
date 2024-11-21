# Refactoring programs using large language models with few-shot examples

**Authors**: Shirafuji, Atsushi and Oda, Yusuke and Suzuki, Jun and Morishita, Makoto and Watanobe, Yutaka

**Abstract**:

A less complex and more straightforward program is a crucial factor that enhances its maintainability and makes writing secure and bug-free programs easier. However, due to its heavy workload and the risks of breaking the working programs, programmers are reluctant to do code refactoring, and thus, it also causes the loss of potential learning experiences. To mitigate this, we demonstrate the application of using a large language model (LLM), GPT-3.5, to suggest less complex versions of the user-written Python program, aiming to encourage users to learn how to write better programs. We propose a method to leverage the prompting with few-shot examples of the LLM by selecting the best-suited code refactoring examples for each target programming problem based on the prior evaluation of prompting with the one-shot example. The quantitative evaluation shows that 95.68% of programs can be refactored by generating 10 candidates each, resulting in a 17.35% reduction in the average cyclomatic complexity and a 25.84% decrease in the average number of lines after filtering only generated programs that are semantically correct. Further-more, the qualitative evaluation shows outstanding capability in code formatting, while unnecessary behaviors such as deleting or translating comments are also observed.

**Link**: [Read Paper](No Link Available)

**Labels**: code generation, program transformation
