import re
import cv2
import numpy as np
import cvzone
from cvzone.HandTrackingModule import HandDetector
from picamera2 import Picamera2
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640,480)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()
detector = HandDetector(maxHands=2,detectionCon=0.5, minTrackCon=0.5)


while True:
      im= picam2.capture_array()
      im=cv2.flip(im,-1)
#      im=cv2.flip(im,1)
      hands,im=detector.findHands(im,draw=True)
      if hands:
          hand1=hands[0]
          lmlist1=hand1['lmList']
          cx=(lmlist1[4][0])
          cy=(lmlist1[4][1])
          cv2.circle(im,(cx,cy),13,(255,0,0),-1)
          fingers1 = detector.fingersUp(hand1)
          print(f'H1 = {fingers1.count(1)}')
      cv2.imshow("im",im)
      key = cv2.waitKey(1)
      if key == 27:  # esc
         break


cv2.destroyAllWindows()