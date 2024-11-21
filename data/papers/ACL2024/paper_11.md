# Virtual Compiler Is All You Need For Assembly Code Search

**Authors**: Gao, Zeyu and Wang, Hao and Wang, Yuanda and Zhang, Chao

**Abstract**:

Assembly code search is vital for reducing the burden on reverse engineers, allowing them to quickly identify specific functions using natural language within vast binary programs.Despite its significance, this critical task is impeded by the complexities involved in building high-quality datasets. This paper explores training a Large Language Model (LLM) to emulate a general compiler. By leveraging Ubuntu packages to compile a dataset of 20 billion tokens, we further continue pre-train CodeLlama as a Virtual Compiler (ViC), capable of compiling any source code to assembly code. This approach allows for “virtual” compilation across a wide range of programming languages without the need for a real compiler, preserving semantic equivalency and expanding the possibilities for assembly code dataset construction. Furthermore, we use ViC to construct a sufficiently large dataset for assembly code search. Employing this extensive dataset, we achieve a substantial improvement in assembly code search performance, with our model surpassing the leading baseline by 26%.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.167)

**Labels**: code generation, program transformation, static analysis, code search, code model, training, source code model
