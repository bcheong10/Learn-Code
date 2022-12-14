import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# Grayscale histogram (Using mask)
blank = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow("Blank Image", blank)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("Circle", circle)

masked = cv.bitwise_and(gray, gray, mask = circle)
cv.imshow("Masked Image", masked)

gray_hist_masked = cv.calcHist([gray], [0], masked, [256], [0,256])

plt.figure()
plt.title("Grayscale Histogram (Masked)")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(gray_hist_masked)
plt.xlim([0,256])
plt.show()

# Histogram for color

plt.figure()
plt.title("Colored Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")

colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)
