import cv2 as cv
import numpy as np

## reading a video
cam = cv.VideoCapture(0)
wCam, hCam = 640, 480
cam.set(3, wCam)
cam.set(4, hCam)

while True:
    isTrue, frame = cam.read()
    cv.imshow("video", frame)

    if cv.waitKey(1) == ord('d'):
        break

cam.release()
cv.destroyAllWindows()