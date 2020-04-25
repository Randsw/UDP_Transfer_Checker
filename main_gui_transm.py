import tkinter
import tkinter.scrolledtext as ScrolledText
from tkinter import filedialog
import os


def clicked_btn():
    txt.insert("insert", 'Текстовое поле' + '\n')
    pass


def clicked_open_file():
    file = filedialog.askopenfilename()
    txt.insert("insert", os.path.basename(file) + '\n')
    return file


window = tkinter.Tk()
window.title("Welcome to Python3 GUI")
window.geometry('600x450')

f_nw = tkinter.LabelFrame(text='Лог')
f_nw.pack(side='left', anchor='nw')


txt = ScrolledText.ScrolledText(f_nw, width=70, height=12)
txt.pack(side='left')

IP_label = tkinter.Label(window, width=15, height=1, text='IP адрес')
IP_label.pack(side='bottom')
Port_label = tkinter.Label(window, width=15, height=1, text='Номер порта')
Port_label.pack(side='bottom')
Buff_size_label = tkinter.Label(window, width=20, height=1, text='Размер данных в UDP')
Buff_size_label.pack(side='bottom')
open_file_label = tkinter.Label(window, width=20, height=1, text='Файл для отправки')
open_file_label.pack(side='bottom')

IP_entry = tkinter.Entry(window, width=10)
IP_entry.pack(side='bottom')
Port_entry = tkinter.Entry(window, width=10)
Port_entry.pack(side='bottom')
Buff_size_entry = tkinter.Entry(window, width=10)
Buff_size_entry.pack(side='bottom')
open_file_entry = tkinter.Entry(window, width=100)
open_file_entry.pack(side='bottom')

btn = tkinter.Button(window, text="Клик", command=clicked_btn)
btn.pack(side='bottom')
btn_open_file = tkinter.Button(window, text="Open File", command=clicked_open_file)
btn_open_file.pack(side='bottom')




window.mainloop()
