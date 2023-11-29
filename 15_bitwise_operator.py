import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np



img = np.array(cv.imread("images/pic1.jpg"))
img = cv.resize(img, (400, 300))
cv.imshow("image", img)

blank = np.zeros((400, 400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (120, 120), (280, 280), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 100, (255, 0, 0), -1)

cv.imshow("rectangled image", rectangle)
cv.imshow("circled image", circle)

# bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("bitwise and", bitwise_and)

# bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise or", bitwise_or)

# bitwise xor (for non intersecting region)
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("bitwise_xor", bitwise_xor)

# bitwise not (for inverting the black to white ans white to black)
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("bitwise not", bitwise_not)

cv.waitKey(0)

