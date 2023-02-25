#Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должнаподсказывать “больше” или “меньше” после каждой попытки. 

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
attempts = 10

from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)

while attempts != 0:
    guess = int(input(f"У вас есть {attempts} попыток угадать число от {LOWER_LIMIT} до {UPPER_LIMIT}. Введите ваш вариант: "))
    if guess == num:
        print("Ура! Вы угадали!")
        break
    elif guess < num:
        print("Загаданное число больше указанного Вами")
        attempts -=1
        if attempts == 0:
            print(f"Увы, вы не угадали. Было загадано число {num}")
    elif guess > num:
        print("Загаданное число меньше указанного Вами")
        attempts -=1
        if attempts == 0:
            print(f"Увы, вы не угадали. Было загадано число {num}")
    