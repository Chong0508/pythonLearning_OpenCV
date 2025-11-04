# needs to import haar_face.xml (from github opencv/data/haarcascades/haarcascade_frontalface_default.xml)
# Face detection does not involve skin tone / color
# Reduce sensitivity  to noise ~ modifying scale factor in minimum neighbors 
# Not very accurate

import cv2 as cv

img = cv.imread('Resources/Photos/group 2.jpg')
cv.imshow('Group of 5 persons', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

haar_cascade = cv.CascadeClassifier('Section3-Faces/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
  cv.rectangle(img, (x,y), (x+w, y+h),(0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)