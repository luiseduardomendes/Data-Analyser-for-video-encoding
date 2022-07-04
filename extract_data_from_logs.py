from numpy import array
import source.gprof_log_manipulation as gp
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

# group same video logs in the same data set
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
    gpSetsNames[name].createExcel(excel_dir+'/'+name)
    gpSetsNames[name].createCsv(csv_dir+'/'+name)

    df = gpSetsNames[name].returnDataFrame()
    data_lists.append(df.to_dict('list'))

