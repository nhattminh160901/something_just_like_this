from manage import *

class FrontProgram:
    def check(self, n):
        try:
            n = int(n)
        except ValueError:
            print("No valid integer! Please try again")
        return n

    def checkFloat(self, n):
        try:
            n = float(n)
        except ValueError:
            print("No valid float! Please try again")
        return n

    def inputStudentAndCourse(self):
        mng = ManagementAll()
        fN = input("First Name: ")
        lN = input("Last Name: ")
        while True:
            age = input("Age: ")
            age = FrontProgram().check(age)
            if type(age) == int:
                break
        sex = input("Sex: ")
        phone = input("Phone Number: ")
        phone = phone.replace("0", "+84", 1)
        email = input("Email: ")
        sN = input("Student Number: ")
        sv = mng.inputStudent(fN, lN, age, sex, phone, email, sN)
        print("Course Type\n1. Engineer\n2. Bachelor")
        while True:
            coursetype = input("Input Course Type: ")
            coursetype = FrontProgram().check(coursetype)
            if coursetype == 1 or coursetype == 2:
                break
        specName = input("Input your Specialization: ")
        listTerms = []
        listCredits = []
        while True:
            term = input("Input Term Name: ")
            listTerms.append(term)
            credit = input("Number of Credits of Term: ")
            listCredits.append(credit)
            print("Do you want continue?\n1. Continue\n2. End")
            anotherChoose = input("Your choose: ")
            anotherChoose = FrontProgram().check(anotherChoose)
            if anotherChoose == 2:
                break
            elif anotherChoose != 1:
                anotherChoose = input("Your choose: ")
                anotherChoose = FrontProgram().check(anotherChoose)
        course = mng.inputCourse(coursetype, specName, listTerms, listCredits)
        return sv, course

    def addStudentToList(self, informationStudent:tuple, listStudent:list):
        mng = ManagementAll()
        mng.addStudenttoList(informationStudent[0], informationStudent[1], listStudent)
        return listStudent

    def manageYUM(self, informationStudent:tuple, managerYUM:list):
        mng = ManagementAll()
        print("Are you a Youth Union member?")
        while True:
            check = input("Your answer(Y/N): ")
            if check in "Yy":
                managerYUM.append(mng.addYUMList(True, informationStudent[0]))
                break
            elif check in "Nn":
                managerYUM.append(mng.addYUMList(False, informationStudent[0]))
                break
            else:
                print("Wrong answer")
        return managerYUM

    def addStudentToClassLecturer(self, listStudent:list, allClass:dict, listLecturer:list):
        mng = ManagementAll()
        fN = input("First Name: ")
        lN = input("Last Name: ")
        while True:
            age = input("Age: ")
            age = FrontProgram().check(age)
            if type(age) == int:
                break
        sex = input("Sex: ")
        phone = input("Phone Number: ")
        phone = phone.replace("0", "+84", 1)
        email = input("Email: ")
        dT = input("Degree Type: ")
        major = input("Major: ")
        tN = input("Term Name Teaching: ")
        lec = mng.inputLecturer(fN, lN, age, sex, phone, email, dT, major, tN)
        print(lec.getInformationLecturer())
        listLecturer.append(lec.getInformationLecturer())
        allClass[lec.getFullName()+(lec.getClassName(),)] = mng.addStudentToClass(lec, listStudent)
        return allClass and listLecturer

    def addPointsAndRanks(self, listStudent:list):
        find = 0
        check = 0
        mng = ManagementAll()
        fN = input("First Name: ")
        lN = input("Last Name: ")
        sN = input("Student Number: ")
        for i in listStudent:
            if lN == i[0] and fN == i[1] and sN == i[6]:
                pP = input("Process Point: ")
                pP = FrontProgram().checkFloat(pP)       
                eP = input("Exam Point: ")
                eP = FrontProgram().checkFloat(eP)
                tP = input("Traning Point: ")
                tP = FrontProgram().check(tP)
                listStudent[find] = i + (mng.getGPA(pP, eP), tP, mng.getRank(pP, eP, tP))
                check += 1
            find += 1
        if check == 0:
            print("Student Information is not found")
        return listStudent

    def findStudentbyFullName(self, listStudent:list):
        mng = ManagementAll()
        fN = input("First Name: ")
        lN = input("Last Name: ")
        mng.findByFullName(fN, lN, listStudent)

    def findStudentbyClass(self, listStudent:list):
        mng = ManagementAll()
        cN = input("Class Name: ")
        mng.findByClass(listStudent, cN)

    def findStudentbySex(self, listStudent:list):
        mng = ManagementAll()
        print("1. Male\n2. Female")
        choose = input("Your choose: ")
        choose = FrontProgram().check(choose)
        if choose == 1:
            mng.findBySex(listStudent, "Male")
        if choose == 2:
            mng.findBySex(listStudent, "Female")

    def findStudentbyRank(self, listStudent:list):
        mng = ManagementAll()
        print("1. Very Good\n2. Good\n3. Average\n4. Weak\n5. Poor")
        choose = input("Your choose: ")
        choose = FrontProgram().check(choose)
        if choose == 1:
            mng.findByRank(listStudent, "Very Good")
        if choose == 2:
            mng.findByRank(listStudent, "Good")
        if choose == 3:
            mng.findByRank(listStudent, "Average")
        if choose == 4:
            mng.findByRank(listStudent, "Weak")
        if choose == 5:
            mng.findByRank(listStudent, "Poor")
    
    def sortStudentsList(self, listStudent):
        mng = ManagementAll()
        print("Choose condition to sort: ")
        print("1. Sort by First Name\n2. Sort by GPA\n3. Sort by Training Point")
        choose = input("Your choose: ")
        choose = FrontProgram().check(choose)
        if choose == 1:
            print("1. Ascending\n2. Descending")
            option = input("Your choose: ")
            option = FrontProgram().check(option)
            if option == 1:
                optioN = False
                studentSort = mng.sortList(listStudent, 1, optioN)
            elif option == 2:
                optioN = True
                studentSort = mng.sortList(listStudent, 1, optioN)
        if choose == 2:
            print("1. Ascending\n2. Descending")
            option = input("Your choose: ")
            option = FrontProgram().check(option)
            if option == 1:
                optioN = False
                studentSort = mng.sortList(listStudent, 10, optioN)
            elif option == 2:
                optioN = True
                studentSort = mng.sortList(listStudent, 10, optioN)
        if choose == 3:
            print("1. Ascending\n2. Descending")
            option = input("Your choose: ")
            option = FrontProgram().check(option)
            if option == 1:
                optioN = False
                studentSort = mng.sortList(listStudent, 11, optioN)
            elif option == 2:
                optioN = True
                studentSort = mng.sortList(listStudent, 11, optioN)
        return studentSort