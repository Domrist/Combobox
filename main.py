from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Combobox example")
root.geometry("250x200")


def selected(event):
    selection = combobox.get()
    print(selection)


teachers = ["Katya", "Vyachek", "Vera", "Sveta"]
combobox = ttk.Combobox(values=teachers, state="readonly")
combobox.pack(anchor=NW, fill=X, padx=5, pady=5)
combobox.bind("<<ComboboxSelected>>", selected)
print("Programm started")
root.mainloop()