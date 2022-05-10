from flask import Flask, render_template
from PIL import Image
import numpy as np
import os


image_path = "test.jpg"

def read_image(path):
    try:
        image = Image.open(path)
        return image
    except Exception as e:
         print(e)

def convert_to_grayscale(image):
    grayscale = image.convert("L")
    return grayscale

def get_binary_image(image, threshold):
    grayscale = convert_to_grayscale(image)
    arr = np.array(grayscale)

    for i in range(0, len(arr)): 
        for j in range(0, len(arr[i])):
            if arr[i][j] >= threshold:
                arr[i][j] = 255
            else:
                arr[i][j] = 0
    return Image.fromarray(arr)

def get_rainbow_image(image):
    arr = np.array(image)

    for i in range(0, len(arr)): 
        for j in range(0, len(arr[i])):
            arr[i][j] += 100
    return Image.fromarray(arr)

UPLOAD_FOLDER = "static/"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def show_image(image):
    return render_template("index.html", image)

image = read_image(image_path)
grayscale = convert_to_grayscale(image)
binary = get_binary_image(image, 100)
rainbow = get_rainbow_image(image)
show_image(image)
