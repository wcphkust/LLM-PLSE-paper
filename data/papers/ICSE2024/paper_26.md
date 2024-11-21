# Language Models for Code Completion: A Practical Evaluation

**Authors**: Izadi, Maliheh and Katzy, Jonathan and Van Dam, Tim and Otten, Marc and Popescu, Razvan Mihai and Van Deursen, Arie

**Abstract**:

Transformer-based language models for automatic code completion have shown great promise so far, yet the evaluation of these models rarely uses real data. This study provides both quantitative and qualitative assessments of three public code language models when completing real-world code. We first developed an open-source IDE extension, Code4Me, for the online evaluation of the models. We collected real auto-completion usage data for over a year from more than 1200 users, resulting in over 600K valid completions. These models were then evaluated using six standard metrics across twelve programming languages. Next, we conducted a qualitative study of 1690 real-world completion requests to identify the reasons behind the poor model performance. A comparative analysis of the models' performance in online and offline settings was also performed, using benchmark synthetic datasets and two masking strategies.Our findings suggest that while developers utilize code completion across various languages, the best results are achieved for mainstream languages such as Python and Java. InCoder outperformed the other models across all programming languages, highlighting the significance of training data and objectives. Our study also revealed that offline evaluations do not accurately reflect real-world scenarios. Upon qualitative analysis of the models' predictions, we found that 66.3\% of failures were due to models' limitations, 24.4\% occurred due to inappropriate model usage in a development context, and 9.3\% were valid requests that developers overwrote. Given these findings, we propose several strategies to overcome the current limitations. These include refining training objectives, improving resilience to typographical errors, adopting hybrid approaches, and enhancing implementations and usability.

**Link**: [Read Paper](https://doi.org/10.1145/3597503.3639138)

**Labels**: code generation, code completion
