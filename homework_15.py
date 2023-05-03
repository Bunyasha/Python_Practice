import logging

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(level=logging.INFO, filename='my_hw.log', encoding='utf-8',
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def prime_factors_of_number(n: int) -> list:
    """ Функция получает натуральное число N и составляет список простых множителей числа 
    """
    result = [] 
    for i in range(2, n):
        while n % i == 0:
            result.append(i)
            n = n/i
        if n == 1:
            break

    if len(result) == 0:
        logger.error(f'"Число {n} является простым"')
        return float('inf')
    else:
        logger.info(f'Список простых множителей числа {n}: {result}')
        return result


if __name__ == '__main__':
    print(prime_factors_of_number(0))
    print(prime_factors_of_number(10))
    print(prime_factors_of_number(174)) 