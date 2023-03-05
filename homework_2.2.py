#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
#Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

import math
import fractions

first_numerator,first_denominator = map(int, input("Введите числитель и знаменатель дроби через /\n").split("/"))
second_numerator,second_denominator = map(int, input("Введите числитель и знаменатель второй дроби через /\n").split("/"))

sum_numerator = first_numerator + second_numerator
mult_num = first_numerator*second_numerator
mult_denom = first_denominator*second_denominator
gc_sum = math.gcd(sum_numerator,first_denominator)
gc_mult = math.gcd(mult_num,mult_denom)
lc = math.lcm(first_denominator,second_denominator)

if first_denominator == second_denominator:
    
    print(f"Произведение дробей равно {int(mult_num/gc_mult)}/{int(mult_denom/gc_mult)}")
    print(f"Сумма дробей равна {int(sum_numerator/gc_sum)}/{int(first_denominator/gc_sum)}")

else:
    print(f"Произведение дробей равно {int(mult_num/gc_mult)}/{int(mult_denom/gc_mult)}")

    mult_first_num = int(lc / first_denominator) * first_numerator
    mult_second_num = int(lc / second_denominator) * second_numerator
    print(f"Сумма дробей равна {mult_first_num + mult_second_num}/{lc}")


f1 = fractions.Fraction(first_numerator,first_denominator)
f2 = fractions.Fraction(second_numerator,second_denominator)

print(f1*f2)
print(f1+f2)