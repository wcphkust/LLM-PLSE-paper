# Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning

**Authors**: Yadavally, Aashish and Li, Yi and Nguyen, Tien N

**Abstract**:

Program slicing, the process of extracting program statements that influence values at a designated location (known as the slicing criterion), is helpful in both manual and automated debugging. However, such slicing techniques prove ineffective in scenarios where executing specific inputs is prohibitively expensive, or even impossible, as with partial code. In this paper, we introduce ND-Slicer, a predictive slicing methodology that caters to specific executions based on a particular input, overcoming the need for actual execution. We enable such a process by leveraging execution-aware pre-training to learn the dynamic program dependencies, including both dynamic data and control dependencies between variables in the slicing criterion and the remaining program statements. Such knowledge forms the cornerstone for constructing a predictive backward slice. Our empirical evaluation revealed a high accuracy in predicting program slices, achieving an exact-match accuracy of 81.3% and a ROUGE-LCS F1-score of 95.4% on Python programs. As an extrinsic evaluation, we illustrate ND-Slicer’s usefulness in crash detection, with it locating faults with an accuracy of 63.9%. Furthermore, we include an in-depth qualitative evaluation, assessing ND-Slicer’s understanding of branched structures such as if-else blocks and loops, as well as the control flow in inter-procedural calls.

**Link**: [Read Paper](No Link Available)

**Labels**: program testing, debugging, code model, training, source code model
