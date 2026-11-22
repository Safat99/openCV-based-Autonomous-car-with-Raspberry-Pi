

import cv2
import numpy as np
from src.hardware.motor import Motor


def track(x):
    pass


def main():
    motor = Motor(10,22,9,4,17,27)
    speed = 20
    straight_speed = 30
    pixel_scale = 5000

    cv2.namedWindow('minimum')
    cv2.createTrackbar('Min', 'minimum', 125, 255, track)
    cv2.createTrackbar('Switch', 'minimum', 0, 1, track)

    cap = cv2.VideoCapture(0)

    while True:
        min_ = cv2.getTrackbarPos("Min", "minimum")
        switch = cv2.getTrackbarPos("Switch", "minimum")

        _, image = cap.read()
        if image is None:
            break

        image = cv2.flip(image,0)
        image = cv2.flip(image,1)
        image = image[310:,:]
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 3)
        _, thresh = cv2.threshold(blurred, min_,255,cv2.THRESH_BINARY)

        center_x = thresh.shape[1] // 2
        cv2.line(image,(center_x,0),(center_x,480),(0,255,0),2)
        left_portion = thresh[:,0:center_x]
        right_portion = thresh[:,center_x:]
        left_pixel = cv2.countNonZero(left_portion)
        right_pixel = cv2.countNonZero(right_portion)

        # 5000 pixels divide one large lane-count difference into a small steering value.
        # Differences smaller than this scale are treated as straight.
        curveVal = -1 * int((left_pixel - right_pixel) / pixel_scale)

        cv2.imshow("thresh",thresh)
        cv2.imshow("Frame",image)

        if switch == 1:
            if left_pixel == 0 and right_pixel == 0:
                motor.motor_control(0,0)
            elif curveVal > 0:
                motor.motor_control(speed * abs(curveVal), speed * abs(curveVal) // 11)
            elif curveVal < 0:
                motor.motor_control(speed * abs(curveVal) // 11, speed * abs(curveVal))
            else:
                motor.motor_control(straight_speed, straight_speed)
        else:
            motor.motor_control(0,0)

        print(curveVal,left_pixel,right_pixel)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    motor.motor_control(0,0)
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()




