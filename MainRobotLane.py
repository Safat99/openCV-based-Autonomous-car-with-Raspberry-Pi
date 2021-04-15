from motormodule import Motor
from LaneDetectionModule import getLaneCurve
import WebcamModule



motor = Motor(4,17,27,22,10,9)

Kp = 30

def main():
	
	img = WebcamModule.getImg()
	curveVal = getLaneCurve(img,1)
	
	#controlling like PID's P control>>>with Kp
	left_speed = 50 + Kp * curveVal
	right_speed = 50 - Kp * curveVal
	
	if left_speed > 75: left_speed = 75
	if left_speed < 25: left_speed = 25
	if right_speed > 75: right_speed =75
	if right_speed < 25: right_speed =25
	
	print(curveVal,left_speed, right_speed)
	motor.motor_control(left_speed, right_speed)
	
if __name__ == '__main__':
	while True:
		main()
	
