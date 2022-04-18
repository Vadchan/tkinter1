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
    if re.search(r'\bReal-Time Strategy\b', w):
        w = 'Real-Time Strategy'
    if re.search(r'\bSim\b', w):
        w = 'Sim'
    if re.search(r'\bArcade\b', w):
        w = 'Arcade'
    if re.search(r'\bModern Jet\b', w):
        w = 'Modern Jet'
    if re.search(r'\bOther Shooters\b', w):
        w = 'Other Shooters'
    if re.search(r'\bHistoric\b', w):
        w = 'Historic'
    if re.search(r'\bTurn-Based Strategy\b', w):
        w = 'Turn-Based Strategy'
    if re.search(r'\bSci-Fi\b', w):
        w = 'Sci-Fi'
    if re.search(r'\bPuzzle\b', w):
        w = 'Puzzle'
    if re.search(r'\bAdventure Games\b', w):
        w = 'Adventure Games'
    if re.search(r'\b3D\b', w):
        w = '3D'
    if re.search(r'\bGeneral\b', w):
        w = 'General'
    if re.search(r'\b2D\b', w):
        w = '2D'
    if re.search(r'\bModern\b', w):
        w = 'Modern'
    if re.search(r'\bPlatformers\b', w):
        w = 'Platformers'
    if re.search(r'\bMiscellaneous\b', w):
        w = 'Miscellaneous'
    if re.search(r'\bFantasy\b', w):
        w = 'Fantasy'
    if re.search(r'\bOther Strategy Games\b', w):
        w = 'Other Strategy Games'
    if re.search(r'\bRole-Playing\b', w):
        w = 'Role-Playing'
    if re.search(r'\bFormula One\b', w):
        w = 'Formula One'
    if re.search(r'\bGT / Street\b', w):
        w = 'GT / Street'
    if re.search(r'\bStock Car\b', w):
        w = 'Stock Car'
    if re.search(r'\bStreet\b', w):
        w = 'Street'
    if re.search(r'\bRacing\b', w):
        w = 'Racing'
    if re.search(r'\bRally / Offroad\b', w):
        w = 'Rally / Offroad'
    if re.search(r'\bMotocross\b', w):
        w = 'Motocross'
    if re.search(r'\bKart\b', w):
        w = 'Kart'
    if re.search(r'\bFuturistic\b', w):
        w = 'Futuristic'
    if re.search(r'\bSmall Spaceship\b', w):
        w = 'Small Spaceship'
    if re.search(r'\bFuturistic Combat Sims\b', w):
        w = 'Futuristic Combat Sims'
    if re.search(r'\bLarge Spaceship\b', w):
        w = 'Large Spaceship'
    if re.search(r'\bFuturistic Jet\b', w):
        w = 'Futuristic Jet'
    if re.search(r'\bWWII\b', w):
        w = 'WWII'
    if re.search(r'\bCombat Sims\b', w):
        w = 'Combat Sims'
    if re.search(r'\bTank\b', w):
        w = 'Tank'
    if re.search(r'\bShip\b', w):
        w = 'Ship'
    if re.search(r'\bCivilian Plane\b', w):
        w = 'Civilian Plane'
    if re.search(r'\bTrain\b', w):
        w = 'Train'
    if re.search(r'\bSubmarine\b', w):
        w = 'Submarine'
    if re.search(r'\bTycoon\b', w):
        w = 'Tycoon'
    if re.search(r'\bFirst-Person Shooters\b', w):
        w = 'First-Person Shooters'
    if re.search(r'\bTactical Shooters\b', w):
        w = 'Tactical Shooters'
    if re.search(r'\bAction\b', w):
        w = 'Action'
    if re.search(r'\bWrestling\b', w):
        w = 'Wrestling'
    if re.search(r'\bScrolling\b', w):
        w = 'Scrolling'
    if re.search(r'\bRail\b', w):
        w = 'Rail'
    if re.search(r'\bStatic\b', w):
        w = 'Static'
    if re.search(r'\bLight Gun\b', w):
        w = 'Light Gun'
    if re.search(r'\bShooter\b', w):
        w = 'Shooter'
    if re.search(r'\bFirst-Person\b', w):
        w = 'First-Person'
    if re.search(r'\bMOBA\b', w):
        w = 'MOBA'
    if re.search(r'\bCompilation\b', w):
        w = 'Compilation'
    if re.search(r'\bFighting Games\b', w):
        w = 'Fighting Games'
    if re.search(r'\bMusic\b', w):
        w = 'Music'
    if re.search(r'\bSimulations\b', w):
        w = 'Simulations'
    if re.search(r'\bHelicopter\b', w):
        w = 'Helicopter'
    if re.search(r'\bMilitary\b', w):
        w = 'Military'
    if re.search(r'\bWWI\b', w):
        w = 'WWI'
    if re.search(r'\bOld Jet\b', w):
        w = 'Old Jet'
    if re.search(r'\bFighting\b', w):
        w = 'Fighting'
    if re.search(r'\bAction Adventure\b', w):
        w = 'Action Adventure'
    if re.search(r'\bInteractive Movie\b', w):
        w = 'Interactive Movie'
    if re.search(r'\bHorror\b', w):
        w = 'Horror'
    if re.search(r'\bTennis\b', w):
        w = 'Tennis'
    if re.search(r'\bSoccer\b', w):
        w = 'Soccer'
    if re.search(r'\bManagement\b', w):
        w = 'Management'
    if re.search(r'\bOther Sports Games\b', w):
        w = 'Other Sports Games'
    if re.search(r'\bBaseball\b', w):
        w = 'Baseball'
    if re.search(r'\bBasketball\b', w):
        w = 'Basketball'
    if re.search(r'\bSurfing\b', w):
        w = 'Surfing'
    if re.search(r'\bAlternative Sports\b', w):
        w = 'Alternative Sports'
    if re.search(r'\bOlympic Sports\b', w):
        w = 'Olympic Sports'
    if re.search(r'\bSnowboarding\b', w):
        w = 'Snowboarding'
    if re.search(r'\bGolf\b', w):
        w = 'Golf'
    if re.search(r'\bOther\b', w):
        w = 'Other'
    if re.search(r'\bSkateboarding\b', w):
        w = 'Skateboarding'
    if re.search(r'\bBiking\b', w):
        w = 'Biking'
    if re.search(r'\bBilliards\b', w):
        w = 'Billiards'
    if re.search(r'\bVolleyball\b', w):
        w = 'Volleyball'
    if re.search(r'\bHunting\b', w):
        w = 'Hunting'
    if re.search(r'\bRugby\b', w):
        w = 'Rugby'
    if re.search(r'\bFootball\b', w):
        w = 'Football'
    if re.search(r'\bBowling\b', w):
        w = 'Bowling'
    if re.search(r'\bHockey\b', w):
        w = 'Hockey'
    if re.search(r'\bTruck\b', w):
        w = 'Truck'
    if re.search(r'\bOn-foot\b', w):
        w = 'On-foot'
    if re.search(r'\bVirtual Life\b', w):
        w = 'Virtual Life'
    if re.search(r'\bFuturistic Sub\b', w):
        w = 'Futuristic Sub'
    if re.search(r'\bMech\b', w):
        w = 'Mech'
    if re.search(r'\bBreeding/Constructing\b', w):
        w = 'Breeding/Constructing'
    if re.search(r'\bPC-style RPG\b', w):
        w = 'PC-style RPG'
    if re.search(r'\bMassively Multiplayer\b', w):
        w = 'Massively Multiplayer'
    if re.search(r'\bConsole-style RPG\b', w):
        w = 'Console-style RPG'

    ss = Meta1[(Meta1['genre_tags'] == str(w))]
    s1 = ss.drop(columns=['user_score', 'publisher', 'critics_reviews_count',
                            'maturity_rating','genre_tags', 'user_reviews_count'])
    pd.set_option('display.max_rows', None)
    #вывод без \n
    pd.options.display.expand_frame_repr = False

    return s1



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