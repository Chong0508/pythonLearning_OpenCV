import cv2 as cv

# Reading Videos
# 0 represent your computer webcam, 1 represent 1st camera connected to your computer and so on
#capture = cv.VideoCapture(0)
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

# use while loop to read video frame by frame
while True:
  isTrue, frame = capture.read()
  cv.imshow('Video', frame)

  if cv.waitKey(20) & 0xFF==ord('d'):
    break

capture.release()
cv.destroyAllWindows()