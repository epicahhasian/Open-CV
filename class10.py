import cv2 

carsvideo = cv2.VideoCapture("carsvid.mp4")
cascade = cv2.CascadeClassifier("cars.xml")

while True:
    success,frame = carsvideo.read()
    if not success:
        break
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars = cascade.detectMultiScale(grey,1.1,1)
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(00,00,255),3)

    cv2.imshow("Car Camera",frame)

    if cv2.waitKey(30) == 27:
        break 

cv2.destroyAllWindows()