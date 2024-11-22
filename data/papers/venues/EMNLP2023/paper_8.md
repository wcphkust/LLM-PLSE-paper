# CRUSH4SQL: Collective Retrieval Using Schema Hallucination For Text2SQL

**Authors**: Kothyari, Mayank and Dhingra, Dhruva and Sarawagi, Sunita and Chakrabarti, Soumen

**Abstract**:

Existing Text-to-SQL generators require the entire schema to be encoded with the user text. This is expensive or impractical for large databases with tens of thousands of columns. Standard dense retrieval techniques are inadequate for schema subsetting of a large structured database, where the correct semantics of retrieval demands that we rank sets of schema elements rather than individual documents. In response, we propose a two-stage process for effective coverage during retrieval. First, we use an LLM to hallucinate a minimal DB schema that it deems adequate to answer the query. We use the hallucinated schema to retrieve a subset of the actual schema, by composing the results from multiple dense retrievals. Remarkably, hallucination — generally considered a nuisance — turns out to be actually useful as a bridging mechanism. Since no existing benchmarks exist for schema subsetting on large databases, we introduce two benchmarks: (1) A semi-synthetic dataset of 4502 schema elements, by taking a union of schema on the well-known SPIDER dataset, and (2) A real-life benchmark called SocialDB sourced from an actual large data warehouse comprising of 17844 schema elements. We show that our method leads to significantly higher recall than SOTA retrieval-based augmentation methods.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.868)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)
