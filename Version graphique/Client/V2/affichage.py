

from tkinter import *

class Fenetre(Tk):
    def __init__(self, thread_read, thread_write):
        self.thread_read = thread_read
        self.thread_write = thread_write

        super().__init__()
        self.geometry("640x460")
        self.configureColumn()
        self.createFrame()
        self.initFrame1()
        self.initFrame2()
        self.initFrame4()
        self.gridFrame()
        self.run()

    def createFrame(self):
        self.frame1 = Frame(self, highlightbackground="black", highlightthickness=1) # Frame haut gauche
        self.frame2 = Frame(self, highlightbackground="black", highlightthickness=1) # Frame bas gauche
        self.frame3 = Frame(self, highlightbackground="black", highlightthickness=1) # Frame haut droite
        self.frame4 = Frame(self, highlightbackground="black", highlightthickness=1) # Frame bas droite

    def configureColumn(self):
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1,weight=5)
        self.rowconfigure(0, weight=9)
        self.rowconfigure(1,weight=4)

    def initFrame1(self):
        self.label1 = Label(self.frame1, text="PSEUDO") # Changer par le pseudo de la personne connecté
        self.label2 = Label(self.frame1, text="Information du seveur :") # Le texte suivant le deux point (:) sera variable (Ex: Information serveur : <ip serveur> <...>, ...)

        self.label1.pack(expand=YES)
        self.label2.pack(expand=YES)

    def initFrame2(self):
        self.label3 = Label(self.frame2, text="LOGO")
        self.label3.pack(expand=YES)

    def initFrame4(self):
        self.entry = Entry(self.frame4)
        self.button = Button(self.frame4, text="Envoyer")

        self.entry.pack(fill=X, expand=YES)
        self.button.pack()


    def gridFrame(self):
        self.frame1.grid(column=0,row=0, sticky='NESW')
        self.frame2.grid(column=0,row=1, sticky='NESW')
        self.frame3.grid(column=1, row=0, sticky='NESW')
        self.frame4.grid(column=1, row=1, sticky='NESW')

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    fenetre = Fenetre()