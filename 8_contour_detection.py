import cv2 as cv
import numpy as np

img = cv.imread("images\pic3.png")
initial_image = cv.resize(img, (600, 400))
cv.imshow("ammu", initial_image)

canny = cv.Canny(initial_image, 125, 175)
cv.imshow("canny image", canny)

# finding the contours in the canny images
# it is advisable to apply the findcontour method in the grey scale image
contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

# showing the contour in the real image
contoured_image = cv.drawContours(initial_image, contours, -1, (0, 255, 0), 3)
cv.imshow("contoured images", contoured_image)

cv.waitKey(0)