from os import path, listdir
import re
from os import remove, rename

dir = '.'

files = [f for f in listdir(dir) if path.isfile(path.join(dir, f)) and f[-4:] == '.cfg']

pattern = re.compile(r'(/home/videos/)(/home/videos/)(.+)')

for f in files:
    data = open(f, 'r')
    new_data = open(f[:-4]+'_copy.cfg', 'w')
    for line in data:
        check = pattern.findall(line)
        if len(check) > 0:
            new_data.write('InputFile                     : ' + check[0][1]+check[0][2]+'\n')
        else:
            new_data.write(line)
    data.close()
    new_data.close()
    remove(f)
    rename(f[:-4]+'_copy.cfg', f)
    
