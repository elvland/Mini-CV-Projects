import cv2 as cv
import numpy as np

camera: cv.VideoCapture = cv.VideoCapture(0)

while True:
    _, frame = camera.read()

    cv.imshow('frame', frame)

    laplacian = cv.Laplacian(frame,cv.CV_64F)

    #Converting frames to floats (255,255,255) for visualization of pixel values
    laplacian = np.uint8(laplacian)


    edges = cv.Canny(frame,120,120)
    cv.imshow('Canny', edges)

    cv.imshow('laplacian', laplacian)

    if cv.waitKey(5) == ord('x'):
        break


camera.release()
cv.releaseAllWindows()