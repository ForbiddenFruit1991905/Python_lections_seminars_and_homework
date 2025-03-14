# Задача3.
# Перевод целого числа в римское число.
# Программа принимает целое число и возвращает
# его римское представление в виде строки.


def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

num = 3549
roman_num = int_to_roman(num)
print("Римское представление числа", num, "равно:", roman_num)

