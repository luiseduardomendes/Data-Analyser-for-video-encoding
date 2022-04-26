import os
import re
from fileSubstitution import fileSubs
from pprint import pprint
from src.gprof_executer import gprof_executer as gpexe

vtm_dir = '/home/luispmendes/VVCSoftware_VTM/'
satd_src = '/home/luispmendes/Data-Analyser-for-video-encoding/FilesForVVC/'
satd_dir = vtm_dir + 'source/Lib/CommonLib/'
cfg_dir = vtm_dir + 'cfg-files/'
enc_cfg = 'encoder_lowdelay_vtm.cfg'
video_cfg = cfg_dir + 'RaceHorses.cfg'

pattern = re.compile(r'^/home/luispmendes/Data-Analyser-for-video-encoding/FilesForVVC/(.+)\.cpp$')

satd_settings = []
for (dirpath, dirnames, filenames) in os.walk(satd_src):
    satd_settings += [os.path.join(dirpath, file) for file in filenames]

for settings in satd_settings:
    fileSubs(settings, satd_dir)
    print(f"cmake {vtm_dir} -DCMAKE_BUILD_TYPE=Release")
    print("make")
