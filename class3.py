import cv2
import os 


pikachu = cv2.imread("pikachu.png",1)
cv2.imshow("original",pikachu)
cv2.waitKey()
cv2.destroyAllWindows()


pikachugreyscale= cv2.cvtColor(pikachu,cv2.COLOR_BGR2GRAY)
cv2.imshow("greyscale",pikachugreyscale)
cv2.waitKey()


row,column= pikachu.shape[0:2]
for i in range(row):
    for j in range(column): 
        pikachu[i,j]= sum(pikachu[i,j])*0.33

cv2.imshow("greyscale without function",pikachu)
cv2.waitKey()



pikachu = cv2.imread("pikachu.png",1)
row,column = pikachu.shape[0:2]
matrix= cv2.getRotationMatrix2D((column/2,row/2),45,1)
rotation =cv2.warpAffine(pikachu,matrix,(column,row))

cv2.imshow("rotated",rotation)
cv2.waitKey()


edges=cv2.Canny(pikachu,100,200)
cv2.imshow("edge",edges)
cv2.waitKey()



hsvimg = cv2.cvtColor(pikachu,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",hsvimg)
cv2.waitKey()

