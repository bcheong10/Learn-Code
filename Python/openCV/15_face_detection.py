import cv2 as cv

img = cv.imread('Photos/group 2.jpg')
cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

# Read the face detection xml file
haar_cascade = cv.CascadeClassifier('Haarcascade/haar_face.xml')

# The rectangular coordinates of faces found
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)

# Printing number of faces detected
print(f"Number of faces detected: {len(faces_rect)}")
print(f"The coordinates of faces found: {faces_rect}")

# Draw a rectangular border around the faces detected
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness = 2)

cv.imshow('Detected Faces', img)


cv.waitKey(0)