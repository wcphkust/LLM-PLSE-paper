# Instruction tuning for secure code generation

**Authors**: He, Jingxuan and Vero, Mark and Krasnopolska, Gabriela and Vechev, Martin

**Abstract**:

Modern language models (LMs) have gained widespread acceptance in everyday and professional contexts, particularly in programming. An essential procedure enabling this adoption is instruction tuning, which substantially enhances LMs' practical utility by training them to follow user instructions and human preferences. However, existing instruction tuning schemes overlook a crucial aspect: the security of generated code. As a result, even the state-of-the-art instruction-tuned LMs frequently produce unsafe code, posing significant security risks. In this work, we introduce SafeCoder to address this gap. SafeCoder performs security-centric fine-tuning using a diverse and high-quality dataset that we collected using an automated pipeline. We integrate the security fine-tuning with standard instruction tuning, to facilitate a joint optimization of both security and utility. Despite its simplicity, we show that SafeCoder is effective across a variety of popular LMs and datasets. It is able to drastically improve security (by about 30%), while preserving utility.

**Link**: [Read Paper](https://arxiv.org/pdf/2405.00218)

**Labels**: [code generation](../../labels/code_generation.md), [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md), [defense](../../labels/defense.md)
