from gprof_out_manipulation import GprofToCSV
from os import path, listdir
import pandas as pd

path_dir = '/home/luispmendes/VVCSoftware_VTM/out/logs_gprof/'

files = [f for f in listdir(path_dir) if path.isfile(path.join(path_dir, f)) and f[-4:] == '.csv']

dict_functions = {}

gp = GprofToCSV(path_dir+files[0])
gp.gprof_read_csv() 
bufferDataFrame = gp.get_data_frame()
bufferDataFrame = bufferDataFrame.to_dict()
for key in bufferDataFrame.keys():
    dict_functions[key] = []

print(dict_functions)

for f in files:
    gp = GprofToCSV(path_dir+f)
    gp.gprof_read_csv()
    bufferDataDict = gp.get_data_frame().to_dict()
    
    bufferDataDict = gp.__to_list_of_struct__(bufferDataDict)

    for dict_elem in bufferDataDict:
        if dict_functions['function'].count(dict_elem['function']) > 0:
            for key in dict_functions.keys():
                if type(dict_elem[key]) != str:
                    dict_functions[key][dict_functions['function'].index(dict_elem['function'])] += dict_elem[key]
        else:
            for key in dict_functions.keys():
                dict_functions[key].append(dict_elem[key])

dataFrame = pd.DataFrame.from_dict(dict_functions)
print(dataFrame)
