from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Combobox example")
root.geometry("250x200")


def selected(event):
    selection = combobox.get()
    print(selection)


Art = ["Шишкин", "Пушкин", "Толстой", "Шолохов"]
combobox = ttk.Combobox(values=Art, state="readonly")
combobox.pack()
combobox.bind("<<ComboboxSelected>>", selected)
print("Programm started")
root.mainloop()