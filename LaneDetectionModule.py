import numpy as np
import cv2
import utils

curveList = []
avrgVal = 10

def getLaneCurve(img,display=2):
	#sent an image and get the value of curve
	imgCopy = img.copy()
	imgResult = img.copy()
	######step 1
	imgThresh = utils.thresholding(img)
	
	######step 2
	hT, wT, c = img.shape	
	#for points we need trackbar
	points = utils.valTrackbars()
	imgWarp = utils.warpImg(imgThresh, points, wT,hT)
	imgWarpPoints = utils.drawPoints(imgCopy,points)


	#############step 3
	middlePoint, imgHist = utils.getHistogram(imgWarp,display=True,minPer=0.5,region=4)
	curveAveragePoint, imgHist = utils.getHistogram(imgWarp,display=True,minPer=0.9)
	#print(basePoint - midPoint)
	curveRaw = curveAveragePoint - middlePoint


	##########step 4 (avrg)
	#avrging because want to smooth transition>> noise reduce happens
	curveList.append(curveRaw)
	if len(curveList) > avrgVal:
		curveList.pop(0) # maane koyta niye avrg korbo otar beshi batch hoye gele frst er ta baad diye dibe
	curve = int(sum(curveList)/len(curveList))
	
	
	#####Step 5  Display
	if display != 0:
		   imgInvWarp = utils.warpImg(imgWarp, points, wT, hT,inv = True)
		   imgInvWarp = cv2.cvtColor(imgInvWarp,cv2.COLOR_GRAY2BGR)
		   imgInvWarp[0:hT//3,0:wT] = 0,0,0
		   imgLaneColor = np.zeros_like(img)
		   imgLaneColor[:] = 0, 255, 0
		   imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
		   imgResult = cv2.addWeighted(imgResult,1,imgLaneColor,1,0)
		   midY = 450
		   cv2.putText(imgResult,str(curve),(wT//2-80,85),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),3)
		   cv2.line(imgResult,(wT//2,midY),(wT//2+(curve*3),midY),(255,0,255),5)
		   cv2.line(imgResult, ((wT // 2 + (curve * 3)), midY-25), (wT // 2 + (curve * 3), midY+25), (0, 255, 0), 5)
		   for x in range(-30, 30):
		       w = wT // 20
		       cv2.line(imgResult, (w * x + int(curve//50 ), midY-10),
		                (w * x + int(curve//50 ), midY+10), (0, 0, 255), 2)
		   #fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
		   #cv2.putText(imgResult, 'FPS '+str(int(fps)), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (230,50,50), 3);
	if display == 2:
		imgStacked = utils.stackImages(0.7,([img,imgWarpPoints,imgWarp],
			[imgHist,imgLaneColor,imgResult]))
		cv2.imshow('ImageStack',imgStacked)
   
	elif display == 1:
		cv2.imshow('Result',imgResult)
		
	#normalization
	curve = curve / 100
	if curve >1: curve =1
	if curve <-1: curve =-1
	
	'''
	cv2.imshow('Threshold', imgThresh)
	cv2.imshow('Warp', imgWarp)
	cv2.imshow('Warp Points', imgWarpPoints)
	cv2.imshow('Histogram', imgHist)
	'''
	return curve


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
		curve = getLaneCurve(img,display=1)
		print(curve)
		cv2.imshow('frame', img)
		k = cv2.waitKey(1) & 0xFF
		if k == ord('q'):
			break
	
	cv2.destroyAllWindows()
	cap.release()
		
