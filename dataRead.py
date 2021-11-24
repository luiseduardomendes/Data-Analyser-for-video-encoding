from os import read

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def removeParemeter(string):
    index = string.find("(")
    return string[:index]

class DataStruct:
    percentageTime = float
    cumulativeTIme = float
    selfTime = float
    calls = int
    selfSCall = float
    totalSCall = float
    name = str



dados = DataStruct
listaDados = list()


dataFile = open ("akiyo.txt", "r")

lineBegin = 5

stringList = list()

res = list()

for i in range (0, lineBegin):
    dataFile.readline()

for i in range (0,20):
    str = dataFile.readline()
    stringList.append(str)

for sub in stringList:
    res.append(sub.split())

print("name", end="")
print(" "*48, end="")
print("time(%)       " + "c. seconds    " + "s. seconds    " + "calls         " + "self call     " + "total call")
print()
for i in res:
    print(f"{removeParemeter(i[6]):50}", end='  ')
    for j in i:
        if is_number(j):
            print(f"{j:12}", end='  ')
    print()
    


dataFile.close()
