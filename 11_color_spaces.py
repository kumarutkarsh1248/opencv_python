import cv2 as cv
import numpy as np

## reading a video
capture = cv.VideoCapture(0)
while True:
    # changing the frame in every iteration
    isTrue, frame = capture.read()

    # fliping the frame
    flipped_frame = cv.flip(frame, 1)
    cv.imshow("flipped_image", flipped_frame)

    # making the image gray
    gray_frame = cv.cvtColor(flipped_frame, cv.COLOR_BGR2GRAY)
    cv.imshow("gray_frame", gray_frame)

    # BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)

    # BGR to LAB
    lab = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
    cv.imshow("lab", lab)

    if cv.waitKey(17) == ord('d'):
        break

capture.release()
cv.destroyAllWindows()