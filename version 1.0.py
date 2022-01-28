from os import name, system, terminal_size
import sys
from tkinter import *
from tkinter import font
from tkinter import ttk
import re
from matplotlib import pyplot as plt
import os
from PIL import Image, ImageTk
from matplotlib.animation import Animation


root = Tk()

class Aplication():

    videoAddres = str
    quantizationParameter = int
    numberOfFrames = int
    configuration = str

    def __init__(self):
        self.root = root
        self.display()
        self.displayFrames()
        self.placeButtons()
        root.mainloop()

    def display(self):
        self.root.title("Analisador de dados")
        self.root.configure(background="#2c2d31")
        self.root.geometry("1024x576")
        self.root.resizable(False, False)

    def displayFrames(self):
        self.frame1 = Frame(self.root)
        self.frame1.configure(background="#393842", bd=4, relief="groove")
        self.frame1.place(relx=0.005, rely=0.01, relheight=0.98, relwidth=0.245)

        self.frame2 = Frame(self.root)
        self.frame2.configure(background="#393842", bd=4, relief="groove")
        self.frame2.place(relx=0.255, rely=0.01, relheight=0.98, relwidth=0.74)

    # LABELS

    def labelQuantizationParameter(self):
        self.lb_qParameter = Label(self.frame1, text="Parâmetro de quantização", font="arial 11", fg="#a9a8a2")
        self.lb_qParameter.configure(bg="#2c2d31")
        self.lb_qParameter.place(relx= 0.025, rely=0.08, relwidth=0.95, relheight=0.05)

    def labelNumberOfFrames(self):
        self.lb_frames = Label(self.frame1, text="Número de frames", font="arial 11", fg="#a9a8a2")
        self.lb_frames.configure(bg="#2c2d31")
        self.lb_frames.place(relx= 0.025, rely=0.21, relwidth=0.95, relheight=0.05)

    def labelVideoAddress(self):
        self.lb_videoAddress = Label(self.frame2, text="Endereço do vídeo", font="arial 11", fg="#a9a8a2")
        self.lb_videoAddress.configure(bg="#2c2d31")
        self.lb_videoAddress.place(relx= 0.01, rely=0.01, relwidth=0.98, relheight=0.05)

    # ENTRIES

    def configsSelectBox(self):
        configsAvailableList = ["All Intra", "Low Delay", "Random Acces"]
        self.vConfig = StringVar()
        self.vConfig.set("Configurações de codificação")
        self.cb_cfg = OptionMenu(self.frame1, self.vConfig, *configsAvailableList)
        self.cb_cfg.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        self.cb_cfg.place(relx= 0.025, rely=0.01, relwidth=0.95, relheight=0.05)

    def entryVideoAddress(self):
        self.entry_vidAddress = Entry(self.frame2,text="endereço do vídeo", font="arial 11")
        self.entry_vidAddress.place(relx= 0.01, rely=0.07, relwidth=0.88, relheight=0.05)

    def buttonConfirmAddress(self):
        self.btn_confirmAddress = Button(self.frame2, text="Abrir", font="arial 11", command=lambda: self.btn_confirmAddress_pressed())
        self.btn_confirmAddress.place(relx= 0.9, rely=0.07, relwidth=0.09, relheight=0.05)

    def buttonPlotGraph(self):
        self.btn_plotGraph = Button(self.frame1, text="Plotar gráfico", font="arial 11", command=lambda: self.callPlotCreator())
        self.btn_plotGraph.configure(font="arial 11", bg="#393842", fg="#a9a8a2")
        self.btn_plotGraph.place(relx= 0.025, rely=0.5, relwidth=0.95, relheight=0.05)

    def entryQuantizationParameter(self):
        self.entry_qParameter = Entry(self.frame1,text="Parâmetro de quantização", font="arial 11")
        self.entry_qParameter.configure
        self.entry_qParameter.place(relx= 0.025, rely=0.14, relwidth=0.95, relheight=0.05)

    def entryNumberOfFrames(self):
        self.entry_frames = Entry(self.frame1,text="Número de frames", font="arial 11")
        self.entry_frames.configure
        self.entry_frames.place(relx= 0.025, rely=0.27, relwidth=0.95, relheight=0.05)

    def buttonCreateTXT(self):
        self.btn_createTXT = Button(self.frame1, text="Criar arquivo de texto de saída", font="arial 11", command=lambda: system("gprof EncoderAppStatic gmon.out >> akiyo.txt"))
        open('akiyo.txt', 'w')
        self.btn_createTXT.place(relx= 0.025, rely=0.6, relwidth=0.95, relheight=0.05)

    # FUNCTIONS

    def callPlotCreator(self):
        self.numberOfFrames = int(self.entry_frames.get())
        self.quantizationParameter = int(self.entry_qParameter.get())
        self.configuration = self.vConfig.get()

        if self.numberOfFrames <= 0:
            self.showErrorMessage("Número de Frames inválido \naperte OK para continuar")

        elif self.quantizationParameter <= 0 or self.quantizationParameter > 63:
            self.showErrorMessage("Parâmetro de quantização inválido\naperte OK para continuar")

        elif self.configuration == "Configurações de codificação":
            self.showErrorMessage("Selecione uma configuração\naperte OK para continuar")

        else:
            if self.configuration == "All Intra":
                #cfg = "/home/devluis/Área de Trabalho/VVCSoftware_VTM/bin/encoder_intra_vtm.cfg"
                cfg = "../cfg/encoder_intra_vtm.cfg"
            elif self.configuration == "Low Delay":
                #cfg = "/home/devluis/Área de Trabalho/VVCSoftware_VTM/bin/encoder_lowdelay_vtm.cfg"
                cfg = "../cfg/encoder_lowdelay_vtm.cfg"
            elif self.configuration == "Random Acces":
                #cfg = "/home/devluis/Área de Trabalho/VVCSoftware_VTM/bin/encoder_randomaccess_vtm.cfg"
                cfg = "../cfg/encoder_randomaccess_vtm.cfg"
        system(r'./EncoderAppStatic -c '+ cfg +' -i "' + self.videoAddres + '" -b out.bin -q ' + str(self.quantizationParameter) + ' -f ' + str(self.numberOfFrames) + ' -fr 60 -wdt 176 -hgt 144 --Level=2.1')
        system('gprof EncoderAppStatic gmon.out >> akiyo.txt')
        self.createPlotGraph()
        self.showPlot()
        
            # C:/Users/dudup/OneDrive/Área de Trabalho/VVCSoftware_VTM/bin/akiyo_qcif.y4m
    def placeButtons(self):
        self.configsSelectBox()
        self.entryQuantizationParameter()
        self.entryNumberOfFrames()
        self.entryVideoAddress()
        self.buttonConfirmAddress()
        self.buttonPlotGraph()
        #self.buttonCreateTXT()

        self.labelQuantizationParameter()
        self.labelNumberOfFrames()
        self.labelVideoAddress()

    def verifyFile(self, nameFile):
        try:
            with open(nameFile, 'r') as f:
                return True
        except IOError:
            return False

    def btn_confirmAddress_pressed(self):
        self.videoAddres = self.entry_vidAddress.get()
        if self.verifyFile(self.videoAddres) == False:
            self.showErrorMessage("Arquivo não encontrado, \nclique em OK para continuar")
        else:
            self.showErrorMessage("Arquivo aberto com sucesso, \nclique em OK para continuar")

    def showErrorMessage(self, message):
        
        self.lb_showErrorMessage = Label(self.frame2, text=message, font="arial 13", fg="#a9a8a2", bd=5, relief="groove")
        self.lb_showErrorMessage.configure(bg="#2c2d31")
        self.lb_showErrorMessage.place(relx= 0.3, rely=0.3, relwidth=0.4, relheight=0.4)

        self.btn_closeErrorMessage = Button(self.frame2, text="OK",command=lambda: self.closeErrorMessage())
        self.btn_closeErrorMessage.place(relx=0.4, rely=0.6, relheight=0.05, relwidth=0.2)

    def closeErrorMessage(self):
        self.lb_showErrorMessage.place_forget()
        self.btn_closeErrorMessage.place_forget()

    def createPlotGraph(self):
        data = open('akiyo.txt')
        stringList = data.read()

        pattern = re.compile(r'([\d]+\.[\d]+)[ ]+([\d]+\.[\d]+)[ ]+([\d]+\.[\d]+|[ ]+)[ ]+([\d]+|[ ]+)[ ]+([\d]+\.[\d]+|[ ]+)[ ]+([\d]+\.[\d]+|[ ]+)[ ]+(.+)')
        check = pattern.findall(stringList)

        namePatternFunction = re.compile(r'.+\(')


        structBuffer = dict()
        dataList = list()

        for i in check:
            
            structBuffer['percentage time'] = i[0]
            structBuffer['cumulative time'] = i[1]
            structBuffer['self seconds'] = i[2]
            
            if i[3] != ' ':
                structBuffer['calls'] = int(i[3])
            else:
                structBuffer['calls'] = -1
            
            if i[4] != ' ':
                structBuffer['self ms/call'] = float(i[4])
            else:
                structBuffer['self ms/call'] = -1.00
            
            if i[5] != ' ':
                structBuffer['total ms/call'] = float(i[5])
            else:
                structBuffer['total ms/call'] = -1.00

            structBuffer['name'] = i[6]    

            dataList.append(structBuffer.copy())

        #for i in range(0,20):
            #print(f"{dataList[i]['percentage time']:8}{dataList[i]['cumulative time']:8}{dataList[i]['self seconds']:8}{dataList[i]['calls']:12}{dataList[i]['self ms/call']:8}{dataList[i]['total ms/call']:8}\t{dataList[i]['name']}")

        percentageTime = []
        nameFunctions = []

        for i in range(0,20):
            percentageTime.append(dataList[i]['percentage time'][:])
            nameFunctions.append(namePatternFunction.findall(dataList[i]['name'])[0][:])
            print(percentageTime[i] + ' ' + nameFunctions[i])

        percentageTime.reverse()
        nameFunctions.reverse() 

        plt.style.use('ggplot')
        plt.figure(figsize=(12.8, 7.2))

        plt.title('Functions', fontsize=16)
        plt.xlabel('Percentage time')
        
        
        yticks = [i for i in nameFunctions]

        plt.tight_layout()

        plt.barh(yticks, percentageTime)

        plt.subplots_adjust(left=0.5)

        plt.savefig('plot.png')

        percentageTime.clear()
        nameFunctions.clear()

        

        plt.show()

        

        # /home/devluis/Área de Trabalho/VVCSoftware_VTM/bin/akiyo_qcif.y4m

    def showPlot(self):
        self.amostra = ImageTk.PhotoImage(Image.open("plot.png"))
        self.plot = self.amostra
        Label(self.frame2, image=self.plot).place(relx= 0.01, rely=0.15, relwidth=0.98, relheight=0.8)

Aplication()
