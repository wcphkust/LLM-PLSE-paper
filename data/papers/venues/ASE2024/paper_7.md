# LLM Meets Bounded Model Checking: Neuro-symbolic Loop Invariant Inference

**Authors**: Wu, Guangyuan and Cao, Weining and Yao, Yuan and Wei, Hengfeng and Chen, Taolue and Ma, Xiaoxing

**Abstract**:

Loop invariant inference, a key component in program verification, is a challenging task due to the inherent undecidability and complex loop behaviors in practice. Recently, machine learning based techniques have demonstrated impressive performance in generating loop invariants automatically. However, these methods highly rely on the labeled training data, and are intrinsically random and uncertain, leading to unstable performance. In this paper, we investigate a synergy of large language models (LLMs) and bounded model checking (BMC) to address these issues. The key observation is that, although LLMs may not be able to return the correct loop invariant in one response, they usually can provide all individual predicates of the correct loop invariant in multiple responses. To this end, we propose a "query-filter-reassemble" strategy, namely, we first leverage the language generation power of LLMs to produce a set of candidate invariants, where training data is not needed. Then, we employ BMC to identify valid predicates from these candidate invariants, which are assembled to produce new candidate invariants and checked by off-the-shelf SMT solvers. The feedback is incorporated into the prompt for the next round of LLM querying. We expand the existing benchmark of 133 programs to 316 programs, providing a more comprehensive testing ground. Experimental results demonstrate that our approach significantly outperforms the state-of-the-art techniques, successfully generating 309 loop invariants out of 316 cases, whereas the existing baseline methods are only able to tackle 219 programs at best. The code is publicly available at https://github.com/SoftWiser-group/LaM4Inv.git.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695014)

**Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)
