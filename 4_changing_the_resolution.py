import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # will work with images, videos and live videos
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def changeRes(capture, width, height):
    # will work only with live videos or recorded video
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture(0)
changeRes(capture, 100, 100)

while True:
    isTrue, frame = capture.read()
    # frame_rescaled = rescaleFrame(frame, 0.5)

    cv.imshow("video1", frame)
    # cv.imshow("video2", frame_rescaled)

    if cv.waitKey(1000) == ord('d'):
        break

capture.release()
cv.destroyAllWindows()