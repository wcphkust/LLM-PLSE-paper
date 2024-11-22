# Using an LLM to Help With Code Understanding

**Authors**: Nam, Daye and Macvean, Andrew and Hellendoorn, Vincent and Vasilescu, Bogdan and Myers, Brad

**Abstract**:

Understanding code is challenging, especially when working in new and complex development environments. Code comments and documentation can help, but are typically scarce or hard to navigate. Large language models (LLMs) are revolutionizing the process of writing code. Can they do the same for helping understand it? In this study, we provide a first investigation of an LLM-based conversational UI built directly in the IDE that is geared towards code understanding. Our IDE plugin queries OpenAI's GPT-3.5-turbo model with four high-level requests without the user having to write explicit prompts: to explain a highlighted section of code, provide details of API calls used in the code, explain key domain-specific terms, and provide usage examples for an API. The plugin also allows for open-ended prompts, which are automatically contextualized to the LLM with the program being edited. We evaluate this system in a user study with 32 participants, which confirms that using our plugin can aid task completion more than web search. We additionally provide a thorough analysis of the ways developers use, and perceive the usefulness of, our system, among others finding that the usage and benefits differ between students and professionals. We conclude that in-IDE prompt-less interaction with LLMs is a promising future direction for tool builders.

**Link**: [Read Paper](https://doi.org/10.1145/3597503.3639187)

**Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md)
