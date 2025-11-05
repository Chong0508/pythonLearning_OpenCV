import cv2 as cv
from matplotlib import pyplot as plt

image_file = "Section4-Preprocess_Images_For_TextOCR/data/page_01.jpg"
img = cv.imread(image_file)
cv.imshow('Original Image', img)

# displaying different images with actual size in matplotlib subplot
def display(im_path):
  dpi = 80
  im_data = plt.imread(im_path)
  height, width, depth = im_data.shape

  # What size does the figure need to be in inches to fit the image?
  figsize = width / float(dpi), height / float(dpi)

  # Create a figure of the right size with one axes that takes up the full figure
  fig = plt.figure(figsize=figsize)
  ax = fig.add_axes([0,0,1,1])

  # Hide spines, ticks, etc.
  ax.axis('off')

  # Display the image.
  ax.imshow(im_data, cmap='gray')

  plt.show()
display(image_file)

# Inverted Image
inverted_image = cv.bitwise_not(img)
cv.imwrite("Section4-Preprocess_Images_For_TextOCR/temp/inverted.jpg", inverted_image)
display("Section4-Preprocess_Images_For_TextOCR/temp/inverted.jpg")

cv.waitKey(0)
