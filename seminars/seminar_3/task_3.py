# Задание №3.
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где: ключ — тип элемента,
# значение — список элементов данного типа.


_tuple_ = (1, 'who', 2, 'is', 3.14, 'it')
res_dict = {}

keys = _tuple_[::2]
values = _tuple_[1::2]

for i in range(len(keys)):
    key = type(keys[i]).__name__
    value = values[i]

    if key in res_dict:
        res_dict[key].append(value)
    else:
        res_dict[key] = [value]

print(res_dict)