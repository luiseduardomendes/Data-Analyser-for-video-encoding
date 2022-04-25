import fileSubstitution as fs
import os

satd_src = 'FilesForVVC/'

satd = []
for (dirpath, dirnames, filenames) in os.walk(satd_src):
    satd += [os.path.join(dirpath, file) for file in filenames]

for f in satd:
    fs.fileSubs(f, 'testeFsubs/')
    input()
    
