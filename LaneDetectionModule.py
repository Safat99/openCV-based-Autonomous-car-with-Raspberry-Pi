import numpy as np
import cv2
import utils



def getLaneCurve(img):
	
	imgThresh = utils.thresholding(img)
	cv2.imshow('Threshold', imgThresh)
	
	return None



if __name__ == '__main__':
	cap = cv2.VideoCapture(0)	
	while True:
		_, img = cap.read()
		img = cv2.resize(img, (640,480))
		getLaneCurve(img)
		
		cv2.imshow('frame', img)
		k = cv2.waitKey(1) & 0xFF
		if k == ord('q'):
			break
	
	cv2.destroyAllWindows()
	cap.release()
		
