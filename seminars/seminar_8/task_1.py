# Задание №1
# 📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый
# файл с псевдо именами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее файла новый с
# данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.

import json

def txt_to_json(file_txt, file_json):
    with(open(file_txt, 'r', encoding='utf-8') as f_read,
         open(file_json, 'w', encoding='utf-8') as f_write):
        data = {}
        for line in f_read:
            data[line.split()[0].capitalize()] = line.split()[2]
        res = json.dump(data, f_write, indent=2, separators=(',', ':'), sort_keys=True)
    return res

txt_to_json('example_3.txt', 'test_res.json')