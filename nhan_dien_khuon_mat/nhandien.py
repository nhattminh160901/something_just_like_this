import cv2
import numpy as np
import sqlite3
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizer/training_data.yml")

def get_profile(id):
    conn = sqlite3.connect('Data.db')
    query = "Select * from People WHERE ID="+str(id)
    cursor = conn.execute(query)
    profile = None
    
    for row in cursor:
        profile = row
    conn.close()
    return profile

cap =cv2.VideoCapture(0)
font_face = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        r_gray = gray[y:y+h, x:x+w]
        id, confidence = recognizer.predict(r_gray)
        if confidence < 40:
            profile = get_profile(id)
            if profile != None:
                cv2.putText(frame, "Name: " + str(profile[1]), (x+10, y+h+30), font_face, 1, (0, 255, 0), 2)
                cv2.putText(frame, "Age: " + str(profile[2]), (x+10, y+h+60), font_face, 1, (0, 255, 0), 2)
                cv2.putText(frame, "MSSV: " + str(profile[3]), (x+10, y+h+90), font_face, 1, (0, 255, 0), 2)             
        else:
            cv2.putText(frame, "Unknown", (x+10, y+h+30), font_face, 1, (0, 255, 0), 2)
    cv2.imshow('nhan_dien', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows