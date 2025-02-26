# Задача4.
# Сумма и произведение дробей.
# Программа принимает две строки вида "a/b" - дробь с числителем и знаменателем.
# Возвращает сумму и произведение дробей. Для проверки используется модуль fractions.

from fractions import Fraction

def sum(a, b):
    return a + b
def product(a, b):
    return a * b

frac_1 = input("Введите дробь (a/b): ")
frac_2 = input("Введите дробь (a/b): ")
num_1, denom_1 = map(int,frac_1.split('/'))
num_2, denom_2 = map(int,frac_2.split('/'))
f_1 = Fraction(num_1, denom_1)
f_2 = Fraction(num_2, denom_2)
res_sum = sum(f_1, f_2)
res_prod = product(f_1, f_2)
print("Сумма дробей:", res_sum)
print("Произведение дробей:", res_prod)