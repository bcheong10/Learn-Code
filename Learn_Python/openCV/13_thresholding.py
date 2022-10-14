import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Original', img)

# Thresholding - Converting regular images to blank or white within a certain threshold

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple thresholding
# Returns 0 if below 150, returns 255 if above 150
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

# Simple thresholding - Inverse
threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold (Inverse)', thresh_inv)

# Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive thresholding', adaptive_thresh)

cv.waitKey(0)