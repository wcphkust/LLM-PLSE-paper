# Program-Aided Reasoners (Better) Know What They Know

**Authors**: Kabra, Anubha and Rangreji, Sanketh and Mathur, Yash and Madaan, Aman and Liu, Emmy and Neubig, Graham

**Abstract**:

Prior work shows that program-aided reasoning, in which large language models (LLMs) are combined with programs written in programming languages such as Python, can significantly improve accuracy on various reasoning tasks. However, while accuracy is essential, it is also important for such reasoners to “know what they know”, which can be quantified through the calibration of the model. In this paper, we compare the calibration of Program Aided Language Models (PAL) and text-based Chain-of-thought (COT) prompting techniques over 5 datasets and 2 model types - LLaMA models and OpenAI models. Our results indicate that PAL leads to improved calibration in 75% of the instances. Our analysis uncovers that prompting styles that produce lesser diversity in generations also have more calibrated results, and thus we also experiment with inducing lower generation diversity using temperature scaling and find that for certain temperatures, PAL is not only more accurate but is also more calibrated than COT. Overall, we demonstrate that, in the majority of cases, program-aided reasoners better know what they know than text-based counterparts.

**Link**: [Read Paper](https://doi.org/10.18653/v1/2024.naacl-long.125)

**Labels**: prompt strategy, reason with code
