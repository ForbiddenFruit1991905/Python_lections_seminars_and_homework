# Задание №1
# ✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

import random

# def func_fill_nums():
#     text = []
#     for _ in range(2000):
#         random_number = random.randint(-1000, 1001)
#         random_float_number = random.uniform(-1000.0, 1001.0)
#         text.append(str(random_number))
#         text.append(" | ")
#         text.append(str(random_float_number))
#         text.append(" | ")
#     my_string = ''.join(text)
#     print(my_string)
#
#     with open('example_1.txt', 'a', encoding='utf-8') as filename:
#         filename.write(my_string)
#
# func_fill_nums()

def func_fill_nums(num_lines, file_name):
    with open(file_name, 'a', encoding='utf-8') as filename:
        for _ in range(num_lines):
            random_number = random.randint(-1000, 1000)
            random_float_number = random.uniform(-1000.0, 1000.0)
            line = f"{random_number} | {random_float_number}\n"
            filename.write(line)

func_fill_nums(5, 'example_1.txt')