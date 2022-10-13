import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow("Original", img)

# Image translation function
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100)
cv.imshow("Translated", translated)

# Image rotation function
def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

        rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions = (width, height)

        return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow("Rotated", rotated)

# Flipping the image
# 0 -> Flip vertically, 1 -> flip horizontally, -1 -> flip vertically and horizontally
flip = cv.flip(img, 0)
cv.imshow('Flip', flip)

cv.waitKey(0)


