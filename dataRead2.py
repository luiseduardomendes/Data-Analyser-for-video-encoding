import matplotlib.pyplot as plt


class DataStruct:
    percentageTime = list()
    cumulativeTime = list()
    selfTime = list()
    calls = list()
    selfSCall = list()
    totalSCall = list()
    names = list()

    def appendPT (self, data):
        self.percentageTime.append(data)
    def appendCT (self, data):
        self.cumulativeTime.append(data)
    def appendST (self, data):
        self.selfTime.append(data)
    def appendCall (self, data):
        self.selfTime.append(data)
    def appendSSC (self, data):
        self.selfSCall.append(data)
    def appendTSC (self, data):
        self.totalSCall.append(data)
    def appendName (self, data):
        self.names.append(data)

    def showData(self, begin, end):
        for i in range (begin, end):
            print(f"{self.names[i]:75}, {self.percentageTime[i]:5}, {self.cumulativeTime[i]:5}, {self.selfTime[i]:5}, {self.selfSCall[i]:5}, {self.totalSCall[i]:5}")
    
    def plotGraph(self):
        fig1 = plt
        
        fig1.plot(self.percentageTime, 2)
        fig1.show()

dataStruct = DataStruct()
dataFile = open("akiyo.txt", "r")
stringList = list()
names = list()
splitStr = list()

# jump not used lines
for i in range (0, 5):
    dataFile.readline()

# get data from dataFile
for i in range (0,50):
    str = dataFile.readline()
    stringList.append(str[:54])
    names.append(str.replace('\n', '')[54:])

# split data
for sub in stringList:
    splitStr.append(sub.split())

for cont in range (0, len(stringList)):
    dataStruct.appendPT(float(splitStr[cont][0]))
    dataStruct.appendCT(float(splitStr[cont][1]))
    dataStruct.appendST(float(splitStr[cont][2]))
    dataStruct.appendCall(int(splitStr[cont][3]))
    dataStruct.appendSSC(float(splitStr[cont][4]))
    dataStruct.appendTSC(float(splitStr[cont][5]))
    dataStruct.appendName(names[cont])

dataStruct.showData(0,20)

dataStruct.plotGraph()

