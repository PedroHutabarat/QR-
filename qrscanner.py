import cv2
from pyzbar.pyzbar import decode
import time

cam = cv2.VideoCapture(1)
cam.set(3, 320)
cam.set(4, 240)

camera = True
while camera == True:
    success, frame = cam.read()

    for i in decode(frame):
        print(i.type)
        print(i.data.decode('utf-8'))
        time.sleep(0.5)

        cv2.imshow("QrCode",frame)
        cv2.waitKey(1)
    