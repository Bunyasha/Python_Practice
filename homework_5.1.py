"""Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""

import os


def get_file_path(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension


full_path = r'C:/Users/eleni/OneDrive/Documents/GeekBrains/Знакомство с базами данных/SQL_Polnoe_rukovodstvo_3_izd_2019_Groff_Vaynberg_Oppel.pdf'
data_list = []
temp, file_extension = full_path.split('.')
*path, file_name = temp.split('/')
path = '/'.join(path)
data_list.append(path)
data_list.append(file_name)
data_list.append(file_extension)
print(tuple(data_list))

print()
print(get_file_path('C:/Users/eleni/OneDrive/Documents/GeekBrains/Знакомство с базами данных/SQL_Polnoe_rukovodstvo_3_izd_2019_Groff_Vaynberg_Oppel.pdf'))



