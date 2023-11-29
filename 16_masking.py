import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img1 = cv.imread("images/pic1.jpg")
img2 = cv.imread("images/pic2.jpg")
img1 = cv.resize(img1, (400, 300))
img2 = cv.resize(img2, (400, 300))

cv.imshow("image1", img1)
cv.imshow("image2", img2)

blank = np.zeros(img1.shape[:2], dtype="uint8")
cv.imshow("blank", blank)

mask = cv.circle(blank, (img1.shape[1] // 2, img1.shape[0] // 2), 100, 255, -1)
cv.imshow("mask", mask)

# creating a msked image
masked_image = cv.bitwise_and(src1=img1, src2=img2, mask=mask)
cv.imshow("masked_image", masked_image)
cv.waitKey(0)

