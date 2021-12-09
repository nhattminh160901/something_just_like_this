from frontprogram import *
import time
import pickle as pk
fp = FrontProgram()
print("READ FILE FROM FOLDER")
while True:
    print("1. Students List")
    print("2. Youth Union Member List")
    print("3. Lecturer List")
    print("3. Lecturer List")
    print("4. Information All Class")
    print("5. Students List with Points and Rank")
    print("6. Sorted List")
    print("7. Exit Program")
    choose = input("Enter your choose: ")
    choose = fp.check(choose)
    if choose == 1:
        fileName = input("File Name read: ")
        fileName = fileName + ".pickle"
        with open(fileName, "rb") as f:
            listStudent = pk.load(f)
        print("ALL TASKS")
        while True:
            print("1. Show students list")
            print("2. Find student by Full Name")
            print("3. Find student by Class")
            print("4. Exit")
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
                break
    if choose == 2:
        fileName = input("File Name read: ")
        fileName = fileName + ".pickle"
        with open(fileName, "rb") as f:
            listYUM = pk.load(f)
        print("ALL TASK")
        while True:
            print("1. Show Youth Union members list")
            print("2. Exit")
            option = input("Enter your choose: ")
            option = fp.check(option)
            if option == 1:
                for i in listYUM:
                    print(i)
            if option == 2:
                break
    if choose == 2:
        pass


print("ALL FIND TASKS")
while True:
    print("1. Find student by Full Name")
    print("2. Find student by Class")
    print("3. Find student by Rank")
    choose = input("Enter your choose: ")
    choose = fp.check(choose)
    if choose == 1:
        fp.findStudentbyFullName(listStudentPointsandRank)
        time.sleep(5)
    if choose == 2:
        fp.findStudentbyClass(listStudentPointsandRank)
        time.sleep(5)
    if choose == 3:
        fp.findStudentbyRank(listStudentPointsandRank)
        time.sleep(5)