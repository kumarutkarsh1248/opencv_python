import cv2 as cv
import numpy as np

img = cv.imread("images\pic1.jpg")
img = cv.resize(img, (300, 200))
cv.imshow("ammu", img)

# converting the image to gray
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("img_gray", img_gray)

# blurring the image(gaussian blur)
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("img_blur", blur)

#edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("canny edges", canny)
cv.waitKey(0)
