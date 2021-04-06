import numpy as np
import cv2

def thresholding(img):
	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	lowerwhite = np.array([0,0,0])
	upperwhite = np.array([179,255,255])
	maskwhite = cv2.inRange(imgHSV, lowerwhite, upperwhite)
	
	return maskwhite
