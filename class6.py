import cv2 
import os 
from  PIL import Image 

os. chdir("C:\\Users\\amnah\\OneDrive\\Desktop\\New folder (9)")
path = "C:\\Users\\amnah\\OneDrive\\Desktop\\New folder (9)"
mean_height= 0 
mean_width = 0 

numofimg = len(os.listdir("."))
for i in os.listdir("."):
    img = Image.open(os.path.join(path,i))
    width,height= img.size
    mean_width += width 
    mean_height += height 


mean_width = mean_width//numofimg
mean_height = mean_height//numofimg

for i in os.listdir("."):
    if i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png"):
        img = Image.open (os.path.join(path,i))
        width,height = img.size 
        imgresize = img.resize ((mean_width,mean_height),Image.LANCZOS)
        imgresize.save(i,"jpg",quality = 95)


def createvideo():
    videoname = "Golden era"
    os.chdir("C:\\Users\\amnah\\OneDrive\\Desktop\\New folder (9)")
    images = []
    for i in os.listdir("."):
        if i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png"):
            images.append(i)

    frame = cv2.imread(os.path.join(".",images[[0]]))
    height,width,layers = frame.shape 
    video=cv2.VideoWriter(videoname,0,1,(width,height))
    for i in images:
        video.write(cv2.imread(os.path.join(".",i)))
    cv2.destroyAllWindows()
    video.release()


createvideo()