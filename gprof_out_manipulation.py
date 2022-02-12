
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

    def __init__(self, file_path: str, path_output: str = 'default') -> None:
        self.set_file_path(file_path)
        if path_output == 'default':
            self.file_output = f'{self.file_path.split(sep=".txt")[0]}.csv'    
        else:
            self.file_output = path_output

        self.read_gprof_out()
        self.convert_file()
        
    def set_file_path(self, file_path : str):
        self.file_path = file_path
        self.file_output = f'{self.file_path.split(sep=".txt")[0]}.csv'

    def set_file_output(self, txt : str):
        self.file_output = f'{txt}'

    def get_output_path(self) -> str:
        return self.file_output

    def convert_file(self):
        dataOut = open(self.file_output, 'w') 
        dataOut.write(self.data_frame)
        dataOut.close()

    def read_gprof_out(self):           

        pattern = re.compile(r'(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+|\s+)\s+(\d+|\s+)\s+(\d+\.\d+|\s+)\s+(\d+\.\d+|\s+)\s+(.+)()')

        # pattern of end of file, after this, the data represented is granularity
        pattern_end = re.compile(r' %         the percentage of the total running time of the')
            
        structBuffer = {}
        for param in self.parameters_gprof:
            structBuffer[param] = []

        dataFile = open(self.file_path) 
        
        for k in dataFile:
            line = dataFile.readline()
            
            ptrn_found = pattern_end.findall(line)
            
            if len(ptrn_found) > 0:
                break
                
            check = pattern.findall(line)
            

            if len(check) != 0:
                buffer = check[0][:]
                for i, parameter in enumerate(self.parameters_gprof):
                    if buffer[i] == '':
                        structBuffer[parameter].append(0)
                    else:
                        try:
                            structBuffer[parameter].append(float(buffer[i]))
                        except:
                            structBuffer[parameter].append(buffer[i])
                if '::' in buffer[6]:
                    class_name = buffer[6].split(sep='::')[0]
                else:
                    class_name = 'no_class'
                funct_name = buffer[6].split(sep='(')[0]
                structBuffer['class'][-1] = class_name
                structBuffer['function'][-1] = funct_name

        
        self.data_frame = pd.DataFrame.from_dict(structBuffer).to_csv(index=False, line_terminator='\n')
        dataFile.close()

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

    file_path_set = False

    def __init__(self, file_path: str) -> None:
        self.set_file_path(file_path)
        if self.file_path_set:
            self.functions_dict()
            self.split_by_function()
    
    def functions_dict(self):
        # turn the csv data by functions into a dict
        self.data_frame = pd.read_csv(self.file_path)        

    def set_file_path(self, file : str = 'akiyo.csv'):
        # check if the file is valid 
        if os.path.isfile(file):
            if len(re.compile(r'\.csv$').findall(file)) > 0:
                self.file_path = file
                self.file_path_set = True
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

    def __set_dict_of_lists_to_plot_data__(self):

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

    def __sum_numeric_elements_with_same_name__(self, data: list, parameter: str) -> list:
        new_list = []
        for i, element in enumerate(data):
            index = self.__return_element_id__(element[parameter], new_list, parameter)
            
            # index == -1 if the class is not in the list yet
            if index == -1:
                new_list.append(element.copy())
            else:
                # sums the content that is already in the dict with the new element
                for parameter in element.keys():
                    if type(new_list[index][parameter]) != str:
                        new_list[index][parameter] += element[parameter]

        return new_list

    def __to_list_of_struct__(self, __buffer__: dict) -> list:
        new_list = []
        __dict_buffer__ = {}

        for element in range(0, len(__buffer__['function'])):
            for i, param in enumerate(__buffer__.keys()):
                __dict_buffer__[param] = __buffer__[param][element]
            new_list.append(__dict_buffer__.copy())

        return new_list


    def split_by_function(self):

        __list_data__ = self.__to_list_of_struct__(self.data_frame.to_dict())        

        self.list_data_by_class = []
        self.list_data_by_funct = __list_data__[:]

        # sum the elements with same class
        self.list_data_by_class = self.__sum_numeric_elements_with_same_name__(__list_data__, 'class')

        self.__sort_list_of_dicts__('percentageTime', self.list_data_by_class)

        self.__set_dict_of_lists_to_plot_data__()
