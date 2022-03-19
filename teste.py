from csv import excel_tab
import csv
from unicodedata import name
import gprof_log_manipulation as gp
from os import listdir, path,mkdir
import re

directory = 'AI/'
files = [directory+f for f in listdir(directory) if path.isfile(path.join(directory, f))]

fileNames = []

namePattern = re.compile(r'AI/(.+)_QP\d{2}\.txt')

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
excel_dir = 'excelFiles'
csv_dir = 'csvFiles'

if not path.isdir(excel_dir):
    mkdir(excel_dir)
if not path.isdir(csv_dir):
    mkdir(csv_dir)

for name in fileNames:
    gpSetsNames[name].createExcel(excel_dir+'/'+name)
    gpSetsNames[name].createCsv(csv_dir+'/'+name)
