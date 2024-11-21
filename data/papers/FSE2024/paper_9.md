# Can Large Language Models Transform Natural Language Intent into Formal Method Postconditions?

**Authors**: Endres, Madeline and Fakhoury, Sarah and Chakraborty, Saikat and Lahiri, Shuvendu K.

**Abstract**:

Informal natural language that describes code functionality, such as code comments or function documentation, may contain substantial information about a program’s intent. However, there is typically no guarantee that a program’s implementation and natural language documentation are aligned. In the case of a conflict, leveraging information in code-adjacent natural language has the potential to enhance fault localization, debugging, and code trustworthiness. In practice, however, this information is often underutilized due to the inherent ambiguity of natural language, which makes natural language intent challenging to check programmatically. The “emergent abilities” of Large Language Models (LLMs) have the potential to facilitate the translation of natural language intent to programmatically checkable assertions. However, it is unclear if LLMs can correctly translate informal natural language specifications into formal specifications that match programmer intent. Additionally, it is unclear if such translation could be useful in practice.     In this paper, we describe nl2postcondition, the problem of leveraging LLMs for transforming informal natural language to formal method postconditions, expressed as program assertions.   We introduce and validate metrics to measure and compare different nl2postcondition approaches, using the correctness and discriminative power of generated postconditions.   We then use qualitative and quantitative methods to assess the quality of nl2postcondition postconditions, finding that they are generally correct and able to discriminate incorrect code. Finally, we find that  via LLMs has the potential to be helpful in practice;  generated postconditions were able to catch 64 real-world historical bugs from Defects4J.

**Link**: [Read Paper](https://doi.org/10.1145/3660791)

**Labels**: static analysis, specification inference, empirical study
