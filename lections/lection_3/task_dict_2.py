# Если ли мы хотим гарантировать отсутствие ошибки
# KeyError при обращении к элементу словаря, можно
# обратиться к значению через метод get, а не
# квадратные скобки.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.get('two'))
print(my_dict.get('five'))
print(my_dict.get('five', 5))
print(my_dict)
print(my_dict.get('ten', 5))
print(my_dict.get('four', 5))
print(my_dict.get('four'))

# При обращении к существующему ключу метод get работает
# аналогично доступу через квадратные скобки. Если обратиться
# к несуществующему ключу, get возвращает None. Метод get принимает
# второй аргумент, значение по умолчанию. Если ключ отсутствует
# в словаре, вместо None будет возвращено указанное значение.

