import numpy as np
import cv2
import utils



def getLaneCurve(img):
	#sent an image and get the value of curve
	
	######step 1
	imgThresh = utils.thresholding(img)
	
	######step 2
	h, w, c = img.shape	
	#for points we need trackbar
	points = utils.valTrackbars()
	imgWarp = utils.warpImg(img, points, w,h)
	imgWarpPoints = utils.drawPoints(img,points)

	cv2.imshow('Threshold', imgThresh)
	cv2.imshow('Warp', imgWarp)
	cv2.imshow('Warp Points', imgWarpPoints)
	return None


if __name__ == '__main__':
	cap = cv2.VideoCapture('vid1.mp4')	
	intialTracbarVals = [102,80,20,214]
	utils.initalizeTrackbars(intialTracbarVals)
	frameCounter = 0
	
	while True:	
		frameCounter +=1
		if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
			cap.set(cv2.CAP_PROP_POS_FRAMES,0)
			frameCounter=0
		
		_, img = cap.read()
		img = cv2.resize(img,(480,240))
		getLaneCurve(img)
		
		cv2.imshow('frame', img)
		k = cv2.waitKey(1) & 0xFF
		if k == ord('q'):
			break
	
	cv2.destroyAllWindows()
	cap.release()
		
