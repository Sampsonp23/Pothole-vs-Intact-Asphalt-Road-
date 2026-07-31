"""
GET324 EE25 - Pothole vs. Intact Asphalt Road Detection
Streamlit Web Application
Group 25
"""

import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import json
import os
from PIL import Image

st.set_page_config(
    page_title="Pothole vs Intact Road - GET324 EE25",
    page_icon="🛣️",
    layout="centered"
)

st.title("🛣️ Pothole vs. Intact Asphalt Road Detection")
st.write("Upload a road image to classify it as **Pothole** or **Plain (Intact Asphalt)**.")


@st.cache_resource
def load_model():
    model_path = os.path.join("models", "pothole_model.keras")
    config_path = os.path.join("models", "model_config.json")

    model = tf.keras.models.load_model(model_path)

    with open(config_path, "r") as f:
        config = json.load(f)

    class_names = config["classes"]
    return model, class_names


try:
    model, class_names = load_model()
except Exception as e:
    st.error(f"Failed to load model: {e}")
    st.stop()


uploaded_file = st.file_uploader(
    "Choose a road image...",
    type=["jpg", "jpeg", "png"],
    help="Supported formats: JPG, JPEG, PNG"
)

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_container_width=True)

    img_resized = img.resize((224, 224))
    img_array = np.array(img_resized, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    with st.spinner("Analyzing image..."):
        prediction = model.predict(img_array, verbose=0)
        raw_score = float(prediction[0][0])
        pred_index = int(raw_score > 0.5)
        confidence = raw_score if pred_index == 1 else 1.0 - raw_score
        predicted_class = class_names[pred_index]

    st.divider()
    st.subheader("Prediction Result")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Predicted Class", predicted_class)
    with col2:
        st.metric("Confidence", f"{confidence:.2%}")

    if predicted_class == "Pothole":
        st.warning("⚠️ Pothole detected on the road surface.")
    else:
        st.success("✅ Road surface appears intact (no pothole).")

    with st.expander("Prediction Details"):
        st.write(f"**Raw sigmoid output:** {raw_score:.4f}")
        st.write(f"**Decision threshold:** 0.5")
        st.write(f"**Class mapping:** Plain = 0, Pothole = 1")

else:
    st.info("Upload a road image above to get started.")


with st.sidebar:
    st.header("About")
    st.write(
        "This application uses a custom Convolutional Neural Network (CNN) "
        "trained on the Road Anomaly Detection System Dataset to classify "
        "road images as **Pothole** or **Plain (Intact Asphalt)**."
    )
    st.divider()
    st.subheader("Model Info")
    st.write("**Architecture:** Custom CNN (3 Conv blocks)")
    st.write("**Input size:** 224 x 224 px")
    st.write("**Framework:** TensorFlow / Keras")
    st.write("**Classes:** Plain, Pothole")
    st.divider()
    st.subheader("Dataset")
    st.write(
        "Road Anomaly Detection System Dataset — "
        "600 images (300 Pothole, 300 Plain)"
    )
    st.write("[Mendeley Data](https://data.mendeley.com/datasets/fbhdy3bxgv/2)")
    st.divider()
    st.caption("GET324 Group 25 (EE25) | University of Uyo")
