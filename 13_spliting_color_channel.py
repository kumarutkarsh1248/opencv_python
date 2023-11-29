import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np



img = np.array(cv.imread("images/pic1.jpg"))
img = cv.resize(img, (300, 200))
cv.imshow("img", img)

# creating a blank image
blank = np.zeros(img.shape[:2], dtype='uint8')

# spliting the color channel
b, g, r = cv.split(img)
print(b.shape, g.shape, r.shape)
cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)

# merginng the color channel
merged = cv.merge([b, g, r])
cv.imshow("merged", merged)

# creating a blue, green and red image
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow("blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)


cv.waitKey(0)

