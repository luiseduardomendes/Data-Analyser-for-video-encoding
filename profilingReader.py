import re
from matplotlib import pyplot as plt

class DataAnalyses:
    def readData(self):
        fileName = "akiyo.txt"

        dataFile = open(fileName) 

        stringList = list()
        stringList.clear()

        for line in dataFile:
            stringList.append(dataFile.readline())

        pattern = re.compile(r'([\d]+\.[\d]+)[ ]+([\d]+\.[\d]+)[ ]+([\d]+\.[\d]+|[ ]+)[ ]+([\d]+|[ ]+)[ ]+([\d]+\.[\d]+|[ ]+)[ ]+([\d]+\.[\d]+|[ ]+)[ ]+(.+)::(.+[\w])[\(](.+)')

        structBuffer = dict()
        self.dataList = list()
        self.dataList.clear()

        for i in range(0,150):
            
            check = pattern.findall(stringList[i])
            if len(check) > 0:
                
                buffer = check[0][:]
                
                try:
                    structBuffer['percentage time'] = float(buffer[0])
                except:
                    structBuffer['percentage time'] = buffer[0]

                try:
                    structBuffer['cumulative time'] = float(buffer[1])
                except:
                    structBuffer['cumulative time'] = buffer[1]

                try:
                    structBuffer['self seconds'] = float(buffer[2])
                except:
                    structBuffer['self seconds'] = buffer[2]
                
                try:
                    structBuffer['calls'] = int(buffer[3])
                except:
                    structBuffer['calls'] = -1
                
                try:
                    structBuffer['self ms/call'] = float(buffer[4])
                except:
                    structBuffer['self ms/call'] = -1.00

                try:
                    structBuffer['total ms/call'] = float(buffer[5])
                except:
                    structBuffer['total ms/call'] = -1.00


                structBuffer['className'] = buffer[6]    

                structBuffer['functionName'] = buffer[7]
                    
                self.dataList.append(structBuffer.copy())

    def separateDataByClassName(self):
        self.dataPerClass = list()
        for i in self.dataList:
            index = self.returnElementIndex(i['className'])
            if index == -1:
                self.dataPerClass.append(i)
            else:
                self.dataPerClass[index]['percentage time'] = self.dataPerClass[index]['percentage time'] + i['percentage time']
                self.dataPerClass[index]['cumulative time'] = self.dataPerClass[index]['cumulative time'] + i['cumulative time']
                self.dataPerClass[index]['self seconds'] = self.dataPerClass[index]['self seconds'] + i['self seconds']
                self.dataPerClass[index]['calls'] = self.dataPerClass[index]['calls'] + i['calls']
                self.dataPerClass[index]['self ms/call'] = self.dataPerClass[index]['self ms/call'] + i['self ms/call']
                self.dataPerClass[index]['total ms/call'] = self.dataPerClass[index]['total ms/call'] + i['total ms/call']
            
    def isClassInList(self, className):
        for i in self.dataPerClass:
            if i['nameClass'] == className:
                return True
        return False

    def returnElementIndex(self, className):
        for i in range(0, len(self.dataPerClass)):
            if self.dataPerClass[i]['className'] == className:
                return i
        return -1
        
    def displayPercentageTimeOfClass(self, text):
        print(self.dataPerClass[self.returnElementIndex(text)])

    def displayPercentageTime(self):
        for i in range(0,10):
            classes = self.dataPerClass[i]
            print(f"Nome da classe:.........{classes['className']}")
            print(f"Tempo(%)................{classes['percentage time']:.2f}")
            print(f"Tempo(sec)..............{classes['cumulative time']:.2f}")
            print(f"Tempo(self).............{classes['self seconds']:.2f}")
            print(f"Chamadas................{classes['calls']}")
            print(f"Tempo por chamada.......{classes['self ms/call']:.2f}")
            print(f"Tempo por chamada.......{classes['total ms/call']:.2f}")
            print(f"Função mais custosa.....{classes['functionName']}")
            print('-*'*40)
            print()


    def initPlotter(self):

        dataListsforPlotter = dict()  
        dataListsforPlotter['percentage time'] = list()
        dataListsforPlotter['cumulative time'] = list()
        dataListsforPlotter['self seconds'] = list()
        dataListsforPlotter['calls'] = list()
        dataListsforPlotter['self ms/call'] = list()
        dataListsforPlotter['total ms/call'] = list()
        dataListsforPlotter['functionName'] = list()
        dataListsforPlotter['className'] = list()

        for i in range(0,10):
            dataListsforPlotter['percentage time'].append(self.dataList[i]['percentage time'])
            dataListsforPlotter['functionName'].append(self.dataList[i]['functionName'])
            dataListsforPlotter['cumulative time'].append(self.dataList[i]['cumulative time'])
            dataListsforPlotter['self seconds'].append(self.dataList[i]['self seconds'])
            dataListsforPlotter['calls'].append(self.dataList[i]['calls'])
            dataListsforPlotter['self ms/call'].append(self.dataList[i]['self ms/call'])
            dataListsforPlotter['total ms/call'].append(self.dataList[i]['total ms/call'])
            dataListsforPlotter['className'].append(self.dataList[i]['className'])
            
        
        dataListsforPlotter['percentage time'].reverse()
        dataListsforPlotter['functionName'].reverse()
        dataListsforPlotter['cumulative time'].reverse()
        dataListsforPlotter['self seconds'].reverse()
        dataListsforPlotter['calls'].reverse()
        dataListsforPlotter['self ms/call'].reverse()
        dataListsforPlotter['total ms/call'].reverse()
        dataListsforPlotter['className'].reverse()
        
        print(dataListsforPlotter['functionName'])

        plt.style.use('ggplot')
        plt.figure(figsize=(12.8, 7.2))

        plt.title('Functions', fontsize=16)
        plt.xlabel('Percentage time')        
        
        yticks = [i for i in dataListsforPlotter['functionName']]

        plt.tight_layout()

        plt.barh(yticks, dataListsforPlotter['percentage time'])

        plt.subplots_adjust(left=0.25)

        plt.savefig('plot.png')        

        plt.show()


d = DataAnalyses()

d.readData()
d.separateDataByClassName()
d.displayPercentageTime()
d.initPlotter()