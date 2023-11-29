import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img1 = cv.imread("images/pic1.jpg")
img2 = cv.imread("images/pic2.jpg")
img1 = cv.resize(img1, (400, 400))
img2 = cv.resize(img2, (400, 400))
cv.imshow("image", img1)

# creating a binary mask
blank = np.zeros(img1.shape[:2], dtype="uint8")
mask = cv.circle(blank, (img1.shape[1] // 2, img1.shape[0] // 2), 100, 255, -1)

# creating a gray scale image
gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
cv.imshow("gray image", gray)

# gray scale image histogram
gray_hist = cv.calcHist([img1], [0], mask, [256], [0, 256])
print(gray_hist)

# ploting the histogram
plt.figure()
plt.title("gray scale histogram")
plt.xlabel("bins")
plt.ylabel("number of pixel")
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

# making the histogram of all the channels
plt.figure()
plt.title("bgr histogram")
plt.xlabel("pixel value")
plt.ylabel("number of pixel")
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img1], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
    
plt.show()
cv.waitKey(0)

