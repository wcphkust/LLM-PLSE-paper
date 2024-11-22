# Generating API Parameter Security Rules with LLM for API Misuse Detection

**Authors**: Liu, Jinghua and Yang, Yi and Chen, Kai and Lin, Miaoqian

**Abstract**:

In this paper, we present a new framework, named GPTAid, for automatic APSRs generation by analyzing API source code with LLM and detecting API misuse caused by incorrect parameter use. To validate the correctness of the LLM-generated APSRs, we propose an execution feedback-checking approach based on the observation that security-critical API misuse is often caused by APSRs violations, and most of them result in runtime errors. Specifically, GPTAid first uses LLM to generate raw APSRs and the Right calling code, and then generates Violation code for each raw APSR by modifying the Right calling code using LLM. Subsequently, GPTAid performs dynamic execution on each piece of Violation code and further filters out the incorrect APSRs based on runtime errors. To further generate concrete APSRs, GPTAid employs a code differential analysis to refine the filtered ones. Particularly, as the programming language is more precise than natural language, GPTAid identifies the key operations within Violation code by differential analysis, and then generates the corresponding concrete APSR based on the aforementioned operations. These concrete APSRs could be precisely interpreted into applicable detection code, which proven to be effective in API misuse detection. Implementing on the dataset containing 200 randomly selected APIs from eight popular libraries, GPTAid achieves a precision of 92.3%. Moreover, it generates 6 times more APSRs than state-of-the-art detectors on a comparison dataset of previously reported bugs and APSRs. We further evaluated GPTAid on 47 applications, 210 unknown security bugs were found potentially resulting in severe security issues (e.g., system crashes), 150 of which have been confirmed by developers after our reports.

**Link**: [Read Paper](https://arxiv.org/abs/2409.09288)

**Labels**: [static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md)
