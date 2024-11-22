# Hallucination In Reasoning

- [A survey on hallucination in large language models: Principles, taxonomy, challenges, and open questions](../venues/arXiv2023/paper_12.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: The emergence of large language models (LLMs) has marked a significant breakthrough in natural language processing (NLP), leading to remarkable advancements in text understanding and generation. Nevertheless, alongside these strides, LLMs exhibit a critical tendency to produce hallucinations, resulting in content that is inconsistent with real-world facts or user inputs. This phenomenon poses substantial challenges to their practical deployment and raises concerns over the reliability of LLMs in...
  - **Labels**: [hallucination in reasoning](hallucination_in_reasoning.md), [survey](survey.md)


- [Cumulative reasoning with large language models](../venues/arXiv2023/paper_13.md), ([arXiv2023](../venues/arXiv2023/README.md))

  - **Abstract**: While language models are powerful and versatile, they often fail to address highly complex problems. This is because solving complex problems requires deliberate thinking, which has been only minimally guided during training. In this paper, we propose a new method called Cumulative Reasoning (CR), which employs language models in a cumulative and iterative manner to emulate human thought processes. By decomposing tasks into smaller components, \ournameb streamlines the problem-solving process, ...
  - **Labels**: [hallucination in reasoning](hallucination_in_reasoning.md), [prompt strategy](prompt_strategy.md)


- [Deceptive Semantic Shortcuts on Reasoning Chains: How Far Can Models Go without Hallucination?](../venues/NAACL2024/paper_6.md), ([NAACL2024](../venues/NAACL2024/README.md))

  - **Abstract**: Despite the high performances of large language models (LLMs) across numerous benchmarks, recent research has unveiled their suffering from hallucinations and unfaithful reasoning. This work studies a type of hallucination induced by semantic associations. We investigate to what extent LLMs take shortcuts from certain keyword/entity biases in the prompt instead of following correct reasoning paths. To quantify this phenomenon, we propose a novel probing method and benchmark called EUREQA. EUREQA...
  - **Labels**: [hallucination in reasoning](hallucination_in_reasoning.md), [empirical study](empirical_study.md)


- [Gsm-symbolic: Understanding the limitations of mathematical reasoning in large language models](../venues/Apple2024/paper_1.md), ([Apple2024](../venues/Apple2024/README.md))

  - **Abstract**: Recent advancements in Large Language Models (LLMs) have sparked interest in their formal reasoning capabilities, particularly in mathematics. The GSM8K benchmark is widely used to assess the mathematical reasoning of models on grade-school-level questions. While the performance of LLMs on GSM8K has significantly improved in recent years, it remains unclear whether their mathematical reasoning capabilities have genuinely advanced, raising questions about the reliability of the reported metrics. ...
  - **Labels**: [hallucination in reasoning](hallucination_in_reasoning.md), [empirical study](empirical_study.md)


- [React: Synergizing reasoning and acting in language models](../venues/NeurIPS2022/paper_1.md), ([NeurIPS2022](../venues/NeurIPS2022/README.md))

  - **Abstract**: While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help th...
  - **Labels**: [hallucination in reasoning](hallucination_in_reasoning.md), [prompt strategy](prompt_strategy.md)


- [Reflexion: Language agents with verbal reinforcement learning](../venues/NeurIPS2023/paper_4.md), ([NeurIPS2023](../venues/NeurIPS2023/README.md))

  - **Abstract**: Large language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning. We propose Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic...
  - **Labels**: [hallucination in reasoning](hallucination_in_reasoning.md), [prompt strategy](prompt_strategy.md)


- [Satlm: Satisfiability-aided language models using declarative prompting](../venues/NeurIPS2023/paper_5.md), ([NeurIPS2023](../venues/NeurIPS2023/README.md))

  - **Abstract**: Prior work has combined chain-of-thought prompting in large language models (LLMs) with programmatic representations to perform effective and transparent reasoning. While such an approach works well for tasks that only require forward reasoning (e.g., straightforward arithmetic), it is less effective for constraint solving problems that require more sophisticated planning and search. In this paper, we propose a new satisfiability-aided language modeling (SatLM) approach for improving the reasoni...
  - **Labels**: [hallucination in reasoning](hallucination_in_reasoning.md), [prompt strategy](prompt_strategy.md)


- [Self-consistency improves chain of thought reasoning in language models](../venues/NeurIPS2022/paper_2.md), ([NeurIPS2022](../venues/NeurIPS2022/README.md))

  - **Abstract**: Chain-of-thought prompting combined with pre-trained large language models has achieved encouraging results on complex reasoning tasks. In this paper, we propose a new decoding strategy, self-consistency, to replace the naive greedy decoding used in chain-of-thought prompting. It first samples a diverse set of reasoning paths instead of only taking the greedy one, and then selects the most consistent answer by marginalizing out the sampled reasoning paths. Self-consistency leverages the intuitio...
  - **Labels**: [hallucination in reasoning](hallucination_in_reasoning.md), [prompt strategy](prompt_strategy.md)


- [Self-contradictory hallucinations of large language models: Evaluation, detection and mitigation](../venues/ICLR2024/paper_8.md), ([ICLR2024](../venues/ICLR2024/README.md))

  - **Abstract**: Large language models (large LMs) are susceptible to producing text that contains hallucinated content. An important instance of this problem is self-contradiction, where the LM generates two contradictory sentences within the same context. In this work, we present a comprehensive investigation into self-contradiction for various instruction-tuned LMs, covering evaluation, detection, and mitigation. Our primary evaluation task is open-domain text generation, but we also demonstrate the applicabi...
  - **Labels**: [hallucination in reasoning](hallucination_in_reasoning.md), [empirical study](empirical_study.md)


- [Self-evaluation guided beam search for reasoning](../venues/NeurIPS2023/paper_2.md), ([NeurIPS2023](../venues/NeurIPS2023/README.md))

  - **Abstract**: Breaking down a problem into intermediate steps has demonstrated impressive performance in Large Language Model (LLM) reasoning. However, the growth of the reasoning chain introduces uncertainty and error accumulation, making it challenging to elicit accurate final results. To tackle this challenge of uncertainty in multi-step reasoning, we introduce a stepwise self-evaluation mechanism to guide and calibrate the reasoning process of LLMs. We propose a decoding algorithm integrating the self-eva...
  - **Labels**: [hallucination in reasoning](hallucination_in_reasoning.md), [prompt strategy](prompt_strategy.md)


- [Tree of thoughts: Deliberate problem solving with large language models](../venues/NeurIPS2023/paper_3.md), ([NeurIPS2023](../venues/NeurIPS2023/README.md))

  - **Abstract**: Language models are increasingly being deployed for general problem solving across a wide range of tasks, but are still confined to token-level, left-to-right decision-making processes during inference. This means they can fall short in  tasks that require exploration, strategic lookahead, or where initial decisions play a pivotal role. To surmount these challenges, we introduce a new framework for language model inference, “Tree of Thoughts” (ToT), which generalizes over the popular “Chain of T...
  - **Labels**: [hallucination in reasoning](hallucination_in_reasoning.md), [prompt strategy](prompt_strategy.md)
