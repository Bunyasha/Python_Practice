#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

max_capacity = 7

list_of_items = {'tent': 3, 'first aid kit': 0.6, 'raincoat': 0.5, 'axe': 1, 'ropes': 1, \
    'foodstuff': 2, 'matches': 0.1, 'sleeping bag': 1}
my_bag = {}


for things, weight in list_of_items.items():
    if weight <= max_capacity:
        my_bag.update({things: weight})
        max_capacity = max_capacity - weight
        
print(my_bag)