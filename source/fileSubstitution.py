from os.path import isdir, isfile
from os import system

def file_subs(file_path, destiny_dir) -> None:

    if __verify_path__(file_path):
        source_path = f'{file_path}'
    else:   
        raise Exception("invalid file path!")
    
    if __verify_dir__(destiny_dir):
        destiny_path = f'{destiny_dir}'
    else:   
        raise Exception("Destiny is not a directory!")

    system(f"cp \"{source_path}\" \"{destiny_path}RdCost.cpp\"") 

def __verify_path__(self, path:str) -> bool:
    if isfile(path):
        return True
    return False

def __verify_dir__(self, dir1 : str) -> bool:
    if isdir(dir1):
        return True
    return False
    
