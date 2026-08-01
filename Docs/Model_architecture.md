# Model Architecture
We built a custom CNN (Convolutional Neural Network)
from scratch using TensorFlow and Keras.
## Settings
- Input image size: 224 x 224 pixels, 3 colour channels
- Output: one number between 0 and 1
- Closer to 1 means pothole, closer to 0 means plain road
## Three convolutional blocks
1. First block: 32 filters, BatchNorm, MaxPool, Dropout
2. Second block: 64 filters, BatchNorm, MaxPool, Dropout
3. Third block: 128 filters, BatchNorm, MaxPool, Dropout
## Dense layer
- 256 neurons with ReLU activation
- BatchNorm and 50 percent Dropout
- Final output: 1 neuron with sigmoid activation
