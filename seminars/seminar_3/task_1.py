# Задание №1.
# ✔ Вручную создайте список с целыми числами, которые повторяются.
# Получите новый список, который содержит уникальные (без повтора)
# элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое не
# использует другие коллекции помимо списков.
from distutils.command.clean import clean

my_list = [1, 3, 3, 5, 6, 7, 9, 3]
new_set = set(my_list)
print(f'Первый вариант:\n{new_set = }')

unique_list = []
print('Второй вариант:')
for elem in my_list:
    if elem not in unique_list:
        unique_list.append(elem)
        print(elem, end=' ')
# for elem in unique_list:
#     print(elem, end=' ')