# Задание
# Перед вами несколько строк кода. Напишите что выведет программа, не
# запуская код.

from typing import Callable

def main(x: int) -> Callable[[int], dict[int, int]]:
    d = {}
    def loc(y: int) -> dict[int, int]:
        for i in range(y):
            d[i] = x ** i
        return d
    return loc

small = main(42)
big = main(73)

print(small(7))
# 42 ** 0, 42 ** 1, 42 ** 2 ... 42 ** 7 -> {0: 1, 1: 42, ....}
print(big(7))
# 73-//-
print(small(3))
# 42 key 0..6 value 1, 42 и возведение в степень