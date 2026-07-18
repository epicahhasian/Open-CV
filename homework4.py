import cv2 

background = cv2.imread("blue.jpg",1)



base = cv2.rectangle(background,(50,50),(150,300),(0,0,0),-1)


red = cv2.circle(base,(100,100),40,(0,0,255),-1)
yellow = cv2.circle(base,(100,170),40,(0,255,255),-1)
green = cv2.circle(base,(100,250),40,(0,255,0),-1)

cv2.imshow("trafficlight",base)
cv2.waitKey()
