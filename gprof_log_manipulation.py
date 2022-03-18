import re
import pandas as pd
class gprofLogManip():
    def __init__(self, datafile: str) -> None:
        if self.__verifyFile__(datafile):
            with open(datafile) as f:
                self._data_ = f.read()
                f.close()

        _data_ = re.findall(r'^\s+(\d+)\s+a\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+$', self._data_, flags=re.M)

        data_dict = {
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
                try:
                    data_dict[key] = int(log[i])
                except:
                    data_dict[key] = float(log[i])
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

    def returnDataFrame(self) -> pd.DataFrame:
        try:
            return pd.DataFrame(self.data_dict)
        except:
            raise Exception("data dict has not been set yet")

class gprofLogSets:
    pass
