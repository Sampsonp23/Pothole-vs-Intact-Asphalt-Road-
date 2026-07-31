#!/usr/bin/env python
"""
Command-line prediction script for Pothole Detection.
Usage: python predict.py --image path/to/image.jpg
"""

import argparse
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import json
import os


def load_model_artifacts(model_path="models/pothole_model.keras",
                         config_path="models/model_config.json"):
    model = tf.keras.models.load_model(model_path)
    with open(config_path, "r") as f:
        config = json.load(f)
    class_names = config["classes"]
    return model, class_names


def predict_image(img_path, model, class_names, img_size=(224, 224)):
    img = image.load_img(img_path, target_size=img_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    pred = model.predict(img_array, verbose=0)
    raw_score = float(pred[0][0])
    pred_index = int(raw_score > 0.5)
    confidence = raw_score if pred_index == 1 else 1.0 - raw_score

    return class_names[pred_index], confidence, raw_score


def main():
    parser = argparse.ArgumentParser(description="Predict pothole vs intact asphalt")
    parser.add_argument("--image", "-i", type=str, required=True,
                        help="Path to the image file")
    parser.add_argument("--model", "-m", type=str, default="models/pothole_model.keras",
                        help="Path to the model file")
    args = parser.parse_args()

    if not os.path.exists(args.image):
        print(f"Error: Image file '{args.image}' not found.")
        return

    model, class_names = load_model_artifacts(args.model)
    pred_class, confidence, raw = predict_image(args.image, model, class_names)

    print(f"\nPrediction: {pred_class}")
    print(f"Confidence: {confidence:.2%}")
    print(f"Raw output: {raw:.4f}")


if __name__ == "__main__":
    main()
