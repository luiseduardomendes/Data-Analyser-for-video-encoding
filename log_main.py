import source.gprof_log_manipulation as gplog
from pathlib import Path
import os
import sys

out_path = '.execution_buffer.cache'
dir_path = 'FilesForVVC/'

files_list = [str(f) for f in Path(dir_path).rglob('*.cpp')]

with open(out_path, 'w') as f:
    for line in files_list:
        f.write(line + '\n')
    f.close()


