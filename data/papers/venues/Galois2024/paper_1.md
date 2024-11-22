# Function Argument Nullability Using an LLM

**Authors**: Galois

**Abstract**:

We think that Rust is a great language, and maybe you agree! Unfortunately, even if you do, there’s a good chance whatever application you’re working on is written in some older language such as C. To help with this, Galois has been developing c2rust, an automated transpiler (source-to-source translator) from C code into Rust code. c2rust can take almost any C and turn it into C-like Rust code, the first step in creating a new Rust application. And we’re building more features to turn C into safe, idiomatic Rust code. Recently, we have been experimenting with LLMs to help with transpilation from C to Rust. This blog describes one such experiment, where we built an analysis for determining nullability of function arguments in C. This is a necessary stage in the c2rust translation pipeline, and we already have an existing interprocedural static analysis tool that performs this task. We built a companion LLM-based tool using GPT-4o, and compared the performance between our static and LLM-based analysis. 

**Link**: [Read Paper](https://galois.com/blog/2024/11/function-argument-nullability-using-an-llm/)

**Labels**: [static analysis](../../labels/static_analysis.md), [fundamental analysis](../../labels/fundamental_analysis.md)
