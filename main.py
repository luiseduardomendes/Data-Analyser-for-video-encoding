import sys
from os import path, listdir
from source.gprof_executer import gprof_executer as gp_exe
import pandas as pd

# create a pandas series to generalize the paths used
temp =  pd.read_csv('source/server_paths.csv')
sv_path = temp['path']
sv_path = sv_path.set_axis(temp['dir'])

cfg_videos_dir = sv_path['vtm'] + '/cfg-files/'
satd_src = sv_path['repo'] + '/FilesForVVC/'
satd_dir = sv_path['commonlib']
out_videos_dir = sv_path['out']

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
