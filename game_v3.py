"""Игра угадай число
Верное число угадывается меньше чем за 20 попыток"""


import random

lower = 1
upper = 101
number = random.randint(lower,upper) #предпологаемое число

count = 0

while count < 20:
    count += 1
    #Предпологаемый ответ
    guess_number = int(input ("Загаданное число Это:- "))
    
    #Проверка условия
    if number > guess_number:
        print("Это число больше!")
        
    elif number < guess_number:
        print("Это число меньше!")
        
    else: 
        print("Ура! Поздравляю, Вы справились за", count, "попыток")
        break #конец игры выход из цикла
  