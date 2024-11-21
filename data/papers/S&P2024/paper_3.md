# TrojanPuzzle: Covertly Poisoning Code-Suggestion Models

**Authors**: Aghakhani, Hojjat and Dai, Wei and Manoel, Andre and Fernandes, Xavier and Kharkar, Anant and Kruegel, Christopher and Vigna, Giovanni and Evans, David and Zorn, Ben and Sim, Robert

**Abstract**:

With tools like GitHub Copilot, automatic code suggestion is no longer a dream in software engineering. These tools, based on large language models, are typically trained on massive corpora of code mined from unvetted public sources. As a result, these models are susceptible to data poisoning attacks where an adversary manipulates the model’s training by injecting malicious data. Poisoning attacks could be designed to influence the model’s suggestions at run time for chosen contexts, such as inducing the model into suggesting insecure code payloads. To achieve this, prior attacks explicitly inject the insecure code payload into the training data, making the poison data detectable by static analysis tools that can remove such malicious data from the training set. In this work, we demonstrate two novel attacks, Covert and TrojanPuzzle, that can bypass static analysis by planting malicious poison data in out-of-context regions such as docstrings. Our most novel attack, TrojanPuzzle, goes one step further in generating less suspicious poison data by never explicitly including certain (suspicious) parts of the payload in the poison data, while still inducing a model that suggests the entire payload when completing code (i.e., outside docstrings). This makes TrojanPuzzle robust against signature-based dataset-cleansing methods that can filter out suspicious sequences from the training data. Our evaluation against models of two sizes demonstrates that both Covert and TrojanPuzzle have significant implications for practitioners when selecting code used to train or tune code-suggestion models.

**Link**: [Read Paper](No Link Available)

**Labels**: code model, security, attack, code generation, code completion
