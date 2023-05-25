### 1. Imports and class names setup ### 
import gradio as gr
import os
import numpy as np
import pytesseract
# from model import create_effnetb2_model
from timeit import default_timer as timer
from typing import Tuple, Dict
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Path to tesseract.exe
)

# Create predict function
def predict(img, lang) -> Tuple[str, float]:
    """Transforms and performs a prediction on img and returns prediction and time taken.
    """
    # Start the timer
    start_time = timer()
    
    # Transform the target image and add a batch dimension
    # img = np.array(Image.open(img))
    text = pytesseract.image_to_string(img, lang=lang)
    
    # Calculate the prediction time
    pred_time = round(timer() - start_time, 5)
    
    # Return the prediction dictionary and prediction time 
    return text, pred_time

### 4. Gradio app ###

# Create title, description and article strings
title = "OCR with Dat👁"
description = "An OCR demo with pytesseract"
article = "Created at [OCR_python](https://github.com/phamdinhdat-ai/OCR_python)."

# Create examples list from "examples/" directory
example_list = [["sample_image/" + example] for example in os.listdir("sample_image")]

# Create Gradio interface 
demo = gr.Interface(
    fn=predict,
    inputs=[gr.Image(type="pil"),gr.Dropdown(['eng','china','vie'],label="Language")],
    outputs=[
        gr.Textbox(label="Text Generation"),
        gr.Number(label="Prediction time (s)"),
    ],
    examples=example_list,
    title=title,
    description=description,
    article=article,
)

# Launch the app!
demo.launch()
gr.T