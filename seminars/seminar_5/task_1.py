# Задание №1.
# ✔ Пользователь вводит строку из четырёх или более целых чисел,
# разделённых символом “/”. Сформируйте словарь, где:
# ✔ второе и третье число являются ключами.
# ✔ первое число является значением для первого ключа.
# ✔ четвертое и все возможные последующие числа
# хранятся в кортеже как значения второго ключа.

def func_pack(data: str):
    dict_pack = {}
    key_1 = data[1]
    key_2 = data[2]

    for elem in data:
        if key_1 not in dict_pack:
            dict_pack[key_1] = elem[0]
        if key_2 not in dict_pack:
            dict_pack[key_2] = data[3:]
    return dict_pack

txt = input("Введите числа через /: ").split("/")
# print(txt)
res = func_pack(txt)
print(res)
