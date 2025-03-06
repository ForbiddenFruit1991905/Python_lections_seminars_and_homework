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

def func_guess_num(LOW_BOUND: int, UPPER_BOUND: int, ATTEMPTS: int):
    random_num = randint(LOW_BOUND, UPPER_BOUND)
    z = (f'В диапазоне от {LOW_BOUND} до {UPPER_BOUND} '
         f'получили {random_num}')
    print(z)
    attempt = 0
    while attempt < ATTEMPTS:
        person_attempt = int(input(f"Угадайте число в указанном диапазоне от {LOW_BOUND} до {UPPER_BOUND}: "))
        if LOW_BOUND <= person_attempt <= UPPER_BOUND:
            if person_attempt < random_num:
                print("Вы не угадали. Попробуйте еще раз. Число должно быть больше указанного.")
            elif person_attempt > random_num:
                print("Вы не угадали. Попробуйте еще раз. Число должно быть меньше указанного.")
            else:
                return True
            attempt += 1
        else:
            print("Вы ввели значение не из указанного диапазона")
    return False

# if __name__ == '__main__':
#     print(func_guess_num(1, 10, 3))