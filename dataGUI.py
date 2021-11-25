from tkinter import *
from tkinter import font


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
        
    def displayFrames(self):
        self.frame1 = Frame(self.root)
        self.frame1.configure(background="#393842", bd=4, relief="groove")
        self.frame1.place(relx=0.005, rely=0.01, relheight=0.98, relwidth=0.2475)

        self.frame2 = Frame(self.root)
        self.frame2.configure(background="#393842", bd=4, relief="groove")
        self.frame2.place(relx=0.2525, rely=0.01, relheight=0.98, relwidth=0.7475)

    def displayButtons(self):
        self.btn_cfg = Button(self.frame1, text="Configuração do vídeo", font="Arial 18")
        self.btn_cfg.place(relx= 0.05, rely=0.05, relwidth=0.9, relheight=0.05)

        self.lb_videoAddress = Label(self.frame2, text="endereço do vídeo", font="arial 18", fg="#a9a8a2")
        self.lb_videoAddress.configure(bg="#2c2d31")
        self.lb_videoAddress.place(relx= 0.05, rely=0.05, relwidth=0.9, relheight=0.05)

        self.entry_vidAddress = Entry(self.frame2,text="endereço do vídeo", font="arial 18")
        self.entry_vidAddress.configure
        self.entry_vidAddress.place(relx= 0.05, rely=0.12, relwidth=0.79, relheight=0.05)

        self.btn_confirmAddress = Button(self.frame2, text="Abrir", font="Arial 18")
        self.btn_confirmAddress.place(relx= 0.86, rely=0.12, relwidth=0.09, relheight=0.05)
Aplication()
