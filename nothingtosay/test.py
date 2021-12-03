import cv2
import numpy as np
import time

face_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
cap = cv2.VideoCapture(0)
i = 0
while True:
    ret, frame = cap.read()  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        i += 1
    cv2.imshow("Detecting face", frame)
    print(i)
    i = 0
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()