import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
import tkinter.ttk as ttk
import os
import re
from transmitter import Transmitter
from queue import Queue
from threading import Thread
import time


def check_queue():
    time.sleep(0.01)
    while queue.qsize():
        Prog_bar_w["value"] = queue.get()
        window.update()


def clicked_btn():
    string = r'(25[0-5]|2[0-4][0-9]|[0]|[1]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[0]|[1]?[0-9][0-9]?)){3}'
    ip = IP_entry.get()
    port = int(port_spin.get())
    buff_size = int(Buff_size_spin.get())
    file_name = open_file_entry.get()
    Prog_bar_w.configure(maximum=os.path.getsize(file_name) // buff_size)
    if re.fullmatch(string, ip) and 10000 < int(port) < 65535 and 100 <= int(buff_size) <= 8958 and file_name:
        sender = Transmitter(ip, file_name, buff_size, port)
        t = Thread(target=sender.send, args=(queue,))
        txt.insert("insert",
                   'Sending {} to {} at port {}, UDP data size - {}'.format(os.path.basename(file_name), ip, port,
                                                                            buff_size) + '\n')
        txt.yview('end')
        try:
            t.start()
            check_queue()
        except ConnectionRefusedError:
            txt.insert("insert", "Error" + '\n')
            txt.insert("insert", "-" * 70 + '\n')
            txt.yview('end')
            messagebox.showinfo("Ошибка", "Удаленный компьютер не отвечает")
            Prog_bar_w.stop()
            Prog_bar_w["value"] = 0
        else:
            txt.insert("insert", "Done" + '\n')
            txt.insert("insert", "-" * 70 + '\n')
            txt.yview('end')
            open_file_entry.delete(0, 'end')
            Prog_bar_w.stop()
            Prog_bar_w["value"] = 0
    else:
        messagebox.showinfo("Ошибка", "Некоректные данные сетевого соединения или не выбран файл")


def clicked_open_file():
    file = filedialog.askopenfilename()
    open_file_entry.delete(0, 'end')
    open_file_entry.insert("insert", file)



queue = Queue()

window = tk.Tk()
window.title("UDP Packet Sender")
window.geometry('700x450')

f_nw = tk.LabelFrame(text='Лог')
f_nw.pack(expand="no", fill='x')
txt = scrolledtext.ScrolledText(f_nw, width=80, height=12)
txt.pack(side='left', expand="yes", fill='x')

f_south = tk.LabelFrame(text='Управление')
f_south.pack(expand="yes", fill='both')

f_net_param = tk.LabelFrame(f_south, text='Параметры сетевого соединения')
f_net_param.pack(expand="no")

f_IP = tk.LabelFrame(f_net_param, text='IP адрес', labelanchor='n')
f_IP.pack(side='left', anchor='n')
IP_entry = tk.Entry(f_IP, width=14)
IP_entry.insert('end', '127.0.0.1')
IP_entry.pack(side='bottom', padx=5, pady=5)

f_Port = tk.LabelFrame(f_net_param, text='Порт(10000-65535)', labelanchor='n')
f_Port.pack(side='left', anchor='n')
var = tk.IntVar()
var.set(37777)
port_spin = tk.Spinbox(f_Port, from_=10000, to=65535, width=10, textvariable=var)
port_spin.pack(side='bottom', padx=5, pady=5)

f_buff_size = tk.LabelFrame(f_net_param, text='Размер буффера UDP(100-8952)', labelanchor='n')
f_buff_size.pack(side='left', anchor='n')
var = tk.IntVar()
var.set(8950)
Buff_size_spin = tk.Spinbox(f_buff_size, from_=100, to=8952, width=10, textvariable=var)
Buff_size_spin.pack(side='bottom', padx=5, pady=5)

f_file = tk.LabelFrame(f_south, text='Файл для отправки', labelanchor='n')
f_file.pack(side='top', anchor='center')
open_file_entry = tk.Entry(f_file, width=70)
open_file_entry.pack(side='left', padx=5, pady=5)
btn_open_file = tk.Button(f_file, text="Open File", command=clicked_open_file)
btn_open_file.pack(side='left')

btn = tk.Button(f_south, text="Отправить", command=clicked_btn)
btn.pack(side='top')

Prog_bar = tk.LabelFrame(f_south, text='Прогресс', labelanchor='n')
Prog_bar.pack(side='top', anchor='n')
Prog_bar_w = ttk.Progressbar(Prog_bar, orient="horizontal", length=500, mode="determinate", value=0)
Prog_bar_w.pack(side='top')

window.mainloop()
