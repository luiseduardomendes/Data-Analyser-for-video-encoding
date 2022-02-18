
from datetime import datetime

from sqlalchemy import func
import gprof_out_manipulation as gp
from terminalPlotter import TerminalBarhPlotter as pltd
from plotterData import Plotter
import os

video_list = ['akiyo.txt']
quant_param = [27,29,31,33]
video_cfgs = ['all intra', 'random access', 'low delay']


for video in video_list:
    # for qp in quant_param:
        # for cfg in video_cfgs:
            # gp_to_csv = gp.GprofToCSV()
            # gp_to_csv.initialize_path(file_path=f'{video}_{qp}_{cfg}_{datetime.today}')
            # gp_reader = gp.GprofOutCSVReader(gp_to_csv.get_output_path())


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

    plotter = pltd()
    plotter.barh(percentTime, funct);
    plotter.show()

    plotter = Plotter()
    plotter.insertLists(percentTime, 'percentageTime', funct, 'class')
    plotter.setOutputFileName(gp_to_csv.get_output_path(), 31, 'all_intra')
    plotter.plotBarhGraph()

# qp [22,27,32,37]