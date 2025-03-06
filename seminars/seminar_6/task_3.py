# Задание №3
# 📌 Улучшаем задачу 2.
# 📌 Добавьте возможность запуска функции “угадайки” из модуля в
# командной строке терминала.
# 📌 Строка должна принимать от 1 до 3 аргументов: параметры вызова
# функции.
# 📌 Для преобразования строковых аргументов командной строки в
# числовые параметры используйте генераторное выражение.

from random import randint

LOW_BOUND = 1
UPPER_BOUND = 10
ATTEMPTS = 3

def func_guess_num(n: int):
    random_num = randint(LOW_BOUND, UPPER_BOUND)
    z = (f'В диапазоне от {LOW_BOUND} до {UPPER_BOUND} '
         f'получили {random_num}')
    print(z)
    attempt = 0
    while attempt < ATTEMPTS - 1:
        if n != random_num:
            attempt += 1
            n = int(input("Попробуйте еще раз: "))
        else:
            return True
    return False

person_attempt = int(input("Угадайте число в диапазоне от 1 до 10: "))
print(func_guess_num(person_attempt))