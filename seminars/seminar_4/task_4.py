# Задание №4.
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без
# использования встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

def func_sort(data: list[int]) -> list[int]:
    data_len = len(data)
    for i in range(data_len):
        for j in range(0, data_len - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

my_list = [2, 1, 4, 3, 6, 5, 8, 7]
sorted_list = func_sort(my_list)
print("Отсортированный список:", sorted_list)