import tkinter as tk
import tkinter.scrolledtext as ScrolledText
from tkinter import filedialog
from tkinter import messagebox
import os
import re


def clicked_btn():
    string = r'(25[0-5]|2[0-4][0-9]|[0]|[1]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[0]|[1]?[0-9][0-9]?)){3}'
    IP = IP_entry.get()
    port = Port_entry.get()
    buff_size = Buff_size_entry.get()
    if re.fullmatch(string, IP) and 10000 < int(port) < 65535 and 100 <= int(buff_size) <= 8958:
        txt.insert("insert", 'Текстовое поле' + '\n')
    else:
        messagebox.showinfo("Ошибка", "Некоректные данные сетевого соединения")


def clicked_open_file():
    file = filedialog.askopenfilename()
    txt.insert("insert", os.path.basename(file) + '\n')
    open_file_entry.insert("insert", file)
    return file


window = tk.Tk()
window.title("UDP Packet Sender")
window.geometry('700x450')

f_nw = tk.LabelFrame(text='Лог')
f_nw.pack(expand="no", fill='x')
txt = ScrolledText.ScrolledText(f_nw, width=80, height=12)
txt.pack(side='left', expand="yes", fill='x')

f_south = tk.LabelFrame(text='Управление')
f_south.pack(expand="yes", fill='both')

f_net_param = tk.LabelFrame(f_south, text='Параметры сетевого соединения')
f_net_param.pack(expand="no")

f_IP = tk.LabelFrame(f_net_param, text='IP адрес', labelanchor='n')
f_IP.pack(side='left', anchor='n')
IP_entry = tk.Entry(f_IP, width=14)
IP_entry.pack(side='bottom', padx=5, pady=5)

f_Port = tk.LabelFrame(f_net_param, text='Порт(10000-65535)', labelanchor='n')
f_Port.pack(side='left', anchor='n')
Port_entry = tk.Entry(f_Port, width=10)
Port_entry.pack(side='bottom', padx=5, pady=5)

f_buff_size = tk.LabelFrame(f_net_param, text='Размер буффера UDP(100-8952)', labelanchor='n')
f_buff_size.pack(side='left', anchor='n')
Buff_size_entry = tk.Entry(f_buff_size, width=10)
Buff_size_entry.pack(side='bottom', padx=5, pady=5)

f_file = tk.LabelFrame(f_south, text='Файл для отправки', labelanchor='n')
f_file.pack(side='top', anchor='center')
open_file_entry = tk.Entry(f_file, width=70)
open_file_entry.pack(side='left', padx=5, pady=5)
btn_open_file = tk.Button(f_file, text="Open File", command=clicked_open_file)
btn_open_file.pack(side='left')

btn = tk.Button(f_south, text="Отправить", command=clicked_btn)
btn.pack(side='top')

window.mainloop()
