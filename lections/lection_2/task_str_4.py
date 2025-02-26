# Строки как объекты тратят память на служебную информацию, а как массивы на хранение текста.
# В 64-х разрядной версии Python служебная информация занимает 48 байт. Разберём пример кода:

empty_str = ''
en_str = 'Text'
ru_str = 'Текст'
unicode_str = ' 😀😍😉🙃 '
print(empty_str.__sizeof__())
print(en_str.__sizeof__())
print(ru_str.__sizeof__())
print(unicode_str.__sizeof__())

# Mетод __sizeof__() работает аналогично sys.getsizeof и возвращает количество байт занятых объектом.