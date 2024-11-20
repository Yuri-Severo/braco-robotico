import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.SerialModule import SerialObject
from statsmodels.stats.libqsturng.make_tbls import success

cap = cv2.VideoCapture(1)
detector = HandDetector(maxHands=1, detectionCon=0.7)
mySerial = SerialObject("COM3",9600,1)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    if lmList:
        fingers = detector.fingersUp()
        #print(fingers)
        mySerial.sendData(fingers)
    cv2.imshow("Image", img)
    cv2.waitKey(1)