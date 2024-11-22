# Where is it? Tracing the Vulnerability-relevant Files from Vulnerability Reports

**Authors**: Sun, Jiamou and Chen, Jieshan and Xing, Zhenchang and Lu, Qinghua and Xu, Xiwei and Zhu, Liming

**Abstract**:

With the widely usage of open-source software, supply-chain-based vulnerability attacks, including SolarWind and Log4Shell, have posed significant risks to software security. Currently, people rely on vulnerability advisory databases or commercial software bill of materials (SBOM) to defend against potential risks. Unfortunately, these datasets do not provide finer-grained file-level vulnerability information, compromising their effectiveness. Previous works have not adequately addressed this issue, and mainstream vulnerability detection methods have their drawbacks that hinder resolving this gap. Driven by the real needs, we propose a framework that can trace the vulnerability-relevant file for each disclosed vulnerability. Our approach uses NVD descriptions with metadata as the inputs, and employs a series of strategies with a LLM model, search engine, heuristic-based text matching method and a deep learning classifier to recommend the most likely vulnerability-relevant file, effectively enhancing the completeness of existing NVD data. Our experiments confirm that the efficiency of the proposed framework, with CodeBERT achieving 0.92 AUC and 0.85 MAP, and our user study proves our approach can help with vulnerability-relevant file detection effectively. To the best of our knowledge, our work is the first one focusing on tracing vulnerability-relevant files, laying the groundwork of building finer-grained vulnerability-aware software bill of materials.

**Link**: [Read Paper](https://doi.org/10.1145/3597503.3639202)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
