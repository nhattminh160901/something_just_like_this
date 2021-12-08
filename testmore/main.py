from frontprogram import *
import time
import csv

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
        print(listStudent)
        time.sleep(2)
    elif choose == 4:
        if cd == 0:
            print("Student list is empty")
            time.sleep(2)
        else:
            fp.addStudentToClassLecturer(listStudent, informationAllClass, listLecturer)
            time.sleep(2)
    elif choose == 5:
        fileLSName = input("File Name: ")
        with open(fileLSName+".csv", "w", newline="") as f:
            save = csv.writer(f)
            save.writerow(["Last Name", "First Name", "Age", "Sex", "Phone", "Email", "Student Number"])
            for i in listStudent:
                save.writerow(i)
            f.close()
    elif choose == 6:
        fileYUMName = input("File Name: ")
        with open(fileYUMName+".csv", "w",  newline="") as f:
            save = csv.writer(f)
            save.writerow(["Last Name", "First Name", "Age", "Sex", "Phone", "Email", "Student Number", "Status Youth Union"])
            for i in listYUM:
                save.writerow(i)
            f.close()
    elif choose == 7:
        fileLLName = input("File Name: ")
        with open(fileLLName+".csv", "w",  newline="") as f:
            save = csv.writer(f)
            save.writerow(["Last Name", "First Name", "Age", "Sex", "Phone", "Email", "Degree Type", "Major", "Term Teaching"])
            for i in listLecturer:
                save.writerow(i)
            f.close()
    elif choose == 8:
        fileAICName = input("File Name: ")
        with open(fileAICName+".csv", "w",  newline="") as f:
            save = csv.DictWriter(f, informationAllClass.keys())
            save.writerow(informationAllClass)
            f.close()
    elif choose == 9:
        print(informationAllClass)
    elif choose == 10:
        print("Finish the process of entering information!")
        time.sleep(2)
        break

print("ALL TASKS")
while True:
    print("1. Enter points and rank Student")
    choose = input("Enter your choose: ")
    choose = fp.check(choose)
    if choose == 1:
        fp.addPointsAndRanks(listStudent)
        time.sleep(2)
    if choose == 2:
        break