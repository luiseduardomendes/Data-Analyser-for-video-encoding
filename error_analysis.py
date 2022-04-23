import os
from fileSubstitution import fileSubs
from pprint import pprint


vtm_dir = '/home/luispmendes/VVCSoftware_VTM/'
satd_src = '/home/devluis/Área de Trabalho/vvcprojects/Data-Analyser-for-video-encoding/FilesForVVC/'
satd_dir = vtm_dir + 'source/Lib/CommonLib/'

print(os.path.isdir(satd_src))

satd_settings = []
for (dirpath, dirnames, filenames) in os.walk(satd_src):
    satd_settings += [os.path.join(dirpath, file) for file in filenames]

pprint(satd_settings)
'''
for settings in satd_settings:
    print("\nArquivo: " + settings, end='\n\n')
    fileSubs(settings, satd_dir)
    os.system(f"cmake {vtm_dir} -DCMAKE_BUILD_TYPE=Release")
    os.system("make")
'''