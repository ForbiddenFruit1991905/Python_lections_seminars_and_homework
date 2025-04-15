# Задание №7
# 📌 Прочитайте созданный в прошлом задании csv файл без использования
# csv.DictReader.
# 📌 Распечатайте его как pickle строку.

import csv
import pickle
from pathlib import Path
from memory_profiler import profile

_path = Path.cwd() / 'task_6' / 'users.csv'

@profile
def csv_print(source_file: Path = _path) -> bytes:
    with open(source_file, 'r', newline='') as source:
        return pickle.dumps(list(csv.reader(source)))


if __name__ == '__main__':
    print(csv_print())
