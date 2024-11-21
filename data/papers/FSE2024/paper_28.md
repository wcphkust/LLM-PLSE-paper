# DAInfer: Inferring API Aliasing Specifications from Library Documentation via Neurosymbolic Optimization

**Authors**: Wang, Chengpeng and Zhang, Jipeng and Wu, Rongxin and Zhang, Charles

**Abstract**:

Modern software systems heavily rely on various libraries, necessitating understanding API semantics in static analysis. However, summarizing API semantics remains challenging due to complex implementations or the unavailability of library code. This paper presents DAInfer, a novel approach for inferring API aliasing specifications from library documentation. Specifically, we employ Natural Language Processing (NLP) models to interpret informal semantic information provided by the documentation, which enables us to reduce the specification inference to an optimization problem. Furthermore, we propose a new technique called neurosymbolic optimization to efficiently solve the optimization problem, yielding the desired API aliasing specifications. We have implemented DAInfer as a tool and evaluated it upon Java classes from several popular libraries. The results indicate that DAInfer infers the API aliasing specifications with a precision of 79.78% and a recall of 82.29%, averagely consuming 5.35 seconds per class. These obtained aliasing specifications further facilitate alias analysis, revealing 80.05% more alias facts for API return values in 15 Java projects. Additionally, the tool supports taint analysis, identifying 85 more taint flows in 23 Android apps. These results demonstrate the practical value of DAInfer in library-aware static analysis

**Link**: [Read Paper](No Link Available)

**Labels**: static analysis, specification inference
