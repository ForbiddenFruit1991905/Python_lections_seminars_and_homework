my_list_0 = ['H', 'e', 'l', 'l', 'o', 1, 3, 5, 7]
# my_list_0.sort() # TypeError: '<' not supported between instances of 'int' and 'str'
# res = sorted(my_list_0) # TypeError: '<' not supported between instances of 'int' and 'str'

# При сортировке элементы списка должны быть одного типа.
# Иначе Python может не понять как сравнивать между собой
# элементы разных типов и вызовет ошибку.

my_list = [4, 8, 2, 9, 1, 7, 2]
sort_list = sorted(my_list)
print(my_list, sort_list, sep='\n')
rev_list = sorted(my_list, reverse=True)
print(my_list, rev_list, sep='\n')

# Функция sorted принимает на вход любую коллекцию по которой
# можно итерироваться и возвращает отсортированный список.

# Внутри функции используется алгоритм сортировки Timsort —
# гибридная устойчивая сортировка с временной асимптотикой
# O(n log n). Дополнительно тратится O(n) памяти на создание
# нового отсортированного списка.