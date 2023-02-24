# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MIN_LIMIT = 0
MAX_LIMIT = 100000

while True:
    number = int(input("Введите число от 0 до 100 000 для проверки: "))
    if number < MIN_LIMIT or number > MAX_LIMIT:
        print("Неверно. Попробуйте снова.")
    else:
        break

if number == 1 or number == 0:
    print(f"Число {number} — не является ни простым, ни составным числом, так как у него только один делитель")
else:
    print("Сейчас всё решим")