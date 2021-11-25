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

def showDataTable(datalist):
    print("name", end="")
    print(" "*173, end="")
    print("time(%)       " + "c. seconds    " + "s. seconds    " + "calls         " + "self call     " + "total")
    print()   
    for data in dataList:
        print(f'{data["name"]:175}  {data["percentageTime"]:12}  {data["cumulativeTime"]:12}  {data["selfTime"]:12}  {data["calls"]:12}  {data["selfSCall"]:12}  {data["totalSCall"]:4c}')
    return

dataStruct = dict()
dataStruct["percentageTime"] = 0
dataStruct["cumulativeTime"] = 0
dataStruct["selfTime"] = 0
dataStruct["calls"]  = 0
dataStruct["selfSCall"] = 0
dataStruct["totalSCall"]  = 0
dataStruct["name"] = ""

stringList = list()
splitStr = list()
names = list()
dataList = list()

dataFile = open ("akiyo.txt", "r")


# jump not used lines
for i in range (0, 5):
    dataFile.readline()

# get data from dataFile
for i in range (0,500):
    str = dataFile.readline()
    stringList.append(str[:54])
    names.append(str.replace('\n', '')[54:])

# split data
for sub in stringList:
    splitStr.append(sub.split())

# record data into a list of dicts
for cont in range (0, len(stringList)):
    dataStruct["percentageTime"] = float(splitStr[cont][0])
    dataStruct["cumulativeTime"] = float(splitStr[cont][1])
    dataStruct["selfTime"] = float(splitStr[cont][2])
    dataStruct["calls"] = int(splitStr[cont][3])
    dataStruct["selfSCall"] = float(splitStr[cont][4])
    dataStruct["totalSCall"] = float(splitStr[cont][5])
    dataStruct["name"] = names[cont]
    dataList.append(dataStruct.copy())

showDataTable(dataList)



dataFile.close()
