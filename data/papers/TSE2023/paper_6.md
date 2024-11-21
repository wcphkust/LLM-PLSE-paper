# On the Effectiveness of Transfer Learning for Code Search

**Authors**: Salza, Pasquale and Schwizer, Christoph and Gu, Jian and Gall, Harald C.

**Abstract**:

The Transformer architecture and transfer learning have marked a quantum leap in natural language processing, improving the state of the art across a range of text-based tasks. This paper examines how these advancements can be applied to and improve code search. To this end, we pre-train a BERT-based model on combinations of natural language and source code data and fine-tune it on pairs of StackOverflow question titles and code answers. Our results show that the pre-trained models consistently outperform the models that were not pre-trained. In cases where the model was pre-trained on natural language “and” source code data, it also outperforms an information retrieval baseline based on Lucene. Also, we demonstrated that the combined use of an information retrieval-based approach followed by a Transformer leads to the best results overall, especially when searching into a large search pool. Transfer learning is particularly effective when much pre-training data is available and fine-tuning data is limited. We demonstrate that natural language processing models based on the Transformer architecture can be directly applied to source code analysis tasks, such as code search. With the development of Transformer models designed more specifically for dealing with source code data, we believe the results of source code analysis tasks can be further improved.

**Link**: [Read Paper](https://doi.org/10.1109/TSE.2022.3192755)

**Labels**: static analysis, code search, code model, training, source code model
