import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint

class gprofLogManip():
    def __init__(self, datafile: str, filename: str, qp: int) -> None:
        # verify if 
        if len(re.findall(r'(.+)(?=(?:\.txt$)|(?:\.gplog$))', datafile, flags=re.M)) > 0:
            with open(datafile) as f:
                self._data_ = f.read()
                f.close()

            _data_ = re.findall(r'^\s+(\d+)\s+a\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+$', self._data_, flags=re.M)

            data_dict = {
                'fileName' : str,
                'qp' : int,
                'frames' : int,
                'bitrate' : float,
                'Y_PSNR' : float,
                'U_PSNR' : float,
                'V_PSNR' : float,
                'YUV_PSNR' : float
            }

            if len(_data_) == 1:
                log = _data_[0]
                for i, key in enumerate(data_dict.keys()):
                    if key == 'fileName':
                        data_dict[key] = filename
                    elif key == 'qp':
                        data_dict[key] = qp
                    else:
                        try:
                            data_dict[key] = int(log[i-2])
                        except:
                            data_dict[key] = float(log[i-2])
                self.dataDict = data_dict
                
            elif len(_data_) == 0:
                self.dataDict = data_dict
            
            else:
                raise Exception("File has more than one execution log")
        else: 
            raise Exception('File is not a .txt or a .gplog')
        
    
    def returnDict(self) -> dict:
        try:
            return self.dataDict
        except:
            raise Exception("data dict has not been set yet")



class gprofLogSets:
    keys = ('fileName', 'qp', 'frames', 'bitrate', 'Y_PSNR', 'U_PSNR', 'V_PSNR', 'YUV_PSNR')

    # initialize the dict
    def __init__(self, datafile : str = 'default') -> None:
        if datafile == 'default':
            self.__data_dict = {}

            for key in self.keys:
                self.__data_dict[key] = []
        elif len(re.findall(r'(.+)(?:\.csv$)', datafile)) > 0:
            self.__data_dict = pd.read_csv(datafile).to_dict('list')
        
        elif len(re.findall(r'(.+)(?:\.xlsx$)', datafile)) > 0:
            self.__data_dict = pd.read_excel(datafile, index_col=[0]).to_dict('list')
            
    
    # insert a dict
    def appendDict(self, data_dict : dict):
        for key in self.keys:
            try:
                self.__data_dict[key].append(data_dict[key])
            except:
                raise KeyError("dict insert is invalid")


    # returns the data in a pandas data frame
    def returnDataFrame(self) -> pd.DataFrame:
        return pd.DataFrame(self.__data_dict)

    # outputFileName parameter must be the name without the file extension (.xlsx, .txt)
    def createExcel(self, outputFileName : str):
        pd.DataFrame(self.__data_dict).to_excel(excel_writer=f'{outputFileName}.xlsx')

    def createCsv(self, outputFileName : str):
        pd.DataFrame(self.__data_dict).to_csv(path_or_buf=outputFileName+'.csv', index=False, line_terminator='\n')

    def show(self):
        print(pd.DataFrame(self.__data_dict))

    # TODO: implement the method createGraph to a GprofLogSet()
    
