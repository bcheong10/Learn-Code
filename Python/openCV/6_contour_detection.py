import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow("Blank", blank)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Make image blur
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

# Edge detection
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

# Find contours function - find edges
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"{len(contours)} number of contours found")

# Finding contours method #2
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

# Draw contours on blank image
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Countours', blank)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} number of contours found")


cv.waitKey(0)


