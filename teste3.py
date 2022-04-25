import src.gprof_log_manipulation as gplog
from os.path import isfile
import src.gprof_log_graphs as gpGraph

f_path = 'filesTest/csvFiles/'
file = f_path + 'BasketballPass.csv'

#if isfile(file):

a = gplog.gprofLogManip(file)
a.show()

#gpGraph.comparisonSets()