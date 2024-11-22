# Evaluating Diverse Large Language Models for Automatic and General Bug Reproduction

**Authors**: Kang, Sungmin and Yoon, Juyeon and Askarbekkyzy, Nargiz and Yoo, Shin

**Abstract**:

Bug reproduction is a critical developer activity that is also challenging to automate, as bug reports are often in natural language and thus can be difficult to transform to test cases consistently. As a result, existing techniques mostly focused on crash bugs, which are easier to automatically detect and verify. In this work, we overcome this limitation by using large language models (LLMs), which have been demonstrated to be adept at natural language processing and code generation. By prompting LLMs to generate bug-reproducing tests, and via a post-processing pipeline to automatically identify promising generated tests, our proposed technique &lt;sc&gt;Libro&lt;/sc&gt; could successfully reproduce about one-third of all bugs in the widely used Defects4J benchmark. Furthermore, our extensive evaluation on 15 LLMs, including 11 open-source LLMs, suggests that open-source LLMs also demonstrate substantial potential, with the StarCoder LLM achieving 70\% of the reproduction performance of the closed-source OpenAI LLM code-davinci-002 on the large Defects4J benchmark, and 90\% of performance on a held-out bug dataset likely not part of any LLM's training data. In addition, our experiments on LLMs of different sizes show that bug reproduction using &lt;sc&gt;Libro&lt;/sc&gt; improves as LLM size increases, providing information as to which LLMs can be used with the &lt;sc&gt;Libro&lt;/sc&gt; pipeline.

**Link**: [Read Paper](https://doi.org/10.1109/TSE.2024.3450837)

**Labels**: [program testing](../../labels/program_testing.md), [bug reproduction](../../labels/bug_reproduction.md), [empirical study](../../labels/empirical_study.md)
