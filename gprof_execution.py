import os
import re

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

os.system('cd /home/luispmendes/VVCSoftware_VTM/source/Lib/CommonLib/') 
os.system('make')
os.system('python3 /home/luispmendes/Data-Analyser-for-video-encoding/main.py "{}"'.format(file))
