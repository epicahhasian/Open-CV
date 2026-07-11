import cv2 


#add line through image
pikachu1 = cv2.imread("pikachu.png",1)
pikachuline = cv2.line(pikachu1,(0,0),(300,300),(255,0,0),5)
cv2.imshow("line",pikachuline)
cv2.waitKey()
cv2.destroyAllWindows()




#add rectangle through image
pikachu2 = cv2.imread("pikachu.png",1)
pikachurectangle = cv2.rectangle(pikachu2,(0,0),(300,300),(0,255,0),10)
cv2.imshow("rectangle",pikachurectangle)
cv2.waitKey()








#rectangle filled
pikachurectangle2 = cv2.rectangle(pikachu2,(0,0),(300,300),(0,255,0),-1)
cv2.imshow("rectanglefilled",pikachurectangle2)
cv2.waitKey()


#circle
pikachu3 = cv2.imread("pikachu.png",1)
pikachucircle = cv2.circle(pikachu3,(150,150),100,(0,0,255),10)
cv2.imshow("circle",pikachucircle)
cv2.waitKey()


#circle filled
pikachucircle2 = cv2.circle(pikachu3,(150,150),100,(0,0,255),-1)
cv2.imshow("circlefilled",pikachucircle2)
cv2.waitKey()

#text 
pikachu4= cv2.imread("pikachu.png",1)
text=cv2.putText(pikachu4,"hello im pikachu",(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),10)
cv2.imshow("text",text)
cv2.waitKey()