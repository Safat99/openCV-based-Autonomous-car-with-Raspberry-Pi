import cv2
 
cap = cv2.VideoCapture(0)
 
def getImg(display= False,size=[640,480]):
    _, img = cap.read()
    img = cv2.flip(img,0)
    img = cv2.resize(img,(size[0],size[1]))
    if display:
        cv2.imshow('IMG',img)
    return img
 
if __name__ == '__main__':
    while True:
        img = getImg(True)#if I wanna display
       	
       	if cv2.waitKey(1) & 0xFF == ord('q'):
       		break
   
    cv2.destroyAllWindows()
    cap.release() 
