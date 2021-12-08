from frontprogram import *

fp = FrontProgram()
listStudent = []
informationClass = {}
print("Manage Student")
print("1. Information Student Input")
print("2. Add Student List (Used after each Student Information Input)")
print("3. Check and add Student to Youth Union")
print("4. Add Student List to Class of Lecturer (Used when the student list is complete)")

while True:
    choose = input("Enter your choose: ")
    choose = fp.check(choose)
    if choose == 1:
        informationStudent = fp.inputStudentAndCourse()
    elif choose == 2:
        try:
            fp.addStudentToList(informationStudent, listStudent)
        except NameError:
            print("Please enter Information Student before use this choose")
    elif choose == 3:
        pass
    elif choose == 4:
        break
print(listStudent)