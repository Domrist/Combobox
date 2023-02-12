from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Combobox example")
root.geometry("250x200")


def selected(event):
    selection = combobox.get()
    print(selection)


Game = ["Fortnite", "CS", "Geometry_dash", "Diyng_lite"]
combobox = ttk.Combobox(values=Game, state="readonly")
combobox.pack(anchor=NW, fill=X, padx=5, pady=5)
combobox.bind("<<ComboboxSelected>>", selected)
print("Programm started")
root.mainloop()