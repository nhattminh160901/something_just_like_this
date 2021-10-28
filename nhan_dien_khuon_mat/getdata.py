import cv2
import numpy as np
import sqlite3
import os

def insert0rUpdate(id, name):
    conn = sqlite3.connect('Data.db')
    query = "Select * from People WHERE ID= "+str(id)
    cursor = conn.execute(query)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if(isRecordExist == 0):
        query = "INSERT INTO People(ID, Name, Age) VALUES("+str(id)+","+str(name)+")"
    else:
        query = "UPDATE People SET Name ="+str(name)+"Where ID ="+str(id)

    conn.execute(query)
    conn.commit()
    conn.close()

id = input("ID: ")
name = input("Name: ")
insert0rUpdate(id, name)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
sampleNum = 0
cap = cv2.VideoCapture(0)

while True:
    #ghi hình
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        sampleNum +=1

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if not os.path.exists('dataSet'):
            os.makedirs('dataSet')

        cv2.imwrite("dataSet/vippro."+str(id)+"."+str(sampleNum)+ ".jpg", gray[y:y+h,x:x+w])

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if sampleNum>1000:
        break

cap.release()
cv2.destroyAllWindows