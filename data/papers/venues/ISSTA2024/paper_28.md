# Domain Adaptation for Code Model-Based Unit Test Case Generation

**Authors**: Shin, Jiho and Hashtroudi, Sepehr and Hemmati, Hadi and Wang, Song

**Abstract**:

Recently, deep learning-based test case generation approaches have been proposed to automate the generation of unit test cases. In this study, we leverage Transformer-based code models to generate               unit tests with the help of Domain Adaptation (DA) at a project level. Specifically, we use CodeT5, a relatively small language model trained on source code data, and fine-tune it on the test generation               task. Then, we apply domain adaptation to each target project data to learn project-specific knowledge (project-level DA). We use the Methods2test dataset to fine-tune CodeT5 for the test generation               task and the Defects4j dataset for project-level domain adaptation and evaluation. We compare our approach with (a) CodeT5 fine-tuned on the test generation without DA, (b) the A3Test tool, and (c)               GPT-4 on five projects from the Defects4j dataset. The results show that tests generated using DA can increase the line coverage by 18.62\%, 19.88\%, and 18.02\% and mutation score by 16.45\%, 16.01\%

**Link**: [Read Paper](https://doi.org/10.1145/3650212.3680354)

**Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md)
