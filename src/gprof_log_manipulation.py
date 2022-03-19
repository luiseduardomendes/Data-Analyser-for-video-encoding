import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class gprofLogManip():
    def __init__(self, datafile: str) -> None:
        # verify if 
        if self.__verifyFile__(datafile):
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
                    data_dict[key] = re.findall(r'AI/(.+)_QP\d{2}.txt', datafile)[0]
                elif key == 'qp':
                    data_dict[key] = int(re.findall(r'AI/.+_QP(\d{2}).txt', datafile)[0])
                else:
                    try:
                        data_dict[key] = int(log[i-2])
                    except:
                        data_dict[key] = float(log[i-2])
            self.dataDict = data_dict
            
        elif len(_data_) == 0:
            self.dataDict = data_dict
            return data_dict
        
        else:
            raise Exception("File has more than one execution log")



    def __verifyFile__(self, filename) -> bool:
        if len(re.findall(r'(.+)(?!(?:\.txt$)|(?:\.gplog$))', filename)) > 0:
            return True
        else:
            return False
    
    
    
    def returnDict(self) -> dict:
        try:
            return self.dataDict
        except:
            raise Exception("data dict has not been set yet")



class gprofLogSets:
    keys = ('fileName', 'qp', 'frames', 'bitrate', 'Y_PSNR', 'U_PSNR', 'V_PSNR', 'YUV_PSNR')

    # initialize the dict
    def __init__(self) -> None:
        self.__data_dict = {}

        for key in self.keys:
            self.__data_dict[key] = []
    
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

    # TODO: implement the method createGraph to a GprofLogSet()
    
def createGraph(x_list, y_list, videos, outputFileName : str, title : str = '', xlabel : str = '' , ylabel : str = ''):
    x_axis = []
    y_axis = []

    try:
        for x in x_list:
            x_axis.append(np.array(x))
        for y in y_list:
            y_axis.append(np.array(y))
        
        if len(x_axis) != len(y_axis) or len(x_axis) != len(videos):
            raise Exception("number of y and x axis are not the same")

        for i in range(len(x_axis)):
            if len(x_axis[i]) != len(y_axis[i]):
                raise Exception("size of lists are not the same")

    except:
        raise Exception("Objects for axis are not valid")
    
    for i in range(len(x_axis)):
        t = True
        k = len(x_axis[i]) - 1
        while t == True:
            t = False
            for j in range(k):
                if x_axis[i][j] > x_axis[i][j+1]:
                    b = x_axis[i][j]
                    c = y_axis[i][j]
                    x_axis[i][j] = x_axis[i][j+1]
                    y_axis[i][j] = y_axis[i][j+1]
                    x_axis[i][j+1] = b
                    y_axis[i][j+1] = c
                    t = True
            k -= 1

            
                

            


    fig, ax = plt.subplots()
    
    for i in range(len(x_axis)):
        ax.scatter(x_axis[i], y_axis[i], label=videos[i])
        ax.plot(x_axis[i], y_axis[i], label=videos[i])
        

    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    ax.legend()
    ax.grid()
    fig.savefig(outputFileName+'.png')
    
    


    
