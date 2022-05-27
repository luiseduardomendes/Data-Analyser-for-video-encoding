import re
import os
from textwrap import indent
import pandas as pd
import numpy as np

class GprofOutManip:
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
    in_ext = '.txt'
    out_ext = '.csv'


    def __init__(self, input_file: str, output_file: str = 'default') -> None:
        self.__set_init_names__(input_file, output_file)

    def __set_init_names__(self, input_file, output_file):
        
        # verifies the extension of the input file
        if not input_file.endswith(self.in_ext):
            raise Exception('the input file must be {}'.format(self.in_ext))
        else:
            self.input_file = input_file
        
        if output_file == 'default':
            self.output_file = self.input_file.split(sep=self.in_ext)[0]
        else:
            if  output_file.count('.') > 0:
                raise Exception('the output file must have no extension')
            else:
                self.output_file = output_file        

    def get_output_path(self) -> str:
        return self.output_file

    def get_data_frame(self):
        try:
            return self.data_frame
        except AttributeError as error:
            raise Exception(error)
        except:
            raise Exception('Unnidentified Error')

    def convert_data_frame_into_CSV(self, output_name:str = 'default'):
        if output_name != 'default':
            out = output_name
        else:
            out = self.output_file

        try:
            self.data_frame.to_csv(
                path_or_buf=out+'.csv',
                index=False, 
                line_terminator='\n'
            )
        except AttributeError as error:
            raise Exception(error)
        except:
            raise Exception('Unnidentified Error')

    def convert_data_frame_into_excel(self, output_name:str = 'default'):
        if output_name != 'default':
            out = output_name
        else:
            out = self.output_file

        try:
            self.data_frame.to_excel(sheet_name='', excel_writer=f'{out}.xlsx')
        except AttributeError as error:
            raise Exception(error)
        except:
            raise Exception('Unnidentified Error')

    def read_gprof_out(self):           

        pattern = re.compile(r'(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+|\s+)\s+(\d+|\s+)\s+(\d+\.\d+|\s+)\s+(\d+\.\d+|\s+)\s+(.+)()')

        # pattern of end of file, after this, the data represented is granularity
        pattern_end = re.compile(r' %         the percentage of the total running time of the')

        dataFile = open(self.input_file) 

        temp_data = {}
        for key in self.parameters_gprof:
            temp_data[key] = []
        
        for line in dataFile:
            ptrn_found = pattern_end.findall(line)

            if len(ptrn_found) > 0:
                break
                
            check = pattern.findall(line)
            if len(check) != 0:
                buffer = check[0][:]
                for i, parameter in enumerate(self.parameters_gprof):
                    if buffer[i] == '':
                        temp_data[parameter].append(0)
                    else:
                        try:
                            temp_data[parameter].append(float(buffer[i]))
                        except:
                            temp_data[parameter].append(buffer[i])
                if '::' in buffer[6]:
                    class_name = buffer[6].split(sep='::')[0]
                else:
                    class_name = 'no_class'
                funct_name = buffer[6].split(sep='(')[0]
                funct_name = funct_name.split(sep='::')[-1]
                temp_data['class'][-1] = class_name
                temp_data['function'][-1] = funct_name
        dataFile.close()
        self.data_frame = pd.DataFrame(temp_data)
   
    def gprof_read_csv(self):
        # check if the file is valid 
        try:
            self.data_frame = pd.read_csv(self.input_file)
        except FileNotFoundError as error:
            print(error)
        except:
            print('Unknown error')         

    def group_by_class(self):
        try:
            df = self.data_frame
            df.drop('function', inplace=True, axis=1)
        except:
            raise Exception('Unnidentified Error')

        self.data_frame_by_class = pd.pivot_table(df, index='class', aggfunc='sum')
        return self.data_frame_by_class
        

        

