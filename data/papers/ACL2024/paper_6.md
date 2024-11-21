# AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents

**Authors**: Trivedi, Harsh and Khot, Tushar and Hartmann, Mareike and Manku, Ruskin and Dong, Vinty and Li, Edward and Gupta, Shashank and Sabharwal, Ashish and Balasubramanian, Niranjan

**Abstract**:

Autonomous agents that address day-to-day digital tasks (e.g., ordering groceries for a household), must not only operate multiple apps (e.g., notes, messaging, shopping app) via APIs, but also generate rich code with complex control flow in an iterative manner based on their interaction with the environment. However, existing benchmarks for tool use are inadequate, as they only cover tasks that require a simple sequence of API calls. To remedy this gap, we built AppWorld Engine, a high-quality execution environment (60K lines of code) of 9 day-to-day apps operable via 457 APIs and populated with realistic digital activities simulating the lives of ~100 fictitious users. We then created AppWorld Benchmark (40K lines of code), a suite of 750 natural, diverse, and challenging autonomous agent tasks requiring rich and interactive code generation. It supports robust programmatic evaluation with state-based unit tests, allowing for different ways of completing a task while also checking for unexpected changes, i.e., collateral damage. The state-of-the-art LLM, GPT4O, solves only ~49% of our ‘normal’ tasks and ~30% of ‘challenge’ tasks, while other models solve at least 16% fewer. This highlights the benchmark’s difficulty and AppWorld’s potential to push the frontiers of interactive coding agents.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2024.acl-long.850)

**Labels**: benchmark, agent design
