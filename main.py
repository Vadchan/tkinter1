import tkinter as tk
#from tkinter.ttk import Combobox

class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('1920x1080')
        self.label = tk.Label(self, text="Выборка по игре")
        self.button = tk.Button(self, text="Закрыть", command=self.destroy)

        self.label.pack(padx=20, pady=20)
        self.button.pack(pady=5, ipadx=2, ipady=2)

class StartWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1920x1080')
        self.label = tk.Label(text="Выборка", font=("Arial Bold", 25))
        self.label.grid(column=0, row=0)
        self.txt = tk.Entry( width=30)
        self.txt.grid(column=1, row=0)
        self.txt.focus()
        '''
        self.combo = tk.Combobox()
        self.combo['values'] = (1, 2, 3, 4, 5)
        self.combo.current(1)  # установите вариант по умолчанию
        self.combo.grid(column=2, row=0)
        '''
        self.btn = tk.Button(self, text="Начать", command=self.open_window)
        self.btn.grid(column=3, row=0)

    def open_window(self):
        about = About(self)
        about.grab_set()

if __name__ == "__main__":
    app = StartWindow()
    app.mainloop()