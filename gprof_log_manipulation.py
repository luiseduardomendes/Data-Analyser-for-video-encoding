import re

class gprofLogManip():
    def __init__(self, datafile: str) -> None:
        if self.__verifyFile__(datafile):
            with open(datafile) as f:
                self.data = f.read()
                f.close()
        
    def __verifyFile__(self, filename) -> bool:
        if len(re.findall(r'(?=.txt^|.gplog^)', filename)) > 0:
            return True
        else:
            return False

    def returnInfo(self) -> dict:
        _data_ = re.findall(r'^\s+(\d+)\s+a\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)$')
        
        data_list = []
        data_dict = {
            'bitrate' : int,
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

            data_list.append(data_dict.copy())
        elif len(_data_) == 0:
            return None
        
        else:
            raise Exception("File has more than one execution log")


        return data_list
            
