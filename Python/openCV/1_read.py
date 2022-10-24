import cv2 as cv

# Read image
img = cv.imread('Photos/cat.jpg')

# Opens the image in a new window
# cv.imshow('Name of window', 'matrix of pixels')
cv.imshow('Cat', img) 

# Wait for a delay in miliseconds
cv.waitKey(0)

# Read video
# 0: Webcam
# Filepath : video in file
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.waitKey(100) # Reduces FPS
    cv.imshow('Video', frame)

    # Stops the video from playing indefinitely
    if cv.waitKey(20) & 0xFF==ord('d'): # Breaks out of the loop when 'd' is pressed
        break

capture.release()
cv.destroyAllWindows()
