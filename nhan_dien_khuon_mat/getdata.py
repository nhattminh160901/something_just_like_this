import cv2
import numpy as np
import sqlite3
import os

def insert0rUpdate(id, name, age, gender):
    conn = sqlite3.connect('C:\\test1\SQLiteStudio\data.db')
    query = "Select * from People Where ID= "+str(id)
    cursor = conn.execute(query)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    
    if(isRecordExist == 0):
        query = "Insert into People(ID, Name, Age, Gender) values("+str(id)+","+str(name)+","+str(age)+","+str(gender)+"')"
    else:
        query = "Update People set Name = '"+str(name)+"', Age = '"+str(age)+"', Gender = '"+str(gender)+"Where ID = "+str(id)

    conn.execute(query)
    conn.commit()
    conn.close()

id = input("ID: ")
name = input("Name: ")
age = input("Age: ")
gender = input("Gender: ")
insert0rUpdate(id, name, age, gender)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
sampleNum = 0
cap = cv2.VideoCapture(0)

while True:
    #ghi hình
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if not os.path.exists('dataSet'):
        os.makedirs('datSet')
    
    sampleNum +=1
    cv2.imwrite("dataSet/vippro."+str(id)+"."+str(sampleNum)+ ".jpg", gray[y:y+h,x:x+w])
    cv2.imshow
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows