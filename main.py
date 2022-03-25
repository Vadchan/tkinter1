import tkinter as tk
from tkinter import ttk


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
        self.geometry('1920x1080')
        #Заголовок
        self.label = tk.Label(text="Выборка", font=("Arial Bold", 25))
        self.label.grid(column=0, row=0)
        #Поисковая сторка
        self.txt = tk.Entry(width=30)
        self.txt.place(x=200, y=200, width=1500, height=35)
        self.txt.focus()
        self.label.pack(padx=20,pady=20)
        #Режимы сортировки
        self.combo = ttk.Combobox()
        self.combo['values'] = (1, 2, 3, 4, 5)
        self.combo.current(1)  # установите вариант по умолчанию
        self.combo.place(x=1700, y=200, width=50, height=35)
        #Кнопка перехода во второе окно
        self.btn = tk.Button(self, text="Начать", command=self.open_window)
        self.btn.place(x=700, y=250, width=500, height=25)
        self.text = tk.Text(width=232, height=30, bg="darkgreen", fg='white')
        self.text.place(x=20, y=500)

    def open_window(self):
        about = About(self)
        about.grab_set()
    def print(self):
        pass

if __name__ == "__main__":
    app = StartWindow()
    app.mainloop()
