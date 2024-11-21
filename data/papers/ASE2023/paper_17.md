# Cell2Doc: ML Pipeline for Generating Documentation in Computational Notebooks

**Authors**: Mondal, Tamal and Barnett, Scott and Lal, Akash and Vedurada, Jyothi

**Abstract**:

Computational notebooks have become the go-to way for solving data-science problems. While they are designed to combine code and documentation, prior work shows that documentation is largely ignored by the developers because of the manual effort. Automated documentation generation can help, but existing techniques fail to capture algorithmic details and developers often end up editing the generated text to provide more explanation and sub-steps. This paper proposes a novel machine-learning pipeline, Cell2Doc, for code cell documentation in Python data science notebooks. Our approach works by identifying different logical contexts within a code cell, generating documentation for them separately, and finally combining them to arrive at the documentation for the entire code cell. Cell2Doc takes advantage of the capabilities of existing pre-trained language models and improves their efficiency for code cell documentation. We also provide a new benchmark dataset for this task, along with a data-preprocessing pipeline that can be used to create new datasets. We also investigate an appropriate input representation for this task. Our automated evaluation suggests that our best input representation improves the pre-trained model's performance by 2.5x on average. Further, Cell2Doc achieves 1.33x improvement during human evaluation in terms of correctness, informativeness, and readability against the corresponding standalone pretrained model.

**Link**: [Read Paper](No Link Available)

**Labels**: software maintenance and deployment, documentation generation
