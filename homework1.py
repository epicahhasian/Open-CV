import cv2 
import os 

neymarjr = cv2.imread("neymar.png",1)
cv2.imshow("original",neymarjr)
cv2.waitKey(0)
cv2.destroyAllWindows()

neymarjr2 = cv2.imread("neymar.png",2)
cv2.imshow("greyscale",neymarjr2)
cv2.waitKey(0)

neymarjr2 = cv2.imread("neymar.png",2)
cv2.imshow("black&white",neymarjr2)
cv2.waitKey(0)



saveimg = "c:/Users/amnah/OneDrive/Desktop/Jetlearn/Open CV"
import os 
os.chdir(saveimg)
cv2.imwrite("greyscale.png",neymarjr2)





import cv2
neymarjroriginal = cv2.imread("neymar.png",1)
b,g,r =cv2.split(neymarjroriginal)

cv2.imshow("blue saturated",b)
cv2.waitKey(0)
cv2.imshow("green saturated",g)
cv2.waitKey(0)
cv2.imshow("red saturated",r)
cv2.waitKey(0)