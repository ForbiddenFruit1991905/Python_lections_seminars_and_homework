# Задание №2.
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение
# — код буквы.
# ✔ Напишите преобразование в одну строку.

def func_dict(data):
    dict_txt = {elem: ord(elem) for elem in data if elem.isalpha()}

    # dict_txt = {}
    # for elem in data:
    #     if elem not in dict_txt:
    #         dict_txt[elem] = ord(elem)

    return dict_txt
txt = "Some message".lower()
res = func_dict(txt)
print(res)