from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo, showwarning

from os.path import exists

from parse import parse_document
from generate_json import generate_json


def get_json_and_announce(file_name, save_dir):
    if file_name == '':
        return showwarning('Внимание!', 'Выберите файл протокола!')
    if save_dir == '':
        return showwarning('Внимание!', 'Выберите папку сохранения JSON-файла!')
    if not exists(file_name):
        return showwarning('Внимание!', f'Файла {file_name} не существует!')
    if not exists(save_dir):
        return showwarning('Внимание!', f'Папки {save_dir} не существует!')
    json_name = generate_json(parse_document(file_name), save_dir)
    if json_name is None:
        return showwarning('Ошибка!', 'Не удалось сгенерировать JSON :(')
    return showinfo('Успех!', f'Файл {json_name} сохранён в папке {save_dir}')


class App(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()


def browse_file_path():
    file_name = filedialog.askopenfilename(initialdir = '/',
                                          title = "Выберите файл:",
                                          filetypes = (("Все документы",
                                                        "*.txt* *.docx*"),
                                                        ("Документы WORD",
                                                        "*.docx*"),
                                                        ("Документы TXT",
                                                        "*.txt*")
                                                        ))
    if file_name != '':
        file_name_label['text'] = file_name


def browse_save_dir():
    save_dir = filedialog.askdirectory(initialdir='/',
                                        title="Выберите папку:")
    if save_dir != '':
        save_dir_label['text'] = save_dir


myapp = App()

myapp.master.title("LAPIX")
myapp.master.geometry("700x160")

ttk.Label(myapp, text="Выберите файл протокола:").grid(column=0, row=0, columnspan=8, sticky='nsew')
ttk.Button(myapp, text="Обзор...", command=browse_file_path).grid(column=0, row=1, sticky='nsew')

file_name_label = ttk.Label(myapp)
file_name_label.grid(column=1, row=1, columnspan=7, sticky='nsew')

ttk.Label(myapp, text="Выберите папку для сохранения:").grid(column=0, row=2, columnspan=8, sticky='nsew')
ttk.Button(myapp, text="Обзор...", command=browse_save_dir).grid(column=0, row=3, sticky='nsew')

save_dir_label = ttk.Label(myapp)
save_dir_label.grid(column=1, row=3, columnspan=7, sticky='nsew')

ttk.Label(myapp).grid(column=0, row=4)

ttk.Button(myapp, width=110, text="Извлечь", command=lambda: get_json_and_announce(file_name_label['text'], save_dir_label['text'])).grid(column=0, row=5, columnspan=8, sticky='nsew')

myapp.mainloop()
