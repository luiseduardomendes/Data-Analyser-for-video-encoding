import os

exec_buffer = '.execution_buffer.cache'

with open(exec_buffer, 'r') as f:
    file = f.readline()
    with open('temp' + exec_buffer, 'w') as out:
        for line in f:
            out.write(line)
        out.close()
    f.close()

os.system('rm {}'.format(exec_buffer))
os.system('mv {} {}'.format('./temp'+exec_buffer, './'+exec_buffer))

os.system('python3 main.py "{}"'.format(file))