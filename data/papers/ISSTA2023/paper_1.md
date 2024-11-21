# Who Judges the Judge: An Empirical Study on Online Judge Tests

**Authors**: Liu, Kaibo and Han, Yudong and Zhang, Jie M. and Chen, Zhenpeng and Sarro, Federica and Harman, Mark and Huang, Gang and Ma, Yun

**Abstract**:

Online Judge platforms play a pivotal role in education, competitive programming, recruitment, career training, and large language model training. They rely on predefined test suites to judge the correctness of submitted solutions. It is therefore important that the solution judgement is reliable and free from potentially misleading false positives (i.e., incorrect solutions that are judged as correct). In this paper, we conduct an empirical study of 939 coding problems with 541,552 solutions, all of which are judged to be correct according to the test suites used by the platform, finding that 43.4\% of the problems include false positive solutions (3,440 bugs are revealed in total). We also find that test suites are, nevertheless, of high quality according to widely-studied test effectiveness measurements: 88.2\% of false positives have perfect (100\%) line coverage, 78.9\% have perfect branch coverage, and 32.5\% have a perfect mutation score. Our findings indicate that more work is required to weed out false positive solutions and to further improve test suite effectiveness. We have released the detected false positive solutions and the generated test inputs to facilitate future research.

**Link**: [Read Paper](https://doi.org/10.1145/3597926.3598060)

**Labels**: static analysis, bug detection
