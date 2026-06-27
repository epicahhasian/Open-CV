import cv2 
import numpy 




#weighted image (adding 2 images)


blueread = cv2.imread("blue.jpg",1)
cv2.imshow("blue",blueread)
cv2.waitKey(0)
greenread = cv2.imread("green.jpg",1)
cv2.imshow("green",greenread)
cv2.waitKey(0)

weight = cv2.addWeighted(blueread,0.5,greenread,0.5,0.5)

cv2.imshow("blue+green",weight)
cv2.waitKey(0)
cv2.destroyAllWindows()





#subtract images


minusimage = cv2.subtract(blueread,greenread)
cv2.imshow("blue - green",minusimage)
cv2.waitKey(0)


#resize image

pika = cv2.imread("pikachu.png",1)
cv2.imshow("original",pika)
cv2.waitKey(0)

img = cv2.resize(pika,(1920,1080))
cv2.imshow("resizedimg",img)
cv2.waitKey(0)



#eroded image


array1 = numpy.ones((5,5),numpy.uint8)

imgerode = cv2.erode(pika,array1)
cv2.imshow("eroded",imgerode)
cv2.waitKey(0)


#blur image (3 types)


gaussian = cv2.GaussianBlur(pika,(7,7),0)
cv2.imshow("guassianblur",gaussian)
cv2.waitKey(0)


median = cv2.medianBlur(pika,(7),0)
cv2.imshow("medianblur",median)
cv2.waitKey(0)


bilateral = cv2.bilateralFilter(pika,(7),sigmaColor = 70,sigmaSpace=70)
cv2.imshow("bilateralblur",bilateral)
cv2.waitKey(0)



#image with border

border = cv2.copyMakeBorder(pika,10,10,10,10,cv2.BORDER_CONSTANT)
cv2.imshow("imagewithborder",border)
cv2.waitKey(0)


#reflected/mirror image 


mirror = cv2.copyMakeBorder(pika,20,20,20,20,cv2.BORDER_REFLECT)
cv2.imshow("reflected/mirror image",mirror)
cv2.waitKey(0)