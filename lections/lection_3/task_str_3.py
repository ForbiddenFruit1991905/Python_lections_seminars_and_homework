# Форматирование через % (старый метод форматирования
# лучше не использовать)

name = 'Alex'
age = 12
text = 'Меня зовут %s и мне %d лет' % (name, age)
print(text)

# В строке текста используется знак % с символом типа после него.
# s — строка, d — число ит.п. После строки указывается символ %
# и перечисляются переменные. Если переменных больше одной, они
# заключаются в круглые скобки и разделяются запятой — передаётся
# кортеж.

# Метод format
# Метод формат является строковым методом и позволяет соединять
# заранее заготовленный текст с переменными. Долгое время был основным
# способом форматирования. До версии Python 3.6.

name = 'Alex'
age = 12
text = 'Меня зовут {} и мне {} лет'.format(name, age)
print(text)

# В строке используются фигурные скобки как место для подстановки
# значений. Далее для строки вызывается метод format. В качестве
# аргументов метод получает нужное количество переменных.

# f-строка
# f-строки похожи на более короткую и читаемую запись метода формат.

name = 'Alex'
age = 12
text = f'Меня зовут {name} и мне {age} лет'
print(text)

# Перед открывающей кавычкой пишут f — указатель на отформатированную
# строку. Текст внутри фигурных скобок воспринимается как переменная и
# на печать выводятся из значения.

