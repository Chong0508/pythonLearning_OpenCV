# 5 - Dilation & Erosion
# ~ To actually adjust the font size

import cv2 as cv
import numpy as np

no_noise = cv.imread("Section4-Preprocess_Images_For_TextOCR/temp/no_noise.jpg")
cv.imshow('No Noise Image', no_noise)

def thin_font(image):
  image = cv.bitwise_not(image)
  kernel = np.ones((2,2),np.uint8)
  image = cv.erode(image, kernel, iterations=1)
  image = cv.bitwise_not(image)
  return (image)

eroded_image = thin_font(no_noise)
cv.imwrite("Section4-Preprocess_Images_For_TextOCR/temp/eroded_image.jpg", eroded_image)
cv.imshow('Eroded Image', eroded_image)

def thick_font(image):
  image = cv.bitwise_not(image)
  kernel = np.ones((2,2),np.uint8)
  image = cv.dilate(image, kernel, iterations=1)
  image = cv.bitwise_not(image)
  return (image)

dilated_image = thick_font(no_noise)
cv.imwrite("Section4-Preprocess_Images_For_TextOCR/temp/dilated_image.jpg", dilated_image)
cv.imshow('Dilated Image', dilated_image)

cv.waitKey(0)
