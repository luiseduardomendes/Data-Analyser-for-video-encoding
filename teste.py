from numpy import array
import src.gprof_log_manipulation as gp
from os import listdir, path,mkdir
import pandas as pd
import re
from pprint import pprint

directory = 'filesTest/AI/'
files = [directory+f for f in listdir(directory) if path.isfile(path.join(directory, f))]

fileNames = []

namePattern = re.compile(r'filesTest/AI/(.+)_QP\d{2}\.txt')

# make a list with all video names
for f in files:
    name = namePattern.findall(f)[0]
    if name not in fileNames:
        fileNames.append(name)

# make a gprof_log_set to every name in list
gpSetsNames = {}
for name in fileNames:
    gpSetsNames[name] = gp.gprofLogSets()

#
for f in files:
    elem = gp.gprofLogManip(f)
    name = namePattern.findall(f)[0]
    gpSetsNames[name].appendDict(elem.returnDict())

# directory to storage the excel and csv files
excel_dir = 'filesTest/excelFiles'
csv_dir = 'filesTest/csvFiles'
graph_dir = 'filesTest/graphFiles'

if not path.isdir(excel_dir):
    mkdir(excel_dir)
if not path.isdir(csv_dir):
    mkdir(csv_dir)
if not path.isdir(graph_dir):
    mkdir(graph_dir)

data_lists = []

for name in fileNames:
    #gpSetsNames[name].createExcel(excel_dir+'/'+name)
    #gpSetsNames[name].createCsv(csv_dir+'/'+name)

    df = gpSetsNames[name].returnDataFrame()
    data_lists.append(df.to_dict('list'))

parameter = 'V_PSNR'
gp.createGraph(
    [data_lists[0]['qp'], data_lists[1]['qp'], data_lists[2]['qp']], 
    [data_lists[0][parameter], data_lists[1][parameter], data_lists[2][parameter]], 
    [data_lists[0]['fileName'][0], data_lists[1]['fileName'][0], data_lists[2]['fileName'][0]], 
    data_lists[0]['fileName'][0], 'Video ' + data_lists[0]['fileName'][0] + ' encoding', 'quantization parameter', parameter)

