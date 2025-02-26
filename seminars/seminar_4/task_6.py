# Задание №6.
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def func_sum_between_indexes(data: list[int], index_1, index_2):
    new_data = data[index_1:index_2]
    res_sum = sum(new_data)
    return res_sum
my_list = [5, 10, 15, 20, 25]
index_1 = 1
index_2 = len(my_list) - 1
res = func_sum_between_indexes(my_list, index_1, index_2)
print("Сумма элементов списка между выбранными индексами:", res)