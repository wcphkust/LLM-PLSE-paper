# Semantic GUI Scene Learning and Video Alignment for Detecting Duplicate Video-based Bug Reports

**Authors**: Yan, Yanfu and Cooper, Nathan and Chaparro, Oscar and Moran, Kevin and Poshyvanyk, Denys

**Abstract**:

Video-based bug reports are increasingly being used to document bugs for programs centered around a graphical user interface (GUI). However, developing automated techniques to manage video-based reports is challenging as it requires identifying and understanding often nuanced visual patterns that capture key information about a reported bug. In this paper, we aim to overcome these challenges by advancing the bug report management task of duplicate detection for video-based reports. To this end, we introduce a new approach, called Janus, that adapts the scene-learning capabilities of vision transformers to capture subtle visual and textual patterns that manifest on app UI screens --- which is key to differentiating between similar screens for accurate duplicate report detection. Janus also makes use of a video alignment technique capable of adaptive weighting of video frames to account for typical bug manifestation patterns. In a comprehensive evaluation on a benchmark containing 7,290 duplicate detection tasks derived from 270 video-based bug reports from 90 Android app bugs, the best configuration of our approach achieves an overall mRR/mAP of 89.8\%/84.7\%, and for the large majority of duplicate detection tasks, outperforms prior work by ≈9\% to a statistically significant degree. Finally, we qualitatively illustrate how the scene-learning capabilities provided by Janus benefits its performance.

**Link**: [Read Paper](https://doi.org/10.1145/3597503.3639163)

**Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [code review](../../labels/code_review.md)
