# 4 - Noise Removal

import cv2 as cv
# numpy is a way of working more efficiently with numerical data
import numpy as np

image_file = "Section4-Preprocess_Images_For_TextOCR/temp/im_bw.jpg"
im_bw = cv.imread(image_file, cv.IMREAD_GRAYSCALE)
cv.imshow('Black and White', im_bw)

def noise_removal(image):
  kernel = np.ones((1,1), np.uint8)
  image = cv.dilate(image, kernel, iterations=1)
  kernel = np.ones((1,1), np.uint8)
  image = cv.erode(image, kernel, iterations=1)
  image = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
  image = cv.medianBlur(image, 3)
  return (image)

no_noise = noise_removal(im_bw)
cv.imwrite("Section4-Preprocess_Images_For_TextOCR/temp/no_noise.jpg", no_noise)
cv.imshow('No Noise Image', no_noise)

cv.waitKey(0)