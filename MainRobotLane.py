from motormodule import Motor
from LaneDetectionModule import getLaneCurve
import WebcamModule



motor = Motor(10,22,9,4,17,27)

Kp = 20

def main():
	
	img = WebcamModule.getImg()
	curveVal = getLaneCurve(img,1)
	
	#controlling like PID's P control>>>with Kp
	left_speed = 20 + Kp * curveVal
	right_speed = 20 - Kp * curveVal
	
	if left_speed > 40: left_speed = 40
	if left_speed < 0: left_speed = 0
	if right_speed > 40: right_speed =40
	if right_speed < 0: right_speed =0
	
	print(curveVal,left_speed, right_speed)
	motor.motor_control(left_speed, right_speed)
	
if __name__ == '__main__':
	while True:
		main()
	
