import  matplotlip as plt
#import matplotlib.pyplot as plt
from pandas import read_csv

import pandas as pd

Meta1 = pd.read_csv('metacritic-20141019-152743.csv')
#Удаление не нужных столбцов
Meta1 = Meta1.drop(columns=['link', 'genre', 'platform'])
print('Атрибуты ИГРЫ')
#print(Meta1.head())
#print(Meta1.shape)
#s=print(Meta1.shape)
#print(s)

# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', 7)

# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)

# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)


result = Meta1[(Meta1['title'] == 'Diablo')]
print(result)






'''
from tkinter import *


def insert_text():
    s = "Hello World"
    text.insert(1.0, s)

root = Tk()

text = Text(width=25, height=5)
text.pack()

frame = Frame()
frame.pack()
Button(frame, text="Вставить",
       command=insert_text).pack(side=LEFT)


label = Label()
label.pack()

root.mainloop()
'''
