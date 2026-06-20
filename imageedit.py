import cv2 


imageread = cv2.imread("pikachu.png",1)

cv2.imshow("original",imageread)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
imageread2 = cv2.imread("pikachu.png",0)
cv2.imshow("greyscale",imageread2)
cv2.waitKey(0)


saveimg = "c:/Users/amnah/OneDrive/Desktop/Jetlearn/Open CV"

import cv2
imageread2 = cv2.imread("pikachu.png",0)
cv2.imshow("black&white",imageread2)
cv2.waitKey(0)

import os 
os.chdir(saveimg)
cv2.imwrite("greyscale.png",imageread2)



import cv2 

imagereadoriginal = cv2.imread("pikachu.png",1)
b,g,r = cv2.split(imagereadoriginal)

cv2.imshow("blue saturated",b)
cv2.waitKey(0)

cv2.imshow("green saturated",g)
cv2.waitKey(0)

cv2.imshow("red saturated",r)
cv2.waitKey(0)