# Задание №3.
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили. Сохраните его в итератор.
# ✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору,
# а не к словарю.

def func_dict(data):
    dict_txt = {elem: ord(elem) for elem in data if elem.isalpha()}
    my_dict = {key: dict_txt[key] for key in list(dict_txt)[:5]}
    return my_dict

txt = "Some message".lower()
res = func_dict(txt)
print(res)