# Задание №4
# 📌 Прочитайте созданный в прошлом задании csv файл без использования
# csv.DictReader.
# 📌 Дополните id до 10 цифр незначащими нулями.
# 📌 В именах первую букву сделайте прописной.
# 📌 Добавьте поле хеш на основе имени и идентификатора.
# 📌 Получившиеся записи сохраните в json файл, где каждая строка csv файла
# представлена как отдельный json словарь.
# 📌 Имя исходного и конечного файлов передавайте как аргументы функции.

import csv, json
from pathlib import Path

path_1 = Path.cwd() / 'users.csv'
path_2 = Path.cwd() / 'users_access.json'

def add_zeros(num: str):
    return  '0' * (10 - len(num)) + num
    # return str(num).zfill(10)

def func(source_file: Path = path_1, output_file: Path = path_2):
    with open(source_file, 'r', newline='', encoding='utf-8') as source, \
        open(output_file, 'w', encoding='utf-8') as output:
        reader = csv.reader(source)
        res = []
        count = 0

        for item in reader:
            if count != 0:
                entry = {'uid': add_zeros(item[0]),
                         'name': item[1].capitalize(),
                         'access': item[2],
                         'hash': hash(item[0] + item[1])}
                res.append(entry)
                count += 1
            else:
                count += 1
        json.dump(res, output)

if __name__ == '__main__':
    func()