import cv2 as cv
import numpy as np
import time
import os
import HandTrackingModule 


## reading a video
cam = cv.VideoCapture(0)
wCam, hCam = 640, 480
cam.set(3, wCam)
cam.set(4, hCam)


# extracting the images
folderPath = "images"
img_path_list = os.listdir(folderPath)
print(img_path_list)


# let cv read the image
overlay_list = []
for index, img_path in enumerate(img_path_list):
    image = cv.imread(f"{folderPath}/{img_path}")
    image = cv.resize(image, (100, 100))         # dimensions => (width, height) and frame/image = (height, width)
    overlay_list.append(image)
    cv.imshow(f"{index}", image)

# setting up the hand detector
detector = HandTrackingModule.handDetector(detectionCon=0.7)

### loop to show the video
while True:
    isTrue, frame = cam.read()
    # frame = detector.findHands(frame)

    # slicing the main frame and fitting the other image
    h, w, c = overlay_list[0].shape
    frame[0:h, 0:w] = overlay_list[0]
    
    cv.putText(img=frame, text="hello world", org=(100, 100), fontFace=cv.FONT_HERSHEY_TRIPLEX, color=(255, 255, 255),
           fontScale=2, thickness=2)
    
    cv.imshow("video", frame)

    if cv.waitKey(1) == ord('d'):
        break

cam.release()
cv.destroyAllWindows()