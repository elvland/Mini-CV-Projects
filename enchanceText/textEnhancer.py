import cv2 as cv

img = cv.imread("darkpage.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# image pixels below 35 are white pixels everything else is black pixels
_, result = cv.threshold(img,35, 255, cv.THRESH_BINARY)

# adaptive thresholding is used to remove noise from the image with muliti-thresholding on different part of the image
adaptive = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,21,2)

cv.imshow("result", result)
cv.imshow("darkpage", img)
cv.imshow("adaptive", adaptive)

cv.waitKey(0)
cv.destroyAllWindows()