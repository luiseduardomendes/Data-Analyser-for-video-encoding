from os import listdir, path
from os.path import join
import source.gprof_log as gplog
import re
import sys

try:
    folder = sys.argv[1]
except:
    raise Exception('you must enter the folder path which countains the data')

file_path = [f for f in listdir(folder) if path.isfile(join(folder, f))]
file_path

pattern = re.compile(r'^(.+)QP(\d{2}).+$')

data_set = {}
files_found = []

for file in file_path:
    check = pattern.findall(file)[0]
    file_name = check[0]
    qp = int(check[1])
    if file_name not in files_found:
        files_found.append(file_name)
        data_set[file_name] = []
    data_set[file_name].append(gplog.read_log(join(folder, file), qp))

data_frame = {}
for file_name in files_found:
    data_frame[file_name] = gplog.group_by_filename(data_set[file_name])
    data_frame[file_name].to_csv('log'+file_name+'.csv', index=False)
