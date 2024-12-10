# Semantic-Enhanced Indirect Call Analysis with Large Language Models

**Authors**: Cheng, Baijun and Zhang, Cen and Wang, Kailong and Shi, Ling and Liu, Yang and Wang, Haoyu and Guo, Yao and Li, Ding and Chen, Xiangqun

**Abstract**:

In contemporary software development, the widespread use of indirect calls to achieve dynamic features poses challenges in constructing precise control flow graphs (CFGs), which further impacts the performance of downstream static analysis tasks. To tackle this issue, various types of indirect call analyzers have been proposed. However, they do not fully leverage the semantic information of the program, limiting their effectiveness in real-world scenarios.To address these issues, this paper proposes Semantic-Enhanced Analysis (SEA), a new approach to enhance the effectiveness of indirect call analysis. Our fundamental insight is that for common programming practices, indirect calls often exhibit semantic similarity with their invoked targets. This semantic alignment serves as a supportive mechanism for static analysis techniques in filtering out false targets. Notably, contemporary large language models (LLMs) are trained on extensive code corpora, encompassing tasks such as code summarization, making them well-suited for semantic analysis. Specifically, SEA leverages LLMs to generate natural language summaries of both indirect calls and target functions from multiple perspectives. Through further analysis of these summaries, SEA can determine their suitability as caller-callee pairs. Experimental results demonstrate that SEA can significantly enhance existing static analysis methods by producing more precise target sets for indirect calls.

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695016)

**Labels**: [static analysis](../../labels/static_analysis.md), [call graph analysis](../../labels/call_graph_analysis.md)
