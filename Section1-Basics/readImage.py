import cv2 as cv

# return an image as a matrix of pixels
img = cv.imread('Resources/Photos/cat_large.jpg')

cv.imshow('Cat', img)

# wait for a specific delay
cv.waitKey(0)