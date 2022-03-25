import matplotlib.pyplot as plt
from pandas import read_csv


Meta1 = read_csv('metacritic-20141019-152743.csv')
print(Meta1["platform"].value_counts().head())
print('Атрибуты файла')
print(Meta1.head())
print(Meta1.shape)
#s=print(Meta1.shape)
#print(s)

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
