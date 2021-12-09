from frontprogram import *
import time
import pickle as pk

def checkFileName(data):
    try:
        fileName = input("File Name read: ")
        fileName = fileName + ".pickle"
        with open(fileName, "rb") as f:
            data = pk.load(f)
    except FileNotFoundError:
        print("File not found: " + fileName)
    return data
    
def openData(data):
    while True:
        data = checkFileName(data)
        if data != None:
            break
    return data

fp = FrontProgram()
print("OPEN FILE DATA NAME")
print("Open Students List")
listStudent = None
listStudent = openData(listStudent)
print("Open Youth Union Member List")
listYUM = None
listYUM = openData(listYUM)
print("Open Lecturer List")
listLecturer = None
listLecturer = openData(listLecturer)
print("Open Information All Class")
informationAllClass = None
informationAllClass = openData(informationAllClass)
print("Open Students List with Points and Rank")
listStudentPointsandRank = None
listStudentPointsandRank = openData(listStudentPointsandRank)
print("Finish")
while True:
    print("1. Students List")
    print("2. Youth Union Member List")
    print("3. Lecturer List")
    print("4. Information All Class")
    print("5. Students List with Points and Rank")
    print("6. Sorted List")
    print("7. Exit Program")
    choose = input("Enter your choose: ")
    choose = fp.check(choose)
    if choose == 1:
        while True:
            print("1. Show students list")
            print("2. Find student by Full Name")
            print("3. Find student by Class")
            print("4. Find student by Sex")
            print("5. Exit")
            option = input("Enter your option: ")
            option = fp.check(option)
            if option == 1:
                for i in listStudent:
                    print(i)
            if option == 2:
                fp.findStudentbyFullName(listStudent)
                time.sleep(5)
            if option == 3:
                fp.findStudentbyClass(listStudent)
                time.sleep(5)
            if option == 4:
                fp.findStudentbySex(listStudent)
            if option == 5:
                break
    if choose == 2:
        while True:
            print("1. Show Youth Union members list")
            print("2. Exit")
            option = input("Enter your option: ")
            option = fp.check(option)
            if option == 1:
                for i in listYUM:
                    print(i)
            if option == 2:
                break
    if choose == 3:
        while True:
            print("1. Show lecturer list")
            print("2. Exit")
            option = input("Enter your option: ")
            option = fp.check(option)
            if option == 1:
                for i in listLecturer:
                    print(i)
            if option == 2:
                break
    if choose == 4:
        while True:
            print("1. Show information all class")
            print("2. Exit")
            option = input("Enter your option: ")
            option = fp.check(option)
            if option == 1:
                for i in listLecturer:
                    print(i)
            if option == 2:
                break
    if choose == 5:
        while True:
            print("1. Show students list")
            print("2. Find student by Full Name")
            print("3. Find student by Class")
            print("4. Find student by Sex")
            print("5. Find student by Rank")
            print("6. Exit")
            option = input("Enter your option: ")
            option = fp.check(option)
            if option == 1:
                for i in listStudentPointsandRank:
                    print(i)
            if option == 2:
                fp.findStudentbyFullName(listStudentPointsandRank)
                time.sleep(5)
            if option == 3:
                fp.findStudentbyClass(listStudentPointsandRank)
                time.sleep(5)
            if option == 4:
                fp.findStudentbySex(listStudentPointsandRank)
            if option == 5:
                fp.findStudentbyRank(listStudentPointsandRank)
            if option == 6:
                break
    if option == 6:
        print("1. Show students list sort by First Name")
        print("2. Show students list sort by GPA")
        print("3. Show students list sort by Training Point")
        print("4. Exit")
        option = input("Enter your option: ")
        option = fp.check(option)
        if option == 1 or option == 2 or option == 3:
            listSort = None
            listSort = openData(listSort)
        if option == 4:
            break
    if option == 7:
        break