import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
cv.imshow("Original", img)

# Masking - focus on certain parts of the image

blank = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow("Blank Image", blank)

circle = cv.circle(blank, (img.shape[1]//2 + 70, img.shape[0]//2), 100, 255, -1)
cv.imshow("Circle", circle)

masked = cv.bitwise_and(img, img, mask = circle)
cv.imshow("Masked Image", masked)

cv.waitKey(0)