import numpy as np
import onnxruntime as ort
from PIL import Image
from io import BytesIO
from urllib import request
import os

# Configuration matching the internal docker model
MODEL_FILE = "hair_classifier_empty.onnx"
TARGET_SIZE = (200, 200)

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def preprocess_input(img):
    x = np.array(img, dtype='float32')
    x /= 255.0
    mean = np.array([0.485, 0.456, 0.406], dtype='float32')
    std = np.array([0.229, 0.224, 0.225], dtype='float32')
    x = (x - mean) / std
    x = x.transpose((2, 0, 1))
    x = np.expand_dims(x, axis=0)
    return x.astype('float32')

# Global session to load model only once (standard Lambda practice)
session = None

def init_session():
    global session
    if session is None:
        # Check if the model exists in the container
        if not os.path.exists(MODEL_FILE):
             raise FileNotFoundError(f"Model file {MODEL_FILE} not found. Are you running inside the correct Docker container?")
        session = ort.InferenceSession(MODEL_FILE)

def predict(url):
    init_session()

    # 1. Download and Process
    img = download_image(url)
    img_prepared = prepare_image(img, TARGET_SIZE)
    X = preprocess_input(img_prepared)

    # 2. Inference
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name

    result = session.run([output_name], {input_name: X})
    return float(result[0][0][0])

def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result
