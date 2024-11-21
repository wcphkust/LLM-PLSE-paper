# Instruct, Not Assist: LLM-based Multi-Turn Planning and Hierarchical Questioning for Socratic Code Debugging

**Authors**: Kargupta, Priyanka and Agarwal, Ishika and Tur, Dilek Hakkani and Han, Jiawei

**Abstract**:

Socratic questioning is an effective teaching strategy, encouraging critical thinking and problem-solving. The conversational capabilities of large language models (LLMs) show great potential for providing scalable, real-time student guidance. However, current LLMs often give away solutions directly, making them ineffective instructors. We tackle this issue in the code debugging domain with TreeInstruct, an Instructor agent guided by a novel state space-based planning algorithm. TreeInstruct asks probing questions to help students independently identify and resolve errors. It estimates a student’s conceptual and syntactical knowledge to dynamically construct a question tree based on their responses and current knowledge state, effectively addressing both independent and dependent mistakes concurrently in a multi-turn interaction setting. In addition to using an existing single-bug debugging benchmark, we construct a more challenging multi-bug dataset of 150 coding problems, incorrect solutions, and bug fixes– all carefully constructed and annotated by experts. Extensive evaluation shows TreeInstruct’s state-of-the-art performance on both datasets, proving it to be a more effective instructor than baselines. Furthermore, a real-world case study with five students of varying skill levels further demonstrates TreeInstruct’s ability to guide students to debug their code efficiently with minimal turns and highly Socratic questioning.

**Link**: [Read Paper](https://aclanthology.org/2024.findings-emnlp.553)

**Labels**: program testing, debugging, agent design, planning
