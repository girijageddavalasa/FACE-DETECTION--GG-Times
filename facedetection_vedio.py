import cv2
alg="haarcascade_frontalface_default.xml"
haar_cascade=cv2.CascadeClassifier(alg) #load algorthim
image="song.mp4"
cam=cv2.VideoCapture(image)
while True:
    _,img=cam.read()
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_coord=haar_cascade.detectMultiScale(grayimg,1.3,10)
    for (x,y,w,h) in face_coord:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    if len(face_coord)==0:
        text="face not detected"
    else:
        text="face detected"
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(10,150,20),2)
    cv2.imshow("FACE DETECTION",img)
    key=cv2.waitKey(10)
    if key==27:
        break
cam.release()
cv2.destroyAllWindows()
            
