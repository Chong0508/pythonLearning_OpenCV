# Rescaling video implies modifying its height and width to a particular height and width.

import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
  # Able to use for Images, Videos, Live Videos
  # frame.shape[1] ~ width of image / frame.shape[0] ~ height of image
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)
  dimensions = (width, height)

  return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# Change Resolution
def changeRes(width, height):
  # Use for Live Videos
  capture.set(3, width)
  capture.set(4, height)

# Image
img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)
resized_image = rescaleFrame(img)
cv.imshow('Cat_Resized', resized_image)

# Reading Videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
  isTrue, frame = capture.read()
  frame_resized = rescaleFrame(frame, scale=0.2)

  cv.imshow('Video', frame)
  cv.imshow('Video_Resized', frame_resized)

  if cv.waitKey(20) & 0xFF==ord('d'):
    break

capture.release()
cv.destroyAllWindows()