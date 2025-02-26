# Для удаления пары ключ значение из словаря используют
# метод popitem.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.popitem()
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.popitem()
print(f'{eggs = }\t{my_dict=}')

print()

# Важно! Если измените значение у существующего ключа, положение
# ключа в очереди не меняется, он не считается последним добавленным.

# Метод pop удаляет пару ключ-значение по переданному ключу.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.pop('two')
print(f'{spam = }\t{my_dict=}')
# err1 = my_dict.pop('six') # KeyError: 'six'
# err2 = my_dict.pop() # TypeError: pop expected at least 1 argument, got 0

# Если указать несуществующий ключ, получим ошибку KeyError.
# В отличие от метода pop у списков list, dict.pop вызовет ошибку
# TypeError. Для удаления последнего элемента нужен метод popitem.