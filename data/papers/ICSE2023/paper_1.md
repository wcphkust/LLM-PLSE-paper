# CodaMosa: Escaping Coverage Plateaus in Test Generation with Pre-Trained Large Language Models

**Authors**: Lemieux, Caroline and Inala, Jeevana Priya and Lahiri, Shuvendu K. and Sen, Siddhartha

**Abstract**:

Search-based software testing (SBST) generates high-coverage test cases for programs under test with a combination of test case generation and mutation. SBST's performance relies on there being a reasonable probability of generating test cases that exercise the core logic of the program under test. Given such test cases, SBST can then explore the space around them to exercise various parts of the program. This paper explores whether Large Language Models (LLMs) of code, such as OpenAI's Codex, can be used to help SBST's exploration. Our proposed algorithm, CodaMosa, conducts SBST until its coverage improvements stall, then asks Codex to provide example test cases for under-covered functions. These examples help SBST redirect its search to more useful areas of the search space. On an evaluation over 486 benchmarks, CodaMosa achieves statistically significantly higher coverage on many more benchmarks (173 and 279) than it reduces coverage on (10 and 4), compared to SBST and LLM-only baselines.

**Link**: [Read Paper](https://doi.org/10.1109/ICSE48619.2023.00085)

**Labels**: program testing, fuzzing
