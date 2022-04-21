import tkinter as tk
from tkinter import ttk

import csv_module
from csv_module import Meta1

class StartWindow(tk.Tk):


    def __init__(self):
        super().__init__()
        #Размер и цвет окна
        self.geometry('680x750')
        self.configure(bg='#856ff8')

        #Заголовок
        self.label = tk.Label(text="Выборка по metacritic", background="#856ff8", font=("Arial Bold", 25))
        #self.label.place(x=40, y=100, width=650, height=30)

        #Поисковая сторка
        self.var3 = tk.StringVar()
        self.lbl = tk.Label(self, text="Поисковая строка", background='#856ff8', font=("Arial Bold", 15))
        self.lbl.place(x=20, y=90)
        self.txt = tk.Entry(width=30, textvariable=self.var3)
        self.txt.place(x=20, y=117, width=650, height=30)
        self.txt.focus()
        self.label.pack(padx=20, pady=20)

        #Кнопка перехода во второе окно
        self.btn = tk.Button(self, text="Начать", bg="black", fg="red", command=self.open_window)
        self.btn.place(x=60, y=240, width=550, height=25)

        #Кнопка перехода в третье окно
        self.btn = tk.Button(self, text="Пользователь", bg="black", fg="red", command=self.window3)
        self.btn.place(x=60, y=208, width=550, height=25)

        # Кнопка перехода в четвёртое окно
        self.btn = tk.Button(self, text="Вся информация о таблице", bg="black", fg="red", command=self.information)
        self.btn.place(x=60, y=178, width=550, height=25)



        #Вывод в поле
        def insert_text():

          self.text.insert(1.0, '=-----------------------------------------------------------------------------=\n')
          vr = Meta1[(Meta1['title'] == str(self.txt.get()))]
          self.text.insert(1.0, f'{vr}\n')
          info = 'Вся информация о игре: '
          self.text.insert(1.0, f'{info}\n')
          self.text.insert(1.0, '=-----------------------------------------------------------------------------=\n')
          #self.text.insert(2.0, f'{self.var3.get()}')


        #Размер и цвет текстового поля
        self.text = tk.Text(width=80, height=27, bg="#4169E1", fg='white')
        self.text.place(x=20, y=300)
        self.frame = tk.Frame()
        self.frame.pack()

        #Кнопка записи в тестовое поле
        self.b = tk.Button(self, text="Вся информация о игре", bg="black", fg="red", command=insert_text)
        self.b.place(x=60, y=272, width=550, height=25)


    def open_window(self):
        #Зарываем предыдущее окно
        self.destroy()
        #Создание нового окна
        root = tk.Tk()
        root.title("Второе окно")
        root.geometry("950x700")
        root.configure(bg='#856ff8')
        #Новое текстовое поле
        text = tk.Text(width=113, height=40, bg="#4169E1", fg='white')
        text.pack()
        text.insert(1.0, f"Искал по игре: {self.var3.get()}\n")
        text.insert(2.0, 'Максимально похожие игры по metacritic:\n')

        text.insert(3.0, csv_module.nahod(self.var3.get()))

        esc = tk.Button(root, text="Начальный экран", bg="black", fg="red", command=lambda:[root.destroy(), StartWindow()])
        esc.place(x=20, y=660, width=910, height=35)

    def information(self):
        # Зарываем предыдущее окно
        self.destroy()
        # Создание нового окна
        inf = tk.Tk()
        inf.title("Четвёртое окно")
        inf.geometry("680x750")
        inf.configure(bg='#856ff8')
        #Новое текстовое поле
        text = tk.Text(width=80, height=43, bg="#4169E1", fg='white')
        text.pack()

        text.insert(3.0, csv_module.infor())

        esc = tk.Button(inf, text="Начальный экран", bg="black", fg="red",
                        command=lambda: [inf.destroy(), StartWindow()])
        esc.place(x=10, y=710, width=655, height=35)

    def window3(self):
        # Зарываем предыдущее окно
        self.destroy()
        # Создание нового окна
        zoom = tk.Tk()
        zoom.title("Третье окно")
        zoom.geometry("1300x500")
        zoom.configure(bg='#856ff8')
        zoom.lbl = tk.Label(zoom, text="Первое значение: ",background="#856ff8", font=("Arial Bold", 10))
        zoom.lbl.place(x=20, y=10)
        zoom.lbl = tk.Label(zoom, text="Второе значение: ",background="#856ff8", font=("Arial Bold", 10))
        zoom.lbl.place(x=20, y=40)
        zoom.lbl = tk.Label(zoom, text="Жанр игры: ",background="#856ff8", font=("Arial Bold", 10))
        zoom.lbl.place(x=20, y=70)
        #Первое значение
        zoom.combo1 = ttk.Combobox()
        zoom.combo1['values'] = (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
        59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
        87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100)

        zoom.combo1.current(0)  # установите вариант по умолчанию
        zoom.combo1.place(x=130, y=10, width=40, height=25)

        #Второе значение
        zoom.combo2 = ttk.Combobox()
        zoom.combo2['values'] = (
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
            58,
            59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
            86,
            87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100)

        zoom.combo2.current(80)  # установите вариант по умолчанию
        zoom.combo2.place(x=130, y=40, width=40, height=25)

        #Жанр игр
        zoom.combo3 = ttk.Combobox()
        zoom.combo3['values'] = ('Real-Time Strategy','Action RPG', 'Sim', 'Arcade', 'Modern Jet',
        'Other Shooters', 'Historic', 'Turn-Based Strategy', 'Sci-Fi', 'Puzzle',
        'Adventure Games', '3D', 'General', '2D', 'Modern', 'Platformers',
        'Miscellaneous', 'Fantasy', 'Other Strategy Games', 'Role-Playing',
        'Formula One', 'GT / Street', 'Stock Car', 'Street', 'Racing',
        'Rally / Offroad', 'Motocross', 'Kart', 'Futuristic', 'Small Spaceship',
        'Futuristic Combat Sims', 'Large Spaceship', 'Futuristic Jet', 'WWII',
        'Combat Sims', 'Tank', 'Ship', 'Civilian Plane', 'Train', 'Submarine', 'Tycoon',
        'First-Person Shooters', 'Tactical Shooters', 'Action', 'Wrestling',
        "Beat-'Em-Up", 'Scrolling', 'Rail', 'Static', 'Light Gun', 'Shooter',
        'First-Person', 'MOBA', 'Compilation', 'Fighting Games', 'Music',
        'Simulations', 'Helicopter', 'Military', 'WWI', 'Old Jet', 'Fighting',
        'Action Adventure', 'Interactive Movie', 'Horror', 'Tennis', 'Soccer',
        'Management', 'Other Sports Games', 'Baseball', 'Basketball', 'Surfing',
        'Alternative Sports', 'Olympic Sports', 'Snowboarding', 'Golf', 'Other',
        'Skateboarding', 'Biking', 'Billiards', 'Volleyball', 'Hunting', 'Rugby',
        'Football', 'Bowling', 'Hockey', 'Truck', 'On-foot', 'Virtual Life',
        'Futuristic Sub', 'Mech', 'Breeding/Constructing', 'PC-style RPG',
        'Massively Multiplayer', 'Console-style RPG')


        zoom.combo3.current(0)  # установите вариант по умолчанию
        zoom.combo3.place(x=93, y=70, width=150, height=25)

        text = tk.Text(width=100, height=30,  bg="#4169E1", fg='white')
        text.pack()
        text.insert(1.0, f"Первое значение: {zoom.combo1.get()}\n")
        text.insert(2.0, f'Второе значение:{zoom.combo2.get()}\n')

        def callbackFunc1(event):
            text.delete("1.0", "end")
            text.insert(1.0, f"Первое значение: {zoom.combo1.get()}\n")
        zoom.combo1.bind("<<ComboboxSelected>>", callbackFunc1)

        def callbackFunc2(event):
            text.insert(2.0, f"Второе значение: {zoom.combo2.get()}\n")
        zoom.combo2.bind("<<ComboboxSelected>>", callbackFunc2)

        def callbackFunc3(event):
            text.insert(3.0, f"Жанр: {zoom.combo3.get()}\n")
            text.insert(4.0, csv_module.zom1(zoom.combo1.get(), zoom.combo2.get(), zoom.combo3.get()))
        zoom.combo3.bind("<<ComboboxSelected>>", callbackFunc3)

        esc = tk.Button(zoom, text="Начальный экран", bg="black", fg="red",
                        command=lambda: [zoom.destroy(), StartWindow()])
        esc.place(x=20, y=100, width=160, height=35)


        #root.mainloop()

    def print(self):
        pass


if __name__ == "__main__":
    app = StartWindow()
    app.mainloop()