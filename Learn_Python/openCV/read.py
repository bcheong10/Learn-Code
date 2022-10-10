import cv2 as cv

# Read image
img = cv.imread('Photos/cat.jpg')

# Opens the image in a new window
# cv.imshow('Name of window', 'matrix of pixels')
cv.imshow('Cat, img') 

# Wait for a delay in miliseconds
cv.waitKey(0)