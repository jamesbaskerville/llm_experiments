Fine-tuned classifier based on ALBERT for classifying article titles

Based on [this Medium article](https://towardsdatascience.com/fine-tune-smaller-transformer-models-text-classification-77cbbd3bf02b).

### Description
Project included:
- Experimenting with using Gemma to generate synthetic labeled data
- Pushing datasets + models to HuggingFace
- Fine-tuning ALBERT to classify article titles

### Model
https://huggingface.co/jamesbaskerville/classify-articles

### Dataset
https://huggingface.co/datasets/jamesbaskerville/article-titles



Next steps:
- Extending set of categories to be more exhaustive (e.g. current events, etc.)
- Potentially testing on real data (e.g. RSS feed)
- Creating more of a binary classifier for articles I'm likely to find interesting