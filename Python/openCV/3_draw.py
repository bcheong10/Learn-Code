import cv2 as cv
import numpy as np

# Creating a blank image
# (500,500, 3) is the dimensions of image & 3 channel color
blank = np.zeros((500,500,3), dtype = 'uint8') # 'uint8 = data type of an image
cv.imshow('Blank', blank)

# Paint the image 
# blank[:] references all the pixels
# 0,255,0 is the color code
blank[:] = 0,255,0
cv.imshow('Green', blank)

# Draw rectangle
# cv.rectangle(blank, point1, point2, color, thickness)
blank2 = np.zeros((500,500,3), dtype = 'uint8')
cv.rectangle(blank2, (0,0), (250,250), (0,255,0), thickness = 1)
cv.imshow('Rectangle', blank2)

# Draw circle
blank3 = np.zeros((500,500,3), dtype = 'uint8')

# cv.circle(blank3, origin, radius, color, thickness)
cv.circle(blank3, (250,250), 40, (0,0,255), thickness = -1)
cv.imshow('Circle', blank3)

# Draw a line
cv.line(blank3, (0,0), (250,500), (255,255,255), thickness = 5)
cv.imshow('Line', blank3)

# Writing text on image
cv.putText(blank3, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness = 2)
cv.imshow('Text', blank3)

cv.waitKey(0)