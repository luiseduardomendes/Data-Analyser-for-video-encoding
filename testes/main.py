
from gprof_out_reader import GprofOutReader
from plotterData import Plotter
from terminalPlotter import TerminalBarhPlotter

d = GprofOutReader("akiyo.txt")

'''p = Plotter()
p.insertLists(d.dataListsPerFunctionForPlotter['function'], 'function',
            d.dataListsPerFunctionForPlotter['percentageTime'], 'percentageTime')
p.setOutputFileName("akiyo", '30', 'all_intra')
p.plotBarhGraph()'''

b = TerminalBarhPlotter()
b.barh( xValues=d.dataListsPerFunctionForPlotter['percentageTime'],
        yValues=d.dataListsPerFunctionForPlotter['function']) 
b.show()
