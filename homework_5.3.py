# Создайте функцию генератор чисел Фибоначчи 

number = int(input("Сколько чисел последовательности Фибоначчи Вы хотели бы вывести? "))

def fibonacci(number):
    start_with, next_num = 0, 1
    for __ in range(number):
        yield start_with
        start_with, next_num = next_num, start_with + next_num

print(list(fibonacci(number)))