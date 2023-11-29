import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np



bgr = np.array(cv.imread("images/pic1.jpg"))
cv.imshow("bgr", bgr)

# conversion from bgr to rgb
rgb = cv.cvtColor(bgr, cv.COLOR_RGB)
cv.imshow("rgb", rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)

