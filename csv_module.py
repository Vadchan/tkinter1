import  matplotlip as plt
#import matplotlib.pyplot as plt
import pandas as pd
import re


Meta1 = pd.read_csv('metacritic-20141019-152743.csv')
#Удаление не нужных столбцов
Meta1 = Meta1.drop(columns=['link', 'genre', 'platform'])
#print('Атрибуты ИГРЫ')

pd.set_option('display.max_rows', None)
print('Все игры')
#print((Meta1['genre_tags']))
print('^^Все игры^^')
print(pd.unique(Meta1['genre_tags']))

def nahod(a):
    result = Meta1[(Meta1['title'] == str(a))]
    w = str(result['genre_tags'])
    if re.search(r'\bAction RPG\b', w):
        w = 'Action RPG'
    else:
        w = '235'
    #index = w.find("Action RPG")
    #if Meta1[(Meta1['genre_tags'] == str(w))]:
        #ss = Meta1.drop(columns=['user_score', 'publisher', 'critics_reviews_count', 'release_date',
         #                        'maturity_rating', 'metascore', 'user_reviews_count', 'developer'])
        #print(ss)

    return w



def search(a):
    #a = input('Введите название игры: ')
    result = Meta1[(Meta1['title'] == str(a))]
    #print('Вся информация о вашей игре')
    #print(result)
    #print('Хотите воспользоваться нахождением максимально похожей игры?')
    #print('да')
    #print('нет')
    w = result['genre_tags']
    #print(w)
    b = 'да'

    if b == str('да'):
        #rr = input('введите жанр игры, что указан выше: ')
        if Meta1[(Meta1['genre_tags'] == 'RPG')]:
            ss = Meta1.drop(columns=['user_score', 'publisher', 'critics_reviews_count', 'release_date',
                               'maturity_rating', 'metascore', 'user_reviews_count', 'developer'])
            print(ss)
        '''    
        print('Желаете отсортировать игры по оценке metascore?')
        print('да')
        print('нет')
        z = 'нет'
        if z == str('да'):
            q1 = input('Выберите какое минимальное значение будет по metascore: ')
            q2 = input('Выберите максимальное значение: ')
            sss = Meta1[(Meta1['metascore'] >= int(q1)) & (Meta1['metascore'] <= int(q2)) &
                        (Meta1['genre_tags'] == str(rr))]
            qq = sss.drop(columns=['user_score', 'publisher', 'critics_reviews_count', 'release_date',
                                   'maturity_rating', 'user_reviews_count', 'developer'])
            print(qq)
        if z == str('нет'):
            print('Выход...')
    else:

        print('Выход...')
    #return print('dsnopb')
       '''
    return {result['genre_tags']}
# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', 7)

# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)

# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)


result = Meta1[(Meta1['title'] == 'Diablo')]
#print(result)


'''
if __name__ == "__main__":
    search()
'''