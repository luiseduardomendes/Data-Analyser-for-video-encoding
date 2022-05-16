import source.gprof_out_manipulation as gp
import sys
import os
from os import path, listdir, system
from source.gprof_executer import gprof_executer as gp_exe
from source.fileSubstitution import fileSubs

cfg_videos_dir = '/home/luispmendes/VVCSoftware_VTM/cfg-files/'
satd_src = '/home/luispmendes/Data-Analyser-for-video-encoding/FilesForVVCNEW/'
satd_dir = '/home/luispmendes/VVCSoftware_VTM/source/Lib/CommonLib/'
out_videos_dir = '/home/luispmendes/VVCSoftware_VTM/out/'

video_cfg = [f for f in listdir(cfg_videos_dir) if path.isfile(path.join(cfg_videos_dir, f)) and f[-4:] == '.cfg']

quant_param = [
        22,
        27,
        32,
        37]
enc_cfgs = [
    'encoder_intra_vtm.cfg',
    'encoder_lowdelay_vtm.cfg',
    'encoder_randomaccess_vtm.cfg'
]


setting_name = sys.argv[1]

for video in video_cfg:
    for qp in quant_param:
        for cfg in enc_cfgs:
            gp_exe(cfg, cfg_videos_dir+video, video[:-4], qp, setting_name)