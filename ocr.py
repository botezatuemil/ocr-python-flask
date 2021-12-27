from cv2 import cv2
import base64
import pytesseract
import numpy as np
from PIL import Image
from io import BytesIO
from flask import Flask, jsonify, request
import os


app = Flask(__name__)

def readb64(base64_string):
    sbuf = BytesIO()
    sbuf.write(base64.b64decode(base64_string.encode('ascii')))
    pimg = Image.open(sbuf)
    return cv2.cvtColor(np.array(pimg), cv2.COLOR_BGR2RGB)


@app.route('/post', methods=['POST'])
def return_string_from_image():

    ocrImage = request.json['ocrImage']

    pytesseract.pytesseract.tesseract_cmd = "./vendor/tesseract-ocr/bin/tesseract"
    img = readb64(ocrImage)    
    ocrString = pytesseract.image_to_string(img)

    newOcr = {"ocrImage" : ocrImage, "ocrString": ocrString}
    return jsonify(newOcr)


if __name__ == "__main__":
    app.run(debug=True)
   


# cv2.imshow('Result', img)
# cv2.waitKey(0)
