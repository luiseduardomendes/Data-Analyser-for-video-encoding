import re

class GprofOutReader:
    listParameters = list()
    listParameters.append('percentageTime')
    listParameters.append('function')
    listParameters.append('cumulativeTime')
    listParameters.append('selfSeconds')
    listParameters.append('calls')
    listParameters.append('selfMs/call')
    listParameters.append('totalMs/call')
    listParameters.append('class')

    def __init__(self, FN):
        self.fileName = FN
        self.__readData()
        self.__separateDataByclass()
        self.__setLists()

    def __readData(self):
        dataFile = open(self.fileName) 

        stringList = list()


        for line in dataFile:
            stringList.append(dataFile.readline())

        pattern = re.compile(r'([\d]+\.[\d]+)[ ]+([\d]+\.[\d]+)[ ]+([\d]+\.[\d]+|[ ]+)[ ]+([\d]+|[ ]+)[ ]+([\d]+\.[\d]+|[ ]+)[ ]+([\d]+\.[\d]+|[ ]+)[ ]+(.+)::(.+[\w])[\(](.+)')

        structBuffer = dict()
        self.__dataList = list()
        self.__dataList.clear()

        for i in range(0,150):
            
            check = pattern.findall(stringList[i])
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
                    
    def __isClassInList(self, className):
        for i in self.dataPerClass:
            if i['nameClass'] == className:
                return True
        return False

    def __returnElementIndex(self, className):
        for i in range(0, len(self.dataPerClass)):
            if self.dataPerClass[i]['class'] == className:
                return i
        return -1
        
    def displayPercentageTimeOfClass(self, text):
        print(self.dataPerClass[self.returnElementIndex(text)])

    def displayPercentageTime(self):
        for i in range(0, len(self.dataPerClass)):
            classes = self.dataPerClass[i]
            print('-*'*40)
            print(f"Nome da classe:.........{classes['class']}")
            print(f"Tempo(%)................{classes['percentageTime']:.2f}")
            print(f"Tempo(sec)..............{classes['cumulativeTime']:.2f}")
            print(f"Tempo(self).............{classes['selfSeconds']:.2f}")
            print(f"Chamadas................{classes['calls']}")
            print(f"Tempo por chamada.......{classes['selfMs/call']:.2f}")
            print(f"Tempo por chamada.......{classes['totalMs/call']:.2f}")
            print(f"Função mais custosa.....{classes['function']}")
            print('-*'*40)
            print()

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
