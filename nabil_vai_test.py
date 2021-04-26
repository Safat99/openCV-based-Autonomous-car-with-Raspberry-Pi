

import cv2
import numpy as np
from motormodule import Motor


motor = Motor(10,22,9,4,17,27)

Kp = 20
#u = Utils()
def track(x):
    pass

cv2.namedWindow('minimum')
cv2.createTrackbar('Min', 'minimum', 125, 255, track)
cv2.createTrackbar('Switch', 'minimum', 0, 1, track)

minLineLength = 50
maxLineGap = 15
cap = cv2.VideoCapture(0)
speed = 20
sf =30
while True:
    min_ = cv2.getTrackbarPos("Min", "minimum")
    s = cv2.getTrackbarPos("Switch", "minimum")
    print("SSSS",s)
    _, image = cap.read()
    image = cv2.flip(image,0)
    image = cv2.flip(image,1)
    image = image[310:,:]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # This line might change depending on cv version
    blurred = cv2.GaussianBlur(gray, (5, 5), 3)
    _,thresh = cv2.threshold(blurred, min_,255,cv2.THRESH_BINARY)
    cv2.line(image,(320,0),(320,480),(0,255,0),2)
    left_portion = thresh[:,0:320]
    right_portion = thresh[:,320:]
    left_pixel = cv2.countNonZero(left_portion)
    right_pixel = cv2.countNonZero(right_portion)
    #print("left",left_pixel,"right",right_pixel)
    cv2.imshow("thresh",thresh)
    cv2.imshow("Frame",image)
    curveVal = -1*int((left_pixel-right_pixel)/5000)

    left_speed = 20 + Kp * curveVal
    right_speed = 20 - Kp * curveVal
    if s==1:
        if curveVal > 0:
            motor.motor_control(speed*abs(curveVal), speed*abs(curveVal)//11)
        elif curveVal < 0:
            motor.motor_control((speed*abs(curveVal))//11,speed*abs(curveVal))
        else:
            if left_pixel ==0 and right_pixel ==0:
                motor.motor_control(0,0)
            motor.motor_control(sf,sf)
    else:
        motor.motor_control(0,0)
    print(curveVal,left_pixel, right_pixel)
    
    #print(image.shape)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
       break
cap.release()
cv2.destroyAllWindows()




