# Concrat: An Automatic C-to-Rust Lock API Translator for Concurrent Programs

**Authors**: Hong, Jaemin and Ryu, Sukyoung

**Abstract**:

Concurrent programs suffer from data races. To prevent data races, programmers use locks. However, programs can eliminate data races only when they acquire and release correct locks at correct timing. The lock API of C, in which people have developed a large portion of legacy system programs, does not validate the correct use of locks. On the other hand, Rust, a recently developed system programming language, provides a lock API that guarantees the correct use of locks via type checking. This makes rewriting legacy system programs in Rust a promising way to retrofit safety into them. Unfortunately, manual C-to-Rust translation is extremely laborious due to the discrepancies between their lock APIs. Even the state-of-the-art automatic C-to-Rust translator retains the C lock API, expecting developers to replace them with the Rust lock API. In this work, we propose an automatic tool to replace the C lock API with the Rust lock API. It facilitates C-to-Rust translation of concurrent programs with less human effort than the current practice. Our tool consists of a Rust code transformer that takes a lock summary as an input and a static analyzer that efficiently generates precise lock summaries. We show that the transformer is scalable and widely applicable while preserving the semantics; it transforms 66 KLOC in 2.6 seconds and successfully handles 74\% of real-world programs. We also show that the analyzer is scalable and precise; it analyzes 66 KLOC in 4.3 seconds.

**Link**: [Read Paper](https://doi.org/10.1109/ICSE48619.2023.00069)

**Labels**: code generation, program transformation
