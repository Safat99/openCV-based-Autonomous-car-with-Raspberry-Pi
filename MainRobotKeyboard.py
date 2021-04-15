from motormodule import Motor
import keyboardmodule as kp
import WebcamModule


motor = Motor(4,17,27,22,10,9)
kp.init()

def main(display=False):
	
	if display==True:
		img = WebcamModule.getImg(True)
	
	if kp.getKey('UP'):
		motor.motor_control(50,50)
	elif kp.getKey('DOWN'):
		motor.motor_control(-50,-50)
	elif kp.getKey('LEFT'):
		motor.motor_control(30,-30)
	elif kp.getKey('RIGHT'):
		motor.motor_control(-30,30)
	else:
		motor.motor_control(0,0)


if __name__ == '__main__':
	while True:
		main()	
