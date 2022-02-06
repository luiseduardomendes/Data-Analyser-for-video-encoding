import gprof_out_manipulation as gp

gp_to_csv = gp.GprofToCSV()
gp_to_csv.set_file_path('akiyo.txt')
gp_to_csv.set_file_output('akiyo.csv')
gp_to_csv.convert_file()


gp_reader = gp.GprofOutCSVReader()
gp_reader.set_file_path('akiyo.csv')
gp_reader.functions_dict()
gp_reader.split_by_function()
print(gp_reader.functions_dict())





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
