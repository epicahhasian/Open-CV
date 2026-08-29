import cv2 
import os 

file = "haarcascade_frontalface_default.xml"
dataset = "dataset"
subdata = "Human"
path = os.path.join(dataset,subdata)
if not os.path.isdir(path):
    os.mkdir(path)

(width,height) = (130,100)
face = cv2.CascadeClassifier(file)
webcam = cv2.VideoCapture(0)
count = 1 
while count <30: 
    (_,image) = webcam.read()
    grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale (grey,1.3,4)
    for (x,y,w,h) in faces: 
        cv2.rectangle (image,(x,y),(x+w,y+h),(00,00,255),5)
        f = grey[y:y+h,x:x+w]
        faceresize = cv2.resize(f,(width,height))
        cv2.imwrite("% s/%s.png"%(path,count),faceresize)
    count +=1
    cv2.imshow("Face Recognition",image)
    e = cv2.waitKey()
    if e == 27:
        break