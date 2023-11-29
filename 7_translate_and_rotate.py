import cv2 as cv
import numpy as np

img = cv.imread("images\pic1.jpg")
initial_image = cv.resize(img, (600, 400))

# function for translating the image
def translate(img, x, y):
    trans_matrix = np.float32([[1, 0.1, x],
                              [-0.1, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_matrix, dimensions)

# function for rotating the image
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint == None:
        rotPoint = (width//2, height//2)

    rotMatrix = cv.getRotationMatrix2D(rotPoint, angle, 1)

    return cv.warpAffine(img, rotMatrix, (width, height))


# continously rotating the image
for i in range(100):
    img = rotate(initial_image, i)
    cv.imshow("ammu", img)
    if cv.waitKey(17) == ord('d'):
        break

print(cv.getRotationMatrix2D((2,2), 30, 1))
