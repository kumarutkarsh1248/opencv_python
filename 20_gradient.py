# here we basically convert the image in binary form
import cv2 as cv
import numpy as np

img1 = cv.imread("images/pic1.jpg")
img2 = cv.imread("images/pic2.jpg")
img1 = cv.resize(img1, (400, 400))
img2 = cv.resize(img2, (400, 400))

gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
cv.imshow("gray_image", gray)

# laplacian
lap = cv.Laplacian(gray, ddepth=cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian", lap)

# sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

# cv.imshow("sobelx", sobelx)
cv.imshow("sobely", sobely)
# cv.imshow("combined sobel",combined_sobel)


cv.waitKey(0) 