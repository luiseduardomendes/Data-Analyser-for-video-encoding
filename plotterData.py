from matplotlib import pyplot as plt
from os import path, system
from datetime import datetime

class Plotter:
    __parametersDict__ = {
        'percentageTime' : 'Execution Time',
        'function' : 'Function',
        'cumulativeTime' : 'Cumulative Time',
        'selfSeconds' : 'Self Seconds',
        'calls' : 'Calls',
        'selfMs/call' : 'Self ms/call',
        'totalMs/call' : 'Total ms/call',
        'class' : 'Class'
    }

    __cfgsInGraph = {
        'all_intra' : 'All Intra',
        'low_delay' : 'Low Delay',
        'random_access' : 'Random Access'
    }
    
    def __init__(self): 
        pass

    def insertLists(self, dataListX, dataListXName, dataListY, dataListYName):
        self.__plotterListX = dataListX
        self.__plotterListY = dataListY
        self.__plotterListXName = self.__parametersInGraph[dataListXName]
        self.__plotterListYName = self.__parametersInGraph[dataListYName]
        self.__outputNameX = dataListXName
        self.__outputNameY = dataListYName

    def setOutputFileName(self, outputFileName, quantParam, cfg):
        self.__outputFileName = outputFileName
        self.__quantParam = quantParam
        self.__cfg = self.__cfgsInGraph[cfg]
        self.__fileName = f'plot_{self.__outputNameX}_by_{self.__outputNameY}_{outputFileName}_QP_{quantParam}_cfg_{cfg}_{datetime.today()}.png'
    
    def __createFolder(self): 
        if not path.isdir(f'output/{self.__outputFileName}'):
            system(f'mkdir output/{self.__outputFileName}')

    def __setGraphTitle(self):
        self.__title = f'{self.__plotterListXName} by {self.__plotterListYName} using QP {self.__quantParam} and config {self.__cfg}'

    def plotBarhGraph(self):
        self.__setGraphTitle()
        self.__createFolder()
        plt.style.use('ggplot')
        plt.figure(figsize=(12.8, 7.2))

        plt.title(self.__title, fontsize=18)

        plt.xlabel(self.__plotterListXName) 
        plt.ylabel(self.__plotterListYName)    

        plt.tight_layout()

        plt.barh(self.__plotterListX, self.__plotterListY, color='#acbccc')

        plt.subplots_adjust(left=0.2)

        plt.savefig(f'output/{self.__outputFileName}/plot_{self.__outputNameX}_by_{self.__outputNameY}_{self.__fileName}')        

        plt.show()
