# Замена на новый объект того же типа

a = 5
print(a, id(a))
a += 1
print(a, id(a))

# Переменная a ссылается на число 5,которое лежит в определённом месте в ОЗУ.
# При увеличении значения на единицу был создан новый объект в памяти.
# Переменнаяa теперь указывает на него.

# ● Второй вариант развития событий при изменении неизменяемого — вызов ошибки.
# Строка неизменяема. Попытаемся заменить пробел подчеркиванием.

txt = 'Hello world!'
txt[5] = '_'

# Получим TypeError: 'str' object does not support item assignment,
# т.к. изменить символ в неизменяемой строке нельзя. Но ведь в Python
# есть возможность такой замены.

txt = 'Hello world!'
print(txt, id(txt))
txt = txt.replace(' ', '_')
print(txt, id(txt))