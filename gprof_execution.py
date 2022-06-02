import os
import re
import pandas as pd
import source.fileSubstitution as gpfs

# create a pandas series to generalize the paths used
with pd.read_csv('server_paths.csv') as temp:
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

gpfs.fileSubs(file, sv_path["vtm"]+"source/Lib/CommonLib/")

os.system(f'cd {sv_path["vtm"]+"build"}')
os.system('cmake .. -DCMAKE_BUILD_TYPE=Release')
os.system('make')
os.system(f'cd {sv_path["repo"]}')

os.system('python3 main.py "{}"'.format(file))