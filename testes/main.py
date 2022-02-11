
import gprof_out_manipulation as gp
from terminalPlotter import TerminalBarhPlotter as pltd

video_list = ['akiyo.txt', 'akiyo2.txt']

gp_to_csv = gp.GprofToCSV()
gp_to_csv.set_file_path(video_list[0])
gp_to_csv.convert_file()

gp_reader = gp.GprofOutCSVReader()
gp_reader.set_file_path(gp_to_csv.get_output_path())
gp_reader.functions_dict()
gp_reader.split_by_function()
funct = gp_reader.dict_data_by_class['class'][:20]
percentTime = gp_reader.dict_data_by_class['percentageTime'][:20]

plotter = pltd()
plotter.barh(percentTime, funct);
plotter.show()

