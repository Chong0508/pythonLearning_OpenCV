import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging Blur ~ find average of the surrounding pixels
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur ~ more natural compared to Averaging Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur ~ basically same as Averaging Blur
# it finds the median of the surrounding pixels
# More effective in removing noise in an image
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur ~ most effective
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)