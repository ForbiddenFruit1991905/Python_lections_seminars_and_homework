# Аналогично присваиванию можно сравнить несколько переменных
# внутри конструкции if.

a = b = c = 42
# if a == b and b == c:
if a == b == c:
    print('Полное совпадение')

# Запись становится короче, т.к.исключается команда and внутри
# сравнения. Работает подобная запись не только с проверкой на
# равенство, но и с другими операциями.

if a < b < c:
    print('b больше a и меньше c')