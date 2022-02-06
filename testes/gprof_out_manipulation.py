import re
import pandas as pd
import os



class GprofToCSV: 
    parameters_gprof = (
        'percentageTime',
        'cumulativeTime',
        'selfSeconds',
        'calls',
        'selfMs/call',
        'totalMs/call',
        'function',
        'class'
    )

    def set_file_path(self, txt : str = 'akiyo.txt'):
        self.file_path = txt
        self.file_output = f'{self.file_path.split(sep=".txt")[0]}.csv'

    def set_file_output(self, txt : str):
        self.file_output = f'{txt}'

    def convert_file(self):
        dataFile = open(self.file_path) 
        dataOut = open(self.file_output, 'w') 
        stringList = []

        for line in dataFile:
            stringList.append(dataFile.readline())

        pattern = re.compile(r'(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+|\s+)\s+(\d+|\s+)\s+(\d+\.\d+|\s+)\s+(\d+\.\d+|\s+)\s+(.+)')
        ptrn_cls_name = re.compile(r'(\w+)[::]')
        ptrn_fnc_name = re.compile(r'[::](\w+)[\(]')

        structBuffer = {}
        for param in self.parameters_gprof:
            structBuffer[param] = []
        

        for line in stringList:
            
            check = pattern.findall(line)
            if (len(check) != 0):
                buffer = check[0][:]
                        
                structBuffer['percentageTime'].append(float(buffer[0]))
                structBuffer['cumulativeTime'].append(float(buffer[1]))
                try:
                    structBuffer['selfSeconds'].append(float(buffer[2]))
                except:
                    structBuffer['selfSeconds'].append(-1)

                try:
                    structBuffer['calls'].append(int(buffer[3]))
                except:
                    structBuffer['calls'].append(-1)
                
                try:
                    structBuffer['selfMs/call'].append(float(buffer[4]))
                except:
                    structBuffer['selfMs/call'].append(-1.00)

                try:
                    structBuffer['totalMs/call'].append(float(buffer[5]))
                except:
                    structBuffer['totalMs/call'].append(-1.00)

                className = ptrn_cls_name.findall(buffer[6])
                funcName = ptrn_fnc_name.findall(buffer[6])
                
                if len(className) > 0: 
                    structBuffer['class'].append(className[0])
                    if len(funcName) != 0: 
                        structBuffer['function'].append(funcName[0])
                    else:
                        structBuffer['function'].append(re.compile(r'([\w|\s]+)').findall(buffer[6])[0])
                else:
                    structBuffer['class'].append('void_class')
                    if len(funcName) != 0: 
                        structBuffer['function'].append(funcName[0])
                    else:
                        structBuffer['function'].append(re.compile(r'([\w|\s]+)').findall(buffer[6])[0])
        data_frame = pd.DataFrame(structBuffer).to_csv()
        dataOut.write(data_frame)
        dataFile.close()
        dataOut.close()

# TODO: class csvReaderGprof, to read the file from csv generated by GprofToCSV

# TODO: function to set the dict from the csv file
    
class GprofOutCSVReader:
    parameters_gprof = (
        'percentageTime',
        'cumulativeTime',
        'selfSeconds',
        'calls',
        'selfMs/call',
        'totalMs/call',
        'function',
        'class'
    )
    
    def functions_dict(self) -> dict():
        # turn the csv data by functions into a dict
        self.data_frame = pd.read_csv(self.file_path)
        self.data_by_function = self.data_frame.to_dict()
        return self.data_by_function

    def set_file_path(self, file : str = 'akiyo.csv'):
        # check if the file is valid 
        if os.path.isfile(file):
            if len(re.compile(r'\.csv$').findall(file)) > 0:
                self.file_path = file
            else:
                print('Error - file is not a csv file')
        else:
            print('Error - file not found')

    # auxiliar function to find the first occurrency of a name
    def __return_element_id__(self, class_name : str) -> int:
        for i, j in enumerate(self.dict_data_agl['class']):
            if class_name == j:
                return i
            
        return -1
    
    def split_by_function(self):

        __dict_data_buffer__ = self.data_frame.to_dict()

        self.dict_data = {}
        for param in self.parameters_gprof:
            self.dict_data[param] = []

        self.dict_data_agl = {}
        for param in self.parameters_gprof:
            self.dict_data_agl[param] = []

        # transform into dict of lists
        for i in __dict_data_buffer__.values():
            print(i)

            for j in i[1].values():
                self.dict_data[i[0]].append(j)

        # sum of elements with same name
        for i in range (0, len(self.dict_data['function'])):
            if self.dict_data['class'][i] in self.dict_data_agl['class']:
                for j in self.dict_data_agl.items():
                    if type(j[1][0]) != str:
                        self.dict_data_agl[j[0]][self.__return_element_id__(dict_data['class'][i])] += self.dict_data[j[0]][i]
            else:
                for j in self.dict_data_agl.keys():
                    self.dict_data_agl[j].append(self.dict_data[j][i])

    
    
        

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
