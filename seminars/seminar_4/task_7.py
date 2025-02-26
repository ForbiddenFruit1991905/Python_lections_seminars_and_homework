# Задание №7.
# ✔ Функция получает на вход словарь с названием компании в качестве ключа и
# списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании.
# Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

def values_companies(data: dict[str, list[int]]):
    if any(map(lambda value: sum(value) < 0, data.values())):
        return False
    return True

dict_companies = {
    "Amazon": [10000, 25000, -30000],
    "Google": [115000, -230000, 150000],
    "IKEA": [125000, -40000, 500000]
}
res = values_companies(dict_companies)
print(res)