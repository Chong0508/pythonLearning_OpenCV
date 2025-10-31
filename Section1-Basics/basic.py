import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
# Remove some of the noise (bad lightning/camera issues) - Apply slight blur
# (3,3) is the blur level - (7, 7) is more blured
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
# Find the edge that are present in the image
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding - get back the previous form of dilated image
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
# different from previous video, this resize only get the certain part 
# cv.INTER_CUBIC is much higher quality than INTER_AREA / INTER_LINEAR
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
