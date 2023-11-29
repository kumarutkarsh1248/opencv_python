import cv2 as cv
import numpy as np
import time
import os
import HandTrackingModule
import mediapipe as mp

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


## reading a video
cam = cv.VideoCapture(0)


### loop to show the video
while True:
    isTrue, frame = cam.read()

    #converting the bgr to rgb
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    frame = cv.flip(frame, 1)

    # giving the hand detection function the frame that it had to process
    results = hands.process(frame)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)


    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    cv.imshow("video", frame)
    if cv.waitKey(1) == ord('d'):
        break

cam.release()
cv.destroyAllWindows()