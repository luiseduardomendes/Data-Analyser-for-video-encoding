import re
import string


class GprofOutReader:
    listParameters = [
        'percentageTime',
        'function',
        'cumulativeTime',
        'selfSeconds',
        'calls',
        'selfMs/call',
        'totalMs/call',
        'class'
    ]

    __parametersDict__ = {
        'percentageTime' : 'Execution Time',
        'function' : 'Function',
        'cumulativeTime' : 'Cumulative Time',
        'selfSeconds' : 'Self Seconds',
        'calls' : 'Calls',
        'selfMs/call' : 'Self ms/call',
        'totalMs/call' : 'Total ms/call',
        'class' : 'Class'
    }

    def __init__(self, FN : str):
        self.fileName = FN
        self.__readData()
        self.__separateDataByclass()
        self.__setLists()

    def __readData(self):
        dataFile = open(self.fileName) 

        stringList = []

        for line in dataFile:
            stringList.append(dataFile.readline())

        pattern = re.compile(r'([\d]+\.[\d]+)[ ]+([\d]+\.[\d]+)[ ]+([\d]+\.[\d]+|[ ]+)[ ]+([\d]+|[ ]+)[ ]+([\d]+\.[\d]+|[ ]+)[ ]+([\d]+\.[\d]+|[ ]+)[ ]+(.+)::(.+[\w])[\(](.+)')

        structBuffer = {}
        self.__dataList = []
        self.__dataList.clear()

        for i in stringList[:150]:
            check = pattern.findall(i)
            if len(check) > 0:
                buffer = check[0][:]
                
                structBuffer['percentageTime'] = float(buffer[0])
                structBuffer['cumulativeTime'] = float(buffer[1])
                structBuffer['selfSeconds'] = float(buffer[2])

                try:
                    structBuffer['calls'] = int(buffer[3])
                except:
                    structBuffer['calls'] = -1
                
                try:
                    structBuffer['selfMs/call'] = float(buffer[4])
                except:
                    structBuffer['selfMs/call'] = -1.00

                try:
                    structBuffer['totalMs/call'] = float(buffer[5])
                except:
                    structBuffer['totalMs/call'] = -1.00


                structBuffer['class'] = buffer[6]    
                structBuffer['function'] = buffer[7]
                    
                self.__dataList.append(structBuffer.copy())

    def __separateDataByclass(self):
        self.dataPerClass = list()
        for i in self.__dataList:
            index = self.__returnElementIndex(i['class'])
            if index == -1:
                self.dataPerClass.append(i)
            else:
                for j in self.listParameters:
                    if j != 'function' and j != 'class':
                        self.dataPerClass[index][j] = self.dataPerClass[index][j] + i[j]

    def __returnElementIndex(self, className):
        for i, classes in enumerate(self.dataPerClass):
            if classes['class'] == className:
                return i
        return -1
        
    def displayPercentageTimeOfClass(self, text):
        print(self.dataPerClass[self.returnElementIndex(text)])

    def displayPercentageTime(self):
        
        for classes in self.dataPerClass:
            print('-*'*40)
            for param in self.__parametersDict__:
                if type(classes[param]) == float:
                    stringLine = f'{classes[param]:.2f}'
                else: 
                    stringLine = f'{classes[param]}'
                print(f'{param:20}{stringLine}')
            print('-*'*40, end='\n\n')
            

    def __setLists(self):
        self.dataListsPerClassForPlotter = dict() 
        self.dataListsPerFunctionForPlotter = dict() 

        for i in self.listParameters:
            self.dataListsPerClassForPlotter[i] = list()
            self.dataListsPerFunctionForPlotter[i] = list()

        for i in range(0, len(self.dataPerClass)):
            for j in self.listParameters:
                self.dataListsPerClassForPlotter[j].append(self.dataPerClass[i][j])
            for j in self.listParameters:
                self.dataListsPerFunctionForPlotter[j].append(self.__dataList[i][j])
        for i in self.listParameters:
            self.dataListsPerFunctionForPlotter[i].reverse()
        # TODO: implement quick sort algorythm 

        trade = True
        while trade:
            trade = False
            k = len(self.dataListsPerClassForPlotter['percentageTime'])
            for i in range(0,k-1):
                if self.dataListsPerClassForPlotter['percentageTime'][i] > self.dataListsPerClassForPlotter['percentageTime'][i+1]:
                    for j in self.listParameters:
                        buffer = self.dataListsPerClassForPlotter[j][i]
                        self.dataListsPerClassForPlotter[j][i] = self.dataListsPerClassForPlotter[j][i+1]
                        self.dataListsPerClassForPlotter[j][i+1] = buffer
                    
                    trade = True
