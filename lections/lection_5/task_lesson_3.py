# Задание.
# Перед вами несколько строк кода. Напишите что по вашему мнению
# выведет print, не запуская код.

data = {2, 4, 4, 6, 8, 10, 12}
res1 = {None: item for item in data if item > 4}
res2 = (item for item in data if item > 4)
res3 = [[item] for item in data if item > 4]
print(res1, res2, res3)
# {None: 6, None: 8, None: 10, None: 12} -> res1
# (6, 8, 10, 12) / <generator object <genexpr> at 0x000001B49FF23510>
# [[6], [8], [10], [12]]