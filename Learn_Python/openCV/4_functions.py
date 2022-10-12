import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# Convert to grayscale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Greyscale', gray)

# Blurring image
# (5 ,5) specifies the intensity of blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur image', blur)

# Edge Cascade - Finding the edges of the image
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

# Dilating image - adding pixels to edges of an image
dilated = cv.dilate(canny, (7,7), iterations = 2)
cv.imshow("Dilated", dilated)

# Eroding image - opposite of dilating
eroded = cv.erode(dilated, (7,7), iterations = 2)
cv.imshow("Eroded", eroded)

# Resize image
resized = cv.resize(img, (500,500))
cv.imshow("Resized", resized)

# Cropping
cropped = img[5:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)