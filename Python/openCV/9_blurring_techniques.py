import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow("Original", img)

# Method 1: Averaging
average = cv.blur(img, (7,7))
cv.imshow("Average Blur", average)

# Method 2: Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("Gaussian Blur", gauss)

# Method 3: Median Blurring
median = cv.medianBlur(img, 7)
cv.imshow("Median Blur", median)

# Method 4: Bilateral Blurring - retains the edges in the image
bi = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral BLurring", bi)


cv.waitKey(0)