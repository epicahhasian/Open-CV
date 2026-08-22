import cv2 
import numpy as np 
street = cv2.imread("busystreet.png",1)



greyscalestreet = cv2.cvtColor(street,cv2.COLOR_BGR2GRAY)
greyscalestreet2= cv2.blur(greyscalestreet,(3,3))

detect = cv2.HoughCircles(greyscalestreet,cv2.HOUGH_GRADIENT,1,20,param1 = 50,param2=30,minRadius=1,maxRadius = 40)
if detect is not None:
    detect = np.uint16(np.around(detect))
    for i in detect[0,:]:
        x,y,r = i[0],i[1],i[2]
        cv2.circle(street,(x,y),r,(0,0,255),10)
        cv2.circle(street,(x,y),1,(255,0,0),5)
        cv2.imshow("circle detector",street)
        cv2.waitKey()
        cv2.destroyAllWindows()
