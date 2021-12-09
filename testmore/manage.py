from dataclass import *

class ManagementAll:
    def inputStudent(self, firstName:str, lastName:str, age:int, sex:str, phoneNumber:str, email:str, studentNumber:str):
        st = Student(firstName, lastName, age, sex, phoneNumber, email, studentNumber)
        return st

    def inputCourse(self, courseType:int, specializationName:str, ternName:list, credits:list):
        course = Course(courseType)
        term = Terms(specializationName, course, ternName, credits)
        return term
    
    def inputLecturer(self, firstName:str, lastName:str, age:int, sex:str, phoneNumber:str, email:str, degreeType:str, major:str, classTerm:str):
        lec = Lecturer(firstName, lastName, age, sex, phoneNumber, email, degreeType, major, classTerm)
        return lec

    def addStudenttoList(self, inputStudent, inputCourse, listStudent:list):
        listStudent.append(inputStudent.informationStudentCourse(inputCourse))
        return listStudent

    def addStudentToClass(self, inputLecturer, listStudent:list):
        return inputLecturer.memberClass(listStudent)

    def getGPA(self, processPoint:float=0.0, examPoint:float=0.0):
        sp = StudyPoint(processPoint, examPoint)
        return sp.getGPA()

    def getRank(self, processPoint:float=0.0, examPoint:float=0.0, trainingPoint:int=0):
        sp = StudyPoint(processPoint, examPoint)
        tp = TrainingPoint(trainingPoint)
        rank = Rank(sp, tp)
        return rank.ranked()

    def addYUMList(self, YUM:bool, inputStudent):
        yum = YouthUnion(YUM, inputStudent)
        yum.addYouthUnionMember()
        return yum.youthUnionMember()

    def findByFullName(self, firstName:str, lastName:str, listStudent:list):
        find = 0
        for i in listStudent:
            if lastName == i[0] and firstName == i[1]:
                print(i)
                find += 1
        if find == 0:
            print("Student Information is not found")

    def findBySex(self, listStudent:list, sex:str):
        find = 0
        for i in listStudent:
            if sex == i[3]:
                print(i)
                find += 1
        if find == 0:
            print("Student Information is not found")

    def findByRank(self, listStudent:list, rank:str):
        find = 0
        for i in listStudent:
            if i[12] == rank:
                print(i)
                find += 1
        if find == 0:
            print("Scores have not been entered for any students yet")

    def findByClass(self, listStudent:list, className:str):
        print(className+":")
        find = 0
        for i in listStudent:
            termName = i[9]
            for j in termName:
                if j == className:
                    print(i)
                    find += 1
        if find == 0:
            print("There are no students in the class")

    def sortList(self, sortList:list, choose:int, option:bool):
        sortedList = sorted(sortList, key=lambda tup:tup[choose], reverse=option)
        return sortedList

        
# td = {}   
# zz = []
# mng = ManagementAll()
# sv = mng.inputStudent('Minh', 'Le Quang Nhat', 21, 'male', '8484848', 'minh@gmail.com', '123456')
# course = mng.inputCourse(1, 'KHDL&TTNT', ['NNLTPython', 'THUD'], [4, 4])
# mng.getListStudent(sv, course, zz)
# sv = mng.inputStudent('Tri', 'Ho Minh', 21, 'male', '8484848', 'minh@gmail.com', '123456')
# course = mng.inputCourse(1, 'KTDK&TDH', ['NNLTPython', 'THUD'], [4, 4])
# mng.getListStudent(sv, course, zz)
# print(zz)
# lec = mng.inputLecturer('Cuong', 'Nguyen Dinh Hoa', 31, 'male', '212121', 'cuong@gmail.com', 'TS', 'AI')
# td[lec.getFullName()] = mng.addStudentToClass(lec, zz, 'KHDL&TTNT')
# lec = mng.inputLecturer('Nha', 'Vo Quang', 35, 'male', '212121', 'cuong@gmail.com', 'TS', 'Electronic')
# td[lec.getFullName()] = mng.addStudentToClass(lec, zz, 'KTDK&TDH')
# for i in range(len(zz)):
#     hodem = input("Nhap ho va ten dem: ")
#     ten = input("Nhap ten: ")
#     for i in zz:
#         if i[0] == hodem and i[1] == ten:
#             dqt = int(input("Nhap diem qua trinh: "))
#             dt = int(input("Nhap diem thi: "))
#             danhgia = int(input("Nhap diem danh gia: "))
#             i += (mng.getGPA(dqt, dt), danhgia)
#             i += (mng.getRank(dqt, dt, danhgia),)
#             print(i)
#     else:
#         print('name not found')