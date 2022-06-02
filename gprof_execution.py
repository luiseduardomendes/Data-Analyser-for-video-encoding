import os
import re
import pandas as pd
from source.fileSubstitution import file_subs

# create a pandas series to generalize the paths used
    
temp = pd.read_csv('source/server_paths.csv')
sv_path = temp['path']
sv_path = sv_path.set_axis(temp['dir'])

pattern = re.compile(r'^FilesForVVC/(.+)$')

exec_buffer = '.execution_buffer.cache'

with open(exec_buffer, 'r') as f:
    file = pattern.findall(f.readline())[0]
    with open('temp' + exec_buffer, 'w') as out:
        for line in f:
            out.write(line)
        out.close()
    f.close()

os.system('rm {}'.format(exec_buffer))
os.system('mv {} {}'.format('./temp'+exec_buffer, './'+exec_buffer))

file_subs('FilesForVVC/'+file, sv_path["commonlib"])


os.system(f'cmake {sv_path["vtm"]} -DCMAKE_BUILD_TYPE=Release')
os.system('make')
os.system(f'cd {sv_path["repo"]}')

os.system('python3 main.py "{}"'.format(file))
