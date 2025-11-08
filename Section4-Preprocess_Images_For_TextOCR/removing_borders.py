# 7 - Removing Borders

import cv2 as cv

no_noise = cv.imread("Section4-Preprocess_Images_For_TextOCR/temp/no_noise.jpg")
cv.imshow('No Noise Image', no_noise)

gray = cv.cvtColor(no_noise, cv.COLOR_BGR2GRAY)

# Threshold to get a binary image (invert so text/objects are white)
_, thresh = cv.threshold(gray, 180, 255, cv.THRESH_BINARY_INV)

def remove_borders(image):
  contours, hierarchy = cv.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
  cntsSorted = sorted(contours, key=lambda x:cv.contourArea(x))
  cnt = cntsSorted[-1]
  x, y, w, h = cv.boundingRect(cnt)
  crop = image[y:y+h, x:x+w]
  return (crop)

no_borders = remove_borders(thresh)
cv.imwrite("Section4-Preprocess_Images_For_TextOCR/temp/no_borders.jpg", no_borders)
cv.imshow('No Borders', no_borders)

cv.waitKey(0)