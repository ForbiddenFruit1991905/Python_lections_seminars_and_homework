# Задание №5
# 📌 Напишите функцию, которая ищет json файлы в указанной директории
# и сохраняет их содержимое в виде одноимённых pickle файлов.

import json
import pickle
from os import listdir
from pathlib import Path

path_1 = Path.cwd() / 'task_4'
path_2 = Path.cwd() / 'task_5'

def find_json(source_dir: Path = path_1, output_dir: Path = path_2):
    for item in listdir(source_dir):
        # if Path(source_dir / item).is_file() and item[item.rfind('.'):] == '.json':
        if item.endswith('.json'):
            new_name = item[:item.rfind('.')] + '.pickle'
            with open(source_dir / item, 'r', encoding='utf-8') as source, \
                open(output_dir / new_name, 'wb') as output:
                pickle.dump(json.load(source), output)

if __name__ == '__main__':
    find_json()