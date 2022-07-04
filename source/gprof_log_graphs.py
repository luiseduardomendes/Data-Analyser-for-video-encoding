from logging import raiseExceptions
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import source.gprof_log_manipulation as gplog


mnemonics = {
    'qp' : 'Quantization Parameter',
    'bitrate' : 'Bitrate',
    'Y_PSNR' : 'Y_PSNR', 
    'U_PSNR' : 'U_PSNR', 
    'V_PSNR' : 'V_PSNR', 
    'YUV_PSNR' : 'YUV_PSNR'
}


def createGraph(x_list, y_list, videos, outputFileName : str, title : str = '', xlabel : str = '' , ylabel : str = ''):
    x_axis = []
    y_axis = []

    try:
        for x in x_list:
            x_axis.append(np.array(x))
        for y in y_list:
            y_axis.append(np.array(y))
        
        if len(x_axis) != len(y_axis) or len(x_axis) != len(videos):
            raise Exception("number of y and x axis are not the same")

        for i in range(len(x_axis)):
            if len(x_axis[i]) != len(y_axis[i]):
                raise Exception("size of lists are not the same")

    except:
        raise Exception("Objects for axis are not valid")
    
    for i in range(len(x_axis)):
        t = True
        k = len(x_axis[i]) - 1
        while t == True:
            t = False
            for j in range(k):
                if x_axis[i][j] > x_axis[i][j+1]:
                    b = x_axis[i][j]
                    c = y_axis[i][j]
                    x_axis[i][j] = x_axis[i][j+1]
                    y_axis[i][j] = y_axis[i][j+1]
                    x_axis[i][j+1] = b
                    y_axis[i][j+1] = c
                    t = True
            k -= 1


    fig, ax = plt.subplots()
    
    for i in range(len(x_axis)):
        ax.scatter(x_axis[i], y_axis[i], label=videos[i])
        ax.plot(x_axis[i], y_axis[i])
        

    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    ax.legend()
    ax.grid()
    fig.savefig(outputFileName+'.png')
    
    


def comparisonSets(set1 : gplog.gprofLogSets, set2 : gplog.gprofLogSets, parameters : tuple):
    d = [set1.returnDataFrame().to_dict('list'), set2.returnDataFrame().to_dict('list')]

    if len(parameters) != 2 or any(type(p) != str for p in parameters):
        raise Exception('the parameters must be a tuple with 2 comparison parameters')

    x_param, y_param = parameters
    
    fig, ax = plt.subplots()

    for d1 in d:

        x_axis = d1[x_param]
        y_axis = d1[y_param]

        t = True
        k = len(x_axis) - 1
        while t == True:
            t = False
            for j in range(k):
                if x_axis[j] > x_axis[j+1]:
                    b = x_axis[j]
                    c = y_axis[j]
                    x_axis[j] = x_axis[j+1]
                    y_axis[j] = y_axis[j+1]
                    x_axis[j+1] = b
                    y_axis[j+1] = c
                    t = True
            k -= 1


        x_axis = np.array(x_axis)
        y_axis = np.array(y_axis)
    
        ax.scatter(x_axis, y_axis, label=f'{d1["fileName"][0]}')
        ax.plot(x_axis, y_axis)


    ax.set(title=f'{mnemonics[y_param]} by {mnemonics[x_param]}', xlabel=mnemonics[x_param], ylabel=mnemonics[y_param])
    ax.legend()
    ax.grid()
    
    
    fig.savefig(f'{d[0]["fileName"][0]}_{d[1]["fileName"][0]}_{x_param}_{y_param}.png')


