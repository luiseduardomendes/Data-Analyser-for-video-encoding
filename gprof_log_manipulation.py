import re
import pandas as pd

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
                    data_dict[key] = datafile
                else:
                    try:
                        data_dict[key] = int(log[i-1])
                    except:
                        data_dict[key] = float(log[i-1])
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
    keys = ('fileName', 'frames', 'bitrate', 'Y_PSNR', 'U_PSNR', 'V_PSNR', 'YUV_PSNR')

    # initialize the dict
    def __init__(self) -> None:
        self.__data_dict = {}

        for key in self.keys:
            self.__data_dict[key] = []
    
    # insert a 
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
