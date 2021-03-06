import  matplotlip as plt
import matplotlib.pyplot as plt
import pandas as pd
import re


Meta1 = pd.read_csv('metacritic-20141019-152743.csv')
#Удаление не нужных столбцов
Meta1 = Meta1.drop(columns=['link', 'genre', 'platform'])
#print('Атрибуты ИГРЫ')

pd.set_option('display.max_rows', None)


def son1(a1, a2, b, sort):
    if a1 > a2:
        s = 'Второе значение не может быть меньше первого!\n'
        return s
    sss = Meta1[(Meta1['user_score'] >= int(a1)) & (Meta1['user_score'] <= int(a2)) &
                (Meta1['genre_tags'] == str(b))]
    qq = sss.drop(columns=['metascore', 'publisher', 'critics_reviews_count', 'developer',
                           'maturity_rating', 'user_reviews_count'])
    if re.search(r'\bEmpty\b', str(qq)):
        s = 'Игры с такими оценками нет в таблице metacritic'
        return s
    pd.set_option('display.max_rows', None)
    # вывод без \n
    pd.options.display.expand_frame_repr = False
    # сортировка
    if re.search(r'\bпо убыванию\b', str(sort)):
        s4 = qq.sort_values(by=['user_score'], ascending=False)
    elif re.search(r'\bпо возрастанию\b', str(sort)):
        s4 = qq.sort_values(by=['user_score'])
    elif re.search(r'\bпо title A-Z\b', str(sort)):
        s4 = qq.sort_values(by=['title'])
    elif re.search(r'\bпо title Z-A\b', str(sort)):
        s4 = qq.sort_values(by=['title'], ascending=False)
    elif re.search(r'\bпо дате возрастания\b', str(sort)):
        s4 = qq.sort_values(by=['release_date'])
    elif re.search(r'\bпо дате убывания\b', str(sort)):
        s4 = qq.sort_values(by=['release_date'], ascending=False)
    return f'{s4}'


def zom1(a1, a2, b, sort):
    if a1 > a2:
        s = 'Второе значение не может быть меньше первого!\n'
        return s
    sss = Meta1[(Meta1['metascore'] >= int(a1)) & (Meta1['metascore'] <= int(a2)) &
                (Meta1['genre_tags'] == str(b))]
    qq = sss.drop(columns=['user_score', 'publisher', 'critics_reviews_count', 'developer',
                           'maturity_rating', 'user_reviews_count'])
    if re.search(r'\bEmpty\b', str(qq)):
        s = 'Игры с такими оценками нет в таблице metacritic'
        return s
    pd.set_option('display.max_rows', None)
    # вывод без \n
    pd.options.display.expand_frame_repr = False

    # сортировка
    if re.search(r'\bпо убыванию\b', str(sort)):
        s4 = qq.sort_values(by=['metascore'], ascending=False)
    elif re.search(r'\bпо возрастанию\b', str(sort)):
        s4 = qq.sort_values(by=['metascore'])
    elif re.search(r'\bпо title A-Z\b', str(sort)):
        s4 = qq.sort_values(by=['title'])
    elif re.search(r'\bпо title Z-A\b', str(sort)):
        s4 = qq.sort_values(by=['title'], ascending=False)
    elif re.search(r'\bпо дате возрастания\b', str(sort)):
        s4 = qq.sort_values(by=['release_date'])
    elif re.search(r'\bпо дате убывания\b', str(sort)):
        s4 = qq.sort_values(by=['release_date'], ascending=False)
    return f'{s4}'

    return f'{s4}'

def infor():
    s0 = ('Разброс значений, средняя оценка и медиана')
    s1 = Meta1.describe()
    s2 = ('Название колонок')
    s3 = (Meta1.columns)
    s4 = ('Размеры таблицы')
    s5 = (Meta1.shape)
    s6 = ('Атрибуты файла')
    s7 = (Meta1.head())
    s8 = ('Повторяющиеся данные')
    s9 = (Meta1["title"].value_counts().head())
    s10 = (Meta1['genre_tags'].value_counts().head())
    s11 = ('Максимальное значение в metascore:')
    s12 = (Meta1['metascore'][Meta1.index.min()])
    s13 = ('Минимальное значение в metascore:')
    s14 = (Meta1['metascore'][Meta1.index.max()])
    s15 = ('Сумма metascore:')
    s16 = (Meta1['metascore'].sum())

    # вывод без \n
    pd.set_option('display.max_rows', None)

    return f'{s0}\n{s1}\n\n{s2}\n{s3}\n\n{s4}\n' \
           f'{s5}\n\n{s6}\n{s7}\n\n{s8}\n' \
           f'{s9}\n{s10}\n\n{s11}\n{s12}\n\n' \
           f'{s13}\n{s14}\n{s15}\n\n{s16}\n'


