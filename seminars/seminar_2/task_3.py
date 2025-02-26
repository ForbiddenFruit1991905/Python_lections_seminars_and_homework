# Задание №3
# ✔ Напишите программу, которая получает целое число
# и возвращает его двоичное, восьмеричное строковое
# представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода в преобразованиях
# к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно
from importlib.util import set_package


def my_func(data: list[int]) -> list:
    unique_nums = list(set(data))
    result = []
    for num in unique_nums:
        binary = bin(num)
        octal = oct(num)
        result.append(f"Двоичное представление {num}: {binary}\n")
        result.append(f"Восьмеричное представление {num}: {octal}\n")
        result.append(f"{binary, octal}\n")
    return result

print(''.join(my_func([1, 5, 5, 9, 11, 14])))