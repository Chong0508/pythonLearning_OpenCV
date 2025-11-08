# PyTesseract
# ~ Need to use no noise image
# ~ For unclear image, need to preprocess before using pytesseract

import pytesseract 
from PIL import Image

img_file = "Section4-Preprocess_Images_For_TextOCR/data/page_01.jpg"
no_noise = "Section4-Preprocess_Images_For_TextOCR/temp/no_noise.jpg"

img = Image.open(no_noise)
ocr_result = pytesseract.image_to_string(img)

print(ocr_result)