def nahod(a, sort):
    result = Meta1[(Meta1['title'] == str(a))]
    w = str(result['genre_tags'])
    if re.search(r'\bAction RPG\b', w):
        w = 'Action RPG'
    elif re.search(r'\bReal-Time Strategy\b', w):
        w = 'Real-Time Strategy'
    elif re.search(r'\bSim\b', w):
        w = 'Sim'
    elif re.search(r'\bArcade\b', w):
        w = 'Arcade'
    elif re.search(r'\bModern Jet\b', w):
        w = 'Modern Jet'
    elif re.search(r'\bOther Shooters\b', w):
        w = 'Other Shooters'
    elif re.search(r'\bHistoric\b', w):
        w = 'Historic'
    elif re.search(r'\bTurn-Based Strategy\b', w):
        w = 'Turn-Based Strategy'
    elif re.search(r'\bSci-Fi\b', w):
        w = 'Sci-Fi'
    elif re.search(r'\bPuzzle\b', w):
        w = 'Puzzle'
    elif re.search(r'\bAdventure Games\b', w):
        w = 'Adventure Games'
    elif re.search(r'\b3D\b', w):
        w = '3D'
    elif re.search(r'\bGeneral\b', w):
        w = 'General'
    elif re.search(r'\b2D\b', w):
        w = '2D'
    elif re.search(r'\bModern\b', w):
        w = 'Modern'
    elif re.search(r'\bPlatformers\b', w):
        w = 'Platformers'
    elif re.search(r'\bMiscellaneous\b', w):
        w = 'Miscellaneous'
    elif re.search(r'\bFantasy\b', w):
        w = 'Fantasy'
    elif re.search(r'\bOther Strategy Games\b', w):
        w = 'Other Strategy Games'
    elif re.search(r'\bRole-Playing\b', w):
        w = 'Role-Playing'
    elif re.search(r'\bFormula One\b', w):
        w = 'Formula One'
    elif re.search(r'\bGT / Street\b', w):
        w = 'GT / Street'
    elif re.search(r'\bStock Car\b', w):
        w = 'Stock Car'
    elif re.search(r'\bStreet\b', w):
        w = 'Street'
    elif re.search(r'\bRacing\b', w):
        w = 'Racing'
    elif re.search(r'\bRally / Offroad\b', w):
        w = 'Rally / Offroad'
    elif re.search(r'\bMotocross\b', w):
        w = 'Motocross'
    elif re.search(r'\bKart\b', w):
        w = 'Kart'
    elif re.search(r'\bFuturistic\b', w):
        w = 'Futuristic'
    elif re.search(r'\bSmall Spaceship\b', w):
        w = 'Small Spaceship'
    elif re.search(r'\bFuturistic Combat Sims\b', w):
        w = 'Futuristic Combat Sims'
    elif re.search(r'\bLarge Spaceship\b', w):
        w = 'Large Spaceship'
    elif re.search(r'\bFuturistic Jet\b', w):
        w = 'Futuristic Jet'
    elif re.search(r'\bWWII\b', w):
        w = 'WWII'
    elif re.search(r'\bCombat Sims\b', w):
        w = 'Combat Sims'
    elif re.search(r'\bTank\b', w):
        w = 'Tank'
    elif re.search(r'\bShip\b', w):
        w = 'Ship'
    elif re.search(r'\bCivilian Plane\b', w):
        w = 'Civilian Plane'
    elif re.search(r'\bTrain\b', w):
        w = 'Train'
    elif re.search(r'\bSubmarine\b', w):
        w = 'Submarine'
    elif re.search(r'\bTycoon\b', w):
        w = 'Tycoon'
    elif re.search(r'\bFirst-Person Shooters\b', w):
        w = 'First-Person Shooters'
    elif re.search(r'\bTactical Shooters\b', w):
        w = 'Tactical Shooters'
    elif re.search(r'\bAction\b', w):
        w = 'Action'
    elif re.search(r'\bWrestling\b', w):
        w = 'Wrestling'
    elif re.search(r'\bScrolling\b', w):
        w = 'Scrolling'
    elif re.search(r'\bRail\b', w):
        w = 'Rail'
    elif re.search(r'\bStatic\b', w):
        w = 'Static'
    elif re.search(r'\bLight Gun\b', w):
        w = 'Light Gun'
    elif re.search(r'\bShooter\b', w):
        w = 'Shooter'
    elif re.search(r'\bFirst-Person\b', w):
        w = 'First-Person'
    elif re.search(r'\bMOBA\b', w):
        w = 'MOBA'
    elif re.search(r'\bCompilation\b', w):
        w = 'Compilation'
    elif re.search(r'\bFighting Games\b', w):
        w = 'Fighting Games'
    elif re.search(r'\bMusic\b', w):
        w = 'Music'
    elif re.search(r'\bSimulations\b', w):
        w = 'Simulations'
    elif re.search(r'\bHelicopter\b', w):
        w = 'Helicopter'
    elif re.search(r'\bMilitary\b', w):
        w = 'Military'
    elif re.search(r'\bWWI\b', w):
        w = 'WWI'
    elif re.search(r'\bOld Jet\b', w):
        w = 'Old Jet'
    elif re.search(r'\bFighting\b', w):
        w = 'Fighting'
    elif re.search(r'\bAction Adventure\b', w):
        w = 'Action Adventure'
    elif re.search(r'\bInteractive Movie\b', w):
        w = 'Interactive Movie'
    elif re.search(r'\bHorror\b', w):
        w = 'Horror'
    elif re.search(r'\bTennis\b', w):
        w = 'Tennis'
    elif re.search(r'\bSoccer\b', w):
        w = 'Soccer'
    elif re.search(r'\bManagement\b', w):
        w = 'Management'
    elif re.search(r'\bOther Sports Games\b', w):
        w = 'Other Sports Games'
    elif re.search(r'\bBaseball\b', w):
        w = 'Baseball'
    elif re.search(r'\bBasketball\b', w):
        w = 'Basketball'
    elif re.search(r'\bSurfing\b', w):
        w = 'Surfing'
    elif re.search(r'\bAlternative Sports\b', w):
        w = 'Alternative Sports'
    elif re.search(r'\bOlympic Sports\b', w):
        w = 'Olympic Sports'
    elif re.search(r'\bSnowboarding\b', w):
        w = 'Snowboarding'
    elif re.search(r'\bGolf\b', w):
        w = 'Golf'
    elif re.search(r'\bOther\b', w):
        w = 'Other'
    elif re.search(r'\bSkateboarding\b', w):
        w = 'Skateboarding'
    elif re.search(r'\bBiking\b', w):
        w = 'Biking'
    elif re.search(r'\bBilliards\b', w):
        w = 'Billiards'
    elif re.search(r'\bVolleyball\b', w):
        w = 'Volleyball'
    elif re.search(r'\bHunting\b', w):
        w = 'Hunting'
    elif re.search(r'\bRugby\b', w):
        w = 'Rugby'
    elif re.search(r'\bFootball\b', w):
        w = 'Football'
    elif re.search(r'\bBowling\b', w):
        w = 'Bowling'
    elif re.search(r'\bHockey\b', w):
        w = 'Hockey'
    elif re.search(r'\bTruck\b', w):
        w = 'Truck'
    elif re.search(r'\bOn-foot\b', w):
        w = 'On-foot'
    elif re.search(r'\bVirtual Life\b', w):
        w = 'Virtual Life'
    elif re.search(r'\bFuturistic Sub\b', w):
        w = 'Futuristic Sub'
    elif re.search(r'\bMech\b', w):
        w = 'Mech'
    elif re.search(r'\bBreeding/Constructing\b', w):
        w = 'Breeding/Constructing'
    elif re.search(r'\bPC-style RPG\b', w):
        w = 'PC-style RPG'
    elif re.search(r'\bMassively Multiplayer\b', w):
        w = 'Massively Multiplayer'
    elif re.search(r'\bConsole-style RPG\b', w):
        w = 'Console-style RPG'
    else:
        s1 = 'Такой игры нет в таблице metacritic'
        return s1

    ss = Meta1[(Meta1['genre_tags'] == str(w))]
    s1 = ss.drop(columns=['user_score', 'publisher', 'critics_reviews_count',
                            'maturity_rating','genre_tags', 'user_reviews_count'])
    pd.set_option('display.max_rows', None)
    #вывод без \n
    pd.options.display.expand_frame_repr = False
    if re.search(r'\bпо убыванию\b', str(sort)):
        s4 = s1.sort_values(by=['metascore'], ascending=False)
    elif re.search(r'\bпо возрастанию\b', str(sort)):
        s4 = s1.sort_values(by=['metascore'])
    elif re.search(r'\bпо title A-Z\b', str(sort)):
        s4 = s1.sort_values(by=['title'])
    elif re.search(r'\bпо title Z-A\b', str(sort)):
        s4 = s1.sort_values(by=['title'], ascending=False)
    elif re.search(r'\bпо дате возрастания\b', str(sort)):
        s4 = s1.sort_values(by=['release_date'])
    elif re.search(r'\bпо дате убывания\b', str(sort)):
        s4 = s1.sort_values(by=['release_date'], ascending=False)
    return s4


# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', 7)

# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)

# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)

