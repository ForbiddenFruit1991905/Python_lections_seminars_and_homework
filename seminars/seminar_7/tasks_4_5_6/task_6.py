# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import os
from random import choices
import random

def func_create_files(file_extension, len_name=6, len_byte=256, num_files=3, dir_path="."):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                  'z']

    for i in range(1, num_files + 1):
        random_vowel = ''.join(random.choice(vowels) for _ in range(random.randint(2, 5)))
        random_consonant = ''.join(random.choice(consonants) for _ in range(random.randint(3, 7)))
        custom_name = random_vowel + random_consonant
        name = []
        len_name_range = random.randint(len_name, 30)
        while len(name) < len_name_range:
            name.append(random.choice(''.join(custom_name)))
        random_file_name = (''.join(name)).capitalize()

        filename = f"{i}_{random_file_name}{file_extension}"
        file_path = os.path.join(dir_path, filename)
        if not os.path.exists(file_path):
            with open(file_path, 'wb') as file:
                random_data = os.urandom(random.randint(len_byte, 4096))
                file.write(random_data)

    print(f"{num_files} файл-а(ов) было успешно создано в каталоге {dir_path}.")

def func_random_ext(num_file: int, **kwargs):
    values_extensions = [value for value in kwargs.values()]
    chosen_extensions = [str(*choices(values_extensions)) for _ in range(num_file)]
    return chosen_extensions

func_random_ext(3, a='.txt', b='.doc', c='.pdf', d='.exe')

def func_save_files_into_dir(dir_path, files):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    # file_extensions = func_random_ext(files, a='.txt', b='.doc', c='.pdf', d='.exe')
    for ext in func_random_ext(files, a='.txt', b='.doc', c='.pdf', d='.exe'):
        func_create_files(ext, len_name=6, len_byte=256, num_files=files, dir_path=dir_path)

func_save_files_into_dir("dir_for_task_6", 3)

# # Второй вариант:
# def func_save_into_dir(dir):
#     try:
#         os.makedirs(dir)
#         chdir(dir)
#     except FileExistsError:
#         chdir(dir)
#     func_random_ext(3, a='.txt', b='.doc', c='.pdf', d='.exe')
#     chdir('..')
#
# func_save_into_dir("test_dir_for_task_6")