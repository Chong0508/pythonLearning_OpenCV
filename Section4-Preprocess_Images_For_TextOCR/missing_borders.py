# 8 - Missing Borders

import cv2 as cv

no_borders = cv.imread("Section4-Preprocess_Images_For_TextOCR/temp/no_borders.jpg")
cv.imshow('No Border Image', no_borders)

color = [255, 255, 255]
top, bottom, left, right = [150] * 4

image_with_border = cv.copyMakeBorder(no_borders, top, bottom, left, right, cv.BORDER_CONSTANT, value=color)
cv.imwrite("Section4-Preprocess_Images_For_TextOCR/temp/image_with_border.jpg", image_with_border)
cv.imshow('Image With Borders', image_with_border)

cv.waitKey(0)