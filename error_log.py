import src.gprof_out_manipulation as gp
import os
from os import path, listdir, system
from src.gprof_executer import gprof_executer as gp_exe
from fileSubstitution import fileSubs

cfg_videos_dir = '/home/luispmendes/VVCSoftware_VTM/cfg-files/'
satd_dir = '/home/luispmendes/VVCSoftware_VTM/source/Lib/CommonLib/'
satd_src = '/home/luispmendes/Data-Analyser-for-video-encoding/FilesForVVC/'

video_cfg = [f for f in listdir(cfg_videos_dir) if path.isfile(path.join(cfg_videos_dir, f)) and f[-4:] == '.cfg']

satd_settings = []
for (dirpath, dirnames, filenames) in os.walk(satd_src):
    satd_settings += [os.path.join(dirpath, file) for file in filenames]

os.system("cd /home/luispmendes/VVCSoftware_VTM/build")

for settings in satd_settings:

    fileSubs(settings, satd_dir)

    os.system("cmake -=release")
    os.system("make")
