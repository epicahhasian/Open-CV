import cv2
neymar = cv2.imread("neymar.png",1)
cv2.imshow("best dribbler bro",neymar)
cv2.waitKey()
cv2.destroyAllWindows()

neymargrey= cv2.cvtColor(neymar,cv2.COLOR_BGR2GRAY)
cv2.imshow("neymar greyscale",neymargrey)
cv2.waitKey()

neymar2 = cv2.imread("neymar.png",1)
row,column = neymar2.shape[0:2]
matrix= cv2.getRotationMatrix2D((column/2,row/2),45,1)
rotation =cv2.warpAffine(neymar2,matrix,(column,row))
cv2.imshow("neymar rotated",rotation)
cv2.waitKey()


edges = cv2.Canny(neymar,100,200)
cv2.imshow("edges",edges)
cv2.waitKey()

hsv = cv2.cvtColor(neymar,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",hsv)
cv2.waitKey()