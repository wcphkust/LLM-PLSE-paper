# Towards Understanding the Effectiveness of Large Language Models on Directed Test Input Generation

**Authors**: Jiang, Zongze and Wen, Ming and Cao, Jialun and Shi, Xuanhua and Jin, Hai

**Abstract**:

Automatic testing has garnered significant attention and success over the past few decades. Techniques such as unit testing and coverage-guided fuzzing have revealed numerous critical software bugs and vulnerabilities. However, a long-standing, formidable challenge for existing techniques is how to achieve higher testing coverage. Constraint-based techniques, such as symbolic execution and concolic testing, have been well-explored and integrated into the existing approaches. With the popularity of Large Language Models (LLMs), recent research efforts to design tailored prompts to generate inputs that can reach more uncovered target branches. However, the effectiveness of using LLMs for generating such directed inputs and the comparison with the proven constraint-based solutions has not been systematically explored.To bridge this gap, we conduct the first systematic study on the mainstream LLMs and constraint-based tools for directed input generation with a comparative perspective. We find that LLMs such as ChatGPT are comparable to or even better than the constraint-based tools, succeeding in 43.40%-58.57% samples in our dataset. Meanwhile, there are also limitations for LLMs in specific scenarios such as sequential calculation, where constraint-based tools are in a position of strength. Based on these findings, we propose a simple yet effective method to combine these two types of tools and implement a prototype based on ChatGPT and constraint-based tools. Our evaluation shows that our approach can outperform the baselines by 1.4x to 2.3x relatively. We believe our study can provide novel insights into directed input generation using LLMs, and our findings are essential for future testing research.

**Link**: [Read Paper](No Link Available)

**Labels**: program testing, unit testing, empirical study
