import tkinter as tk
from tkinter import ttk
import re

import csv_module
from csv_module import Meta1, result

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
        self.b = tk.Button(self, text="Вся информация о игре", bg="black", fg="red", command=insert_text)
        self.b.place(x=60, y=272, width=500, height=25)


    def open_window(self):
        self.destroy()
        root = tk.Tk()
        root.title("Второе окно")
        root.geometry("950x700")
        #новое текстовое поле
        text = tk.Text(width=113, height=60, bg="blue", fg='white')
        text.pack()
        text.insert(1.0, f"Искал по игре: {self.var3.get()}\n")
        text.insert(2.0, 'Максимально похожие игры по metacritic:\n')

        text.insert(3.0, csv_module.nahod(self.var3.get()))

        esc = tk.Button(root, text="Начальный экран", bg="black", fg="red", command=lambda:[root.destroy(), StartWindow()])
        esc.place(x=60, y=240, width=500, height=25)





        #root.mainloop()

    def print(self):
        pass


if __name__ == "__main__":
    app = StartWindow()
    app.mainloop()