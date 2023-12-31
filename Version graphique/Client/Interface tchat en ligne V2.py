from tkinter import *

fenetre = Tk()
fenetre.geometry("640x460")

frame1 = Frame(fenetre, highlightbackground="black", highlightthickness=1) # Frame haut gauche
frame2 = Frame(fenetre, highlightbackground="black", highlightthickness=1) # Frame bas gauche
frame3 = Frame(fenetre, highlightbackground="black", highlightthickness=1) # Frame haut droite
frame4 = Frame(fenetre, highlightbackground="black", highlightthickness=1) # Frame bas droite


fenetre.columnconfigure(0, weight=2)
fenetre.columnconfigure(1,weight=5)
fenetre.rowconfigure(0, weight=9)
fenetre.rowconfigure(1,weight=4)

label1 = Label(frame1, text="PSEUDO") # Changer par le pseudo de la personne connecté
label2 = Label(frame1, text="Information du seveur :") # Le texte suivant le deux point (:) sera variable (Ex: Information serveur : <ip serveur> <...>, ...)


label3 = Label(frame2, text="LOGO")


entry = Entry(frame4)
button = Button(frame4, text="Envoyer")


label1.pack(expand=YES)
label2.pack(expand=YES)

label3.pack(expand=YES)

entry.pack(fill=X, expand=YES)
button.pack()


frame1.grid(column=0,row=0, sticky='NESW')
frame2.grid(column=0,row=1, sticky='NESW')
frame3.grid(column=1, row=0, sticky='NESW')
frame4.grid(column=1, row=1, sticky='NESW')

fenetre.mainloop()
