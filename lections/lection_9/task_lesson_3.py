# Задание
# Перед вами несколько строк кода. Напишите что выведет программа, не
# запуская код.

import random
from typing import Callable

def count(num: int = 1):
    def deco(func: Callable):
        counter = []
        def wrapper(*args, **kwargs):
            # counter = []
            for _ in range(num):
                result = func(*args, **kwargs)
                counter.append(result)
            return counter
        return wrapper
    return deco

@count(10)
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)

print(f'{rnd(1, 10) = }')
# создаст 10 рандомных чисед от 1 до 10 (итого 10 значений)
print(f'{rnd(1, 100) = }')
# к списку предыдущему добавит еще 10 рандомных чисел от 1 до 100 (итого 20 значений)
print(f'{rnd(1, 1000) = }')
# к списку предыдущему добавит еще 10 рандомных чисел от 1 до 1000 (итого 30 значений)