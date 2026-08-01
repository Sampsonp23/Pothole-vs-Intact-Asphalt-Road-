# Evaluation Notes
## The overfitting problem
Our model scored 93 percent accuracy on training data
but only 60 percent on validation data. This gap means
the model memorized the training images instead of
learning general patterns.
## Why overfitting happened
- The dataset is small: only 600 images total.
- 480 training images is not enough for a model with
25 million parameters.
## What we report instead of accuracy alone
- Precision: of the ones we called pothole, how many were
- Recall: of all the real potholes, how many did we catch
- F1: the two above combined into one number

