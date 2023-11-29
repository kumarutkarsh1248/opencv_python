import cv2 as cv
import numpy as np

## reading a video
capture = cv.VideoCapture(0)
while True:
    # changing the frame in every iteration
    isTrue, frame = capture.read()

    # creating a black page having the dimension same as the video captured
    black = np.zeros(frame.shape, dtype="uint8")
    cv.imshow("blank page", black)

    # fliping the frame
    flipped_frame = cv.flip(frame, 1)
    cv.imshow("flipped_image", flipped_frame)

    # making the image gray
    gray_frame = cv.cvtColor(flipped_frame, cv.COLOR_BGR2GRAY)
    cv.imshow("gray_frame", gray_frame)

    # converting the frame in canny value
    canny_frame = cv.Canny(flipped_frame, 120, 175)
    cv.imshow("canny_frame", canny_frame)


    # converting the frame in thresh frame
    ret, thresh = cv.threshold(gray_frame, 120, 205, cv.THRESH_BINARY)
    cv.imshow("thresh frame", thresh)

    # finding the contours from the thresh
    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # creating the final frames containing the contours
    contoured_frame = cv.drawContours(black, contours, -1, (0, 255, 255), 1)
    cv.imshow("contoured_frame", contoured_frame)

    if cv.waitKey(17) == ord('d'):
        break

capture.release()
cv.destroyAllWindows()