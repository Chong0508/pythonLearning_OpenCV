# 3 - Binarization
# Convert the image into black & white

import cv2 as cv

image_file = "Section4-Preprocess_Images_For_TextOCR/data/page_01.jpg"
img = cv.imread(image_file)
cv.imshow('Original Image', img)

def grayscale(image):
  return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

gray_image = grayscale(img)
cv.imwrite("Section4-Preprocess_Images_For_TextOCR/temp/gray.jpg", gray_image)
gray = cv.imread("Section4-Preprocess_Images_For_TextOCR/temp/gray.jpg")
cv.imshow('Gray Image',gray)

thresh, im_bw = cv.threshold(gray_image, 200, 230, cv.THRESH_BINARY)
cv.imwrite("Section4-Preprocess_Images_For_TextOCR/temp/im_bw.jpg", im_bw)
cv.imshow('black and white', im_bw)

cv.waitKey(0)