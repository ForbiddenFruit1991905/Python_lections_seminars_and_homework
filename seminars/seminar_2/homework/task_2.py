# Задание 2.
# Преобразование числа в шестнадцатеричное представление.
# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление. Функцию hex
# используйте для проверки своего результата.

def to_hex(num):
    if num < 0:
        return '-' + to_hex(-num)
    hex_chars = "0123456789ABCDEF"
    result = ""
    while num > 0:
        digit = num % 16
        result = hex_chars[digit] + result
        num //= 16
    return result

num = 305
custom_hex = to_hex(num)
print("Шестнадцатеричное представление числа", num, "по нашей функции:", custom_hex)
print("Проверка с использованием встроенной функции hex():", hex(num))

