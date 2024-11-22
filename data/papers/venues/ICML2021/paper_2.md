# Programl: A graph-based program representation for data flow analysis and compiler optimizations

**Authors**: Cummins, Chris and Fisches, Zacharias V and Ben-Nun, Tal and Hoefler, Torsten and O’Boyle, Michael FP and Leather, Hugh

**Abstract**:

Machine learning (ML) is increasingly seen as a viable approach for building compiler optimization heuristics, but many ML methods cannot replicate even the simplest of the data flow analyses that are critical to making good optimization decisions. We posit that if ML cannot do that, then it is insufficiently able to reason about programs. We formulate data flow analyses as supervised learning tasks and introduce a large open dataset of programs and their corresponding labels from several analyses. We use this dataset to benchmark ML methods and show that they struggle on these fundamental program reasoning tasks. We propose ProGraML-Program Graphs for Machine Learning-a language-independent, portable representation of program semantics. ProGraML overcomes the limitations of prior works and yields improved performance on downstream optimization tasks.

**Link**: [Read Paper](https://arxiv.org/abs/2105.04297)

**Labels**: [static analysis](../../labels/static_analysis.md), [fundamental analysis](../../labels/fundamental_analysis.md), [compiler optimization](../../labels/compiler_optimization.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [IR code model](../../labels/IR_code_model.md)
