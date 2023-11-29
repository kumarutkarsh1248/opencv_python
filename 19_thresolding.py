# here we basically convert the image in binary form
import cv2 as cv

img1 = cv.imread("images/pic1.jpg")
img2 = cv.imread("images/pic2.jpg")
img1 = cv.resize(img1, (400, 400))
img2 = cv.resize(img2, (400, 400))

gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
cv.imshow("gray_image", gray)

# simple thresholding
for i in range(255):
    threshold, thresh = cv.threshold(gray, i, 255, cv.THRESH_BINARY)
    cv.imshow("simple thresholded", thresh)

    threshold, thresh_inv = cv.threshold(gray, i, 255, cv.THRESH_BINARY_INV)
    cv.imshow("simple thresholded_inv", thresh_inv)

    if cv.waitKey(17) == ord('d'):
        break

# adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255,cv.ADAPTIVE_THRESH_MEAN_C, 
                                       cv.THRESH_BINARY, 1, 1)
cv.imshow("adaptive_thresh", adaptive_thresh)


cv.waitKey(0)