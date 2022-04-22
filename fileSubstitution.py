from os.path import isdir, isfile
from os import system

class fileSubs:
    def __init__(self, file_path, destiny_dir) -> None:

        if self.__verify_path__(file_path):
            self.source_path = file_path
        else:   
            raise Exception("invalid file path!")

        
        if self.__verify_dir__(destiny_dir):
            self.destiny_path = destiny_dir
        else:   
            raise Exception("Destiny is not a directory!")

        system(f"cp \"{self.source_path}\" \"{self.destiny_path}RdCost.cpp\"")    

    def __verify_path__(self, path:str) -> bool:
        if isfile(path):
            return True
        return False

    def __verify_dir__(self, dir1 : str) -> bool:
        if isdir(dir1):
            return True
        return False
        
