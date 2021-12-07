from test1 import *

class ManagementAll:
    def inputStudent(self, firstName:str, lastName:str, age:int, sex:str, phoneNumber:str, email:str, studentNumber:str):
        sv = Student(firstName, lastName, age, sex, phoneNumber, email, studentNumber)
        return sv

    def inputCourse(self, courseType:int, specializationName:str, ternName:list, credits:list):
        course = Course(courseType)
        term = Terms(specializationName, course, ternName, credits)
        return term
    
    def inputLecturer(self, firstName:str, lastName:str, age:int, sex:str, phoneNumber:str, email:str, degreeType:str, major:str):
        lec = Lecturer(firstName, lastName, age, sex, phoneNumber, email, degreeType, major)
        return lec

    def getListStudent(self, inputStudent, inputCourse, emptyList:list):
        emptyList.append(inputStudent.informationStudentCourse(inputCourse))
        return emptyList

    def addStudentToClass(self, inputLecturer, listStudent:list, className:str):
        return inputLecturer.memberClass(className, listStudent)

    def getGPA(self, processPoint:float=0.0, examPoint:float=0.0):
        sp = StudyPoint(processPoint, examPoint)
        return sp.getGPA()

    def getRank(self, processPoint:float=0.0, examPoint:float=0.0, trainingPoint:int=0):
        sp = StudyPoint(processPoint, examPoint)
        tp = TrainingPoint(trainingPoint)
        rank = Rank(sp, tp)
        return rank.ranked()

    def addYUM(self, YUM:bool, inputStudent):
        yum = YouthUnion(YUM, inputStudent)
        yum.addYouthUnionMember()
        return yum.youthUnionMember()

import random
firstName = ['Minh', 'Tri', 'Thang', 'An', 'Bi', 'Con']
lastName = ['Le Van', 'Le', 'Nguyen', 'Hoang', 'Ngo']
sex = ['male', 'female']
degreeType = ['TS', 'Th.S']
specialization = ['KHDL&TTNT', 'KTDK&TDH']
listTerm = ['python', 'mach dien', 'tin hoc ung dung', 'c++']
listCredits = [2, 3, 4]
listStudent = []
dictClass = {}
mng = ManagementAll()

for i in range(10):
    fN = random.choice(firstName)
    lN = random.choice(lastName)
    age = random.randint(18, 35)
    phone = random.randint(10000, 100000)
    email = fN+'@gmail.com'
    cT = random.randint(1, 2)
    stN = random. randint(1, 100)
    gt = random.choice(sex)
    spN = random.choice(specialization)
    lT = []
    lC = []
    for i in range(1):
        lT.append(random.choice(listTerm))
        lC.append(random.choice(listCredits))

    sv = mng.inputStudent(fN, lN, age, gt, phone, email, stN)
    course = mng.inputCourse(cT, spN, lT, lC)
    mng.getListStudent(sv, course, listStudent)

for i in range(2):
    fN = random.choice(firstName)
    lN = random.choice(lastName)
    age = random.randint(18, 35)
    gt = random.choice(sex)
    phone = random.randint(10000, 100000)
    email = fN+'@gmail.com'
    dT = random.choice(degreeType)
    major = random.choice(specialization)
    lec = mng.inputLecturer(fN, lN, age, gt, phone, email, dT, major)
    dictClass[lec.getFullName()] = mng.addStudentToClass(lec, listStudent, major)
    print(major)

print(dictClass)
for i in range(len(listStudent)):
    pass



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