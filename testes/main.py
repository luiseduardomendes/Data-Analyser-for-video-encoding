from matplotlib.pyplot import plot
import gprof_out_manipulation as gp
from terminalPlotter import TerminalBarhPlotter as pltd

gp_to_csv = gp.GprofToCSV()
gp_to_csv.set_file_path('akiyo.txt')
gp_to_csv.set_file_output('akiyo.csv')
gp_to_csv.convert_file()

gp_reader = gp.GprofOutCSVReader()
gp_reader.set_file_path('akiyo.csv')
gp_reader.functions_dict()
gp_reader.split_by_function()
funct = gp_reader.dict_data_by_funct['function'][:20]
percentTime = gp_reader.dict_data_by_funct['percentageTime'][:20]
#print(i for i in gp_reader.functions_dict().values())
#print(gp_reader.functions_dict())

plotter = pltd()
plotter.barh(percentTime, funct);
#plotter.show()


'''d = GprofOutReader("akiyo.txt")
d.displayPercentageTime()

p = Plotter()
p.insertLists(d.dataListsPerFunctionForPlotter['function'], 'function',
            d.dataListsPerFunctionForPlotter['percentageTime'], 'percentageTime')
p.setOutputFileName("akiyo", '30', 'all_intra')
p.plotBarhGraph()'''

'''b = TerminalBarhPlotter()
b.barh( xValues=d.dataListsPerFunctionForPlotter['percentageTime'],
        yValues=d.dataListsPerFunctionForPlotter['function']) 
b.show()'''
