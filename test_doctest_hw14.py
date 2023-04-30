def count_numbers(a):
    """
    Calculate the sum of digits in a real number
    >>> count_numbers('1.840522218348187')
    64
    >>> count_numbers(1.840522218348187)
    64
    >>> count_numbers(-1.840522218348187)
    Traceback (most recent call last):
    ...
    ValueError: invalid literal for int() with base 10: '-'
    """
    b = str(a).replace('.', '')
    result = sum(map(int, b))
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
