"""Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии"""
#код не работает 

names = ("Vasya", "Ira", "Kate")
cash = (10000, 8700, 4350)
percent = ("10%","3.5%", "5%")

def bonus(names: list(str), cash: list(int), percent: list(str)) -> dict(map(str,float)):
    return {name: salary / 100 * perc
        for name, salary, perc in zip(names, cash, (float(i[:-1]) for i in percent))}


print(*bonus)