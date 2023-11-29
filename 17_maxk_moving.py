import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("images/pic1.jpg")
img = cv.resize(img, (400, 400))

blank = np.zeros(img.shape[:2], dtype="uint8")

x_increase = 1
y_increase = 1
x_center = img.shape[1] // 2
y_center = img.shape[0] // 2 
while True:
    x_center += x_increase
    y_center += y_increase

    mask = cv.circle(blank.copy(), (x_center, y_center), 100, 255, -1)

    masked_image = cv.bitwise_and(src1=img, src2=img, mask=mask)
    cv.imshow("masked_image", masked_image)
    
    if(x_center+100 > 400 or x_center-100 < 0):
        x_increase *= -1
    if(y_center+100 > 400 or y_center-100 < 0):
        y_increase *= -1
    if cv.waitKey(17) == ord('d'):
        break

