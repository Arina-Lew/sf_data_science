"""Игра угадай число
Компьютер угадывает число за меньше чем 20 попыток
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Угадываем число
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 0 # количество попыток
    min_border = 1 # нижняя граница поиска
    max_border = 101 # верхняя граница поиска
    predict_number = np.random.randint(1,101)
    
    while True:
        count += 1
        
        predict_number = round((min_border + max_border)//2)
        
        if number > predict_number:
            min_border = predict_number
            
        elif number < predict_number:
            max_border = predict_number
                 
        else:
            break
        
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 10000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # среднее количество попыток
    
    
   
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

score_game(random_predict)


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    
