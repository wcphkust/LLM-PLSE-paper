# Relational Programming with Foundational Models

**Authors**: Ziyang Li and Jiani Huang and Jason Liu and Felix Zhu and Eric Zhao and William Dodds and Neelay Velingker and Rajeev Alur and Mayur Naik

**Abstract**:

Foundation models have vast potential to enable diverse AI applications. The powerful yet incomplete nature of these models has spurred a wide range of mechanisms to augment them with capabilities such as in-context learning, information retrieval, and code interpreting. We propose VIEIRA, a declarative framework that unifies these mechanisms in a general solution for programming with foundation models. VIEIRA follows a probabilistic relational paradigm and treats foundation models as stateless functions with relational inputs and outputs. It supports neuro-symbolic applications by enabling the seamless combination of such models with logic programs, as well as complex, multi-modal applications by streamlining the composition of diverse sub-models. We implement VIEIRA by extending the SCALLOP compiler with a foreign interface that supports foundation models as plugins. We implement plugins for 12 foundation models including GPT, CLIP, and SAM. We evaluate VIEIRA on 9 challenging tasks that span language, vision, and structured and vector databases. Our evaluation shows that programs in VIEIRA are concise, can incorporate modern foundation models, and have comparable or better accuracy than competitive baselines.

**Link**: [Read Paper](https://doi.org/10.1609/aaai.v38i9.28934)

**Labels**: [PL design for LLMs](../../labels/PL_design_for_LLMs.md)
