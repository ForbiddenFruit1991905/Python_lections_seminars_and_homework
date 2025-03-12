# Задание №2
# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять
# из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

# 1. `random.choice()` - эта функция позволяет случайным образом выбирать
# элемент из последовательности, такой как список символов, что полезно при генерации случайных имен.
# 2. `random.sample()` - эта функция позволяет случайным образом выбирать заданное количество уникальных
# элементов из последовательности. Это может быть полезно при генерации строк без повторяющихся символов.
# 3. `string.ascii_letters` - это модуль `string`, содержащий строки с английскими буквами в нижнем и
# верхнем регистрах. Можно объединить этот модуль с функциями модуля `random` для создания случайных строк.
# 4. `string.ascii_lowercase` и `string.ascii_uppercase` - эти строки содержат английские буквы в нижнем и
# верхнем регистрах соответственно, и они могут быть использованы для генерации строк в нужном регистре.

# s = "example"
# s_capitalized = s.capitalize()
# print(s_capitalized)  # Вывод: "Example

import random

def func_names(n: int):

    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    random_vowel = ''.join(random.choice(vowels) for _ in range(len(vowels)))
    random_consonant = ''.join(random.choice(consonants) for _ in range(len(consonants)))
    custom_name = random_vowel + random_consonant
    name = []
    with open("example_2.txt", 'a', encoding='utf-8') as filename:
        while len(name) < n:
            name.append(random.choice(''.join(custom_name)))
        print((''.join(name)).capitalize())
        filename.write(''.join(name).capitalize() + '\n')

len_name = random.randint(4, 7)
func_names(len_name)