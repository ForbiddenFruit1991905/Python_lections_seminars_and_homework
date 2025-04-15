# Десериализация
#
# Проведём обратные операции. Набор байт мы уже восстанавливали, когда
# разбирались с безопасностью данных. Уточним детали.

import pickle

data = b'\x80\x04\x95\xe3\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\nfirst_name\x94\x8c\x08\xd0\x94\xd0\xb6\xd0\xbe\xd0\xbd\x94\x8c\tlast_name\x94\x8c\x08\xd0\xa1\xd0\xbc\xd0\xb8\xd1\x82\x94\x8c\x07hobbies\x94]\x94(\x8c\x1b\xd0\xba\xd1\x83\xd0\xb7\xd0\xbd\xd0\xb5\xd1\x87 \xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb4\xd0\xb5\xd0\xbb\xd0\xbe\x94\x8c \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\x94\x8c\x16\xd0\xbf\xd1\x83\xd1\x82\xd0\xb5\xd1\x88\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f\x94e\x8c\x03age\x94K#\x8c\x08children\x94]\x94(}\x94(h\x01\x8c\n\xd0\x90\xd0\xbb\xd0\xb8\xd1\x81 \xd0\xb0\x94h\nK\x05u}\x94(h\x01\x8c\x0c\xd0\x9c\xd0\xb0\xd1\x80\ xd1\x83\xd1\x81\xd1\x8f\x94h\nK\x03ueu.'
# new_dict = pickle.loads(data)

try:
    new_dict = pickle.loads(data)
    print(f'{new_dict = }')
except UnicodeDecodeError:
    decoded_data = data.decode('latin1')
    new_dict = pickle.loads(decoded_data)
    print(f'{new_dict = }')

# try:
#     new_dict = pickle.loads(data)
# except UnicodeDecodeError as e:
#     print(f"Ошибка при декодировании: {e}")
# print(f'{new_dict = }')

# Функция получила на вход набор байт и восстановила из них исходный словарь.
# Уточним, что loads имеет ряд дополнительных параметров: fix_imports=True,
# encoding='ASCII', errors='strict'. Они нужны для десериализации объектов
# созданных в Python 2. А так как поддержка второй версии Python завершена
# в 2020 году, нет смысла разбирать назначение параметров. В финале загрузим
# данные из файла my_dict.pickle, который создали ранее.

import pickle

def func(a, b, c):
    return a * b * c

with open('my_dict.pickle', 'rb') as f:
    new_dict = pickle.load(f)
print(f'{new_dict = }')
print(f'{new_dict["functions"][0](2, 3, 4) = }')

# Содержимое словаря в точности соответствует исходному. Но есть одно но.
# При вызове функции func, которая лежит в нулевой ячейке кортежа по ключу
# functions мы получили не сумму трёх чисел, а произведение. В файле, где
# произведена десериализация есть функция func, которая умножает числа.
# Модуль pickle указал в словаре её, а не исходную. Более того, если бы
# функции с нужным именем не было, десериализация завершилась бы ошибкой.
