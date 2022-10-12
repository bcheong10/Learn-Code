import cv2 as cv

# Rescale function
def rescaleFrame(frame, scale = 0.5):
    width = int(frame.shape[1] * scale) # frame.shape[1] = width of image
    height = int(frame.shape[0] * scale) # frame.shape[0] = height of image
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

    
img = cv.imread('Photos/cat_large.jpg')
resized_img = rescaleFrame(img)

cv.imshow('Cat', img)
cv.imshow('Cat Resized', resized_img)

cv.waitKey(0)