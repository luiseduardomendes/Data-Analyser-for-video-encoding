from gprof_out_reader import GprofOutReader
from plotterData import Plotter

d = GprofOutReader("akiyo.txt")

p = Plotter()
p.insertLists(d.dataListsPerFunctionForPlotter['function'], 'function',
            d.dataListsPerFunctionForPlotter['percentageTime'], 'percentageTime')
p.setOutputFileName("akiyo", '30', 'all_intra')
p.plotBarhGraph()