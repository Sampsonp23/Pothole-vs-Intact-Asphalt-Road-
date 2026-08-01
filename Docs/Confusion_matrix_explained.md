# The Confusion Matrix Explained
A confusion matrix is a table with four numbers.
| | Predicted Plain | Predicted Pothole |
|---|---|---|
| Actually Plain | True negative | False positive |
| Actually Pothole | False negative | True positive |
## Our results
- Plain: precision 0.56, recall 1.00
- Pothole: precision 1.00, recall 0.20
## What each one costs us
- False positive: we flag a good road as pothole.
An engineer checks and moves on. Wastes a few minutes.
- False negative: we miss a real pothole.
The road stays damaged. Costs a repair and risks safety.
