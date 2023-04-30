"""
shows a list of prime factors of the number N
"""
def prime_factors_of_number(n):

    list = []  
    for i in range(2, n):
        while n % i == 0:
            list.append(i)
            n = n/i
        if n == 1:
            break

    if len(list) == 0:
        return "Число является простым"
    else:
        return list    



