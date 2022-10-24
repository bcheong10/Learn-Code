import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow("Original", img)

# Split into individual color channels
b,g,r = cv.split(img)

# Region with lighter colors show higher intensity of individual color
cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merge color channels
merged = cv.merge([b,g,r])
cv.imshow("Merged", merged)


cv.waitKey(0)