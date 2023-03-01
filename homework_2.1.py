#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата

number = int(input("Введите число: "))
num = number

result = ""

while number > 0:
    divided_number = number % 16
    result = str(divided_number) + result
    number = number // 16

print(f"Число {num} в шестнадцатеричной системе счисления = {result}")

print(hex(num))

