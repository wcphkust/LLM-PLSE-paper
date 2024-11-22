# Neurosymbolic Repair of Test Flakiness

**Authors**: Chen, Yang and Jabbarvand, Reyhaneh

**Abstract**:

Test flakiness, a non-deterministic behavior of builds irrelevant to code changes, is a major and continuing impediment to deliver- ing reliable software. The very few techniques for the automated repair of test flakiness are specifically crafted to repair either Order- Dependent (OD) or Implementation-Dependent (ID) flakiness. They are also all symbolic approaches, i.e., they leverage program analy- sis to detect and repair known test flakiness patterns and root causes, failing to generalize. To bridge the gap, we propose FlakyDoctor, a neuro-symbolic technique that combines the power of LLMs— generalizability—and program analysis—soundness—to fix different types of test flakiness. Our extensive evaluation using 873 confirmed flaky tests (332 OD and 541 ID) from 243 real-world projects demonstrates the ability of FlakyDoctor in repairing flakiness, achieving 57\% (OD) and 59\% (ID) success rate. Comparing to three alternative flakiness repair approaches, FlakyDoctor can repair 8\% more ID tests than DexFix, 12\% more OD flaky tests than ODRepair, and 17\% more OD flaky tests than iFixFlakies. Regardless of underlying LLM, the non-LLM components of FlakyDoctor contribute to 12–31 \% of the overall performance, i.e., while part of the FlakyDoctor power is from using LLMs, they are not good enough to repair flaky tests in real-world projects alone. What makes the proposed technique superior to related research on test flakiness mitigation specifically and program repair, in general, is repairing 79 previously unfixed flaky tests in real-world projects. We opened pull requests for all cases with corresponding patches; 19 of them were accepted and merged at the time of submission.

**Link**: [Read Paper](https://doi.org/10.1145/3650212.3680369)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)
