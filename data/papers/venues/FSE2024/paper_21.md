# Only diff Is Not Enough: Generating Commit Messages Leveraging Reasoning and Action of Large Language Model

**Authors**: Li, Jiawei and Farag\'{o}, David and Petrov, Christian and Ahmed, Iftekhar

**Abstract**:

Commit messages play a vital role in software development and maintenance. While previous research has introduced various Commit Message Generation (CMG) approaches, they often suffer from a lack of consideration for the broader software context associated with code changes. This limitation resulted in generated commit messages that contained insufficient information and were poorly readable. To address these shortcomings, we approached CMG as a knowledge-intensive reasoning task. We employed ReAct prompting with a cutting-edge Large Language Model (LLM) to generate high-quality commit messages. Our tool retrieves a wide range of software context information, enabling the LLM to create commit messages that are factually grounded and comprehensive. Additionally, we gathered commit message quality expectations from software practitioners, incorporating them into our approach to further enhance message quality. Human evaluation demonstrates the overall effectiveness of our CMG approach, which we named Omniscient Message Generator (OMG). It achieved an average improvement of 30.2\% over human-written messages and a 71.6\% improvement over state-of-the-art CMG methods.

**Link**: [Read Paper](https://doi.org/10.1145/3643760)

**Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [commit message generation](../../labels/commit_message_generation.md)
