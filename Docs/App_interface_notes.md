# App Interface Notes
The app has a deliberately simple interface. The assignment
says grading is on whether the classification works, not on
how the interface looks.
## What is on screen
1. A title and short description of what the app does
2. An upload button for a JPG or PNG image
3. The uploaded image shown back to you
4. The result: Pothole or Plain
5. A confidence percentage
6. A sidebar with model and dataset information
## How the prediction works
- The image is resized to 224 x 224 pixels
- Pixel values are scaled from 0-255 to 0-1
- The model outputs a number between 0 and 1
- Above 0.5 means Pothole, below 0.5 means Plain
