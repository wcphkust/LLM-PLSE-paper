# Repository-Level Prompt Generation for Large Language Models of Code

**Authors**: Disha Shrivastava and Hugo Larochelle and Daniel Tarlow

**Abstract**:

With the success of large language models (LLMs) of code and their use as code assistants (e.g. Codex used in GitHub Copilot), techniques for introducing domain-specific knowledge in the prompt design process become important. In this work, we propose a framework called Repo-Level Prompt Generator that learns to generate example-specific prompts using prompt proposals. The prompt proposals take context from the entire repository, thereby incorporating both the structure of the repository and the context from other relevant files (e.g. imports, parent class files). Our technique doesn't require any access to the weights of the LLM, making it applicable in cases where we only have black-box access to the LLM. We conduct experiments on the task of single-line code-autocompletion using code repositories taken from Google Code archives. We demonstrate that an oracle constructed from our prompt proposals gives a remarkably high relative improvement of 36% over Codex, showing the quality of these proposals. Further, we show that when we train a model to predict a prompt proposal, we can achieve significant performance gains over Codex and other baselines.

**Link**: [Read Paper](https://proceedings.mlr.press/v202/shrivastava23a.html)

**Labels**: code generation, code completion, prompt strategy, RAG
