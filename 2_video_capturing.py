import cv2 as cv
import numpy as np

## reading a video
capture = cv.VideoCapture(0)

isTrue = True
while isTrue:
    isTrue, frame = capture.read()
    cv.imshow("video", frame)

    if cv.waitKey(17) == ord('d'):
        break

capture.release()
cv.destroyAllWindows()