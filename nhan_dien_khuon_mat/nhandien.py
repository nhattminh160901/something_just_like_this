import cv2
import numpy as np
import sqlite3
import os

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizer/trainingdata.yml")

def getProfile(id):
    conn = sqlite3.connect('Data.db')
    query = "Select * from People WHERE ID="+str(id)
    cursor = conn.execute(query)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile

cap =cv2.VideoCapture(0)

fontface = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        rgray = gray[y:y+h, x:x+w]
        id, confidence = recognizer.predict(rgray)
        if confidence < 40:
            profile = getProfile(id)

            if profile != None:
                cv2.putText(frame, "Name: " + str(profile[1]), (x+10, y+h+30), fontface, 1, (0, 255, 0), 2)
                
        else:
            cv2.putText(frame, "Unknown", (x+10, y+h+30), fontface, 1, (0, 255, 0), 2)
    cv2.imshow('vippro', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows