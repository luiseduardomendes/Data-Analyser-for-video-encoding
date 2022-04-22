import src.gprof_out_manipulation as gp
import os
import re
from os import path, listdir, system
from src.gprof_executer import gprof_executer as gp_exe
from fileSubstitution import fileSubs

cfg_videos_dir = '/home/luispmendes/VVCSoftware_VTM/cfg-files/'
satd_src = '/home/luispmendes/Data-Analyser-for-video-encoding/FilesForVVC/'
satd_dir = '/home/luispmendes/VVCSoftware_VTM/source/Lib/CommonLib/'
out_videos_dir = '/home/luispmendes/VVCSoftware_VTM/out/'

video_cfg = [f for f in listdir(cfg_videos_dir) if path.isfile(path.join(cfg_videos_dir, f)) and f[-4:] == '.cfg']

quant_param = 37
enc_cfgs = 'encoder_lowdelay_vtm.cfg'

satd_settings = []
for (dirpath, dirnames, filenames) in os.walk(satd_src):
    satd_settings += [os.path.join(dirpath, file) for file in filenames]

pattern = re.compile(r'^/home/luispmendes/Data-Analyser-for-video-encoding/FilesForVVC/(.+)\.cpp$')

for settings in satd_settings:
    print("\nArquivo: " + settings, end='\n\n')
    setting_name = str(re.findall(pattern, settings)[0]).replace('/', '-').replace('(', '-').replace(')', '-').replace(' ', '-')

    fileSubs(settings, satd_dir)
    os.system("cd /home/luispmendes/VVCSoftware_VTM/build/")
    os.system("cmake /home/luispmendes/VVCSoftware_VTM/ -DCMAKE_BUILD_TYPE=Release")
    os.system("make")
    os.system("cd /home/luispmendes/Data-Analyser-for-video-encoding/")