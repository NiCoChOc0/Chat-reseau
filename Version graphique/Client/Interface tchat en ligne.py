from tkinter import *

fenetre = Tk()
fenetre.geometry("640x460")

frame1 = Frame(fenetre)
frame2 = Frame(fenetre)


fenetre.columnconfigure(0, weight=2)
fenetre.columnconfigure(1,weight=5)
fenetre.columnconfigure(2, weight=7)
fenetre.rowconfigure(0, weight=9)
fenetre.rowconfigure(1,weight=8)
fenetre.rowconfigure(2,weight=3)

label1 = Label(frame1, text="Hello World") # Changer "Hello World" par un pseudo qui peut varier
label1.pack()

label2 = Label(frame1, text="Information du seveur :") # Le texte suivant le deux point (:) sera variable (Ex: Information serveur : <ip serveur> <...>, ...)
label2.pack(pady=20)


frame1.grid(column=0,row=0)
frame2.grid(column=0,row=1)

fenetre.mainloop()

# Méthode pour saisir un message:
##value = StringVar()
##value.set("Saisie ton message")
##entree = Entry(fenetre, textvariable=string, width=30)
##entree.pack()

