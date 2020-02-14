import numpy as np
import cv2
body_cascade=cv2.CascadeClassifier("myhaar.xml")
cap = cv2.VideoCapture(0)
while (True):
    #capture frame by frame
    ret, frame=cap.read()
    frame = cv2.resize(frame, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_LINEAR)
    #print(ret)
    #print(frame)
    #operations from frame
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
    bodies = body_cascade.detectMultiScale(gray, 1.2, 3)
    str1="body"
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.imshow('body', frame)
        cv2.putText(frame,str1,(x,y),cv2.FONT_ITALIC,1,(255,0,255),2,cv2.LINE_AA)
        
   
    #display the resulting frame
    cv2.imshow('frame', gray)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
#release capture
cap.release()
cv2.destroyAllWindows()
