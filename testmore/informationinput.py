from frontprogram import *
import time
import pickle as pk

fp = FrontProgram()
listStudent = []
listYUM = []
listLecturer = []
informationAllClass = {}
cd = 0

print("MANAGE STUDENT")
while True:
    print("1. Information Student Input")
    print("2. Add Information Student to Students List (Used after each Student Information Input)")
    print("3. Show list of students")
    print("4. Add Students List to Class of Lecturer (Used when the student list is complete)")
    print("5. Save Student List")
    print("6. Save Youth Union Member List")
    print("7. Save Lecturer List")
    print("8. Save Information All Class")
    print("9. Show information of Class")
    print("10. Finish the process of entering Information Students")
    choose = input("Enter your choose: ")
    choose = fp.check(choose)
    if choose == 1:
        informationStudent = fp.inputStudentAndCourse()
        fp.manageYUM(informationStudent, listYUM)
        cd += 1
        time.sleep(2)
    elif choose == 2:
        try:
            fp.addStudentToList(informationStudent, listStudent)
        except NameError:
            print("Please enter Information Student before use this")
        time.sleep(2)
    elif choose == 3:
        for i in listStudent:
            print(i)
        time.sleep(2)
    elif choose == 4:
        if cd == 0:
            print("Student list is empty")
            time.sleep(2)
        else:
            fp.addStudentToClassLecturer(listStudent, informationAllClass, listLecturer)
            time.sleep(2)
    elif choose == 5:
        fileName = input("File Name: ")
        with open(fileName+".pickle", "wb") as f:
            save = pk.dump(listStudent, f)
            f.close()
    elif choose == 6:
        fileName = input("File Name: ")
        with open(fileName+".pickle", "wb") as f:
            save = pk.dump(listYUM, f)
            f.close()
    elif choose == 7:
        fileName = input("File Name: ")
        with open(fileName+".pickle", "wb") as f:
            save = pk.dump(listLecturer, f)
            f.close()
    elif choose == 8:
        fileName = input("File Name: ")
        with open(fileName+".pickle", "wb") as f:
            save = pk.dump(informationAllClass, f)
            f.close()
    elif choose == 9:
        for i in informationAllClass:
            print(f"{i}:", informationAllClass[i])
        time.sleep(2)
    elif choose == 10:
        print("Finish the process of entering information!")
        listStudentPointsandRank = listStudent
        time.sleep(2)
        break

print("ENTER POINTS, RANK STUDENT AND SORT STUDENTS LIST")
while True:
    print("1. Show student list")
    print("2. Enter points and rank Student")
    print("3. Save students list with points and rank")
    print("4. Sort students list based on condition and Save")
    print("5. Show sorted list")
    print("6. Exit program")
    choose = input("Enter your choose: ")
    choose = fp.check(choose)
    if choose == 1:
        for i in listStudentPointsandRank:
            print(i)
    elif choose == 2:
        fp.addPointsAndRanks(listStudentPointsandRank)
        time.sleep(2)
    elif choose == 3:
        fileName = input("File Name: ")
        with open(fileName+".pickle", "wb") as f:
            save = pk.dump(listStudentPointsandRank, f)
            f.close()
    elif choose == 4:
        sortedList = fp.sortStudentsList(listStudentPointsandRank)
        while True:
            option = input("Do you want to save?(Y/N): ")
            if option in "Yy":
                fileName = input("File Name: ")
                with open(fileName+".pickle", "wb") as f:
                    save = pk.dump(sortedList, f)
                    f.close()
                    break
            elif option in "Nn":
                break
    elif choose == 5:
        for i in sortedList:
            print(i)
    elif choose == 6:
        break