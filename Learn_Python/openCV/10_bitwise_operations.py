import cv2 as cv
import numpy as np

# Bitwise Operations on openCV deals with black and white images (1s and 0s)

blank = np.zeros((400,400), dtype = 'uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow("Circle", circle)

# Bitwise AND - Returns the combination of black region / intersection of white
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise AND", bitwise_and)

# Bitwise OR - Returns intersection of black / combination of white 
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR", bitwise_or)

# Bitwise XOR - Returns non-intersecting white
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise XOR", bitwise_xor)

# Bitwise NOT - Iverts binary color
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("Bitwise NOT", bitwise_not)

cv.waitKey(0)