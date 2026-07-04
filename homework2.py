import cv2
import os


greenimg = cv2.imread("green.jpg",1)
blueimg = cv2.imread("blue.jpg",1)


weighted1 = cv2.addWeighted(blueimg,0.7,greenimg,0.3,1)
cv2.imshow("0.7+0.3",weighted1)
cv2.waitKey()
cv2.destroyAllWindows()

weighted2 = cv2.addWeighted(blueimg,0.6,greenimg,0.4,1)
cv2.imshow("0.6+0.4",weighted2)
cv2.waitKey()


weighted3 = cv2.addWeighted(blueimg,0.8,greenimg,0.2,1)
cv2.imshow("0.8+0.2",weighted3)
cv2.waitKey()



weighted4 = cv2.addWeighted(blueimg,0.5,greenimg,0.5,1)
cv2.imshow("0.5+0.5",weighted4)
cv2.waitKey()




