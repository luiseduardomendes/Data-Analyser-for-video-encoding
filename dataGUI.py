from os import name, terminal_size
from tkinter import *
from tkinter import font
from tkinter import ttk


root = Tk()

class Aplication():

    def __init__(self):
        self.root = root
        self.display()
        self.displayFrames()
        self.displayButtons()
        root.mainloop()
    
    def display(self):
        self.root.title("Analisador de dados")
        self.root.configure(background="#2c2d31")
        self.root.geometry("1280x720")
        self.root.resizable(False, False)
        
    def displayFrames(self):
        self.frame1 = Frame(self.root)
        self.frame1.configure(background="#393842", bd=4, relief="groove")
        self.frame1.place(relx=0.005, rely=0.01, relheight=0.98, relwidth=0.2475)

        self.frame2 = Frame(self.root)
        self.frame2.configure(background="#393842", bd=4, relief="groove")
        self.frame2.place(relx=0.2525, rely=0.01, relheight=0.98, relwidth=0.7475)

    def displayButtons(self):
        configsAvailableList = ["All Intra", "Low Delay", "Random Acces"]
        vConfig = StringVar()
        vConfig.set(configsAvailableList[0])
        self.cb_cfg = OptionMenu(self.frame1, vConfig, *configsAvailableList)
        ##self.cb_cfg.set("Configurações de codificação de Vídeo")
        self.cb_cfg.place(relx= 0.05, rely=0.05, relwidth=0.9, relheight=0.04)

        #plotOptionList = ["Comparação", "Top 20"]
        #self.opm_plot = OptionMenu(self.frame1, *plotOptionList)

        self.lb_videoAddress = Label(self.frame2, text="Endereço do vídeo", font="arial 11", fg="#a9a8a2")
        self.lb_videoAddress.configure(bg="#2c2d31")
        self.lb_videoAddress.place(relx= 0.05, rely=0.05, relwidth=0.9, relheight=0.04)

        self.entry_vidAddress = Entry(self.frame2,text="endereço do vídeo", font="arial 11")
        self.entry_vidAddress.configure
        self.entry_vidAddress.place(relx= 0.05, rely=0.1, relwidth=0.79, relheight=0.04)
        

        self.btn_confirmAddress = Button(self.frame2, text="Abrir", font="arial 11", command=lambda: self.btn_confirmAddress_pressed())
        self.btn_confirmAddress.place(relx= 0.86, rely=0.1, relwidth=0.09, relheight=0.04)
    
    def verifyFile(self, nameFile):
        try:
            open(file=self.nameFile, mode="r")
            return True
        except ValueError:
            return False

    def btn_confirmAddress_pressed(self):
        self.nameFile = self.entry_vidAddress.get()
        if not self.verifyFile(self.nameFile) == True:
            self.showErrorMessege()
            
    def showErrorMessage(self):
        self.lb_errorMessege = Label(self.frame2, text="Arquivo não encontrado", font="arial 20", fg="#a9a8a2")
        self.lb_errorMessege.configure(bg="#2c2d31")
        self.lb_errorMessege.place(relx= 0.3, rely=0.3, relwidth=0.4, relheight=0.04)
        
            


Aplication()



