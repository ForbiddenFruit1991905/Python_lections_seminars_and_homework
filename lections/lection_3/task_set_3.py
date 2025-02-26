# Для удаления элемента множества используют метод remove.

my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.remove(5)
print(my_set)
# my_set.remove(10) # KeyError: 10

print()

# Метод discard работает аналогично remove — удаляет один элемент
# множества.

my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.discard(5)
print(my_set)
my_set.discard(10)
print(my_set)

# В отличие от remove при попытке удалить несуществующий элемент
# discard не вызывает ошибку. При этом множество не изменяется.