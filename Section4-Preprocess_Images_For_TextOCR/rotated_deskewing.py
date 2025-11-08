# Rotated and Deskewing
# Make sure no borders

import cv2 as cv
import numpy as np

new = cv.imread("Section4-Preprocess_Images_For_TextOCR/data/page_01_rotated.jpg")
cv.imshow('New Image', new)

def getSkewAngle(cvImage) -> float:
  # Prep image, copy, convert to gray scale, blur, and threshold
  newImage = cvImage.copy()
  gray = cv.cvtColor(newImage, cv.COLOR_BGR2GRAY)
  blur = cv.GaussianBlur(gray, (9,9), 0)
  thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

  # Apply dilate to merge text into meaningful lines/paragraphs.
  # Use larger kernel on x axis to merge characters into single line, cancelling out any spaces.
  # But use smaller kernel on Y axis to separate between different blocks of text
  kernel = cv.getStructuringElement(cv.MORPH_RECT, (30, 5))
  dilate = cv.dilate(thresh, kernel, iterations=2)

  # Find all contours
  contours, hierarchy = cv.findContours(dilate, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
  contours = sorted(contours, key= cv.contourArea, reverse = True)
  for c in contours:
    rect = cv.boundingRect(c)
    x,y,w,h = rect
    cv.rectangle(newImage, (x,y), (x+w, y+h), (0,255,0), 2)

    # Find largest contour and surround in min area box
    largestContour = contours[0]
    print(len(contours))
    minAreaRect = cv.minAreaRect(largestContour)
    cv.imwrite("Section4-Preprocess_Images_For_TextOCR/temp/boxes.jpg", newImage)

    # Determine the angle. Convert it to the value that was originally used to obtain skewed image
    angle = minAreaRect[-1]
    if angle < -45:
      angle = 90 + angle
    return -1.0 * angle
  
# Rotate the image around its center
def rotateImage(cvImage, angle:float):
  newImage = cvImage.copy()
  (h, w) = newImage.shape[:2]
  center = (w//2, h//2)
  M = cv.getRotationMatrix2D(center, angle, 1.0)
  newImage = cv.warpAffine(newImage, M, (w,h), flags=cv.INTER_CUBIC, borderMode=cv.BORDER_REPLICATE)
  return newImage

# Deskew image
def deskew(cvImage):
  angle = getSkewAngle(cvImage)
  return rotateImage(cvImage, -1.0 * angle)
  
# Rotate the image to the best view angle
fixed = deskew(new)
cv.imwrite("Section4-Preprocess_Images_For_TextOCR/rotated_fixed.jpg", fixed)
rotated_fixed = cv.imread("Section4-Preprocess_Images_For_TextOCR/rotated_fixed.jpg")
cv.imshow("Rotated Fixed", rotated_fixed)

cv.waitKey(0)