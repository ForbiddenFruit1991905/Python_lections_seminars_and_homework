# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
    # ✔ расширение
    # ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
    # ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
    # ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
    # ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
    # ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

import os
from random import choices
import random

def func_create_files(file_extension, len_name=6, len_byte=256, num_files=3):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                  'z']

    for i in range(1, num_files + 1):
        random_vowel = ''.join(random.choice(vowels) for _ in range(len(vowels)))
        random_consonant = ''.join(random.choice(consonants) for _ in range(len(consonants)))
        custom_name = random_vowel + random_consonant
        name = []
        len_name_range = random.randint(len_name, 30)
        while len(name) < len_name_range:
            name.append(random.choice(''.join(custom_name)))
        random_file_name = (''.join(name)).capitalize()

        filename = f"{i}_{random_file_name}{file_extension}"
        with open(os.path.join(current_dir, filename), 'w') as filename:
            random_data = os.urandom(random.randint(len_byte, 4096))
            filename.write(str(random_data))

    print(f"{num_files} файл-а(ов) было успешно создано в каталоге {current_dir}.")

def func_random_ext(num_file: int, **kwargs):
    values_extensions = []
    for value in kwargs.values():
        values_extensions.append(value)
    for _ in range(num_file):
        ext = str(*choices(values_extensions))
        func_create_files(ext, len_name=6, len_byte=256, num_files=3)

func_random_ext(3, a='.txt', b='.doc', c=3, d='.exe')