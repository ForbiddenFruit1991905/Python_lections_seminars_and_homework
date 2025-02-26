# Задание №4.
# ✔ Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять не менее 42 знаков после запятой.

import math
import decimal

while True:

    r = int(input('Введите радиус: '))
    d = r * 2

    if d <= 1000:
        s = math.pi * pow(r, 2)
        l = math.pi * d
        print(f'Площадь круга равна {round(s, 42)}, длина окружности {round(l, 42)}')
        break
    else:
        print('Неправильный радиус. Введите радиус <= 500.')

# Вар.2 (семинар)
# def area(d):
#     decimal.getcontext().prec = 42
#     pi = decimal.Decimal(str(math.pi))
#     d = decimal.Decimal(str(d))
#     return pi * (d / 2) ** 2
#
# def len_circle(d):
#     decimal.getcontext().prec = 42
#     pi = decimal.Decimal(str(math.pi))
#     d = decimal.Decimal(str(d))
#     return pi * d
#
# print(area(5365))
# print(len_circle(4789.56))