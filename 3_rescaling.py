import cv2 as cv
import numpy as np


def rescaleFrame(frame, scale=0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    frame_rescaled = rescaleFrame(frame, 0.5)

    cv.imshow("video1", frame)
    cv.imshow("video2", frame_rescaled)

    if cv.waitKey(20) == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

