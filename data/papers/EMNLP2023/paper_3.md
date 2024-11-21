# Benchmarking and Improving Text-to-SQL Generation under Ambiguity

**Authors**: Bhaskar, Adithya and Tomar, Tushar and Sathe, Ashutosh and Sarawagi, Sunita

**Abstract**:

Research in Text-to-SQL conversion has been largely benchmarked against datasets where each text query corresponds to one correct SQL. However, natural language queries over real-life databases frequently involve significant ambiguity about the intended SQL due to overlapping schema names and multiple confusing relationship paths. To bridge this gap, we develop a novel benchmark called AmbiQT with over 3000 examples where each text is interpretable as two plausible SQLs due to lexical and/or structural ambiguity. When faced with ambiguity, an ideal top-k decoder should generate all valid interpretations for possible disambiguation by the user. We evaluate several Text-to-SQL systems and decoding algorithms, including those employing state-of-the-art LLMs, and find them to be far from this ideal. The primary reason is that the prevalent beam search algorithm and its variants, treat SQL queries as a string and produce unhelpful token-level diversity in the top-k. We propose LogicalBeam, a new decoding algorithm that navigates the SQL logic space using a blend of plan-based template generation and constrained infilling. Counterfactually generated plans diversify templates while in-filling with a beam-search that branches solely on schema names provides value diversity. LogicalBeam is up to 2.5 times more effective than state-of-the-art models at generating all candidate SQLs in the top-k ranked outputs. It also enhances the top-5 Exact and Execution Match Accuracies on SPIDER and Kaggle DBQA.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2023.emnlp-main.436)

**Labels**: code generation, program synthesis, benchmark
