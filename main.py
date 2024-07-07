from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from parse import parse_document
from generate_json import generate_json


class App(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()


def browseFiles():
    file_name = filedialog.askopenfilename(initialdir = "/",
                                          title = "Выберите файл:",
                                          filetypes = (("Все документы",
                                                        "*.txt* *.docx*"),
                                                        ("Документы WORD",
                                                        "*.docx*"),
                                                        ("Документы TXT",
                                                        "*.txt*")
                                                        ))
    if file_name != '':
        file_name_entry.delete(0, END)
        file_name_entry.insert(0, file_name)


myapp = App()

myapp.master.title("LAPIX")
myapp.master.geometry("700x100")

ttk.Label(myapp, text="Выберите файл:").grid(column=0, row=0, columnspan=8, sticky='nsew')
file_name_entry = ttk.Entry(myapp)
file_name_entry.grid(column=0, row=1, columnspan=7, sticky='nsew')
ttk.Button(myapp, text="Обзор...", command=browseFiles).grid(column=7, row=1, sticky='nsew')
ttk.Button(myapp, width=110, text="Извлечь", command=myapp.destroy).grid(column=0, row=2, columnspan=8, sticky='nsew')

myapp.mainloop()

generate_json(parse_document('file.docx'))