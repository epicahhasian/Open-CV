import cv2 
import numpy as np 
import time 

print(cv2.__version__)

vid = cv2.VideoCapture("invisible.mp4")
count = 0 
background = 0 
for i in range(60):
    returnvalue,background = vid.read()
    if returnvalue == False:
        continue 

background = np.flip(background,axis=1)
while(vid.isOpened()):
    returnvalue,image = vid.read()
    if not returnvalue: 
        break
    count += 1 
    image = np.flip(image,axis=1)
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lowerread= np.array([100,40,40])
    upperread = np.array([100,255,255])
    mask1 = cv2.inRange(hsv,lowerread,upperread)
    lowerread = np.array([155,40,40])
    upperread = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lowerread,upperread)
    mask1 = mask1 + mask2

    mask1= cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations = 1)
    mask2 = cv2.bitwise_not(mask1)
    result1 = cv2.bitwise_and(background,background,mask= mask1)
    result2 = cv2.bitwise_and(image,image,mask = mask2)
    finaloutput = cv2.addWeighted(result1,1,result2,1,0)
    cv2.imshow("Invisible Man",finaloutput)
    k = cv2.waitKey()
    if k ==27:
        break
 
    
