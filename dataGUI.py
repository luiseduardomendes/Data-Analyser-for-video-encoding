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
        self.root.geometry("1024x576")
        self.root.resizable(False, False)
        
    def displayFrames(self):
        self.frame1 = Frame(self.root)
        self.frame1.configure(background="#393842", bd=4, relief="groove")
        self.frame1.place(relx=0.005, rely=0.1, relheight=0.98, relwidth=0.245)

        self.frame2 = Frame(self.root)
        self.frame2.configure(background="#393842", bd=4, relief="groove")
        self.frame2.place(relx=0.255, rely=0.1, relheight=0.98, relwidth=0.74)

    def displayButtons(self):
        configsAvailableList = ["All Intra", "Low Delay", "Random Acces"]
        vConfig = StringVar()
        vConfig.set("Configurações de codificação")
        self.cb_cfg = OptionMenu(self.frame1, vConfig, *configsAvailableList)
        self.cb_cfg.configure(font="arial 10", bg="#393842", fg="#a9a8a2")
        ##self.cb_cfg.set("Configurações de codificação de Vídeo")
        self.cb_cfg.place(relx= 0.025, rely=0.01, relwidth=0.95, relheight=0.05)

        #plotOptionList = ["Comparação", "Top 20"]
        #self.opm_plot = OptionMenu(self.frame1, *plotOptionList)

        self.lb_videoAddress = Label(self.frame2, text="Endereço do vídeo", font="arial 11", fg="#a9a8a2")
        self.lb_videoAddress.configure(bg="#2c2d31")
        self.lb_videoAddress.place(relx= 0.01, rely=0.01, relwidth=0.98, relheight=0.05)

        self.entry_vidAddress = Entry(self.frame2,text="endereço do vídeo", font="arial 11")
        self.entry_vidAddress.configure
        self.entry_vidAddress.place(relx= 0.01, rely=0.07, relwidth=0.88, relheight=0.05)
        

        self.btn_confirmAddress = Button(self.frame2, text="Abrir", font="arial 11", command=lambda: self.btn_confirmAddress_pressed())
        self.btn_confirmAddress.place(relx= 0.9, rely=0.07, relwidth=0.09, relheight=0.05)
    
    def verifyFile(self, nameFile):
        try:
            with open(self.nameFile, 'r') as f:
                return True
        except IOError:
            return False

    def btn_confirmAddress_pressed(self):
        self.nameFile = self.entry_vidAddress.get()
        if self.verifyFile(self.nameFile) == True:
            self.ShowFileFoundMessage()
        else: 
            self.showErrorMessage()
            
    def showErrorMessage(self):
        
        self.lb_errorMessage = Label(self.frame2, text="Arquivo não encontrado\nclique em 'OK' para continuar", font="arial 13", fg="#a9a8a2", bd=5, relief="groove")
        self.lb_errorMessage.configure(bg="#2c2d31")
        self.lb_errorMessage.place(relx= 0.3, rely=0.3, relwidth=0.4, relheight=0.4)

        self.btn_OkFileNotFound = Button(self.frame2, text="OK",command=lambda: self.closeErrorMessage())
        self.btn_OkFileNotFound.place(relx=0.4, rely=0.6, relheight=0.05, relwidth=0.2)
    
    def closeErrorMessage(self):
        self.lb_errorMessage.place_forget()
        self.btn_OkFileNotFound.place_forget()

    def ShowFileFoundMessage(self):
        self.lb_videoFoundMessage = Label(self.frame2, text="Arquivo encontrado\nclique em 'OK' para continuar", font="arial 13", fg="#a9a8a2", bd=5, relief="groove")
        self.lb_videoFoundMessage.configure(bg="#2c2d31")
        self.lb_videoFoundMessage.place(relx= 0.3, rely=0.3, relwidth=0.4, relheight=0.4)

        self.btn_OkFileFound = Button(self.frame2, text="OK",command=lambda: self.closeFoundFileMessage())
        self.btn_OkFileFound.place(relx=0.4, rely=0.6, relheight=0.05, relwidth=0.2)
        
    def closeFoundFileMessage(self):
        self.lb_videoFoundMessage.place_forget()
        self.btn_OkFileFound.place_forget()
            


Aplication()



