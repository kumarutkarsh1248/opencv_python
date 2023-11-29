import cv2 as cv
import numpy as np 

# reading the image
while True:
    img1 = np.array(cv.imread("images/pic1.jpg"))
    cv.imshow("car", img1)

    img2 = np.array(cv.imread("images/pic2.jpg"))
    cv.imshow("cat", img2)
    if cv.waitKey(20) == ord("d"):
        break

# img1 = np.array(cv.imread("images/pic1.jpg"))
# print(img1.shape)

