
import re
import os
import pandas as pd

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

    def get_output_path(self) -> str:
        return self.file_output

    def convert_file(self):
        dataFile = open(self.file_path) 
        dataOut = open(self.file_output, 'w') 

        pattern = re.compile(r'(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+|\s+)\s+(\d+|\s+)\s+(\d+\.\d+|\s+)\s+(\d+\.\d+|\s+)\s+(.+)')
        ptrn_cls_name = re.compile(r'(\w+)[::]')
        ptrn_fnc_name = re.compile(r'[::](\w+)[\(]')

        structBuffer = {}
        for param in self.parameters_gprof:
            structBuffer[param] = []

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
                
        data_frame = pd.DataFrame.from_dict(structBuffer).to_csv(index=False, line_terminator='\n')
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

        for element in range(0, len(__buffer__['function'])):
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
