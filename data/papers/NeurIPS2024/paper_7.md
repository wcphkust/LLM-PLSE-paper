# Towards General Loop Invariant Generation: A Benchmark of Programs with Memory Manipulation

**Authors**: Liu, Chang and Wu, Xiwei and Feng, Yuan and Cao, Qinxiang and Yan, Junchi

**Abstract**:

Program verification is vital for ensuring software reliability, especially in the context of increasingly complex systems. Loop invariants, remaining true before and after each iteration of loops, are crucial for this verification process. Traditional provers and machine learning based methods for generating loop invariants often require expert intervention or extensive labeled data, and typically only handle numerical property verification. These methods struggle with programs involving complex data structures and memory manipulations, limiting their applicability and automation capabilities. In this paper, we introduce a new benchmark named LIG-MM, specifically for programs with complex data structures and memory manipulations. We collect 312 programs from various sources, including daily programs from college homework, the international competition (SV-COMP), benchmarks from previous papers (SLING), and programs from real-world software systems (Linux Kernel, GlibC, LiteOS, and Zephyr). Based on LIG-MM, our findings indicate that previous methods, including GPT-4, fail to automate verification for these programs. Consequently, we propose a novel LLM-SE framework that coordinates LLM with symbolic execution, fine-tuned using self-supervised learning, to generate loop invariants. Experimental results on LIG-MM demonstrate that our LLM-SE outperforms state-of-the-art methods, offering a new direction toward automated program verification in real-world scenarios.

**Link**: [Read Paper](No Link Available)

**Labels**: static analysis, program verification, benchmark
