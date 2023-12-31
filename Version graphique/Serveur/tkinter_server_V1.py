import tkinter as tk

window = tk.Tk()
window.geometry("720x480")

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=9)
window.columnconfigure(0, weight=10)

frame = tk.Frame(window)

title = tk.Label(window, text="TITRE")
label = tk.Label(frame, text="Port")
entry = tk.Entry(frame, textvariable=tk.StringVar())
button = tk.Button(frame, text="Valider") #Mettre la commande associé


label.pack()
entry.pack()
button.pack()



frame.grid(row=1)
title.grid(row=0, sticky='nesw')


def getEntry():
    value = entry.get()
    entry.delete(0, tk.END)
    return value

window.mainloop()
