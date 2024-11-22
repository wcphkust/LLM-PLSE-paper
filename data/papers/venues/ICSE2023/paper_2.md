# CCTest: Testing and Repairing Code Completion Systems

**Authors**: Li, Zongjie and Wang, Chaozheng and Liu, Zhibo and Wang, Haoxuan and Chen, Dong and Wang, Shuai and Gao, Cuiyun

**Abstract**:

Code completion, a highly valuable topic in the software development domain, has been increasingly promoted for use by recent advances in large language models (LLMs). To date, visible LLM-based code completion frameworks such as GitHub Copilot and GPT are trained using deep learning over vast quantities of unstructured text and open source code. As the paramount component and the cornerstone in daily programming tasks, code completion has largely boosted professionals' efficiency in building real-world software systems.In contrast to this flourishing market, we find that code completion systems often output suspicious results, and to date, an automated testing and enhancement framework for code completion systems is not available. This research proposes CCTEST, a framework to test and repair code completion systems in black-box settings. CCTest features a set of novel mutation strategies, namely program structure-consistent (PSC) mutations, to generate mutated code completion inputs. Then, it detects inconsistent outputs, representing possibly erroneous cases, from all the completed code cases. Moreover, CCTest repairs the code completion outputs by selecting the output that mostly reflects the "average" appearance of all output cases, as the final output of the code completion systems. With around 18K test inputs, we detected 33,540 inputs that can trigger erroneous cases (with a true positive rate of 86\%) from eight popular LLM-based code completion systems. With repairing, we show that the accuracy of code completion systems is notably increased by 40\% and 67\% with respect to BLEU score and Levenshtein edit similarity.

**Link**: [Read Paper](https://doi.org/10.1109/ICSE48619.2023.00110)

**Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md)
