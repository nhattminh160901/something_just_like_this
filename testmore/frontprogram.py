from manage import *

class FrontProgram:
    def check(self, n):
        try:
            n = int(n)
        except ValueError:
            print("No valid integer! Please try again ...")
        return n

    def inputStudentAndCourse(self):
        mng = ManagementAll()
        fN = input("First Name: ")
        lN = input("Last Name: ")
        age = int(input("Age: "))
        sex = input("Sex: ")
        phone = input("Phone Number: ")
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

    def addStudentToClassLecturer(self, inputLecturer, listStudent:list):
        pass