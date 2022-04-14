import tkinter as tk
from tkinter import ttk
import re

import csv_module
from csv_module import Meta1, result

class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('1920x1080')
        self.label = tk.Label(self, text="Выборка по игре", font=("Arial Bold", 25))
        self.button = tk.Button(self, text="Новый поиск", command=self.destroy)
        #Расположение текста
        self.label.place(x=840, y=30)
        #Расположение конопки возврата на первый экран
        self.button.place(x=860, y=900, width=140, height=35)

class StartWindow(tk.Tk):


    def __init__(self):
        super().__init__()

        self.geometry('680x750')
        #Заголовок
        self.label = tk.Label(text="Выборка", font=("Arial Bold", 25))
        #self.label.place(x=40, y=100, width=650, height=30)
        #Поисковая сторка
        self.var3 = tk.StringVar()
        self.lbl = tk.Label(self, text="Поисковая строка", font=("Arial Bold", 15))
        self.lbl.place(x=20, y=175)
        self.txt = tk.Entry(width=30, textvariable=self.var3)
        #x = 20, y = 300
        #self.name = var3.get()
        self.txt.place(x=20, y=200, width=650, height=30)
        self.txt.focus()
        self.label.pack(padx=20,pady=20)
        #Режимы сортировки
        #self.combo = ttk.Combobox()
        #self.combo['values'] = (1, 2, 3, 4, 5)
        #self.combo.current(1)  # установите вариант по умолчанию
        #self.combo.place(x=1700, y=200, width=50, height=35)
        #Кнопка перехода во второе окно
        self.btn = tk.Button(self, text="Начать", bg="black", fg="red", command=self.open_window)
        self.btn.place(x=60, y=240, width=500, height=25)




        #Вывод в поле
        def insert_text():
          #s = "print(Meta1.shape)"
          self.text.insert(1.0, '=-----------------------------------------------------------------------------=\n')
          vr = Meta1[(Meta1['title'] == str(self.txt.get()))]
          self.text.insert(1.0, f'{vr}\n')
          info = 'Вся информация о игре: '
          self.text.insert(1.0, f'{info}\n')
          self.text.insert(1.0, '=-----------------------------------------------------------------------------=\n')
          #self.text.insert(2.0, f'{self.var3.get()}')


        #Размер рамки
        self.text = tk.Text(width=80, height=27, bg="blue", fg='white')
        self.text.place(x=20, y=300)
        self.frame = tk.Frame()
        self.frame.pack()
        self.b = tk.Button(self, text="Вставить", bg="black", fg="red", command=insert_text)
        self.b.place(x=60, y=272, width=500, height=25)








    def open_window(self):
        self.destroy()
        root = tk.Tk()
        root.title("Второе окно")
        root.geometry("400x300")
        #новое текстовое поле
        text = tk.Text(width=400, height=240)
        text.pack()
        text.insert(1.0, '00000000000000000000000000000000000000000\n')

        text.insert(3.0, csv_module.search(self.var3.get()))


        #root.mainloop()

    def print(self):
        pass


if __name__ == "__main__":
    app = StartWindow()
    app.mainloop()