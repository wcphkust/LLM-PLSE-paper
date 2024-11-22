# VALAR: Streamlining Alarm Ranking in Static Analysis with Value-Flow Assisted Active Learning

**Authors**: Liu, Pengcheng and Lu, Yifei and Yang, Wenhua and Pan, Minxue

**Abstract**:

Static analyzers play a critical role in program defects and security vulnerabilities detection. Despite their importance, the widespread adoption of static analysis techniques in industrial development faces numerous obstacles, among which the high rate of false alarms constitutes a significant one. To address this issue, we propose a novel approach called Valar, which performs alarm ranking for advanced value-flow analysis using the active learning technique. Active learning algorithms minimize the manual effort for alarm inspection by maximizing the effect of each user labeling in recognizing true/false alarms. Meanwhile, the value-flows provide Valar with a concise and comprehensive summary of the operational semantics about programs. Based on this, Valar is able to reason about the potential correlations between alarms and prioritize the most profitable unlabeled alarm. Additionally, the accuracy of Valar increases as more user labels are given and Valar's active learning model is further refined. We evaluate Valar on 20 real-world C/C++ programs using three value-flow based checkers. Our experimental results demonstrated that Valar significantly lowers the priorities of false alarms with most true alarms ranked high. Notably, Valar ranked all true alarms in the top 47% in 90% projects and ranked 90% true alarms in the top 22% in 75% projects. Furthermore, Valar has no requirement for pretraining and has a negligible computation time of less than 0.1s for each alarm prioritization.

**Link**: [Read Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10298558)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
