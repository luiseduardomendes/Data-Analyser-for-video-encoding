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

quant_param = [
        #22,
        #27,
        #32,
        37]
enc_cfgs = [
    #'encoder_intra_vtm.cfg',
    #'encoder_lowdelay_vtm.cfg',
    'encoder_randomaccess_vtm.cfg'
]

satd_settings = []
for (dirpath, dirnames, filenames) in os.walk(satd_src):
    satd_settings += [os.path.join(dirpath, file) for file in filenames]

pattern = re.compile(r'^/home/luispmendes/Data-Analyser-for-video-encoding/FilesForVVC/(.+)\.cpp$')

for settings in satd_settings:
    print("\nArquivo: " + settings, end='\n\n')
    setting_name = str(re.findall(pattern, settings)[0]).replace('/', '-').replace('(', '-').replace(')', '-').replace(' ', '-')

    if not os.path.isdir(out_videos_dir + setting_name):
        os.mkdir(out_videos_dir + setting_name)

    fileSubs(settings, satd_dir)
    os.system("cd /home/luispmendes/VVCSoftware_VTM/build/")
    os.system("cmake /home/luispmendes/VVCSoftware_VTM/ -DCMAKE_BUILD_TYPE=Release")
    os.system("make")
    os.system("cd /home/luispmendes/Data-Analyser-for-video-encoding/")

    for video in video_cfg[0:2]:
        for qp in quant_param:
            for cfg in enc_cfgs:
                gp_exe(cfg, cfg_videos_dir+video, video[:-4], qp, setting_name)












'''
'''



'''
    # convert the gprof file into a csv file
    # this can be usefull to use the same data after, so, 
    # its just necessary to read the gprof output file once
    # cause its run is very slow in comparison to the csv read
    gp_to_csv = gp.GprofToCSV(path_input=video)
    gp_to_csv.read_gprof_out()
    gp_to_csv.convert_data_frame_into_CSV()
    gp_to_csv.convert_data_frame_into_excel()

    gp_to_csv.data_frame_into_lists_for_plotter()

    funct = gp_to_csv.dict_data_by_class['class'][:100]
    percentTime = gp_to_csv.dict_data_by_class['percentageTime'][:100]

    plotter = tbp()
    plotter.barh(percentTime, funct);
    plotter.show()

    plotter = plt()
    plotter.insertLists(percentTime, 'percentageTime', funct, 'function')
    plotter.setOutputFileName(gp_to_csv.get_output_path(), quant_param[0], video_cfgs[0])
    plotter.plotBarhGraph()
    '''


# testes nao utilizados
'''gp_exe(enc_cfgs[1], cfg_videos_dir + video_cfg[5], video_cfg[5][:-4], quant_param[3], 10)

gp_to_csv = gp.GprofToCSV(path_input='/home/luispmendes/VVCSoftware_VTM/out/logs_gprof/gprof_log_'+video_cfg[5][:-4]+'.txt')
gp_to_csv.read_gprof_out()
gp_to_csv.convert_data_frame_into_CSV()

gp_exe(enc_cfgs[1], cfg_videos_dir + video_cfg[2], video_cfg[2][:-4], quant_param[3], 10)

gp_to_csv = gp.GprofToCSV(path_input='/home/luispmendes/VVCSoftware_VTM/out/logs_gprof/gprof_log_'+video_cfg[2][:-4]+'.txt')
gp_to_csv.read_gprof_out()
gp_to_csv.convert_data_frame_into_CSV()'''
