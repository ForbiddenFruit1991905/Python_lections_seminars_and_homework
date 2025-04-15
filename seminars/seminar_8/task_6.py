# Задание №6
# 📌 Напишите функцию, которая преобразует pickle файл хранящий список
# словарей в табличный csv файл.
# 📌 Для тестирования возьмите pickle версию файла из задачи 4 этого
# семинара.
# 📌 Функция должна извлекать ключи словаря для заголовков столбца из
# переданного файла.

import csv
import pickle
from pathlib import Path

path_1 = Path.cwd() / 'task_5' / 'users_access.pickle'
path_2 = Path.cwd() / 'task_6' / 'users.csv'

def convert(source_file: Path = path_1, output_file: Path = path_2):
    with open(source_file, 'rb') as source, \
        open(output_file, 'w', newline='') as output:
        data_list = pickle.load(source)
        writer = csv.DictWriter(output, fieldnames=data_list[0].keys())
        writer.writeheader()
        for item in data_list:
            writer.writerow(item)

if __name__ == '__main__':
    convert()