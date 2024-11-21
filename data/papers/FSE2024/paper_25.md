# Code-Aware Prompting: A Study of Coverage-Guided Test Generation in Regression Setting using LLM

**Authors**: Ryan, Gabriel and Jain, Siddhartha and Shang, Mingyue and Wang, Shiqi and Ma, Xiaofei and Ramanathan, Murali Krishna and Ray, Baishakhi

**Abstract**:

Testing plays a pivotal role in ensuring software quality, yet conventional Search Based Software Testing (SBST) methods often struggle with complex software units, achieving suboptimal test coverage. Recent work using large language models (LLMs) for test generation have focused on improving generation quality through optimizing the test generation context and correcting errors in model outputs, but use fixed prompting strategies that prompt the model to generate tests without additional guidance. As a result LLM-generated testsuites still suffer from low coverage. In this paper, we present SymPrompt, a code-aware prompting strategy for LLMs in test generation. SymPrompt’s approach is based on recent work that demonstrates LLMs can solve more complex logical problems when prompted to reason about the problem in a multi-step fashion. We apply this methodology to test generation by deconstructing the testsuite generation process into a multi-stage sequence, each of which is driven by a specific prompt aligned with the execution paths of the method under test, and exposing relevant type and dependency focal context to the model. Our approach enables pretrained LLMs to generate more complete test cases without any additional training. We implement SymPrompt using the TreeSitter parsing framework and evaluate on a benchmark challenging methods from open source Python projects. SymPrompt enhances correct test generations by a factor of 5 and bolsters relative coverage by 26\% for CodeGen2. Notably, when applied to GPT-4, SymPrompt improves coverage by over 2x compared to baseline prompting strategies.

**Link**: [Read Paper](https://doi.org/10.1145/3643769)

**Labels**: program testing, fuzzing
