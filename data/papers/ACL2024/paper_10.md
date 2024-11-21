# UniCoder: Scaling Code Large Language Model via Universal Code

**Authors**: Sun, Tao and Chai, Linzheng and Yang, Jian and Yin, Yuwei and Guo, Hongcheng and Liu, Jiaheng and Wang, Bing and Yang, Liqun and Li, Zhoujun

**Abstract**:

Intermediate reasoning or acting steps have successfully improved large language models (LLMs) for handling various downstream natural language processing (NLP) tasks.When applying LLMs for code generation, recent works mainly focus on directing the models to articulate intermediate natural-language reasoning steps, as in chain-of-thought (CoT) prompting, and then output code with the natural language or other structured intermediate steps. However, such output is not suitable for code translation or generation tasks since the standard CoT has different logical structures and forms of expression with the code. In this work, we introduce the universal code (UniCode) as the intermediate representation. It is a description of algorithm steps using a mix of conventions of programming languages, such as assignment operator, conditional operator, and loop. Hence, we collect an instruction dataset UniCoder-Instruct to train our model UniCoder on multi-task learning objectives. UniCoder-Instruct comprises natural-language questions, code solutions, and the corresponding universal code. The alignment between the intermediate universal code representation and the final code solution significantly improves the quality of the generated code. The experimental results demonstrate that UniCoder with the universal code significantly outperforms the previous prompting methods by a large margin, showcasing the effectiveness of the structural clues in pseudo-code.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.100)

**Labels**: code generation, program synthesis, code model, training, IR code model
