# GET324 EE25 - Brief Report

## Pothole vs. Intact Asphalt Road Detection

**Dataset Source:** The Road Anomaly Detection System Dataset was obtained from Mendeley Data (DOI: 10.17632/fbhdy3bxgv.2). It contains 600 road images equally split between two classes: Pothole (300 images) and Plain/Intact Asphalt (300 images).

**How to Use:** Upload a road image (JPG or PNG) through the Streamlit web interface. The application preprocesses the image, passes it through the trained CNN model, and displays the predicted class (Pothole or Plain) along with a confidence score.

**Challenges:** The primary challenge was model overfitting due to the small dataset size (600 images). The model achieved high training accuracy (~93%) but lower validation accuracy (~60%), indicating limited generalization. Deployment required Git LFS to handle the large model file (~300 MB).

**Possible Improvements:** Using transfer learning (e.g., MobileNetV2 or ResNet50) with pre-trained ImageNet weights would likely improve generalization. Increasing the dataset through additional data collection or more aggressive augmentation could also help reduce overfitting.
