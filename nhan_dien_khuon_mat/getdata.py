import cv2
import numpy as np
import sqlite3
import os

def insertor_update(id, name, age, mssv):
    conn = sqlite3.connect("Data.db")
    query = "Select * from People Where ID="+str(id)
    cursor = conn.execute(query)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if(isRecordExist == 0):
        query = "Insert into People(ID, Name, Age, MSSV) values("+str(id)+",'"+str(name)+"','"+str(age)+"','"+str(mssv)+"')"
    else:
        query = "Update People set Name ='"+str(name)+"', Age = '"+str(age)+"', MSSV = '"+str(mssv)+"' Where ID ="+str(id)
    conn.execute(query)
    conn.commit()
    conn.close()

id = input("ID: ")
name = input("Name: ")
age = input("Age: ")
mssv = input("MSSV: ")
insertor_update(id, name, age, mssv)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
sampleNum = 0
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        if not os.path.exists("data"):
            os.makedirs("data")
        sampleNum +=1
        cv2.imwrite("data/user."+id+"."+str(sampleNum)+ ".jpg", gray[y:y+h,x:x+w])
    cv2.imshow("getdata", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if sampleNum>200:
        break

cap.release()
cv2.destroyAllWindows()