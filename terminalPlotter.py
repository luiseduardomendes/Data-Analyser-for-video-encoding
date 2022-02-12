import os

class TerminalBarhPlotter:
    __terminalSize__ = int()
    __dataYaxis__ = list() # names = string
    __dataXaxis__ = list() # values = float
    __color__ = str()
    __bgColor__ = str()    
    
    def __init__(self, color='', bgColor=''):
        self.__color__ = color
        self.__bgColor__ = bgColor
        self.__terminalSize__= os.get_terminal_size()
        self.__terminalSizeX = self.__terminalSize__.columns
        self.__terminalSizeY = self.__terminalSize__.lines
        

    def barh(self, xValues: list, yValues: list):
        self.__dataXaxis__ = xValues
        self.__dataYaxis__ = yValues
        self.__setSize__()

    def __setSize__(self):
        maxValue = max(self.__dataXaxis__)
        if maxValue != 0:
            self.__proportion__ = (self.__terminalSizeX - 50) / maxValue
        else:
            self.__proportion__ = 0
        
    def show(self):
        for i in range(0, len(self.__dataYaxis__)):
            if(i % 2 == 0):
                print('\033[32:40m', end='')
            else:
                print('\033[33:40m', end='')
            print(f'{self.__dataYaxis__[i]:48}[', end='')
            print('#'*int(self.__proportion__*self.__dataXaxis__[i]),end='')
            print(']')
        print('\033[m', end='')