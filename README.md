# GET324 EE25 - Pothole vs. Intact Asphalt Road Detection

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app)

## Project Overview

**Course:** GET324 - Cloud Computing and AI Model Deployment for Engineering Applications  
**Group:** 25 (EE25)  
**Task:** Binary Image Classification - Pothole vs. Intact Asphalt Road  
**CLOs:** CLO5 (Model Design/Training), CLO7 (Cloud Deployment), CLO8 (Documentation)

## Team Members

| Reg Number | Name | GitHub Username |
| :--- | :--- | :--- |
| 22/EG/EE/1996 | Ngadiuba, Sampson Paul (Lead) | [Sampsonp23](https://github.com/Sampsonp23) |
| 22/EG/EE/2114 | James, Solomon Daniel | [solomondaniel2114](https://github.com/solomondaniel2114) |
| 23/EG/EE/091 | George, Napoleon Okon | [Napoleongeorge](https://github.com/Napoleongeorge) |
| 22/EG/EE/2029 | Ekong, Daniel David | [Shady-15-money](https://github.com/Shady-15-money) |
| 22/EG/EE/2088 | Friday, Ekemini Nkerenti | [kemzyfresh](https://github.com/kemzyfresh) |
| 22/EG/EE/2031 | Udo, Benjamin Success | [rapido177](https://github.com/rapido177) |
| 22/EG/EE/1998 | Wariebi, Marcus Wariebi | [Hunterxx](https://github.com/Hunterxx) |
| 22/EG/EE/2080 | Etuk, Samuel Friday | [Samuel-etuk](https://github.com/Samuel-etuk) |
| 23/EG/EE/095 | Akpanam, Destiny Ezekiel | [akpanamdestiny2005](https://github.com/akpanamdestiny2005) |
| 23/EG/EE/094 | Destiny, Peter Peter | [destinypeter76755-eng](https://github.com/destinypeter76755-eng) |
| 22/EG/EE/2099 | Edunoh, John Tiuno | [Samandalichi8-oss](https://github.com/Samandalichi8-oss) |

## Dataset

**Road Anomaly Detection System Dataset** from Mendeley Data.

- **Classes:** `Pothole` (300 images) and `Plain` (300 images)
- **Total:** 600 images
- **Source:** [Mendeley Data - DOI: 10.17632/fbhdy3bxgv.2](https://data.mendeley.com/datasets/fbhdy3bxgv/2)
- **License:** Creative Commons Attribution 4.0 International

## Model Architecture

Custom Convolutional Neural Network (CNN):

| Layer | Details |
| :--- | :--- |
| Conv Block 1 | Conv2D(32) + BatchNorm + MaxPool + Dropout(0.25) |
| Conv Block 2 | Conv2D(64) + BatchNorm + MaxPool + Dropout(0.25) |
| Conv Block 3 | Conv2D(128) + BatchNorm + MaxPool + Dropout(0.25) |
| Dense | 256 units + BatchNorm + Dropout(0.5) |
| Output | 1 unit, sigmoid activation |

- **Input size:** 224 x 224 x 3
- **Optimizer:** Adam
- **Loss:** Binary Crossentropy
- **Training:** 15 epochs (early stopping at epoch 3)

## Model Performance

| Metric | Value |
| :--- | :--- |
| Validation Accuracy | 60.00% |
| Validation Loss | 0.6632 |
| Training Accuracy | ~93% |

| Class | Precision | Recall | F1-Score | Support |
| :--- | :--- | :--- | :--- | :--- |
| Plain | 0.56 | 1.00 | 0.71 | 60 |
| Pothole | 1.00 | 0.20 | 0.33 | 60 |

## Project Structure

```
Pothole-vs-Intact-Asphalt-Road/
├── app.py                    # Streamlit web application
├── predict.py                # CLI prediction script
├── requirements.txt          # Python dependencies
├── report.md                 # Brief project report
├── README.md                 # This file
├── .gitignore
├── .gitattributes            # Git LFS config
├── models/
│   ├── pothole_model.keras   # Trained CNN model (~300 MB, Git LFS)
│   ├── model_config.json     # Model configuration
│   └── label_encoder.pkl     # Class label mapping
├── outputs/
│   ├── plots/
│   │   ├── sample_images.png
│   │   ├── training_curves.png
│   │   └── confusion_matrix.png
│   └── metrics/
│       └── classification_report.txt
└── ee25-pothole-vs-intact-asphalt-road.ipynb  # Training notebook
```

## Setup and Run Locally

### Prerequisites

- Python 3.10 or higher
- Git with [Git LFS](https://git-lfs.com/) installed

### Step 1: Clone the Repository

```bash
git lfs install
git clone https://github.com/Sampsonp23/Pothole-vs-Intact-Asphalt-Road-.git
cd Pothole-vs-Intact-Asphalt-Road-
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`. Upload a road image to classify it.

## Deploy to Streamlit Community Cloud

1. Push this repository to GitHub (with Git LFS for the model file).
2. Go to [share.streamlit.io](https://share.streamlit.io).
3. Click **New app**.
4. Select the GitHub repository, branch `main`, and main file `app.py`.
5. Click **Deploy**.
6. Once deployed, update the badge URL at the top of this README.

## Tech Stack

- **Language:** Python 3.10+
- **ML Framework:** TensorFlow / Keras
- **Web App:** Streamlit
- **Deployment:** Streamlit Community Cloud
- **Version Control:** Git / GitHub (with Git LFS)

## License

This project is for educational purposes as part of the GET324 course at the University of Uyo.

## Acknowledgements

- GET324 Course Lecturer
- [Road Anomaly Detection System Dataset](https://data.mendeley.com/datasets/fbhdy3bxgv/2)
- TensorFlow and Keras communities
