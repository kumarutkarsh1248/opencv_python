import cv2 as cv
import numpy as np

img2 = np.ones((500, 500, 3), dtype='uint8')
img2[200:300, 300:400, 0:2] = 0, 255

# draw a rectangle
cv.rectangle(img=img2, pt1=(200, 200), pt2=(100, 100), color=(255, 0, 0), thickness=-1)

# circle
cv.circle(img=img2, center=(200, 30), radius=30, color=(0, 0, 255), thickness=1)

# line
cv.line(img=img2, pt1=(0, 0), pt2=(200, 200), color=(255, 255, 255), thickness=1)

# writing text on the image
cv.putText(img=img2, text="hello world", org=(100, 100), fontFace=cv.FONT_HERSHEY_TRIPLEX, color=(255, 255, 255),
           fontScale=2, thickness=2)

cv.imshow("blank image", img2)
cv.waitKey(0)
