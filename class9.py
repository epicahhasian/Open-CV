import cv2 
import os 
import numpy as np 

file = "haarcascade_frontalface_default.xml"
datasets = "dataset"
print("Recognisng Face")

(images,labels,names,id)= ([],[],{},0)
for (subdirectory, directory,files) in os.walk(datasets):
    for subdirectory in directory:
        names[id]= subdirectory
        subjectpath = os.path.join(datasets,subdirectory)
        for filename in os.listdir(subjectpath):
            path=subjectpath+"\\"+filename
            label = id 
            images.append(cv2.imread(path,0))
            labels.append(int(label))
        id+= 1

(width,height)= (130,100)
(images,labels)=[np.array(l) for l in [images,labels]]
module=cv2.face.LBPHFaceRecognizer_create ()
module.train(images,labels)
facecascade = cv2.CascadeClassifier (file)
webcam = cv2.VideoCapture(0)
while True:
    (success,I) = webcam.read()
    grey = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(grey,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(I,(x,y),(x+w,y+h),(255,0,0),2)
        f = grey[y:y+h,x:x+w]
        faceresize =  cv2.resize (f,(width,height))
        prediction = module.predict(faceresize)
        cv2.rectangle(I,(x,y),(x+w,y+h),(255,150,0),3)
        if prediction [1] < 500:
            cv2.putText(I,"%s-%.0f"%(names[prediction[0]],prediction[1]),(x-10,y-10),cv2.FONT_HERSHEY_TRIPLEX,1,(0,0,255))
        else:
            cv2.putText(I,"Not Recognised",(x-10,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,150))
    cv2.imshow("Face Recognition",I)
    key = cv2.waitKey()
    if key== 27:
        break