import RPi.GPIO as pin
from time import sleep

pin.setmode(pin.BCM)
pin.setwarnings(False)

class Motor():
	
	def __init__(self,lft1,lft2,lft_pwm,rht1,rht2,rht_pwm):
		
		self.lft1 = lft1
		self.lft2 = lft2
		self.rht1 = rht1
		self.rht2 = rht2
		self.lft_pwm = lft_pwm
		self.rht_pwm = rht_pwm
		
		pin.setup(self.lft1, pin.OUT)
		pin.setup(self.lft2, pin.OUT)
		pin.setup(self.rht1, pin.OUT)
		pin.setup(self.rht2, pin.OUT)
		pin.setup(self.lft_pwm, pin.OUT)
		pin.setup(self.rht_pwm, pin.OUT)
		
		self.lft_pwm = pin.PWM(self.lft_pwm , 100)
		self.rht_pwm = pin.PWM(self.rht_pwm, 100)
		
		self.lft_pwm.start(0)
		self.rht_pwm.start(0)
		
	def motor_control(self, left_speed, right_speed):
		
		if left_speed > 0 :
			pin.output(self.lft1, pin.LOW)
			pin.output(self.lft2, pin.HIGH)
		else:
			pin.output(self.lft2, pin.LOW)
			pin.output(self.lft1, pin.HIGH)
		
		if right_speed > 0 :
			pin.output(self.rht1, pin.HIGH)
			pin.output(self.rht2, pin.LOW)
		else:
			pin.output(self.rht2, pin.HIGH)
			pin.output(self.rht1, pin.LOW)
		
		if left_speed > 100: left_speed =100
		if left_speed < -100: left_speed = -100
		if right_speed > 100: right_speed = 100
		if right_speed < -100: right_speed = -100
		
		self.lft_pwm.ChangeDutyCycle(abs(left_speed))
		self.rht_pwm.ChangeDutyCycle(abs(right_speed))
		
if __name__ == '__main__':
	motor = Motor(17,4,27,22,10,9)
	while True:
		motor.motor_control(50,50)
		sleep(10)
		motor.motor_control(-50,-50)
		sleep(10)
	
		
