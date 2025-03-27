import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convert():
    img = Image.open('img1.jpeg')
    text = pytesseract.image_to_string(img)
    print(text)

convert()