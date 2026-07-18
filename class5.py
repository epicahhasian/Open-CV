import cv2 
import numpy as np
eyes = cv2.imread("eyes.jpg",1)
blobs = cv2.imread("blobs.jpg",0)
#circle detector



greyscaleeyes = cv2.cvtColor(eyes,cv2.COLOR_BGR2GRAY)
greyscaleblur= cv2.blur(greyscaleeyes,(3,3))

detect = cv2.HoughCircles(greyscaleblur,cv2.HOUGH_GRADIENT,1,20,param1 = 50,param2=30,minRadius=1,maxRadius = 40)
if detect is not None:
    detect = np.uint16(np.around(detect))
    for i in detect[0,:]:
        x,y,r = i[0],i[1],i[2]
        cv2.circle(eyes,(x,y),r,(0,0,255),10)
        cv2.circle(eyes,(x,y),1,(255,0,0),5)
        cv2.imshow("circle detector",eyes)
        cv2.waitKey()
        cv2.destroyAllWindows()




#blobs

detection = cv2.SimpleBlobDetector_Params()
detection.filterByArea = True 
detection.minArea = 100
detection.filterByCircularity = True 
detection.minCircularity = 0.9 
detection.filterByConvexity = True 
detection.minConvexity = 0.2 
detection.filterByInertia = True 
detection.minInertiaRatio = 0.01
detector = cv2.SimpleBlobDetector_create(detection)
detecttheblobs = detector.detect(blobs)
imgstuff = np.zeros((1,1))
draw= cv2.drawKeypoints(blobs,detecttheblobs,imgstuff,(255,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
count = len(detecttheblobs)
text = "Number of circular blobs:" +str(count)
cv2.putText(draw,text,(50,150),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),20)
cv2.imshow("blob detector",draw)
cv2.waitKey()