import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np



img = np.array(cv.imread("images/pic1.jpg"))
img = cv.resize(img, (300, 200))
cv.imshow("img", img)

# creating a blank image
blank = np.zeros(img.shape[:2], dtype='uint8')

# averaging
average = cv.blur(img, (7,7))
cv.imshow("average", average)

# gaussian 
gaussian = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("gaussian", gaussian)

# median blurr
median = cv.medianBlur(img, 7)
cv.imshow("median", median)

# bilateral => it preserves the edges while blurring
bilateral = cv.bilateralFilter(img, 10, sigmaColor=150, sigmaSpace=150)
cv.imshow("bilateral", bilateral)

cv.waitKey(0)

