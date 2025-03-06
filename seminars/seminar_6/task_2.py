# Задание №2
# 📌 Создайте модуль с функцией внутри.
# 📌 Функция принимает на вход три целых числа: нижнюю и верхнюю
# границу и количество попыток.
# 📌 Внутри генерируется случайное число в указанных границах и
# пользователь должен угадать его за заданное число попыток.
# 📌 Функция выводит подсказки “больше” и “меньше”.
# 📌 Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь.

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