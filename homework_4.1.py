# Напишите функцию для транспонирования матрицы

def matrix_transposition(array):
    new_array = [*zip(*array)]
    return new_array

print(matrix_transposition([['1','2','3'],['4','5','6'],['7','8','9']]))
