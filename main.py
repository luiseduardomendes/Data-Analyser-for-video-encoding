
from datetime import datetime
import gprof_out_manipulation as gp
from terminalPlotter import TerminalBarhPlotter as tbp
from plotterData import Plotter as plt
import os
from os import path, listdir, system
from gprof_executer import gprof_executer as gp_exe


cfg_videos_dir = '/home/luispmendes/cfg-files/'
output_dir = '/home/luispmendes/output/'
video_cfg = [f for f in listdir(cfg_videos_dir) if path.isfile(f) and f[-4:] == '.cfg']

quant_param = [22,27,32,37]
enc_cfgs = [
    'encoder_intra_vtm.cfg',
    'encoder_lowdelay_vtm.cfg',
    'encoder_randomaccess_vtm.cfg'
]


for video in video_cfg:
    for qp in quant_param:
        for cfg in enc_cfgs:
            exec = gp_exe(cfg, cfg_videos_dir+video, output_dir, video[:-4], qp)
            # gp_to_csv = gp.GprofToCSV()
            # gp_to_csv.initialize_path(file_path=f'{video}_{qp}_{cfg}_{datetime.today}')
            # gp_reader = gp.GprofOutCSVReader(gp_to_csv.get_output_path())


    # convert the gprof file into a csv file
    # this can be usefull to use the same data after, so, 
    # its just necessary to read the gprof output file once
    # cause its run is very slow in comparison to the csv read
    '''gp_to_csv = gp.GprofToCSV(path_input=video)
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