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
    
def inputData(data):
    while True:
        data = checkFileName(data)
        if data != None:
            break
    return data
listStudent = None
print(inputData(listStudent))
# import pickle as pk
# abc = [1,2,3]
# with open("abc.pickle", "wb") as f:
#     pk.dump(abc, f)
#     f.close()