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

list=[]
while True:
      im= picam2.capture_array()
      im=cv2.flip(im,-1)
      hands,im=detector.findHands(im,draw=True)
      if len(hands)==2:
          hand=hands[0]
          hand1=hands[1]
          lmlist=hand['lmList']
          lmlist1=hand1['lmList']
          cx=(lmlist[4][0])
          cy=(lmlist[4][1])
          cx1=(lmlist1[4][0])
          cy1=(lmlist1[4][1])
          cv2.circle(im,(cx,cy),13,(255,0,0),-1)
          cv2.circle(im,(cx1,cy1),13,(255,255,0),-1)

          fingers1 = detector.fingersUp(hand)
          fingers2=detector.fingersUp(hand1)
          list = fingers1 + fingers2
          count_1 = list.count(1)
          count_0 = list.count(0)

          print("Count of 1s:", count_1)
          print("Count of 0s:", count_0)

      
      cv2.imshow("im",im)
      key = cv2.waitKey(1)
      if key == 27:  # esc
         break


cv2.destroyAllWindows()
