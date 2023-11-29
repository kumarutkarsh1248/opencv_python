import cv2 as cv
import numpy as np

## reading a video
capture = cv.VideoCapture(0)
while True:
    # changing the frame in every iteration
    isTrue, frame = capture.read()
    # fliping the frame
    flipped_frame = cv.flip(frame, 1)
    # converting the frame in canny value
    canny_frame = cv.Canny(flipped_frame, 120, 175)
    # finding the contours from the canny
    contours, hierarchy = cv.findContours(canny_frame, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    # creating the final frames containing the contours
    contoured_frame = cv.drawContours(flipped_frame, contours, -1, (0, 255, 255), 3)

    cv.imshow("contoured_frame", contoured_frame)

    if cv.waitKey(17) == ord('d'):
        break

capture.release()
cv.destroyAllWindows()