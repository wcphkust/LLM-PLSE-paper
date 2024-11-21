# Automated Validation of COBOL to Java Transformation

**Authors**: Kumar, Atul and Saha, Diptikalyan and Yasue, Toshiaki and Ono, Kohichi and Krishnan, Saravanan and Hans, Sandeep and Satoh, Fumiko and Mitchell, Gerald and Kumar, Sachin

**Abstract**:

Recent advances in Large Language Model (LLM) based Generative AI techniques have made it feasible to translate enterpriselevel code from legacy languages such as COBOL to modern languages such as Java or Python. While the results of LLM-based automatic transformation are encouraging, the resulting code cannot be trusted to correctly translate the original code. We propose a framework and a tool to help validate the equivalence of COBOL and translated Java. The results can also help repair the code if there are some issues and provide feedback to the AI model to improve. We have developed a symbolic-execution-based test generation to automatically generate unit tests for the source COBOL programs which also mocks the external resource calls. We generate equivalent JUnit test cases with equivalent mocking as COBOL and run them to check semantic equivalence between original and translated programs. Demo Video: https://youtu.be/aqF_agNP-lU

**Link**: [Read Paper](https://doi.org/10.1145/3691620.3695365)

**Labels**: code generation, program transformation
