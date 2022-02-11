
import re
import os
import pandas as pd
from sqlalchemy import false

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
        self.file_output = f'C:\\Users\\dudup\\OneDrive\\Área de Trabalho\\VVC\\Data-Analyser-for-video-encoding\\testes\\{txt}'

    def convert_file(self):
        dataFile = open(self.file_path) 
        dataOut = open(self.file_output, 'w') 

        pattern = re.compile(r'(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+|\s+)\s+(\d+|\s+)\s+(\d+\.\d+|\s+)\s+(\d+\.\d+|\s+)\s+(.+)')
        ptrn_cls_name = re.compile(r'(\w+)[::]')
        ptrn_fnc_name = re.compile(r'[::](\w+)[\(]')

        structBuffer = {}
        for param in self.parameters_gprof:
            structBuffer[param] = []
        print('teste1')

        for index in dataFile:
            line = dataFile.readline()

            pattern_end = re.compile(r' %         the percentage of the total running time of the')
            
            ptrn_found = pattern_end.findall(line)

            if len(ptrn_found) != 0:
                break


            check = pattern.findall(line)
            if len(check) != 0:
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
    
    def functions_dict(self):
        # turn the csv data by functions into a dict
        self.data_frame = pd.read_csv(self.file_path)        

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
    
    def __return_element_id__(self, element, d_list : list, key_word : str) -> int:
        for i, j in enumerate(d_list):
            if element == j[key_word]:
                
                return i
            
        return -1

    def __sort_list_of_dicts__(self, parameter: str, list_data: list) -> None:
        trade = True
        while trade:
            trade = False
            for index in range(0, len(list_data) - 1):
                if list_data[index][parameter] < list_data[index + 1][parameter]:
                    buffer = list_data[index]
                    list_data[index] = list_data[index + 1]
                    list_data[index + 1] = buffer
                    trade = True



    def split_by_function(self):
        __buffer__ = self.data_frame.to_dict();
        __list_data__ = []
        __dict_buffer__ = {}

        for element in range(0, len(__buffer__['Unnamed: 0'])):
            for i, param in enumerate(__buffer__.keys()):
                __dict_buffer__[param] = __buffer__[param][element]
            __list_data__.append(__dict_buffer__.copy())

        self.list_data_by_class = []
        self.list_data_by_funct = __list_data__[:]

        for i, element in enumerate(__list_data__):

            index = self.__return_element_id__(element['class'], self.list_data_by_class, 'class')
            # index == -1 if the class is not in the list yet
            
            if index == -1:
                self.list_data_by_class.append(element.copy())
            else:
                # sums the content that is already in the dict with the new element
                for parameter in self.parameters_gprof:
                    if type(self.list_data_by_class[index][parameter]) != str:
                        self.list_data_by_class[index][parameter] += element[parameter]

        self.__sort_list_of_dicts__('percentageTime', self.list_data_by_class)

        self.dict_data_by_class = {}

        for parameter in self.parameters_gprof:
            self.dict_data_by_class[parameter] = []

        for element in self.list_data_by_class:
            for parameter in self.parameters_gprof:
                self.dict_data_by_class[parameter].append(element[parameter])

        self.dict_data_by_funct = {}

        for parameter in self.parameters_gprof:
            self.dict_data_by_funct[parameter] = []

        for element in self.list_data_by_funct:
            for parameter in self.parameters_gprof:
                self.dict_data_by_funct[parameter].append(element[parameter])



'''import enum
import re
import pandas as pd
import os

from pytest import param



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
        
        print('teste')
        for line in stringList:
            stop_condition = re.compile('Copying and distribution of this file, with or without modification,')
            if len(stop_condition.findall(line)) > 0:
                print('stop')
                break
            
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
    
    def functions_dict(self):
        # turn the csv data by functions into a dict
        self.data_frame = pd.read_csv(self.file_path)        

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
    def __return_element_id__(self, element, d_list : list, key_word : str) -> int:
        for i, j in enumerate(d_list):
            if element == j[key_word]:
                return i
            
        return -1

    def split_by_function(self):
        __buffer__ = self.data_frame.to_dict();
        __list_data__ = []
        __dict_buffer__ = {}

        for element in range(0, len(__buffer__['Unnamed: 0'])):
            for i, param in enumerate(__buffer__.keys()):
                __dict_buffer__[param] = __buffer__[param][element]
            __list_data__.append(__dict_buffer__.copy())

        print(__list_data__)
        
        
        self.list_data_by_class = []
        self.list_data_by_funct = __list_data__[:]

        for i in __list_data__:
            index = self.__return_element_id__(i['class'], self.list_data_by_class, 'class')
            if index == -1:
                self.list_data_by_class.append(i)
            else:
                for j in self.parameters_gprof:
                    if type(self.list_data_by_class[index][j]) != str:
                        self.list_data_by_class[index][j] += i[j]

        self.dict_data_by_class = {}

        for parameter in self.parameters_gprof:
            self.dict_data_by_class[parameter] = []

        for element in self.list_data_by_class:
            for parameter in self.parameters_gprof:
                self.dict_data_by_class[parameter].append(element[parameter])

        self.dict_data_by_funct = {}

        for parameter in self.parameters_gprof:
            self.dict_data_by_funct[parameter] = []

        for element in self.list_data_by_funct:
            for parameter in self.parameters_gprof:
                self.dict_data_by_funct[parameter].append(element[parameter])


    
        

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

'''