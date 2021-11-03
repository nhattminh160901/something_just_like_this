import cv2
import numpy as np
import os
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
path = 'data'

def getImagesWidthID(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
    facelessvoid = []
    IDs = []
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L')
        faceNp=np.array(faceImg, 'uint8')
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces=detector.detectMultiScale(faceNp)
        for (x,y,w,h) in faces:
            facelessvoid.append(faceNp[y:y+h,x:x+w])
            IDs.append(Id)
    return facelessvoid, IDs
        
faces, IDs = getImagesWidthID(path)
recognizer.train(faces, np.array(IDs))
if not os.path.exists('recognizer'):
    os.makedirs('recognizer')

recognizer.save('recognizer/training_data.yml')
cv2.destroyAllWindows()
