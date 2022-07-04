import src.gprof_log_manipulation as gplog
from os.path import isfile
import src.gprof_log_graphs as gpGraph

f_path = 'filesTest/excelFiles/'
file1 = f_path + 'BasketballDrive.xlsx'
file2 = f_path + 'BasketballPass.xlsx'

#if isfile(file):

a = gplog.gprofLogSets(file1)
a.show()

b = gplog.gprofLogSets(file2)
b.show()

gpGraph.comparisonSets(a, b, ('qp', 'bitrate'))