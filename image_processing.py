# image_processing.py

from PIL import Image
import pytesseract
import re

# Set the Tesseract OCR path (adjust it based on your actual installation path)
pytesseract.pytesseract.tesseract_cmd = 'E:\\python\\python projects\\screenshot tool\\tesseract.exe'

def extract_text_from_image(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Use Tesseract OCR to extract text
    text = pytesseract.image_to_string(image, lang='eng+chi_sim+fr')

    # Remove spaces between Chinese characters
    text = re.sub(r'([\u4e00-\u9fa5])\s+(?=[\u4e00-\u9fa5])', r'\1', text)

    # Return the extracted text
    return text
