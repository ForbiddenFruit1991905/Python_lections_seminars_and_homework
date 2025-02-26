# Задание №3.
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет символ из Unicode, а
# значением —  целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.
from pprint import pprint


def func():
    txt = input("Введите текст из двух чисел через пробел: ")
    txt_tuple = tuple(txt.split())
    print(txt_tuple, len(txt_tuple))
    res_dict = {}
    keys = txt_tuple[::2]
    values = txt_tuple[1::2]
    for i in range(len(keys)):
        key = keys[i]
        value = values[i]
        if key in res_dict:
            res_dict[key].append(value)
        else:
            res_dict[chr(int(key))] = int(value)
    print("Вывод v.1:", res_dict)
    print("Вывод v.2:", sorted(res_dict.items(), reverse=False))
    print("Вывод v.3: {")
    for key, value in sorted(res_dict.items()):
        print(f"'{key}': {value},")
    print("}")
    pprint(res_dict, width=1)

    # for key, value in sorted(res_dict.items(), reverse=False):
    #     print(f'{key}: {value}', end=' ')

func()