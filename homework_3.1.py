# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

original_list = [4, 2, 4, 6, 2, 8, 10, 10, 12, 4]
duplicates_list = []
list_without_duplicates = list(set(original_list))

for i in original_list:
    if original_list.count(i) > 1:
        duplicates_list.append(i)
print(f"Список с дублирующимися элементами {duplicates_list}")

print(f"Результирующий список без дубликатов {list_without_duplicates}")