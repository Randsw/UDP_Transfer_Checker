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
txt = ScrolledText.ScrolledText(window, width=40, height=10)
btn = tkinter.Button(window, text="Клик", command=clicked_btn)
btn_open_file = tkinter.Button(window, text="Open File", command=clicked_open_file)
btn.grid(column=3, row=0)
btn_open_file.grid(column=3, row=1)
txt.grid(column=0, row=0)
window.mainloop()
